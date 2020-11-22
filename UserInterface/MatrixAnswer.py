from PyQt5 import QtCore, QtGui, QtWidgets
import matrix_answer_window
class MatrixAnswer(QtWidgets.QWidget, matrix_answer_window.Ui_matrix_answer):
    def __init__(self, parent=None):
        super(MatrixAnswer, self).__init__(parent)
        self.setupUi(self)

    def printAnswer(self,text):
        self.label_answer.setText(text)
