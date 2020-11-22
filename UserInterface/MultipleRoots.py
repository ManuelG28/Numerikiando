import multipleroots_window
from PyQt5 import QtCore, QtGui, QtWidgets
from Methods.MultipleRoots import MultipleRootsMethod

class MultipleRoots(QtWidgets.QWidget, multipleroots_window.Ui_multipleroots):
    def __init__(self, parent=None):
        super(MultipleRoots, self).__init__(parent)
        self.setupUi(self)
        self.header = self.incremental_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.run_button.clicked.connect(self.clickRun)

    def clickRun(self):
        self.fu = self.f_input.toPlainText()
        self.x0 = self.x0_input.toPlainText()
        self.n = self.n_input.toPlainText()
        self.t = self.t_input.toPlainText()
        mul = MultipleRootsMethod(self.fu, self.x0, self.n, self.t)
        mul.roots()