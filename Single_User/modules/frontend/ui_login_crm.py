# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_crmRvDHCg.ui'
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


class Ui_Loginadmin(object):
    def setupUi(self, Loginadmin):
        if not Loginadmin.objectName():
            Loginadmin.setObjectName(u"Loginadmin")
        Loginadmin.resize(300, 420)
        Loginadmin.setMinimumSize(QSize(300, 420))
        Loginadmin.setMaximumSize(QSize(300, 420))
        Loginadmin.setStyleSheet(u"#bg {\n"
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
        self.centralwidget = QWidget(Loginadmin)
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
        self.frame_widgets.setGeometry(QRect(0, -370, 280, 720))
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

        Loginadmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Loginadmin)

        QMetaObject.connectSlotsByName(Loginadmin)
    # setupUi

    def retranslateUi(self, Loginadmin):
        Loginadmin.setWindowTitle(QCoreApplication.translate("Loginadmin", u"Login. PyBlackBOX", None))
        self.user_description.setText(QCoreApplication.translate("Loginadmin", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">ADMIN</span></p></body></html>", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Loginadmin", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Loginadmin", u"Password", None))
    # retranslateUi

