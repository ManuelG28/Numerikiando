import bisection_window
from PyQt5 import QtCore, QtGui, QtWidgets
from Methods.Bisection import BisectionMethod

class Bisection(QtWidgets.QWidget, bisection_window.Ui_bisection):
    def __init__(self, parent=None):
        super(Bisection, self).__init__(parent)
        self.setupUi(self)
        self.header = self.incremental_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.run_button.clicked.connect(self.clickRun)

    def clickRun(self):
        self.fu = self.f_input.toPlainText()
        self.a = self.a_input.toPlainText()
        self.b = self.b_input.toPlainText()
        self.n = self.n_input.toPlainText()
        self.t = self.t_input.toPlainText()
        bisec = BisectionMethod(self.fu, self.a, self.b, self.n, self.t)
        dataTab = bisec.bisection()
        row=0
        self.incremental_table.setRowCount(len(dataTab))
        for dataTab in dataTab:
            self.incremental_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(dataTab["a"])))
            self.incremental_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(dataTab["xm"])))
            self.incremental_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dataTab["b"])))
            self.incremental_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(dataTab["f(xm)"])))
            self.incremental_table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(dataTab["E"])))
            row=row+1