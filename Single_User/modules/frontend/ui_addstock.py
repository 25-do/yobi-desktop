# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addstockPWhZPU.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
from . resources_rc import *

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(570, 500)
        Dialog.setMinimumSize(QSize(570, 500))
        Dialog.setMaximumSize(QSize(570, 500))
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 12);")
        self.frame_33 = QFrame(Dialog)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(0, 0, 571, 703))
        self.frame_33.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_33)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(84)
        self.formLayout.setVerticalSpacing(11)
        self.label_150 = QLabel(self.frame_33)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_150)

        self.label_161 = QLabel(self.frame_33)
        self.label_161.setObjectName(u"label_161")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_161)

        self.lineEdit_20 = QLineEdit(self.frame_33)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_20)

        self.label_172 = QLabel(self.frame_33)
        self.label_172.setObjectName(u"label_172")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_172)

        self.lineEdit_29 = QLineEdit(self.frame_33)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_29)

        self.label_162 = QLabel(self.frame_33)
        self.label_162.setObjectName(u"label_162")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_162)

        self.lineEdit_21 = QLineEdit(self.frame_33)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_21)

        self.label_163 = QLabel(self.frame_33)
        self.label_163.setObjectName(u"label_163")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_163)

        self.lineEdit_22 = QLineEdit(self.frame_33)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.lineEdit_22)

        self.label_164 = QLabel(self.frame_33)
        self.label_164.setObjectName(u"label_164")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_164)

        self.lineEdit_23 = QLineEdit(self.frame_33)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.lineEdit_23)

        self.label_165 = QLabel(self.frame_33)
        self.label_165.setObjectName(u"label_165")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_165)

        self.lineEdit_24 = QLineEdit(self.frame_33)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.lineEdit_24)

        self.label_166 = QLabel(self.frame_33)
        self.label_166.setObjectName(u"label_166")

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_166)

        self.lineEdit_25 = QLineEdit(self.frame_33)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.lineEdit_25)

        self.label_167 = QLabel(self.frame_33)
        self.label_167.setObjectName(u"label_167")

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.label_167)

        self.lineEdit_26 = QLineEdit(self.frame_33)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.lineEdit_26)

        self.label_168 = QLabel(self.frame_33)
        self.label_168.setObjectName(u"label_168")

        self.formLayout.setWidget(28, QFormLayout.LabelRole, self.label_168)

        self.lineEdit_27 = QLineEdit(self.frame_33)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(28, QFormLayout.FieldRole, self.lineEdit_27)

        self.label_169 = QLabel(self.frame_33)
        self.label_169.setObjectName(u"label_169")

        self.formLayout.setWidget(31, QFormLayout.LabelRole, self.label_169)

        self.lineEdit_28 = QLineEdit(self.frame_33)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(31, QFormLayout.FieldRole, self.lineEdit_28)

        self.pushButton_21 = QPushButton(self.frame_33)
        self.pushButton_21.setObjectName(u"pushButton_21")
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 12, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_21.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_21.setFont(font)
        icon = QIcon()
        icon.addFile(u"plus (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon)
        self.pushButton_21.setIconSize(QSize(31, 25))

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_33)
        self.pushButton_22.setObjectName(u"pushButton_22")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_22.setPalette(palette1)
        self.pushButton_22.setFont(font)

        self.formLayout.setWidget(33, QFormLayout.FieldRole, self.pushButton_22)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_33)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(20, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(97, 97, 97);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"stats", None))
        self.label_150.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#cfcfcf;\">Add item</span></p></body></html>", None))
        self.label_161.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#bfbfbf;\">Name</span></p></body></html>", None))
        self.label_172.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#d5d5d5;\">	VAT</span></p></body></html>", None))
        self.label_162.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#f0f0f0;\">cost of goods sold</span></p></body></html>", None))
        self.label_163.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c8c8c8;\">selling price</span></p></body></html>", None))
        self.label_164.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#c8c8c8;\">Quantity</span></p></body></html>", None))
        self.label_165.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#d5d5d5;\">Discount</span></p></body></html>", None))
        self.label_166.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#d8d8d8;\">Supplier</span></p></body></html>", None))
        self.label_167.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#c7c7c7;\">category</span></p></body></html>", None))
        self.label_168.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#d8d8d8;\">Reoder limit</span></p></body></html>", None))
        self.label_169.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#d8d8d8;\">UPC</span></p></body></html>", None))
        self.pushButton_21.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"cancle", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
    # retranslateUi

