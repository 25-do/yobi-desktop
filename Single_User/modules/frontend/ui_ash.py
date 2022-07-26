# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ashFalDOZ.ui'
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
    QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from . resources_rc import *

class Ui_Entrance(object):
    def setupUi(self, Entrance):
        if not Entrance.objectName():
            Entrance.setObjectName(u"Entrance")
        Entrance.resize(1082, 566)
        Entrance.setStyleSheet(u"background-color: rgb(0, 0, 12);")
        self.gridLayout = QGridLayout(Entrance)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Entrance)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 200))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/hr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(7, 10))
        self.pushButton_7.setMaximumSize(QSize(16777215, 10))
        self.pushButton_7.setIconSize(QSize(10, 16))

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 200))
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/accounting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 200))
        self.pushButton_6.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/crm (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 200))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(129, 133))

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 200))
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 200))
        self.pushButton_4.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/payment-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(Entrance)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 10))
        self.frame_2.setMaximumSize(QSize(16777215, 33))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Entrance)

        QMetaObject.connectSlotsByName(Entrance)
    # setupUi

    def retranslateUi(self, Entrance):
        Entrance.setWindowTitle(QCoreApplication.translate("Entrance", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Entrance", u"HR", None))
        self.pushButton_7.setText(QCoreApplication.translate("Entrance", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Entrance", u"Accountts", None))
        self.pushButton_6.setText(QCoreApplication.translate("Entrance", u"CRM", None))
        self.pushButton.setText(QCoreApplication.translate("Entrance", u"Admin", None))
        self.pushButton_5.setText(QCoreApplication.translate("Entrance", u"Inventory", None))
        self.pushButton_4.setText(QCoreApplication.translate("Entrance", u"POS", None))
        self.pushButton_8.setText("")
    # retranslateUi

