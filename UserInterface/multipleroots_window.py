# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer/multipleroots_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_multipleroots(object):
    def setupUi(self, multipleroots):
        multipleroots.setObjectName("multipleroots")
        multipleroots.resize(900, 700)
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
        multipleroots.setPalette(palette)
        self.label = QtWidgets.QLabel(multipleroots)
        self.label.setGeometry(QtCore.QRect(60, 20, 771, 161))
        self.label.setStyleSheet("image: url(:/images/multipleroots_banner.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.f_input = QtWidgets.QTextEdit(multipleroots)
        self.f_input.setGeometry(QtCore.QRect(60, 250, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.f_input.setFont(font)
        self.f_input.setObjectName("f_input")
        self.t_input = QtWidgets.QTextEdit(multipleroots)
        self.t_input.setGeometry(QtCore.QRect(730, 250, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.t_input.setFont(font)
        self.t_input.setObjectName("t_input")
        self.x0_input = QtWidgets.QTextEdit(multipleroots)
        self.x0_input.setGeometry(QtCore.QRect(510, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x0_input.setFont(font)
        self.x0_input.setObjectName("x0_input")
        self.n_input = QtWidgets.QTextEdit(multipleroots)
        self.n_input.setGeometry(QtCore.QRect(620, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_input.setFont(font)
        self.n_input.setObjectName("n_input")
        self.label_2 = QtWidgets.QLabel(multipleroots)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 81, 41))
        self.label_2.setStyleSheet("background-image: url(:/images/function.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(multipleroots)
        self.label_4.setGeometry(QtCore.QRect(500, 200, 81, 41))
        self.label_4.setStyleSheet("background-image: url(:/images/x0.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Designer\\../UserInterface/Util/Images/x0.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(multipleroots)
        self.label_5.setGeometry(QtCore.QRect(620, 200, 81, 41))
        self.label_5.setStyleSheet("background-image: url(:/images/n.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Designer\\../UserInterface/Util/Images/n.png"))
        self.label_5.setObjectName("label_5")
        self.run_button = QtWidgets.QPushButton(multipleroots)
        self.run_button.setGeometry(QtCore.QRect(390, 320, 131, 51))
        self.run_button.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 86, 145);\n"
"border-radius: 12px;\n"
"")
        self.run_button.setObjectName("run_button")
        self.incremental_table = QtWidgets.QTableWidget(multipleroots)
        self.incremental_table.setGeometry(QtCore.QRect(20, 390, 851, 291))
        self.incremental_table.setMinimumSize(QtCore.QSize(851, 291))
        self.incremental_table.setMaximumSize(QtCore.QSize(851, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.incremental_table.setFont(font)
        self.incremental_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.incremental_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.incremental_table.setDragEnabled(False)
        self.incremental_table.setRowCount(0)
        self.incremental_table.setColumnCount(4)
        self.incremental_table.setObjectName("incremental_table")
        item = QtWidgets.QTableWidgetItem()
        self.incremental_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.incremental_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.incremental_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.incremental_table.setHorizontalHeaderItem(3, item)
        self.incremental_table.horizontalHeader().setCascadingSectionResizes(False)
        self.label_3 = QtWidgets.QLabel(multipleroots)
        self.label_3.setGeometry(QtCore.QRect(770, 200, 51, 41))
        self.label_3.setStyleSheet("image: url(:/images/t.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(multipleroots)
        QtCore.QMetaObject.connectSlotsByName(multipleroots)

    def retranslateUi(self, multipleroots):
        _translate = QtCore.QCoreApplication.translate
        multipleroots.setWindowTitle(_translate("multipleroots", "Form"))
        self.run_button.setText(_translate("multipleroots", "Run Method"))
        item = self.incremental_table.horizontalHeaderItem(0)
        item.setText(_translate("multipleroots", "Iteration"))
        item = self.incremental_table.horizontalHeaderItem(1)
        item.setText(_translate("multipleroots", "xi"))
        item = self.incremental_table.horizontalHeaderItem(2)
        item.setText(_translate("multipleroots", "f(xi)"))
        item = self.incremental_table.horizontalHeaderItem(3)
        item.setText(_translate("multipleroots", "E"))
import link_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    multipleroots = QtWidgets.QWidget()
    ui = Ui_multipleroots()
    ui.setupUi(multipleroots)
    multipleroots.show()
    sys.exit(app.exec_())