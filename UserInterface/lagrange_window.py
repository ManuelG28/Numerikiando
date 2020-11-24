# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/lagrange_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lagrange(object):
    def setupUi(self, lagrange):
        lagrange.setObjectName("lagrange")
        lagrange.resize(900, 700)
        lagrange.setMinimumSize(QtCore.QSize(900, 700))
        lagrange.setMaximumSize(QtCore.QSize(900, 700))
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
        lagrange.setPalette(palette)
        self.label = QtWidgets.QLabel(lagrange)
        self.label.setGeometry(QtCore.QRect(60, 20, 771, 161))
        self.label.setStyleSheet("image: url(:/images/lagrange_anner.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(lagrange)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 41))
        self.label_5.setStyleSheet("background-image: url(:/images/n.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.n_input = QtWidgets.QTextEdit(lagrange)
        self.n_input.setGeometry(QtCore.QRect(120, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_input.setFont(font)
        self.n_input.setObjectName("n_input")
        self.vector_button = QtWidgets.QPushButton(lagrange)
        self.vector_button.setGeometry(QtCore.QRect(230, 200, 171, 51))
        self.vector_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.vector_button.setObjectName("vector_button")
        self.run_button = QtWidgets.QPushButton(lagrange)
        self.run_button.setGeometry(QtCore.QRect(380, 630, 151, 51))
        self.run_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.run_button.setObjectName("run_button")

        self.retranslateUi(lagrange)
        QtCore.QMetaObject.connectSlotsByName(lagrange)

    def retranslateUi(self, lagrange):
        _translate = QtCore.QCoreApplication.translate
        lagrange.setWindowTitle(_translate("lagrange", "Form"))
        self.vector_button.setText(_translate("lagrange", "Generate Vectors"))
        self.run_button.setText(_translate("lagrange", "Run method"))
import link_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lagrange = QtWidgets.QWidget()
    ui = Ui_lagrange()
    ui.setupUi(lagrange)
    lagrange.show()
    sys.exit(app.exec_())
