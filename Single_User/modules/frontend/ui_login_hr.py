# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_hrDEkPxt.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
from . res import *

class Ui_Singnup(object):
    def setupUi(self, Singnup):
        if not Singnup.objectName():
            Singnup.setObjectName(u"Singnup")
        Singnup.resize(300, 420)
        Singnup.setMinimumSize(QSize(300, 420))
        Singnup.setMaximumSize(QSize(300, 420))
        Singnup.setStyleSheet(u"#bg {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel {\n"
"	color:  rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-top: 20px;\n"
"}\n"
".QLineEdit {\n"
"	border: 3px solid rgb(47, 48, 50);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
".QLineEdit:hover {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(62, 63, 66);\n"
"}\n"
".QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 3px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}")
        self.centralwidget = QWidget(Singnup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setFrameShape(QFrame.NoFrame)
        self.bg.setFrameShadow(QFrame.Raised)
        self.frame_widgets = QFrame(self.bg)
        self.frame_widgets.setObjectName(u"frame_widgets")
        self.frame_widgets.setGeometry(QRect(0, -369, 280, 720))
        self.frame_widgets.setMinimumSize(QSize(280, 720))
        self.frame_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_widgets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_widgets)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 20, 10)
        self.preloader = QFrame(self.frame_widgets)
        self.preloader.setObjectName(u"preloader")
        self.preloader.setMinimumSize(QSize(240, 240))
        self.preloader.setMaximumSize(QSize(260, 260))
        self.preloader.setFrameShape(QFrame.NoFrame)
        self.preloader.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.preloader)

        self.user_description = QLabel(self.frame_widgets)
        self.user_description.setObjectName(u"user_description")
        self.user_description.setStyleSheet(u"background: transparent;")

        self.verticalLayout_2.addWidget(self.user_description)

        self.label = QLabel(self.frame_widgets)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label)

        self.username = QLineEdit(self.frame_widgets)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 30))
        self.username.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.username)

        self.password = QLineEdit(self.frame_widgets)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setMaximumSize(QSize(16777215, 40))
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password)


        self.verticalLayout.addWidget(self.bg)

        Singnup.setCentralWidget(self.centralwidget)

        self.retranslateUi(Singnup)

        QMetaObject.connectSlotsByName(Singnup)
    # setupUi

    def retranslateUi(self, Singnup):
        Singnup.setWindowTitle(QCoreApplication.translate("Singnup", u"Login. PyBlackBOX", None))
        self.user_description.setText(QCoreApplication.translate("Singnup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">SIGNUP</span></p></body></html>", None))
        self.label.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Singnup", u"Email", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Singnup", u"Password", None))
    # retranslateUi

