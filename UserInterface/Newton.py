import newton_window
import math
from CustomDialog import CustomDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Newton(QtWidgets.QWidget, newton_window.Ui_Newton):
    def __init__(self, parent=None):
        super(Newton, self).__init__(parent)
        self.setupUi(self)

        self.header = self.newton_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.run_button.clicked.connect(self.runMethod)

    def runMethod(self):
        self.tol=float(self.tolerance.toPlainText())
        self.functionF=self.f_input.toPlainText()
        self.functionFderiv=self.derivate_input.toPlainText()
        self.xInit=float(self.x0.toPlainText())
        self.nMaxCounter=0
        self.nMaximo=int(self.nMax.toPlainText())
        self.dataTable=[]
        answ=self.iterate(self.xInit)
        row = 0
        self.newton_table.setRowCount(len(self.dataTable))
        for line in self.dataTable:
            self.newton_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(line["iter"])))
            self.newton_table.setItem(row,1,QtWidgets.QTableWidgetItem(str(line["xi"])))
            self.newton_table.setItem(row,2,QtWidgets.QTableWidgetItem(str(line["f(x)"])))
            self.newton_table.setItem(row,3,QtWidgets.QTableWidgetItem(str(line["Err"])))
            row+=1
        self.showFinalValue(answ)

    def showFinalValue(self, answ):
        dialog = CustomDialog(self, "The root reached was: "+str(answ))
        dialog.show()

    def iterate(self, x):
        xi= x-(self.evaluateF(x)/self.evaluateFDerived(x))
        if abs( xi - x ) < self.tol or self.nMaxCounter == self.nMax:
            self.dataTable.append({"iter":self.nMaxCounter, "xi":xi, "f(x)":self.evaluateF(xi), "Err":abs(xi-x)})
            return xi
        else:
            self.dataTable.append({"iter":self.nMaxCounter, "xi":xi, "f(x)":self.evaluateF(xi), "Err":abs(xi-x)})
            self.nMaxCounter+=1
            return self.iterate(xi)

    def evaluateF(self, x):
        f= lambda x: eval(self.functionF)
        y= f(x)
        return y
    
    def evaluateFDerived(self, x):
        fd= lambda x: eval(self.functionFderiv)
        y= fd(x)
        return y