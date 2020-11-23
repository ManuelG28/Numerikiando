import fake_ruke_window
import math
from CustomDialog import CustomDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class FakeRule(QtWidgets.QWidget, fake_ruke_window.Ui_fake_rule):
    def __init__(self, parent=None):
        super(FakeRule, self).__init__(parent)
        self.setupUi(self)

        self.header = self.fake_rule_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        self.run_button.clicked.connect(self.runMethod)

    def runMethod(self):
        self.tol=float(self.tolerance.toPlainText())
        self.functionF=self.f_input.toPlainText()
        self.pa=float(self.a.toPlainText())
        self.pb=float(self.b.toPlainText())
        self.nMaxCounter=0
        self.nMaximo=int(self.nMax.toPlainText())
        self.dataTable=[]
        answ=self.iterate(self.pa, self.pb)
        row = 0
        self.fake_rule_table.setRowCount(len(self.dataTable))
        for line in self.dataTable:
            self.fake_rule_table.setItem(row,0,QtWidgets.QTableWidgetItem(str(line["iter"])))
            self.fake_rule_table.setItem(row,1,QtWidgets.QTableWidgetItem(str(line["a"])))
            self.fake_rule_table.setItem(row,2,QtWidgets.QTableWidgetItem(str(line["xm"])))
            self.fake_rule_table.setItem(row,3,QtWidgets.QTableWidgetItem(str(line["b"])))
            self.fake_rule_table.setItem(row,4,QtWidgets.QTableWidgetItem(str(line["f(x)"])))
            self.fake_rule_table.setItem(row,5,QtWidgets.QTableWidgetItem(str(line["Err"])))
            row+=1
        self.showFinalValue(answ)

    def showFinalValue(self, answ):
        dialog = CustomDialog(self, "The root reached was: "+str(answ))
        dialog.show()

    def iterate(self, a, b):
        aEvaluated=self.evaluateF(a)
        bEvaluated=self.evaluateF(b)
        r=((a*bEvaluated)-(b*aEvaluated))/(bEvaluated-aEvaluated)
        rEvaluated=self.evaluateF(r)
        if rEvaluated*aEvaluated<0:
            if abs(r-b)<self.tol or self.nMaxCounter==self.nMax:
                self.dataTable.append({"iter":self.nMaxCounter, "a":a, "xm":r, "b":b,"f(x)":rEvaluated, "Err":abs(r-b)})
                return r
            else:
                self.dataTable.append({"iter":self.nMaxCounter, "a":a, "xm":r, "b":b,"f(x)":rEvaluated, "Err":abs(r-b)})
                self.nMaxCounter+=1
            return self.iterate(a,r)
        elif rEvaluated*bEvaluated<0:
            if abs(r-a)<self.tol or self.nMaxCounter==self.nMax:
                self.dataTable.append({"iter":self.nMaxCounter, "a":a, "xm":r, "b":b,"f(x)":rEvaluated, "Err":abs(r-a)})
                return r
            else:
                self.dataTable.append({"iter":self.nMaxCounter, "a":a, "xm":r, "b":b,"f(x)":rEvaluated, "Err":abs(r-a)})
                self.nMaxCounter+=1
                return self.iterate(r,b)
        else:
            self.showException("There isn't sign change")
            return 0

    def showException(self, msg):
        dialog = CustomDialog(self, msg)
        dialog.show()

    def evaluateF(self, x):
        f= lambda x: eval(self.functionF)
        y= f(x)
        return y