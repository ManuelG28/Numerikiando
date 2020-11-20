import full_pivoting_window
from PyQt5 import QtCore, QtGui, QtWidgets


class FullPivoting(QtWidgets.QWidget, full_pivoting_window.Ui_full_pivoting):
    def __init__(self, parent=None):
        super(FullPivoting, self).__init__(parent)
        self.setupUi(self)



