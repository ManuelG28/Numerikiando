import sor_window
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Methods.Sor import SorMethod
from CustomDialog import CustomDialog
from MatrixAnswer import MatrixAnswer



class Sor(QtWidgets.QWidget, sor_window.Ui_sor):
    def __init__(self, parent=None):
        super(Sor, self).__init__(parent)
        self.setupUi(self)
        self.matrix_button.clicked.connect(self.clickMatrix)
        self.run_button.clicked.connect(self.runMethod)

        self.a_X = 90
        self.a_Y = 290
        self.a_adder = 60
        self.a_counter = 0
        self.b_X = 610
        self.b_Y = 320
        self.b_adder = 60
        self.b_counter = 0
        self.x0_X = 710
        self.x0_Y = 320
        self.x0_adder = 60
        self.x0_counter = 0

    def createAttributes(self):
        self.a_X = 90
        self.a_Y = 290
        self.a_adder = 60
        self.a_counter = 0
        self.b_X = 610
        self.b_Y = 320
        self.b_adder = 60
        self.b_counter = 0
        self.x0_X = 710
        self.x0_Y = 320
        self.x0_adder = 60
        self.x0_counter = 0
        self.matrix_text = np.empty((self.n, self.n), dtype=object)
        self.vector_text = [None]*self.n
        self.vectorX0_text = [None]*self.n

    def clickMatrix(self):
        if (self.is_number(self.n_input.toPlainText())):
            self.n = int(self.n_input.toPlainText())
            self.createAttributes()
            if self.n < 7:
                self.drawA()
                self.drawB()
                self.drawX0()
                # Draw 'A' and 'b' and 'x0' label
                self.label_2 = QtWidgets.QLabel(self)
                self.label_2.setGeometry(QtCore.QRect(10, 400, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(36)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self)
                self.label_3.setGeometry(QtCore.QRect(610, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(36)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                
                self.label_4 = QtWidgets.QLabel(self)
                self.label_4.setGeometry(QtCore.QRect(710, 270, 71, 41))
                font = QtGui.QFont()
                font.setPointSize(36)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("")
                self.label_4.setObjectName("label_4")

                self.label_2.setText("A:")
                self.label_3.setText("b:")
                self.label_4.setText("x0:")
                self.label_2.show()
                self.label_3.show()
                self.label_4.show()
        else:
            self.showRestriction(
                        'N\'s field must be a integer.')

    def drawA(self):
        self.matrix_text = np.empty((self.n, self.n), dtype=object)
        for i in range(self.n):
            for j in range(self.n):
                self.a = QtWidgets.QTextEdit(self)
                self.a.setGeometry(QtCore.QRect(self.a_X, self.a_Y, 40, 40))
                object_name = ('a_' + str(self.a_counter))
                self.a.setObjectName(object_name)
                self.a.show()
                self.matrix_text[i][j] = self.a
                self.a_X = self.a_X+self.a_adder
                self.a_counter = self.a_counter+1
            self.a_Y = self.a_Y+self.a_adder
            self.a_X = 90

    def drawB(self):
        self.n = int(self.n_input.toPlainText())
        self.vector_text = [None]*self.n
        for i in range(self.n):
            self.b = QtWidgets.QTextEdit(self)
            self.b.setGeometry(QtCore.QRect(self.b_X, self.b_Y, 40, 40))
            object_name = ('b_' + str(self.b_counter))
            self.b.setObjectName(object_name)
            self.b.show()
            self.vector_text[i] = self.b
            self.b_Y = self.b_Y+self.b_adder
            self.b_counter = self.b_counter+1
    
    def drawX0(self):
        self.n = int(self.n_input.toPlainText())
        self.vectorX0_text = [None]*self.n
        for i in range(self.n):
            self.x0 = QtWidgets.QTextEdit(self)
            self.x0.setGeometry(QtCore.QRect(self.x0_X, self.x0_Y, 40, 40))
            object_name = ('x0_' + str(self.x0_counter))
            self.x0.setObjectName(object_name)
            self.x0.show()
            self.vectorX0_text[i] = self.x0
            self.x0_Y = self.x0_Y+self.x0_adder
            self.x0_counter = self.x0_counter+1

    def runMethod(self):
        self.a_matrix = np.empty((self.n, self.n))
        self.b_vector = [None]*self.n
        self.x0_vector = [None]*self.n

        self.a_matrix = self.constructA()
        self.b_vector = self.constructB()
        self.x0_vector = self.constructX0()
        self.t = self.t_input.toPlainText()
        self.w = self.w_input.toPlainText()
        self.iter = self.iter_input.toPlainText()
        if (self.a_matrix is not None) and (self.b_vector is not None):
            s = SorMethod(self.a_matrix,self.b_vector, self.x0_vector, self.t, self.iter, self.w)
            s.sor()
            answer = s.answer
            self.matrix_answer = MatrixAnswer()
            self.matrix_answer.show()
            self.matrix_answer.printAnswer(answer)

    def constructA(self):
        a_matrix = np.empty((self.n, self.n))
        for i in range(len(self.matrix_text[0])):
            for j in range(len(self.matrix_text[0])):
                text = self.matrix_text[i][j].toPlainText().replace(' ', '')
                if not text or not self.is_number(text):
                    self.showRestriction(
                        'Each of the matrix\'s fields must contain a number')
                    return None
                else:
                    a_matrix[i][j] = float(text)
        return a_matrix

    def constructB(self):
        b_vector = [None]*self.n
        for i in range(len(self.vector_text)):
            text = self.vector_text[i].toPlainText().replace(' ', '')
            if not text or not self.is_number(text):
                self.showRestriction(
                    'Each of the vector\'s fields must contain a number')
                return None
            else:
                b_vector[i] = float(text)
        return b_vector
    
    def constructX0(self):
        x0_vector = [None]*self.n
        for i in range(len(self.vectorX0_text)):
            text = self.vectorX0_text[i].toPlainText().replace(' ', '')
            if not text or not self.is_number(text):
                self.showRestriction(
                    'Each of the vector\'s fields must contain a number')
                return None
            else:
                x0_vector[i] = float(text)
        return x0_vector

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
