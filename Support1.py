# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Helper3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 519)
        MainWindow.setMinimumSize(QtCore.QSize(519, 519))
        MainWindow.setMaximumSize(QtCore.QSize(519, 519))
        MainWindow.setBaseSize(QtCore.QSize(519, 519))
        MainWindow.setStyleSheet("background-color: #e2e3ff\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: #191919;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 221, 41))
        self.label.setStyleSheet("QLabel{\n"
"}")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 350, 401, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #fafafa;\n"
"border: 3px solid #000000;\n"
"border-radius: 20%;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:#cbcbcb;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:#9c9c9c;\n"
"}\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #fafafa;\n"
"border: 3px solid #000000;\n"
"border-radius: 20%;\n"
"color:black;\n"
"font: Rubik;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:#cbcbcb;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:#9c9c9c;\n"
"}\n"
"")
        self.pushButton_2.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.textEdit = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 461, 251))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"background-color: #dadada;\n"
"border: 3px solid #c2d300;\n"
"border-radius: 20%;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Помощник"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#dee11a;\">Помощник</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Слушать"))
        self.pushButton.setShortcut(_translate("MainWindow", "Space"))
        self.pushButton_2.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Alt+S, Esc"))
