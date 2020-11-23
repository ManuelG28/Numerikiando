import fixed_point_window
import math
from CustomDialog import CustomDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class FixedPoint(QtWidgets.QWidget, fixed_point_window.Ui_fixed_point):
    def __init__(self, parent=None):
        super(FixedPoint, self).__init__(parent)
        self.setupUi(self)

        self.header = self.fixed_point_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        self.run_button.clicked.connect(self.runMethod)

    def runMethod(self):
        self.tol=float(self.tolerance.toPlainText())
        self.functionF=self.f_input.toPlainText()
        self.functionG=self.g_input.toPlainText()
        self.xInit=float(self.x0.toPlainText())
        self.nMaxCounter=0
        self.nMaximo=int(self.nMax.toPlainText())
        self.dataTable=[]
        answ=self.iterate(self.xInit)
        row = 0
        self.fixed_point_table.setRowCount(len(self.dataTable))
        for line in self.dataTable:
            self.fixed_point_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(line["iter"])))
            self.fixed_point_table.setItem(row,1,QtWidgets.QTableWidgetItem(str(line["xi"])))
            self.fixed_point_table.setItem(row,2,QtWidgets.QTableWidgetItem(str(line["g(x)"])))
            self.fixed_point_table.setItem(row,3,QtWidgets.QTableWidgetItem(str(line["f(x)"])))
            self.fixed_point_table.setItem(row,4,QtWidgets.QTableWidgetItem(str(line["Err"])))
            row+=1
        self.showFinalValue(answ)

    def showFinalValue(self, answ):
        dialog = CustomDialog(self, "The root reached was: "+str(answ))
        dialog.show()

    def iterate(self, x):
        xi= self.evaluateG(x)
        if abs( xi - x ) < self.tol or self.nMaxCounter == self.nMax:
            # print("| " + str(self.nMaxCounter) + " " + "|  " + str(x) + "  " + "|  " + str(xi) + "  " + "|  " + str(self.evaluateF(x)) + "  " + "|  " + str(abs(xi - x)) + "  |")
            # print("The root reached was " + str(xi))
            self.dataTable.append({"iter":self.nMaxCounter, "xi":x, "g(x)":xi, "f(x)":self.evaluateF(x), "Err":abs(xi-x)})
            return xi
        else:
            self.dataTable.append({"iter":self.nMaxCounter, "xi":x, "g(x)":xi, "f(x)":self.evaluateF(x), "Err":abs(xi-x)})
            # print("| " + str(self.nMaxCounter) + " " + "|  " + str(x) + "  " + "|  " + str(xi) + "  " + "|  " + str(self.evaluateF(x)) + "  " + "|  " + str(abs(xi - x)) + "  |")
            self.nMaxCounter+=1
            return self.iterate(xi)

    def evaluateF(self, x):
        f= lambda x: eval(self.functionF)
        y= f(x)
        return y
    
    def evaluateG(self, x):
        g= lambda x: eval(self.functionG)
        y= g(x)
        return y
