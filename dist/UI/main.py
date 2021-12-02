# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoffeeWindow(object):
    def setupUi(self, CoffeeWindow):
        CoffeeWindow.setObjectName("CoffeeWindow")
        CoffeeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CoffeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 0, 0, 1, 1)
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setObjectName("edit_btn")
        self.gridLayout.addWidget(self.edit_btn, 0, 1, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        CoffeeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CoffeeWindow)
        self.statusbar.setObjectName("statusbar")
        CoffeeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CoffeeWindow)
        QtCore.QMetaObject.connectSlotsByName(CoffeeWindow)

    def retranslateUi(self, CoffeeWindow):
        _translate = QtCore.QCoreApplication.translate
        CoffeeWindow.setWindowTitle(_translate("CoffeeWindow", "Кофе"))
        self.add_btn.setText(_translate("CoffeeWindow", "Добавить"))
        self.edit_btn.setText(_translate("CoffeeWindow", "Изменить"))
        self.delete_btn.setText(_translate("CoffeeWindow", "Удалить"))
