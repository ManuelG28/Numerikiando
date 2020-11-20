import incremental_searches_window
from PyQt5 import QtCore, QtGui, QtWidgets


class IncrementalSearches(QtWidgets.QWidget, incremental_searches_window.Ui_incremental_searches):
    def __init__(self, parent=None):
        super(IncrementalSearches, self).__init__(parent)
        self.setupUi(self)
        self.header = self.incremental_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.run_button.clicked.connect(self.clickRun)

    def clickRun(self):
        print('.')