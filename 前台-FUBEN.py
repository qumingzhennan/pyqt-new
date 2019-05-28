# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '前台-FUBEN.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from sqlite_db import *
import json
import datetime

class Ui_MainWindow(object):
    sd = Sqlite_Database()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_roomid = QtWidgets.QLabel(self.centralwidget)
        self.label_roomid.setObjectName("label_roomid")
        self.verticalLayout_2.addWidget(self.label_roomid)
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setObjectName("label_start")
        self.verticalLayout_2.addWidget(self.label_start)
        self.label_endtime = QtWidgets.QLabel(self.centralwidget)
        self.label_endtime.setObjectName("label_endtime")
        self.verticalLayout_2.addWidget(self.label_endtime)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 2)
        self.check_in = QtWidgets.QPushButton(self.centralwidget)
        self.check_in.setObjectName("check_in")
        self.gridLayout.addWidget(self.check_in, 1, 3, 1, 1)
        self.gettime = QtWidgets.QPushButton(self.centralwidget)
        self.gettime.setObjectName("gettime")
        self.gridLayout.addWidget(self.gettime, 2, 3, 1, 1)
        self.gettime2 = QtWidgets.QPushButton(self.centralwidget)
        self.gettime2.setObjectName("gettime2")
        self.gridLayout.addWidget(self.gettime2, 3, 3, 1,1 )
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.createRDR = QtWidgets.QPushButton(self.centralwidget)
        self.createRDR.setObjectName("createRDR")
        self.verticalLayout_3.addWidget(self.createRDR)
        self.showRDR = QtWidgets.QTextBrowser(self.centralwidget)
        self.showRDR.setObjectName("showRDR")
        self.verticalLayout_3.addWidget(self.showRDR)
        self.gridLayout.addLayout(self.verticalLayout_3, 6, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.createinvoice = QtWidgets.QPushButton(self.centralwidget)
        self.createinvoice.setObjectName("createinvoice")
        self.verticalLayout_4.addWidget(self.createinvoice)
        self.showinvoice = QtWidgets.QTextBrowser(self.centralwidget)
        self.showinvoice.setObjectName("showinvoice")
        self.verticalLayout_4.addWidget(self.showinvoice)
        self.gridLayout.addLayout(self.verticalLayout_4, 6, 2, 1, 2)
        self.printRDR = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.printRDR.setFont(font)
        self.printRDR.setObjectName("printRDR")
        self.gridLayout.addWidget(self.printRDR, 7, 1, 1, 1)
        self.printinvoice = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.printinvoice.setFont(font)
        self.printinvoice.setObjectName("printinvoice")
        self.gridLayout.addWidget(self.printinvoice, 7, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.createRDR.clicked.connect(lambda: self.CreateRDR())  # 这边改槽
        self.createinvoice.clicked.connect(lambda:self.CreateInvoice())#这边改槽
        self.printRDR.clicked.connect(lambda: self.PrintRDR())  # 这边改槽
        self.printinvoice.clicked.connect(lambda: self.PrintInvoice())  # 这边改槽
        self.gettime.clicked.connect(lambda: self.GetTime_in())
        self.gettime2.clicked.connect(lambda: self.GetTime_out())
        self.check_in.clicked.connect(lambda: self.Check_in())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_roomid.setText(_translate("MainWindow", "房间号"))
        self.label_start.setText(_translate("MainWindow", "开始时间"))
        self.label_endtime.setText(_translate("MainWindow", "截至时间"))
        self.check_in.setText(_translate("MainWindow", "登记入住"))
        self.gettime.setText(_translate("MainWindow", "获取当前时间-IN"))
        self.gettime2.setText(_translate("MainWindow","获取当前时间-OUT"))
        self.createRDR.setText(_translate("MainWindow", "创建详单"))
        self.createinvoice.setText(_translate("MainWindow", "创建账单"))
        self.printRDR.setText(_translate("MainWindow", "打印详单"))
        self.printinvoice.setText(_translate("MainWindow", "打印账单"))
        self.menu.setTitle(_translate("MainWindow", "前台"))

    def Check_in(self):
        #这儿应该设置空调被激活？就是可以使用了。
        print("Check_in了哦")
        self.lineEdit.setText("12345")
    def GetTime_in(self):
        time = datetime.datetime.now()
        self.lineEdit_2.setText(str(time))
        #self.lineEdit_3.setText(str(time))
    def GetTime_out(self):
        time2 = datetime.datetime.now()
        self.lineEdit_3.setText(str(time2))
    def CreateRDR(self):
        self.showRDR.setText("")
        RoomId = self.lineEdit.text()
        date_in = self.lineEdit_2.text()
        date_out = self.lineEdit_3.text()
        print("This is CreateRDR ", RoomId,date_in,date_out)
        print("This is CreateRDR ")
        d = {
            'name': 'python书籍',
            'price': 62.3,
            'is_valid': True
        }
        createrdr = json.dumps(d, ensure_ascii=False)
        print(createrdr)
        self.showRDR.insertPlainText(createrdr)
    def PrintRDR(self):  # RDR详单
        self.showRDR.setText("")
        print("This is PrintRDR")

       # print(self.d) #到这儿都ok
       # printinvoice = json.dumps(self.d, ensure_ascii=False)
       # print(printinvoice)
       # self.showRDR.insertPlainText(printinvoice)

    def CreateInvoice(self):  # Invoice 账单
        self.showRDR.setText("")
        #createinvoice = json.dumps(self.d, ensure_ascii=False)
        #print(createinvoice)
        #self.showRDR.insertPlainText(createinvoice)
        print("This is CreateInvoice")

    def PrintInvoice(self):
        self.showRDR.setText("")
        print("This is PrintInvoice")
        #printinvoice = json.dumps(self.d, ensure_ascii=False)
        #print(printinvoice)
        #self.showRDR.insertPlainText(printinvoice)

if  __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
