import secant_window
import math
from CustomDialog import CustomDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *

class Secant(QtWidgets.QWidget, secant_window.Ui_Secant):
    def __init__(self, parent=None):
        super(Secant, self).__init__(parent)
        self.setupUi(self)

        self.header = self.secant_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.run_button.clicked.connect(self.runMethod)

    def runMethod(self):
        self.tol=float(self.tolerance.toPlainText())
        self.functionF=self.f_input.toPlainText()
        self.xPrev=float(self.x0.toPlainText())
        self.xPost=float(self.x1.toPlainText())
        self.nMaxCounter=0
        self.nMaximo=int(self.nMax.toPlainText())
        self.dataTable=[]
        x = Symbol('x')
        f= lambda x: eval(self.functionF)
        self.dataTable.append({"iter":self.nMaxCounter, "xi":self.xPrev, "f(x)":f(self.xPrev), "Err":0})
        self.nMaxCounter+=1
        self.dataTable.append({"iter":self.nMaxCounter, "xi":self.xPost, "f(x)":f(self.xPost), "Err":0})
        self.nMaxCounter+=1
        answ=self.iterate(self.xPost, self.xPrev)
        row = 0
        self.secant_table.setRowCount(len(self.dataTable))
        for line in self.dataTable:
            self.secant_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(line["iter"])))
            self.secant_table.setItem(row,1,QtWidgets.QTableWidgetItem(str(line["xi"])))
            self.secant_table.setItem(row,2,QtWidgets.QTableWidgetItem(str(line["f(x)"])))
            self.secant_table.setItem(row,3,QtWidgets.QTableWidgetItem(str(line["Err"])))
            row+=1
        self.showFinalValue(answ)

    def showFinalValue(self, answ):
        dialog = CustomDialog(self, "The root reached was: "+str(answ))
        dialog.setWindowTitle("Success!")
        dialog.show()

    def iterate(self, xPost, xPrev):
        x = Symbol('x')
        f= lambda x: eval(self.functionF)
        xEvaluated= f(xPost)
        xi= xPost-(xEvaluated*(xPost-xPrev)/(xEvaluated-f(xPrev)))
        if abs( xi - xPost ) < self.tol or self.nMaxCounter == self.nMax:
            self.dataTable.append({"iter":self.nMaxCounter, "xi":round(xi,10), "f(x)":round(f(xi),10), "Err":round(abs(xi-xPost),10)})
            return xi
        else:
            self.dataTable.append({"iter":self.nMaxCounter, "xi":round(xi,10), "f(x)":round(f(xi),10), "Err":round(abs(xi-xPost),10)})
            self.nMaxCounter+=1
            return self.iterate(xi,xPost)
