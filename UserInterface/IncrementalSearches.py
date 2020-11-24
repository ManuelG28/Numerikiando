import incremental_searches_window
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Methods.IncrementalSearches import IncrementalSearchesMethod
from CustomDialog import CustomDialog
from MatrixAnswer import MatrixAnswer



class IncrementalSearches(QtWidgets.QWidget, incremental_searches_window.Ui_incremental_searches):
    def __init__(self, parent=None):
        super(IncrementalSearches, self).__init__(parent)
        self.setupUi(self)
        self.run_button.clicked.connect(self.clickRun)

    def clickRun(self):
        self.fu = self.f_input.toPlainText()
        self.delta = self.delta_input.toPlainText()
        self.distance = self.distance_input.toPlainText()
        self.n = self.n_input.toPlainText()
       
        inc = IncrementalSearchesMethod(self.delta, self.distance, self.n, self.fu)
        dataTab = inc.runSearch()
        answer = inc.answer

        self.matrix_answer = MatrixAnswer()
        self.matrix_answer.show()
        self.matrix_answer.printAnswer(answer)