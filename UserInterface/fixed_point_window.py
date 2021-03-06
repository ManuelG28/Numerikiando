# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/fixed_point_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fixed_point(object):
    def setupUi(self, fixed_point):
        fixed_point.setObjectName("fixed_point")
        fixed_point.resize(900, 647)
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
        fixed_point.setPalette(palette)
        self.label = QtWidgets.QLabel(fixed_point)
        self.label.setGeometry(QtCore.QRect(60, 20, 771, 161))
        self.label.setStyleSheet("background-image: url(:/images/BannerFixedPoint.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.f_input = QtWidgets.QTextEdit(fixed_point)
        self.f_input.setGeometry(QtCore.QRect(60, 250, 221, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(14)
        font.setKerning(True)
        self.f_input.setFont(font)
        self.f_input.setObjectName("f_input")
        self.x0 = QtWidgets.QTextEdit(fixed_point)
        self.x0.setGeometry(QtCore.QRect(530, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x0.setFont(font)
        self.x0.setObjectName("x0")
        self.label_2 = QtWidgets.QLabel(fixed_point)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 81, 41))
        self.label_2.setStyleSheet("background-image: url(:/images/function.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(fixed_point)
        self.label_4.setGeometry(QtCore.QRect(520, 200, 81, 41))
        self.label_4.setStyleSheet("background-image: url(:/images/x0.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Designer/../UserInterface/Util/Images/x0.png"))
        self.label_4.setObjectName("label_4")
        self.run_button = QtWidgets.QPushButton(fixed_point)
        self.run_button.setGeometry(QtCore.QRect(390, 320, 131, 51))
        self.run_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.run_button.setObjectName("run_button")
        self.fixed_point_table = QtWidgets.QTableWidget(fixed_point)
        self.fixed_point_table.setGeometry(QtCore.QRect(20, 390, 851, 291))
        self.fixed_point_table.setMinimumSize(QtCore.QSize(851, 291))
        self.fixed_point_table.setMaximumSize(QtCore.QSize(851, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fixed_point_table.setFont(font)
        self.fixed_point_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fixed_point_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.fixed_point_table.setDragEnabled(False)
        self.fixed_point_table.setRowCount(0)
        self.fixed_point_table.setColumnCount(5)
        self.fixed_point_table.setObjectName("fixed_point_table")
        item = QtWidgets.QTableWidgetItem()
        self.fixed_point_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fixed_point_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fixed_point_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fixed_point_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.fixed_point_table.setHorizontalHeaderItem(4, item)
        self.fixed_point_table.horizontalHeader().setCascadingSectionResizes(False)
        self.g_input = QtWidgets.QTextEdit(fixed_point)
        self.g_input.setGeometry(QtCore.QRect(300, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.g_input.setFont(font)
        self.g_input.setObjectName("g_input")
        self.tolerance = QtWidgets.QTextEdit(fixed_point)
        self.tolerance.setGeometry(QtCore.QRect(720, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tolerance.setFont(font)
        self.tolerance.setObjectName("tolerance")
        self.nMax = QtWidgets.QTextEdit(fixed_point)
        self.nMax.setGeometry(QtCore.QRect(630, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nMax.setFont(font)
        self.nMax.setObjectName("nMax")
        self.label_3 = QtWidgets.QLabel(fixed_point)
        self.label_3.setGeometry(QtCore.QRect(350, 200, 81, 41))
        self.label_3.setStyleSheet("background-image: url(:/images/functionG.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(fixed_point)
        self.label_5.setGeometry(QtCore.QRect(740, 200, 81, 41))
        self.label_5.setStyleSheet("background-image: url(:/images/tolerance.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(fixed_point)
        self.label_6.setGeometry(QtCore.QRect(630, 200, 81, 41))
        self.label_6.setStyleSheet("background-image: url(:/images/nmax.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(fixed_point)
        QtCore.QMetaObject.connectSlotsByName(fixed_point)

    def retranslateUi(self, fixed_point):
        _translate = QtCore.QCoreApplication.translate
        fixed_point.setWindowTitle(_translate("fixed_point", "Form"))
        self.run_button.setText(_translate("fixed_point", "Run Method"))
        item = self.fixed_point_table.horizontalHeaderItem(0)
        item.setText(_translate("fixed_point", "Iter"))
        item = self.fixed_point_table.horizontalHeaderItem(1)
        item.setText(_translate("fixed_point", "xi"))
        item = self.fixed_point_table.horizontalHeaderItem(2)
        item.setText(_translate("fixed_point", "g(x)"))
        item = self.fixed_point_table.horizontalHeaderItem(3)
        item.setText(_translate("fixed_point", "f(x)"))
        item = self.fixed_point_table.horizontalHeaderItem(4)
        item.setText(_translate("fixed_point", "Error"))
import link_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fixed_point = QtWidgets.QWidget()
    ui = Ui_fixed_point()
    ui.setupUi(fixed_point)
    fixed_point.show()
    sys.exit(app.exec_())
