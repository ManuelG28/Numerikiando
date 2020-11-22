import dialog_window
from PyQt5 import QtCore, QtGui, QtWidgets

class CustomDialog(QtWidgets.QDialog, dialog_window.Ui_Dialog):
    def __init__(self, parent=None,text=''):
        super(CustomDialog, self).__init__(parent)
        self.setupUi(self)
        self.message.setText(text)
        self.setWindowTitle('Be careful!')
