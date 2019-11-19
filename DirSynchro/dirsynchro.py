import ui
from PyQt5 import QtWidgets, QtCore, QtGui

import dirproc
import dirutil
import replaceutil


class DirSynchro(QtWidgets.QMainWindow, ui.Ui_DirSynchro):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.state = {}
        self.toggle_direction(True)
        self.toggle_record(True)

        self.left_dir_proc = dirproc.DirProc()
        self.right_dir_proc = dirproc.DirProc()
        self.utility = dirutil.DirUtil()

        self.place_elements()
        self.connect_signals()

    def place_elements(self):
        self.leftDirProcLayout.addWidget(self.left_dir_proc)
        self.rightDirProcLayout.addWidget(self.right_dir_proc)

    def connect_signals(self):
        self.leftToRightButton.clicked.connect(
            lambda: self.toggle_direction(True))
        self.rightToLeftButton.clicked.connect(
            lambda: self.toggle_direction(False))
        self.recordButton.clicked.connect(
            lambda: self.toggle_record(True))
        self.stopButton.clicked.connect(
            lambda: self.toggle_record(False))

        self.textReplaceButton.clicked.connect(self.replace_text)

    def toggle_direction(self, _left_to_right):
        self.state['left_to_right'] = _left_to_right
        self.toggle_opposite_buttons(
            self.leftToRightButton,
            self.rightToLeftButton,
            self.state['left_to_right']
        )

    def toggle_record(self, record_state):
        self.state['record'] = record_state
        self.toggle_opposite_buttons(
            self.recordButton,
            self.stopButton,
            self.state['record']
        )

    @staticmethod
    def toggle_opposite_buttons(on, off, condition):
        qss_active = "QPushButton{" \
            "height: 25px;" \
            "width: 70px;" \
            "background-color: white;" \
            "border-radius: 2px;" \
            "border: 1px solid #4a90d9;" \
            "}"

        qss_inactive = "QPushButton{" \
            "height: 25px;" \
            "width: 70px;" \
            "background-color: white;" \
            "border-radius: 2px;" \
            "border: 1px solid #cccccc;" \
            "}"

        if condition:
            on.setStyleSheet(qss_active)
            off.setStyleSheet(qss_inactive)
        else:
            off.setStyleSheet(qss_active)
            on.setStyleSheet(qss_inactive)

    def is_recording(self):
        return self.state['record']

    @staticmethod
    def replace_text():
        return replaceutil.ReplaceUtil()