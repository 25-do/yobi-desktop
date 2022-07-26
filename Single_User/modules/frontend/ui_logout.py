# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoutWsAxCV.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_logout(object):
    def setupUi(self, logout):
        if not logout.objectName():
            logout.setObjectName(u"logout")
        logout.resize(474, 136)
        logout.setStyleSheet(u"background-color: rgb(0, 0, 29);")
        self.gridLayout = QGridLayout(logout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(logout)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 29);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 44))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"    border-radius : 15px;	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(252, 0, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 44))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius : 15px;	\n"
"	\n"
"	background-color: rgb(58, 58, 58);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 211, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(logout)

        QMetaObject.connectSlotsByName(logout)
    # setupUi

    def retranslateUi(self, logout):
        logout.setWindowTitle(QCoreApplication.translate("logout", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("logout", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("logout", u"Ok", None))
        self.label.setText(QCoreApplication.translate("logout", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Are you sure you want to logout !</span></p></body></html>", None))
    # retranslateUi

