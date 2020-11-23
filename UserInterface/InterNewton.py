import internewton_window
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Methods.InterNewton import InterNewtonMethod
from CustomDialog import CustomDialog
from MatrixAnswer import MatrixAnswer



class InterNewton(QtWidgets.QWidget, internewton_window.Ui_internewton):
    def __init__(self, parent=None):
        super(InterNewton, self).__init__(parent)
        self.setupUi(self)
        self.vector_button.clicked.connect(self.clickVectors)
        self.run_button.clicked.connect(self.runMethod)

        self.x1_X = 90
        self.x1_Y = 320
        self.x1_adder = 60
        self.x1_counter = 0
        self.y1_X = 200
        self.y1_Y = 320
        self.y1_adder = 60
        self.y1_counter = 0

    def createAttributes(self):
        self.x1_X = 90
        self.x1_Y = 320
        self.x1_adder = 60
        self.x1_counter = 0
        self.y1_X = 200
        self.y1_Y = 320
        self.y1_adder = 60
        self.y1_counter = 0
        self.vector_text = [None]*self.n
        self.vectorY1_text = [None]*self.n

    def clickVectors(self):
        if (self.is_number(self.n_input.toPlainText())):
            self.n = int(self.n_input.toPlainText())
            self.createAttributes()
            if self.n < 7:
                self.drawX1()
                self.drawY1()
                # Draw 'x1' and 'y1' label
                self.label_3 = QtWidgets.QLabel(self)
                self.label_3.setGeometry(QtCore.QRect(90, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(30)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                
                self.label_4 = QtWidgets.QLabel(self)
                self.label_4.setGeometry(QtCore.QRect(200, 270, 71, 41))
                font = QtGui.QFont()
                font.setPointSize(30)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("")
                self.label_4.setObjectName("label_4")

                self.label_3.setText("x:")
                self.label_4.setText("y:")

                self.label_3.show()
                self.label_4.show()
        else:
            self.showRestriction(
                        'N\'s field must be a integer.')

    def drawX1(self):
        self.n = int(self.n_input.toPlainText())
        self.vector_text = [None]*self.n
        for i in range(self.n):
            self.x1 = QtWidgets.QTextEdit(self)
            self.x1.setGeometry(QtCore.QRect(self.x1_X, self.x1_Y, 40, 40))
            object_name = ('x1_' + str(self.x1_counter))
            self.x1.setObjectName(object_name)
            self.x1.show()
            self.vector_text[i] = self.x1
            self.x1_Y = self.x1_Y+self.x1_adder
            self.x1_counter = self.x1_counter+1
    
    def drawY1(self):
        self.n = int(self.n_input.toPlainText())
        self.vectorY1_text = [None]*self.n
        for i in range(self.n):
            self.y1 = QtWidgets.QTextEdit(self)
            self.y1.setGeometry(QtCore.QRect(self.y1_X, self.y1_Y, 40, 40))
            object_name = ('y1_' + str(self.y1_counter))
            self.y1.setObjectName(object_name)
            self.y1.show()
            self.vectorY1_text[i] = self.y1
            self.y1_Y = self.y1_Y+self.y1_adder
            self.y1_counter = self.y1_counter+1

    def runMethod(self):
        self.x1_vector = [None]*self.n
        self.y1_vector = [None]*self.n

        self.x1_vector = self.constructX1()
        self.y1_vector = self.constructY1()
        if (self.x1_vector is not None):
            ne = InterNewtonMethod(self.x1_vector, self.y1_vector)
            ne.newton()
            answer = ne.answer
            self.matrix_answer = MatrixAnswer()
            self.matrix_answer.show()
            self.matrix_answer.printAnswer(answer)
    

    def constructX1(self):
        x1_vector = [None]*self.n
        for i in range(len(self.vector_text)):
            text = self.vector_text[i].toPlainText().replace(' ', '')
            if not text or not self.is_number(text):
                self.showRestriction(
                    'Each of the vector\'s fields must contain a number')
                return None
            else:
                x1_vector[i] = float(text)
        return x1_vector
    
    def constructY1(self):
        y1_vector = [None]*self.n
        for i in range(len(self.vectorY1_text)):
            text = self.vectorY1_text[i].toPlainText().replace(' ', '')
            if not text or not self.is_number(text):
                self.showRestriction(
                    'Each of the vector\'s fields must contain a number')
                return None
            else:
                y1_vector[i] = float(text)
        return y1_vector

    def showRestriction(self, restriction):
        dialog = CustomDialog(self, restriction)
        dialog.show()

    def is_number(self,n):
        is_number = True
        try:
            num = float(n)
            # check for "nan" floats
            is_number = num == num  
        except ValueError:
            is_number = False
        return is_number
