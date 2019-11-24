# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 90, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 721, 650))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 140, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 190, 221, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_1.setGeometry(QtCore.QRect(750, 240, 110, 41))
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.pushButton_3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3_2.setGeometry(QtCore.QRect(860, 240, 110, 41))
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 290, 221, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 340, 221, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 390, 221, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(750, 440, 221, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(750, 490, 221, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(750, 540, 221, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(750, 590, 221, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(750, 640, 221, 41))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(790, 40, 31, 31))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(850, 40, 31, 31))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(910, 40, 31, 31))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton.clicked.connect(MainWindow.p1_ck)
        self.pushButton_2.clicked.connect(MainWindow.p2_ck)
        self.pushButton_3.clicked.connect(MainWindow.p3_ck)
        self.pushButton_3_1.clicked.connect(MainWindow.R1)#
        self.pushButton_3_2.clicked.connect(MainWindow.R2)#
        self.pushButton_4.clicked.connect(MainWindow.p4_ck)
        self.pushButton_5.clicked.connect(MainWindow.p5_ck)
        self.pushButton_6.clicked.connect(MainWindow.p6_ck)
        self.pushButton_7.clicked.connect(MainWindow.p7_ck)
        self.pushButton_8.clicked.connect(MainWindow.p8_ck)
        self.pushButton_9.clicked.connect(MainWindow.p9_ck)
        self.pushButton_10.clicked.connect(MainWindow.p10_ck)
        self.pushButton_11.clicked.connect(MainWindow.p11_ck)

        self.pushButton_12.clicked.connect(self.close)  # 关闭窗口
        self.pushButton_14.clicked.connect(self.showMinimized)  # 最小化窗口

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "读取xls"))
        self.pushButton_2.setText(_translate("MainWindow", "查询数据量和基本结构"))
        self.pushButton_3.setText(_translate("MainWindow", "查询NaN,导出csv,判断清洗模式"))
        self.pushButton_3_1.setText(_translate("MainWindow", "自动填充模式"))
        self.pushButton_3_2.setText(_translate("MainWindow", "删除数据模式"))
        self.pushButton_4.setText(_translate("MainWindow", "查询课程名,项目名,类型，二级实验室"))
        self.pushButton_5.setText(_translate("MainWindow", "统计每一门课程实验课时数"))
        self.pushButton_6.setText(_translate("MainWindow", "统计每周开设课程实验课时数"))
        self.pushButton_7.setText(_translate("MainWindow", "统计每门课程实验类型分布"))
        self.pushButton_8.setText(_translate("MainWindow", "统计每个班级的实验课课表"))
        self.pushButton_9.setText(_translate("MainWindow", "分析各二级实验室承担的实验课时量"))
        self.pushButton_10.setText(_translate("MainWindow", "分析各二级实验室能够支持的实验类型"))
        self.pushButton_11.setText(_translate("MainWindow", "清屏"))

        self.pushButton_12.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''')
        self.pushButton_13.setStyleSheet('''QPushButton{background:#F7D674;border-radius:15px;}
        QPushButton:hover{background:yellow;}''')
        self.pushButton_14.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:15px;}
        QPushButton:hover{background:green;}''')

        self.setWindowOpacity(0.95)                             # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   # 设置窗口背景透明

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)       # 隐藏边框
        pe = QtGui.QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QtGui.QPalette.Window, QtCore.Qt.lightGray) # 设置背景色
        #pe.setColor(QtGui.QPalette.Background,QtCore.Qt.blue)
        self.setPalette(pe)

        self.centralwidget.setStyleSheet('''
            QPushButton{
                    border:2px solid #F3F3F5;color:white;padding-left:5px;
                    height:35px;
                    font-size:12px;
                    padding-right:5px;
            }
            QPushButton:hover{ color:white;
                border:2px solid #F3F3F5;
                border-radius:15px;
                background:black;
            }
            QWidget#centralwidget{
                background:Gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            ''')

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()        # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor)) # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)    # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
