# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/gauss_elim_simple_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gauss_elim_simple(object):
    def setupUi(self, gauss_elim_simple):
        gauss_elim_simple.setObjectName("gauss_elim_simple")
        gauss_elim_simple.resize(900, 700)
        gauss_elim_simple.setMinimumSize(QtCore.QSize(900, 700))
        gauss_elim_simple.setMaximumSize(QtCore.QSize(900, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 86, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        gauss_elim_simple.setPalette(palette)
        self.label = QtWidgets.QLabel(gauss_elim_simple)
        self.label.setGeometry(QtCore.QRect(60, 20, 771, 161))
        self.label.setStyleSheet("isbdviaebhfvildfvke")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(gauss_elim_simple)
        self.label_5.setGeometry(QtCore.QRect(90, 210, 81, 41))
        self.label_5.setStyleSheet("background-image: url(:/images/n.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.n_input = QtWidgets.QTextEdit(gauss_elim_simple)
        self.n_input.setGeometry(QtCore.QRect(220, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_input.setFont(font)
        self.n_input.setObjectName("n_input")
        self.matrix_button = QtWidgets.QPushButton(gauss_elim_simple)
        self.matrix_button.setGeometry(QtCore.QRect(370, 200, 171, 51))
        self.matrix_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.matrix_button.setObjectName("matrix_button")
        self.run_button = QtWidgets.QPushButton(gauss_elim_simple)
        self.run_button.setGeometry(QtCore.QRect(380, 630, 151, 51))
        self.run_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.run_button.setObjectName("run_button")

        self.retranslateUi(gauss_elim_simple)
        QtCore.QMetaObject.connectSlotsByName(gauss_elim_simple)

    def retranslateUi(self, gauss_elim_simple):
        _translate = QtCore.QCoreApplication.translate
        gauss_elim_simple.setWindowTitle(_translate("gauss_elim_simple", "Form"))
        self.label.setText(_translate("gauss_elim_simple", "gaussian elimination simple"))
        self.matrix_button.setText(_translate("gauss_elim_simple", "Generate Matrix"))
        self.run_button.setText(_translate("gauss_elim_simple", "Run method"))
import link_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gauss_elim_simple = QtWidgets.QWidget()
    ui = Ui_gauss_elim_simple()
    ui.setupUi(gauss_elim_simple)
    gauss_elim_simple.show()
    sys.exit(app.exec_())