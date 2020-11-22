import lu_simple_window
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from CustomDialog import CustomDialog
from MatrixAnswer import MatrixAnswer
from Methods.LuSimple import LuSimpleMethod


class LuSimple(QtWidgets.QWidget, lu_simple_window.Ui_lu_simple_window):
    def __init__(self, parent=None):
        super(LuSimple, self).__init__(parent)
        self.setupUi(self)
        self.matrix_button.clicked.connect(self.clickMatrix)
        self.run_button.clicked.connect(self.runMethod)

        self.a_X = 90
        self.a_Y = 290
        self.a_adder = 60
        self.a_counter = 0
        self.b_X = 710
        self.b_Y = 290
        self.b_adder = 60
        self.b_counter = 0

    def createAttributes(self):
        self.a_X = 90
        self.a_Y = 290
        self.a_adder = 60
        self.a_counter = 0
        self.b_X = 710
        self.b_Y = 290
        self.b_adder = 60
        self.b_counter = 0
        self.matrix_text = np.empty((self.n, self.n), dtype=object)
        self.vector_text = [None]*self.n

    def clickMatrix(self):
        if (self.is_number(self.n_input.toPlainText())):
            self.n = int(self.n_input.toPlainText())
            self.createAttributes()
            if self.n < 7:
                self.drawA()
                self.drawB()
                # Draw 'A' and 'b' label
                self.label_2 = QtWidgets.QLabel(self)
                self.label_2.setGeometry(QtCore.QRect(10, 400, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(36)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self)
                self.label_3.setGeometry(QtCore.QRect(710, 210, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(36)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                self.label_2.setText("A:")
                self.label_3.setText("b:")
                self.label_2.show()
                self.label_3.show()
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

    def runMethod(self):
        self.a_matrix = np.empty((self.n, self.n))
        self.b_vector = [None]*self.n

        self.a_matrix = self.constructA()
        self.b_vector = self.constructB()
        if (self.a_matrix is not None) and (self.b_vector is not None):
            self.lu_simple = LuSimpleMethod(self.a_matrix,self.n,self.b_vector)
            answer = self.lu_simple.answer
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
