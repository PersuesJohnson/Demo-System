# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiMainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1381, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 681, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.QtHomepage = QtWidgets.QLabel(self.frame)
        self.QtHomepage.setGeometry(QtCore.QRect(20, 50, 631, 471))
        self.QtHomepage.setObjectName("QtHomepage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1060, 450, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(700, 40, 251, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.QtPhoto = QtWidgets.QLabel(self.frame_2)
        self.QtPhoto.setGeometry(QtCore.QRect(10, 10, 231, 261))
        self.QtPhoto.setObjectName("QtPhoto")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(960, 40, 261, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Qtvideo = QtWidgets.QLabel(self.frame_3)
        self.Qtvideo.setGeometry(QtCore.QRect(10, 10, 241, 131))
        self.Qtvideo.setText("")
        self.Qtvideo.setObjectName("Qtvideo")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(700, 340, 251, 301))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 231, 281))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.QtName1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.QtName1.setObjectName("QtName1")
        self.verticalLayout_4.addWidget(self.QtName1)
        self.QtName2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.QtName2.setObjectName("QtName2")
        self.verticalLayout_4.addWidget(self.QtName2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.NULL_ = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.NULL_.setText("")
        self.NULL_.setObjectName("NULL_")
        self.verticalLayout_5.addWidget(self.NULL_)
        self.QtPhoto1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.QtPhoto1.setObjectName("QtPhoto1")
        self.verticalLayout_5.addWidget(self.QtPhoto1)
        self.QtPhoto2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.QtPhoto2.setObjectName("QtPhoto2")
        self.verticalLayout_5.addWidget(self.QtPhoto2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(960, 200, 261, 241))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.QtuserName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QtuserName.setObjectName("QtuserName")
        self.verticalLayout_3.addWidget(self.QtuserName)
        self.QtFirstVisit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QtFirstVisit.setObjectName("QtFirstVisit")
        self.verticalLayout_3.addWidget(self.QtFirstVisit)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.QtVisit1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QtVisit1.setObjectName("QtVisit1")
        self.verticalLayout_6.addWidget(self.QtVisit1)
        self.QtVisit2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QtVisit2.setObjectName("QtVisit2")
        self.verticalLayout_6.addWidget(self.QtVisit2)
        self.QtVisit3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.QtVisit3.setObjectName("QtVisit3")
        self.verticalLayout_6.addWidget(self.QtVisit3)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1381, 31))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVideo = QtWidgets.QAction(MainWindow)
        self.actionVideo.setObjectName("actionVideo")
        self.actionRecognize = QtWidgets.QAction(MainWindow)
        self.actionRecognize.setObjectName("actionRecognize")
        self.actionAdd_Target = QtWidgets.QAction(MainWindow)
        self.actionAdd_Target.setObjectName("actionAdd_Target")
        self.menuEdit.addAction(self.actionVideo)
        self.menuEdit.addAction(self.actionRecognize)
        self.menuEdit.addAction(self.actionAdd_Target)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QtHomepage.setText(_translate("MainWindow", "videoArea"))
        self.pushButton.setText(_translate("MainWindow", "Video"))
        self.pushButton_2.setText(_translate("MainWindow", "Recognize"))
        self.pushButton_3.setText(_translate("MainWindow", "Advance settings"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))
        self.QtPhoto.setText(_translate("MainWindow", "infoArea"))
        self.label_7.setText(_translate("MainWindow", "Familiar people"))
        self.QtName1.setText(_translate("MainWindow", "Name1"))
        self.QtName2.setText(_translate("MainWindow", "Name2"))
        self.QtPhoto1.setText(_translate("MainWindow", "Photo1"))
        self.QtPhoto2.setText(_translate("MainWindow", "Photo2"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "FirstVisit"))
        self.label_4.setText(_translate("MainWindow", "Visit Record"))
        self.QtuserName.setText(_translate("MainWindow", "(Null)"))
        self.QtFirstVisit.setText(_translate("MainWindow", "(Null)"))
        self.QtVisit1.setText(_translate("MainWindow", "(Null)"))
        self.QtVisit2.setText(_translate("MainWindow", "(Null)"))
        self.QtVisit3.setText(_translate("MainWindow", "((Null)"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionVideo.setText(_translate("MainWindow", "Video"))
        self.actionRecognize.setText(_translate("MainWindow", "Recognize"))
        self.actionAdd_Target.setText(_translate("MainWindow", "Add Target"))

