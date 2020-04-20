# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase import *


class Ui_MainWindow(object):

    def loadData(self):
        db = DataBase("movements.db")
        db.initialize()
        rows = db.fetchColumnFromTable("*", "movements")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        db.closeConnection()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 11, 1011, 391))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(460, 470, 113, 32))
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect(self.loadData)
        self.loadData()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 22))
        self.menubar.setObjectName("menubar")
        self.menuExpenses = QtWidgets.QMenu(self.menubar)
        self.menuExpenses.setObjectName("menuExpenses")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuExpenses.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.menuExpenses.setTitle(_translate("MainWindow", "Expenses"))
