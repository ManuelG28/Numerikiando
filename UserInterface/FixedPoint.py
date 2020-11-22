import fixed_point_window
import math
from PyQt5 import QtCore, QtGui, QtWidgets

class FixedPoint(QtWidgets.QWidget, fixed_point_window.Ui_fixed_point):
    def __init__(self, parent=None):
        super(FixedPoint, self).__init__(parent)
        self.setupUi(self)
        self.run_button.clicked.connect(self.runMethod)

    def runMethod(self):
        self.tol=float(self.tolerance.toPlainText())
        self.functionF=self.f_input.toPlainText()
        self.functionG=self.g_input.toPlainText()
        self.xInit=float(self.x0.toPlainText())
        self.nMaxCounter=0
        self.nMaximo=int(self.nMax.toPlainText())
        self.iterate(self.xInit)

    def iterate(self, x):
        xi= self.evaluateG(x)
        if abs( xi - x ) < self.tol or self.nMaxCounter == self.nMax:
            print("| " + str(self.nMaxCounter) + " " + "|  " + str(x) + "  " + "|  " + str(xi) + "  " + "|  " + str(self.evaluateF(x)) + "  " + "|  " + str(abs(xi - x)) + "  |")
            print("The root reached was " + str(xi))
            return xi
        else:
            print("| " + str(self.nMaxCounter) + " " + "|  " + str(x) + "  " + "|  " + str(xi) + "  " + "|  " + str(self.evaluateF(x)) + "  " + "|  " + str(abs(xi - x)) + "  |")
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
