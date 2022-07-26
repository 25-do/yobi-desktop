# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uomMSJxnZ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_UOM(object):
    def setupUi(self, UOM):
        if not UOM.objectName():
            UOM.setObjectName(u"UOM")
        UOM.resize(441, 233)
        UOM.setMinimumSize(QSize(400, 200))
        UOM.setMaximumSize(QSize(441, 233))
        UOM.setStyleSheet(u"background-color: rgb(0, 0, 12);")
        self.gridLayout = QGridLayout(UOM)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(UOM)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 12);\n"
"	\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 0, 235);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(0, 0, 12);\n"
"}\n"
"QComboBox{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-r"
                        "adius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {	\n"
"	color: rgb(253, 253, 253);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.comboBox, 3, 1, 1, 2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.pushButton, 4, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.pushButton_2, 4, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(UOM)

        QMetaObject.connectSlotsByName(UOM)
    # setupUi

    def retranslateUi(self, UOM):
        UOM.setWindowTitle(QCoreApplication.translate("UOM", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("UOM", u"<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("UOM", u"<html><head/><body><p><span style=\" color:#ffffff;\">UOM Abbreviation</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("UOM", u"<html><head/><body><p><span style=\" color:#ffffff;\">Staus</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("UOM", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("UOM", u"Cancel", None))
    # retranslateUi

