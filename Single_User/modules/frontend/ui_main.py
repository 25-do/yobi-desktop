# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainTgXamm.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1397, 745)
        MainWindow.setMinimumSize(QSize(940, 26))
        icon = QIcon()
        icon.addFile(u":/images/images/images/yobi.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 0, 235);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#Logo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo14.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(0, 0, 214); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	bord"
                        "er: 2px solid rgb(64, 71, 88);\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 211);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 211);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-le"
                        "ft: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(0, 0, 211);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(0, 0, 214)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#ext"
                        "raCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 211);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { "
                        "background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(0, 0, 211); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButto"
                        "n:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 211);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(0, 0, 211);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 67);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {"
                        "	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
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
"\n"
"\n"
"QTextEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
""
                        "	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 0, 235);\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 0, 235);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border:"
                        " none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0, 0, 214);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScroll"
                        "Bar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(0, 0, 214);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: no"
                        "ne;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
""
                        "    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"\n"
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
"	border-bottom-right-radius: 3px;	\n"
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
"\n"
" /////////////////////////////////////////////"
                        "////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(0, 0, 211);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(0, 0, 235);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(0, 0, 211);\n"
"	border: none;\n"
"    height: 10px;\n"
""
                        "    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(0, 0, 235);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(0, 0, 235);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(0, 0, 214);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer Q"
                        "PushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(50, 0))
        self.leftMenuBg.setMaximumSize(QSize(50, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 456, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 234, 16))
        self.titleLeftDescription.setMinimumSize(QSize(234, 0))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_15 = QLabel(self.topLogoInfo)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 41, 41))
        self.label_15.setPixmap(QPixmap(u":/images/images/images/yobi.svg"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(1)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-notes.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-wallet.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cart.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)

        self.btn_widgets_2 = QPushButton(self.topMenu)
        self.btn_widgets_2.setObjectName(u"btn_widgets_2")
        sizePolicy.setHeightForWidth(self.btn_widgets_2.sizePolicy().hasHeightForWidth())
        self.btn_widgets_2.setSizePolicy(sizePolicy)
        self.btn_widgets_2.setMinimumSize(QSize(0, 45))
        self.btn_widgets_2.setFont(font)
        self.btn_widgets_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-3d.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets_2)

        self.pushButton = QPushButton(self.topMenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-truck.png);")
        self.pushButton.setIconSize(QSize(36, 32))

        self.verticalLayout_8.addWidget(self.pushButton)

        self.client_btn_2 = QPushButton(self.topMenu)
        self.client_btn_2.setObjectName(u"client_btn_2")
        self.client_btn_2.setMinimumSize(QSize(0, 45))
        self.client_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_btn_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.client_btn_2)

        self.pushButton_37 = QPushButton(self.topMenu)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(0, 45))
        self.pushButton_37.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.pushButton_37)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-female.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)

        self.label_28 = QLabel(self.extraCenter)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setPixmap(QPixmap(u"../.designer/backup/Capture.svg"))
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.label_28)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_26 = QPushButton(self.rightButtons)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_26.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_26)

        self.pushButton_129 = QPushButton(self.rightButtons)
        self.pushButton_129.setObjectName(u"pushButton_129")

        self.horizontalLayout_2.addWidget(self.pushButton_129)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.frame_7 = QFrame(self.pagesContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_7)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMaximumSize(QSize(16777215, 16777215))
        self.home.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.home)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(400, 852))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"border-radius: 15px;\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.widget_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_22 = QFrame(self.widget_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 140))
        self.frame_22.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(34, 34, 34);\n"
"\n"
"\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_22)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_66 = QLabel(self.frame_22)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.label_66, 0, 1, 1, 1)

        self.label_24 = QLabel(self.frame_22)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.label_24, 0, 0, 1, 1)

        self.frame_48 = QFrame(self.frame_22)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 70))
        self.frame_48.setMaximumSize(QSize(16777215, 100))
        self.frame_48.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(17, 17, 17);\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_25 = QLabel(self.frame_48)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_11.addWidget(self.label_25)


        self.gridLayout_26.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_49 = QFrame(self.frame_22)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(17, 17, 17);\n"
"	\n"
"\n"
"\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_26 = QLabel(self.frame_49)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_12.addWidget(self.label_26)


        self.gridLayout_26.addWidget(self.frame_49, 1, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_22)

        self.frame_29 = QFrame(self.widget_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 140))
        self.frame_29.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(34, 34, 34);\n"
"\n"
"\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_29)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_88 = QLabel(self.frame_29)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"")

        self.gridLayout_27.addWidget(self.label_88, 0, 1, 1, 1)

        self.label_107 = QLabel(self.frame_29)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"")

        self.gridLayout_27.addWidget(self.label_107, 0, 0, 1, 1)

        self.frame_50 = QFrame(self.frame_29)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 70))
        self.frame_50.setMaximumSize(QSize(16777215, 100))
        self.frame_50.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(17, 17, 17);\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_108 = QLabel(self.frame_50)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_108)


        self.gridLayout_27.addWidget(self.frame_50, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.frame_29)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(17, 17, 17);\n"
"	\n"
"\n"
"\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_109 = QLabel(self.frame_51)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_14.addWidget(self.label_109)


        self.gridLayout_27.addWidget(self.frame_51, 1, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_29)

        self.label_67 = QLabel(self.widget_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(16777215, 14))

        self.verticalLayout_21.addWidget(self.label_67)

        self.tableWidget_8 = QTableWidget(self.widget_2)
        if (self.tableWidget_8.columnCount() < 3):
            self.tableWidget_8.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setMaximumSize(QSize(16777215, 286))
        self.tableWidget_8.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_8.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_8.setAlternatingRowColors(True)
        self.tableWidget_8.setShowGrid(False)
        self.tableWidget_8.setGridStyle(Qt.NoPen)
        self.tableWidget_8.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.tableWidget_8)


        self.gridLayout_3.addWidget(self.widget_2, 0, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"border-radius: 15px;\n"
"	\n"
"background: transparent;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.widget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(300, 0))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"border-radius: 15px;\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_21 = QFrame(self.widget_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 101))
        self.frame_21.setMaximumSize(QSize(16777215, 88))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius: 15px;\n"
"	\n"
"\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_21)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_35 = QLabel(self.frame_21)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_28.addWidget(self.label_35, 1, 0, 1, 2)

        self.label_34 = QLabel(self.frame_21)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_28.addWidget(self.label_34, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_21)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 23))
        self.label_33.setStyleSheet(u"")

        self.gridLayout_28.addWidget(self.label_33, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_21, 4, 0, 1, 2)

        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_19, 0, 0, 1, 2)

        self.tableWidget_7 = QTableWidget(self.widget_3)
        if (self.tableWidget_7.columnCount() < 3):
            self.tableWidget_7.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setMinimumSize(QSize(10, 50))
        self.tableWidget_7.setMaximumSize(QSize(16777215, 401))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(29, 29, 29, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(33, 37, 43, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_7.setPalette(palette)
        self.tableWidget_7.setAutoFillBackground(False)
        self.tableWidget_7.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_7.setFrameShape(QFrame.Box)
        self.tableWidget_7.setFrameShadow(QFrame.Plain)
        self.tableWidget_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_7.setAlternatingRowColors(True)
        self.tableWidget_7.setShowGrid(False)
        self.tableWidget_7.setGridStyle(Qt.NoPen)
        self.tableWidget_7.horizontalHeader().setVisible(True)
        self.tableWidget_7.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.tableWidget_7, 1, 0, 1, 2)

        self.frame_20 = QFrame(self.widget_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 78))
        self.frame_20.setMaximumSize(QSize(16777215, 110))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius: 15px;\n"
"	\n"
"\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_20)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_32 = QLabel(self.frame_20)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_29.addWidget(self.label_32, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_20)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 23))
        self.label_22.setStyleSheet(u"")

        self.gridLayout_29.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.frame_20)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_29.addWidget(self.label_23, 1, 0, 1, 2)


        self.gridLayout_6.addWidget(self.frame_20, 3, 0, 1, 2)

        self.frame_32 = QFrame(self.widget_3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 80))
        self.frame_32.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_123 = QGridLayout(self.frame_32)
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.pushButton_127 = QPushButton(self.frame_32)
        self.pushButton_127.setObjectName(u"pushButton_127")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/images/target.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_127.setIcon(icon6)
        self.pushButton_127.setIconSize(QSize(63, 45))

        self.gridLayout_123.addWidget(self.pushButton_127, 1, 1, 1, 1)

        self.pushButton_171 = QPushButton(self.frame_32)
        self.pushButton_171.setObjectName(u"pushButton_171")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/images/receipt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_171.setIcon(icon7)
        self.pushButton_171.setIconSize(QSize(53, 44))

        self.gridLayout_123.addWidget(self.pushButton_171, 1, 2, 1, 1)

        self.pushButton_145 = QPushButton(self.frame_32)
        self.pushButton_145.setObjectName(u"pushButton_145")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/images/checkout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_145.setIcon(icon8)
        self.pushButton_145.setIconSize(QSize(44, 47))

        self.gridLayout_123.addWidget(self.pushButton_145, 2, 1, 1, 1)

        self.pushButton_105 = QPushButton(self.frame_32)
        self.pushButton_105.setObjectName(u"pushButton_105")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/images/vendor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_105.setIcon(icon9)
        self.pushButton_105.setIconSize(QSize(53, 49))

        self.gridLayout_123.addWidget(self.pushButton_105, 1, 0, 1, 1)

        self.pushButton_172 = QPushButton(self.frame_32)
        self.pushButton_172.setObjectName(u"pushButton_172")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/images/ledger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_172.setIcon(icon10)
        self.pushButton_172.setIconSize(QSize(43, 46))

        self.gridLayout_123.addWidget(self.pushButton_172, 2, 2, 1, 1)

        self.pushButton_144 = QPushButton(self.frame_32)
        self.pushButton_144.setObjectName(u"pushButton_144")
        icon11 = QIcon()
        icon11.addFile(u":/images/images/images/accounting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_144.setIcon(icon11)
        self.pushButton_144.setIconSize(QSize(51, 41))

        self.gridLayout_123.addWidget(self.pushButton_144, 2, 0, 1, 1)

        self.label_384 = QLabel(self.frame_32)
        self.label_384.setObjectName(u"label_384")

        self.gridLayout_123.addWidget(self.label_384, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_32, 2, 0, 1, 2)


        self.verticalLayout_20.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{\n"
"border-radius: 15px;\n"
"	background: transparent;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setContentsMargins(-1, -1, 0, 1)

        self.verticalLayout_20.addWidget(self.widget_4)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.home)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_16)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_30.addWidget(self.label_8, 3, 2, 1, 1)

        self.frame_4 = QFrame(self.frame_16)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_68 = QGridLayout(self.frame_4)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 10))

        self.gridLayout_68.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 49))

        self.gridLayout_68.addWidget(self.label_18, 1, 0, 1, 1)


        self.gridLayout_30.addWidget(self.frame_4, 1, 2, 1, 1)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_30.addWidget(self.label_6, 3, 0, 1, 1)

        self.preloader = QFrame(self.frame_16)
        self.preloader.setObjectName(u"preloader")
        self.preloader.setStyleSheet(u"QFrame{\n"
"	\n"
"border-radius: 15px;\n"
"	\n"
"\n"
"}")
        self.preloader.setFrameShape(QFrame.StyledPanel)
        self.preloader.setFrameShadow(QFrame.Raised)

        self.gridLayout_30.addWidget(self.preloader, 4, 2, 1, 1)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_30.addWidget(self.frame_18, 4, 1, 1, 1)

        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 2))
        self.label_20.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_30.addWidget(self.label_20, 3, 1, 1, 1)

        self.label_63 = QLabel(self.frame_16)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 15))
        self.label_63.setMaximumSize(QSize(16777215, 15))
        self.label_63.setFont(font)
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_63, 5, 1, 1, 1)

        self.scrollArea = QScrollArea(self.frame_16)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 183))
        self.scrollArea.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 400, 183))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_30.addWidget(self.scrollArea, 6, 0, 1, 3)

        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_67 = QGridLayout(self.frame_13)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_67.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 59))

        self.gridLayout_67.addWidget(self.label_12, 1, 0, 1, 1)


        self.gridLayout_30.addWidget(self.frame_13, 0, 2, 1, 1)

        self.frame_31 = QFrame(self.frame_16)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 76))
        self.frame_31.setMaximumSize(QSize(300, 500))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 29, 29);\n"
"\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_31)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_89 = QLabel(self.frame_31)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 9))
        self.label_89.setMaximumSize(QSize(16777215, 17))
        self.label_89.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.label_89)

        self.label_27 = QLabel(self.frame_31)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 50))
        self.label_27.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.label_27)

        self.frame_52 = QFrame(self.frame_31)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 99))
        self.frame_52.setMaximumSize(QSize(300, 101))
        self.frame_52.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 29, 29);\n"
"\n"
"}")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_52)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_93 = QLabel(self.frame_52)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(0, 9))
        self.label_93.setMaximumSize(QSize(16777215, 17))
        self.label_93.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.label_93)

        self.label_37 = QLabel(self.frame_52)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 50))
        self.label_37.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_37)


        self.verticalLayout_16.addWidget(self.frame_52)


        self.gridLayout_30.addWidget(self.frame_31, 0, 0, 2, 2)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 136))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius: 15px;\n"
"	\n"
"\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_30.addWidget(self.frame_10, 4, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_16, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_23 = QGridLayout(self.page_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_15)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_35 = QFrame(self.frame_15)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 100))
        self.frame_35.setMaximumSize(QSize(16777215, 200))
        self.frame_35.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_35)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_78 = QLabel(self.frame_35)
        self.label_78.setObjectName(u"label_78")

        self.verticalLayout_27.addWidget(self.label_78)


        self.gridLayout_17.addWidget(self.frame_35, 1, 0, 1, 1)

        self.label_64 = QLabel(self.frame_15)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_17.addWidget(self.label_64, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_15, 0, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_70 = QPushButton(self.page_3)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-truck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_70.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.pushButton_70)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_26)

        self.pushButton_27 = QPushButton(self.page_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon13)
        self.pushButton_27.setIconSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.pushButton_27)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_28)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.page_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(100, 27))
        palette1 = QPalette()
        brush3 = QBrush(QColor(229, 229, 229, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(48, 48, 48, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_2.setPalette(palette1)
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_9.addWidget(self.comboBox_2)

        self.lineEdit_9 = QLineEdit(self.page_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_9.addWidget(self.lineEdit_9)

        self.pushButton_21 = QPushButton(self.page_3)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(16777215, 20))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon14)
        self.pushButton_21.setIconSize(QSize(28, 30))

        self.horizontalLayout_9.addWidget(self.pushButton_21)


        self.gridLayout_23.addLayout(self.horizontalLayout_9, 1, 2, 1, 2)

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_11)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.frame_24 = QFrame(self.frame_11)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 100))
        self.frame_24.setMaximumSize(QSize(16777215, 200))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_24)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_74 = QLabel(self.frame_24)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_74)


        self.gridLayout_32.addWidget(self.frame_24, 1, 0, 1, 1)

        self.label_54 = QLabel(self.frame_11)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_32.addWidget(self.label_54, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_11, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.page_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_59 = QLabel(self.frame_12)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_31.addWidget(self.label_59, 0, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_12)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 100))
        self.frame_34.setMaximumSize(QSize(16777215, 200))
        self.frame_34.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_34)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_77 = QLabel(self.frame_34)
        self.label_77.setObjectName(u"label_77")

        self.verticalLayout_28.addWidget(self.label_77)


        self.gridLayout_31.addWidget(self.frame_34, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_12, 0, 1, 1, 1)

        self.frame_33 = QFrame(self.page_3)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 144))
        self.frame_33.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_33)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_37 = QFrame(self.frame_33)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 100))
        self.frame_37.setMaximumSize(QSize(16777215, 200))
        self.frame_37.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_37)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_79 = QLabel(self.frame_37)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font)

        self.verticalLayout_26.addWidget(self.label_79)


        self.gridLayout_16.addWidget(self.frame_37, 1, 0, 1, 1)

        self.label_69 = QLabel(self.frame_33)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_16.addWidget(self.label_69, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_33, 0, 3, 1, 1)

        self.tableWidget_6 = QTableWidget(self.page_3)
        if (self.tableWidget_6.columnCount() < 10):
            self.tableWidget_6.setColumnCount(10)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setMaximumSize(QSize(16777215, 426))
        self.tableWidget_6.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"alternate-background-color: rgb(43, 43, 43);\n"
"")
        self.tableWidget_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setAlternatingRowColors(True)
        self.tableWidget_6.setGridStyle(Qt.NoPen)
        self.tableWidget_6.verticalHeader().setVisible(False)

        self.gridLayout_23.addWidget(self.tableWidget_6, 2, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.gridLayout_41 = QGridLayout(self.page_17)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.frame = QFrame(self.page_17)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_92 = QGridLayout(self.frame)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.frame_88 = QFrame(self.frame)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_39 = QVBoxLayout(self.frame_88)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_299 = QLabel(self.frame_88)
        self.label_299.setObjectName(u"label_299")

        self.verticalLayout_39.addWidget(self.label_299)

        self.lineEdit_62 = QLineEdit(self.frame_88)
        self.lineEdit_62.setObjectName(u"lineEdit_62")

        self.verticalLayout_39.addWidget(self.lineEdit_62)

        self.label_301 = QLabel(self.frame_88)
        self.label_301.setObjectName(u"label_301")

        self.verticalLayout_39.addWidget(self.label_301)

        self.comboBox_20 = QComboBox(self.frame_88)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.verticalLayout_39.addWidget(self.comboBox_20)

        self.label_302 = QLabel(self.frame_88)
        self.label_302.setObjectName(u"label_302")

        self.verticalLayout_39.addWidget(self.label_302)

        self.comboBox_21 = QComboBox(self.frame_88)
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.verticalLayout_39.addWidget(self.comboBox_21)


        self.gridLayout_92.addWidget(self.frame_88, 2, 3, 1, 1)

        self.pushButton_25 = QPushButton(self.frame)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(30, 30))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon15)

        self.gridLayout_92.addWidget(self.pushButton_25, 0, 0, 1, 1)

        self.orders_update_btn = QPushButton(self.frame)
        self.orders_update_btn.setObjectName(u"orders_update_btn")
        self.orders_update_btn.setMaximumSize(QSize(70, 30))
        self.orders_update_btn.setFont(font)
        self.orders_update_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.orders_update_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orders_update_btn.setIcon(icon16)

        self.gridLayout_92.addWidget(self.orders_update_btn, 1, 1, 1, 1)

        self.tableWidget_36 = QTableWidget(self.frame)
        if (self.tableWidget_36.columnCount() < 3):
            self.tableWidget_36.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_36.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_36.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_36.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        self.tableWidget_36.setObjectName(u"tableWidget_36")

        self.gridLayout_92.addWidget(self.tableWidget_36, 4, 3, 1, 2)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_92.addItem(self.horizontalSpacer_33, 1, 2, 1, 1)

        self.frame_86 = QFrame(self.frame)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_86)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setVerticalSpacing(0)
        self.pushButton_118 = QPushButton(self.frame_86)
        self.pushButton_118.setObjectName(u"pushButton_118")
        self.pushButton_118.setStyleSheet(u"background-color: rgb(0, 158, 158);")

        self.gridLayout_40.addWidget(self.pushButton_118, 3, 0, 1, 1)

        self.pushButton_119 = QPushButton(self.frame_86)
        self.pushButton_119.setObjectName(u"pushButton_119")
        self.pushButton_119.setStyleSheet(u"background-color: rgb(0, 158, 0);")

        self.gridLayout_40.addWidget(self.pushButton_119, 1, 0, 1, 1)

        self.pushButton_117 = QPushButton(self.frame_86)
        self.pushButton_117.setObjectName(u"pushButton_117")
        self.pushButton_117.setStyleSheet(u"background-color: rgb(85, 0, 255);")

        self.gridLayout_40.addWidget(self.pushButton_117, 4, 0, 1, 1)

        self.pushButton_120 = QPushButton(self.frame_86)
        self.pushButton_120.setObjectName(u"pushButton_120")
        self.pushButton_120.setStyleSheet(u"background-color: rgb(204, 21, 45);")

        self.gridLayout_40.addWidget(self.pushButton_120, 2, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_40.addItem(self.verticalSpacer_22, 5, 0, 1, 1)


        self.gridLayout_92.addWidget(self.frame_86, 2, 4, 1, 1)

        self.frame_87 = QFrame(self.frame)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.gridLayout_91 = QGridLayout(self.frame_87)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.gridLayout_91.setVerticalSpacing(18)
        self.lineEdit_3 = QLineEdit(self.frame_87)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_3, 3, 1, 1, 3)

        self.label_75 = QLabel(self.frame_87)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_91.addWidget(self.label_75, 3, 0, 1, 1)

        self.label_106 = QLabel(self.frame_87)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_91.addWidget(self.label_106, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_87)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_2, 2, 1, 1, 3)

        self.label_51 = QLabel(self.frame_87)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_91.addWidget(self.label_51, 7, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.frame_87)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_19.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_19, 5, 1, 1, 3)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_22, 10, 2, 1, 1)

        self.label_55 = QLabel(self.frame_87)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_91.addWidget(self.label_55, 1, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_23, 10, 3, 1, 1)

        self.label_85 = QLabel(self.frame_87)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_91.addWidget(self.label_85, 8, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_87)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_5, 4, 1, 1, 3)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_21, 10, 0, 1, 1)

        self.label_105 = QLabel(self.frame_87)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_91.addWidget(self.label_105, 2, 0, 1, 1)

        self.label_52 = QLabel(self.frame_87)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_91.addWidget(self.label_52, 5, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_18, 10, 1, 1, 1)

        self.label_84 = QLabel(self.frame_87)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_91.addWidget(self.label_84, 9, 0, 1, 1)

        self.label_96 = QLabel(self.frame_87)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_91.addWidget(self.label_96, 6, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_19, 0, 0, 1, 2)

        self.lineEdit_4 = QLineEdit(self.frame_87)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_4, 1, 1, 1, 3)

        self.lineEdit_24 = QLineEdit(self.frame_87)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_24, 8, 1, 1, 3)

        self.lineEdit_25 = QLineEdit(self.frame_87)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_91.addWidget(self.lineEdit_25, 9, 1, 1, 3)

        self.comboBox_49 = QComboBox(self.frame_87)
        self.comboBox_49.setObjectName(u"comboBox_49")

        self.gridLayout_91.addWidget(self.comboBox_49, 6, 1, 1, 2)

        self.comboBox_51 = QComboBox(self.frame_87)
        self.comboBox_51.setObjectName(u"comboBox_51")

        self.gridLayout_91.addWidget(self.comboBox_51, 7, 1, 1, 2)


        self.gridLayout_92.addWidget(self.frame_87, 2, 0, 3, 3)

        self.plainTextEdit_5 = QPlainTextEdit(self.frame)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setFrameShape(QFrame.Panel)
        self.plainTextEdit_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_92.addWidget(self.plainTextEdit_5, 3, 3, 1, 2)


        self.gridLayout_41.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_17)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.gridLayout_60 = QGridLayout(self.page_21)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.pushButton_83 = QPushButton(self.page_21)
        self.pushButton_83.setObjectName(u"pushButton_83")
        self.pushButton_83.setMinimumSize(QSize(45, 45))
        self.pushButton_83.setMaximumSize(QSize(76, 16777215))
        self.pushButton_83.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_83.setIcon(icon17)

        self.gridLayout_60.addWidget(self.pushButton_83, 0, 0, 1, 1)

        self.label_119 = QLabel(self.page_21)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_60.addWidget(self.label_119, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_29)

        self.comboBox_9 = QComboBox(self.page_21)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(143, 0))
        self.comboBox_9.setMaximumSize(QSize(119, 28))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_9.setPalette(palette2)
        self.comboBox_9.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_18.addWidget(self.comboBox_9)

        self.lineEdit_39 = QLineEdit(self.page_21)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_39.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_18.addWidget(self.lineEdit_39)

        self.pushButton_39 = QPushButton(self.page_21)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMaximumSize(QSize(16777215, 20))
        self.pushButton_39.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_39.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_39.setIcon(icon14)
        self.pushButton_39.setIconSize(QSize(28, 30))

        self.horizontalLayout_18.addWidget(self.pushButton_39)


        self.gridLayout_60.addLayout(self.horizontalLayout_18, 2, 1, 1, 1)

        self.frame_53 = QFrame(self.page_21)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_53)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.lib_btn4_7 = QPushButton(self.frame_53)
        self.lib_btn4_7.setObjectName(u"lib_btn4_7")
        self.lib_btn4_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn4_7.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.lib_btn4_7.setIcon(icon2)
        self.lib_btn4_7.setIconSize(QSize(44, 38))

        self.gridLayout_59.addWidget(self.lib_btn4_7, 0, 1, 1, 1)

        self.client_btn_3 = QPushButton(self.frame_53)
        self.client_btn_3.setObjectName(u"client_btn_3")
        self.client_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_btn_3.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.client_btn_3.setIcon(icon13)
        self.client_btn_3.setIconSize(QSize(49, 41))

        self.gridLayout_59.addWidget(self.client_btn_3, 0, 0, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_59.addItem(self.horizontalSpacer_59, 0, 2, 1, 1)


        self.gridLayout_60.addWidget(self.frame_53, 2, 0, 1, 1)

        self.tableWidget_14 = QTableWidget(self.page_21)
        if (self.tableWidget_14.columnCount() < 6):
            self.tableWidget_14.setColumnCount(6)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        self.tableWidget_14.setObjectName(u"tableWidget_14")
        self.tableWidget_14.setMinimumSize(QSize(759, 0))
        self.tableWidget_14.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"alternate-background-color: rgb(43, 43, 43);\n"
"")
        self.tableWidget_14.setAlternatingRowColors(True)
        self.tableWidget_14.setShowGrid(False)
        self.tableWidget_14.setGridStyle(Qt.NoPen)
        self.tableWidget_14.verticalHeader().setVisible(False)
        self.tableWidget_14.verticalHeader().setHighlightSections(True)

        self.gridLayout_60.addWidget(self.tableWidget_14, 3, 0, 1, 1)

        self.frame_58 = QFrame(self.page_21)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_120 = QGridLayout(self.frame_58)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.label_390 = QLabel(self.frame_58)
        self.label_390.setObjectName(u"label_390")

        self.gridLayout_120.addWidget(self.label_390, 3, 0, 1, 1)

        self.label_388 = QLabel(self.frame_58)
        self.label_388.setObjectName(u"label_388")

        self.gridLayout_120.addWidget(self.label_388, 6, 0, 1, 1)

        self.label_389 = QLabel(self.frame_58)
        self.label_389.setObjectName(u"label_389")

        self.gridLayout_120.addWidget(self.label_389, 5, 0, 1, 1)

        self.label_398 = QLabel(self.frame_58)
        self.label_398.setObjectName(u"label_398")

        self.gridLayout_120.addWidget(self.label_398, 6, 1, 1, 1)

        self.label_387 = QLabel(self.frame_58)
        self.label_387.setObjectName(u"label_387")

        self.gridLayout_120.addWidget(self.label_387, 7, 0, 1, 1)

        self.label_396 = QLabel(self.frame_58)
        self.label_396.setObjectName(u"label_396")

        self.gridLayout_120.addWidget(self.label_396, 5, 1, 1, 1)

        self.label_392 = QLabel(self.frame_58)
        self.label_392.setObjectName(u"label_392")

        self.gridLayout_120.addWidget(self.label_392, 10, 0, 1, 1)

        self.label_399 = QLabel(self.frame_58)
        self.label_399.setObjectName(u"label_399")

        self.gridLayout_120.addWidget(self.label_399, 8, 1, 1, 1)

        self.label_385 = QLabel(self.frame_58)
        self.label_385.setObjectName(u"label_385")

        self.gridLayout_120.addWidget(self.label_385, 9, 0, 1, 1)

        self.label_395 = QLabel(self.frame_58)
        self.label_395.setObjectName(u"label_395")

        self.gridLayout_120.addWidget(self.label_395, 4, 1, 1, 1)

        self.label_397 = QLabel(self.frame_58)
        self.label_397.setObjectName(u"label_397")

        self.gridLayout_120.addWidget(self.label_397, 7, 1, 1, 1)

        self.label_386 = QLabel(self.frame_58)
        self.label_386.setObjectName(u"label_386")

        self.gridLayout_120.addWidget(self.label_386, 8, 0, 1, 1)

        self.label_400 = QLabel(self.frame_58)
        self.label_400.setObjectName(u"label_400")

        self.gridLayout_120.addWidget(self.label_400, 9, 1, 1, 1)

        self.label_394 = QLabel(self.frame_58)
        self.label_394.setObjectName(u"label_394")

        self.gridLayout_120.addWidget(self.label_394, 3, 1, 1, 1)

        self.label_401 = QLabel(self.frame_58)
        self.label_401.setObjectName(u"label_401")

        self.gridLayout_120.addWidget(self.label_401, 10, 1, 1, 1)

        self.label_391 = QLabel(self.frame_58)
        self.label_391.setObjectName(u"label_391")

        self.gridLayout_120.addWidget(self.label_391, 4, 0, 1, 1)

        self.label_393 = QLabel(self.frame_58)
        self.label_393.setObjectName(u"label_393")

        self.gridLayout_120.addWidget(self.label_393, 0, 0, 1, 2)

        self.pushButton_177 = QPushButton(self.frame_58)
        self.pushButton_177.setObjectName(u"pushButton_177")
        self.pushButton_177.setIcon(icon9)
        self.pushButton_177.setIconSize(QSize(99, 86))

        self.gridLayout_120.addWidget(self.pushButton_177, 1, 0, 1, 2)


        self.gridLayout_60.addWidget(self.frame_58, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_21)
        self.page_59 = QWidget()
        self.page_59.setObjectName(u"page_59")
        self.gridLayout_116 = QGridLayout(self.page_59)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.pushButton_161 = QPushButton(self.page_59)
        self.pushButton_161.setObjectName(u"pushButton_161")

        self.gridLayout_116.addWidget(self.pushButton_161, 0, 0, 1, 1)

        self.label_373 = QLabel(self.page_59)
        self.label_373.setObjectName(u"label_373")

        self.gridLayout_116.addWidget(self.label_373, 1, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_116.addItem(self.horizontalSpacer_14, 0, 1, 1, 1)

        self.tableWidget_43 = QTableWidget(self.page_59)
        self.tableWidget_43.setObjectName(u"tableWidget_43")

        self.gridLayout_116.addWidget(self.tableWidget_43, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_59)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_34 = QGridLayout(self.page_8)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_95 = QLabel(self.page_8)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_34.addWidget(self.label_95, 5, 0, 1, 1)

        self.pushButton_68 = QPushButton(self.page_8)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(45, 45))
        self.pushButton_68.setMaximumSize(QSize(30, 16777215))
        self.pushButton_68.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_68.setIcon(icon17)
        self.pushButton_68.setIconSize(QSize(26, 30))

        self.gridLayout_34.addWidget(self.pushButton_68, 0, 0, 1, 1)

        self.lineEdit_28 = QLineEdit(self.page_8)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(27, 27, 27);")
        self.lineEdit_28.setReadOnly(True)

        self.gridLayout_34.addWidget(self.lineEdit_28, 2, 1, 1, 1)

        self.lineEdit_32 = QLineEdit(self.page_8)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_34.addWidget(self.lineEdit_32, 6, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.lineEdit_30 = QLineEdit(self.page_8)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_34.addWidget(self.lineEdit_30, 4, 1, 1, 1)

        self.label_61 = QLabel(self.page_8)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_34.addWidget(self.label_61, 2, 0, 1, 1)

        self.label_4 = QLabel(self.page_8)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_34.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_31 = QLineEdit(self.page_8)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_34.addWidget(self.lineEdit_31, 5, 1, 1, 1)

        self.pushButton_32 = QPushButton(self.page_8)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_32.setIcon(icon16)

        self.gridLayout_34.addWidget(self.pushButton_32, 7, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.pushButton_48 = QPushButton(self.page_8)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(80, 0))
        self.pushButton_48.setMaximumSize(QSize(89, 16777215))
        self.pushButton_48.setStyleSheet(u"background-color: rgb(0, 198, 0);")

        self.gridLayout_34.addWidget(self.pushButton_48, 1, 3, 1, 1)

        self.tableWidget_9 = QTableWidget(self.page_8)
        if (self.tableWidget_9.columnCount() < 8):
            self.tableWidget_9.setColumnCount(8)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(7, __qtablewidgetitem32)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_34.addWidget(self.tableWidget_9, 8, 0, 1, 4)

        self.label_103 = QLabel(self.page_8)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_34.addWidget(self.label_103, 6, 0, 1, 1)

        self.label_70 = QLabel(self.page_8)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_34.addWidget(self.label_70, 4, 0, 1, 1)

        self.label_62 = QLabel(self.page_8)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_34.addWidget(self.label_62, 3, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.page_8)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_34.addWidget(self.lineEdit_29, 3, 1, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_58, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.gridLayout_42 = QGridLayout(self.page_20)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_154 = QLabel(self.page_20)
        self.label_154.setObjectName(u"label_154")

        self.gridLayout_42.addWidget(self.label_154, 7, 0, 1, 1)

        self.label_169 = QLabel(self.page_20)
        self.label_169.setObjectName(u"label_169")

        self.gridLayout_42.addWidget(self.label_169, 6, 4, 1, 1)

        self.label_153 = QLabel(self.page_20)
        self.label_153.setObjectName(u"label_153")

        self.gridLayout_42.addWidget(self.label_153, 6, 0, 1, 1)

        self.label_171 = QLabel(self.page_20)
        self.label_171.setObjectName(u"label_171")

        self.gridLayout_42.addWidget(self.label_171, 2, 3, 1, 1)

        self.label_148 = QLabel(self.page_20)
        self.label_148.setObjectName(u"label_148")

        self.gridLayout_42.addWidget(self.label_148, 4, 0, 1, 1)

        self.label_158 = QLabel(self.page_20)
        self.label_158.setObjectName(u"label_158")

        self.gridLayout_42.addWidget(self.label_158, 6, 2, 1, 1)

        self.label_162 = QLabel(self.page_20)
        self.label_162.setObjectName(u"label_162")

        self.gridLayout_42.addWidget(self.label_162, 3, 3, 1, 1)

        self.label_159 = QLabel(self.page_20)
        self.label_159.setObjectName(u"label_159")

        self.gridLayout_42.addWidget(self.label_159, 7, 2, 1, 1)

        self.label_145 = QLabel(self.page_20)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_42.addWidget(self.label_145, 3, 0, 1, 1)

        self.label_168 = QLabel(self.page_20)
        self.label_168.setObjectName(u"label_168")

        self.gridLayout_42.addWidget(self.label_168, 5, 4, 1, 1)

        self.label_144 = QLabel(self.page_20)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_42.addWidget(self.label_144, 1, 0, 1, 1)

        self.label_160 = QLabel(self.page_20)
        self.label_160.setObjectName(u"label_160")

        self.gridLayout_42.addWidget(self.label_160, 2, 2, 1, 1)

        self.label_163 = QLabel(self.page_20)
        self.label_163.setObjectName(u"label_163")

        self.gridLayout_42.addWidget(self.label_163, 5, 3, 1, 1)

        self.label_166 = QLabel(self.page_20)
        self.label_166.setObjectName(u"label_166")

        self.gridLayout_42.addWidget(self.label_166, 3, 4, 1, 1)

        self.label_164 = QLabel(self.page_20)
        self.label_164.setObjectName(u"label_164")

        self.gridLayout_42.addWidget(self.label_164, 6, 3, 1, 1)

        self.label_155 = QLabel(self.page_20)
        self.label_155.setObjectName(u"label_155")

        self.gridLayout_42.addWidget(self.label_155, 8, 2, 1, 1)

        self.label_165 = QLabel(self.page_20)
        self.label_165.setObjectName(u"label_165")

        self.gridLayout_42.addWidget(self.label_165, 4, 3, 1, 1)

        self.label_156 = QLabel(self.page_20)
        self.label_156.setObjectName(u"label_156")

        self.gridLayout_42.addWidget(self.label_156, 3, 2, 1, 1)

        self.label_157 = QLabel(self.page_20)
        self.label_157.setObjectName(u"label_157")

        self.gridLayout_42.addWidget(self.label_157, 4, 2, 2, 1)

        self.label_167 = QLabel(self.page_20)
        self.label_167.setObjectName(u"label_167")

        self.gridLayout_42.addWidget(self.label_167, 4, 4, 1, 1)

        self.label_152 = QLabel(self.page_20)
        self.label_152.setObjectName(u"label_152")

        self.gridLayout_42.addWidget(self.label_152, 5, 0, 1, 1)

        self.pushButton_69 = QPushButton(self.page_20)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMinimumSize(QSize(45, 45))
        self.pushButton_69.setMaximumSize(QSize(67, 16777215))
        self.pushButton_69.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_69.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_69.setIcon(icon17)
        self.pushButton_69.setIconSize(QSize(26, 30))

        self.gridLayout_42.addWidget(self.pushButton_69, 0, 0, 1, 1)

        self.tableWidget_15 = QTableWidget(self.page_20)
        if (self.tableWidget_15.columnCount() < 5):
            self.tableWidget_15.setColumnCount(5)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        self.tableWidget_15.setObjectName(u"tableWidget_15")
        self.tableWidget_15.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"alternate-background-color: rgb(43, 43, 43);\n"
"")
        self.tableWidget_15.setAlternatingRowColors(True)
        self.tableWidget_15.setGridStyle(Qt.NoPen)
        self.tableWidget_15.verticalHeader().setVisible(False)

        self.gridLayout_42.addWidget(self.tableWidget_15, 9, 0, 1, 5)

        self.label_358 = QLabel(self.page_20)
        self.label_358.setObjectName(u"label_358")

        self.gridLayout_42.addWidget(self.label_358, 2, 0, 1, 1)

        self.label_359 = QLabel(self.page_20)
        self.label_359.setObjectName(u"label_359")

        self.gridLayout_42.addWidget(self.label_359, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_20)
        self.page_31 = QWidget()
        self.page_31.setObjectName(u"page_31")
        self.verticalLayout_17 = QVBoxLayout(self.page_31)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_21 = QLabel(self.page_31)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_17.addWidget(self.label_21)

        self.frame_97 = QFrame(self.page_31)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(0, 45))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton_130 = QPushButton(self.frame_97)
        self.pushButton_130.setObjectName(u"pushButton_130")
        self.pushButton_130.setMinimumSize(QSize(50, 45))
        self.pushButton_130.setIcon(icon17)

        self.horizontalLayout_29.addWidget(self.pushButton_130)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_36)


        self.verticalLayout_17.addWidget(self.frame_97)

        self.label_36 = QLabel(self.page_31)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_17.addWidget(self.label_36)

        self.tableWidget_24 = QTableWidget(self.page_31)
        if (self.tableWidget_24.columnCount() < 5):
            self.tableWidget_24.setColumnCount(5)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_24.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        self.tableWidget_24.setObjectName(u"tableWidget_24")
        self.tableWidget_24.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_24.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_24.setAlternatingRowColors(True)
        self.tableWidget_24.setGridStyle(Qt.NoPen)
        self.tableWidget_24.verticalHeader().setVisible(False)

        self.verticalLayout_17.addWidget(self.tableWidget_24)

        self.stackedWidget.addWidget(self.page_31)
        self.page_32 = QWidget()
        self.page_32.setObjectName(u"page_32")
        self.gridLayout_69 = QGridLayout(self.page_32)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.client_btn_4 = QPushButton(self.page_32)
        self.client_btn_4.setObjectName(u"client_btn_4")
        self.client_btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_btn_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.client_btn_4.setIcon(icon13)
        self.client_btn_4.setIconSize(QSize(49, 41))

        self.gridLayout_69.addWidget(self.client_btn_4, 2, 0, 1, 1)

        self.frame_98 = QFrame(self.page_32)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 45))
        self.frame_98.setMaximumSize(QSize(16777215, 30))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_131 = QPushButton(self.frame_98)
        self.pushButton_131.setObjectName(u"pushButton_131")
        self.pushButton_131.setMinimumSize(QSize(50, 35))
        self.pushButton_131.setIcon(icon17)

        self.horizontalLayout_30.addWidget(self.pushButton_131)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_37)


        self.gridLayout_69.addWidget(self.frame_98, 0, 0, 1, 2)

        self.label_42 = QLabel(self.page_32)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 39))
        self.label_42.setMaximumSize(QSize(16777215, 58))

        self.gridLayout_69.addWidget(self.label_42, 1, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_69.addItem(self.horizontalSpacer_11, 2, 1, 1, 1)

        self.tableWidget_25 = QTableWidget(self.page_32)
        if (self.tableWidget_25.columnCount() < 5):
            self.tableWidget_25.setColumnCount(5)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_25.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        self.tableWidget_25.setObjectName(u"tableWidget_25")
        self.tableWidget_25.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_25.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_25.setAlternatingRowColors(True)
        self.tableWidget_25.setGridStyle(Qt.NoPen)
        self.tableWidget_25.verticalHeader().setVisible(False)

        self.gridLayout_69.addWidget(self.tableWidget_25, 3, 0, 1, 4)

        self.frame_108 = QFrame(self.page_32)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.comboBox_39 = QComboBox(self.frame_108)
        self.comboBox_39.setObjectName(u"comboBox_39")
        self.comboBox_39.setMinimumSize(QSize(143, 0))
        self.comboBox_39.setMaximumSize(QSize(119, 28))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_39.setPalette(palette3)
        self.comboBox_39.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_36.addWidget(self.comboBox_39)

        self.lineEdit_80 = QLineEdit(self.frame_108)
        self.lineEdit_80.setObjectName(u"lineEdit_80")
        self.lineEdit_80.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_80.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_36.addWidget(self.lineEdit_80)

        self.pushButton_151 = QPushButton(self.frame_108)
        self.pushButton_151.setObjectName(u"pushButton_151")
        self.pushButton_151.setMaximumSize(QSize(16777215, 20))
        self.pushButton_151.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_151.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_151.setIcon(icon14)
        self.pushButton_151.setIconSize(QSize(28, 30))

        self.horizontalLayout_36.addWidget(self.pushButton_151)


        self.gridLayout_69.addWidget(self.frame_108, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_32)
        self.page_62 = QWidget()
        self.page_62.setObjectName(u"page_62")
        self.gridLayout_119 = QGridLayout(self.page_62)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.label_381 = QLabel(self.page_62)
        self.label_381.setObjectName(u"label_381")

        self.gridLayout_119.addWidget(self.label_381, 1, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.page_62)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_119.addWidget(self.checkBox_8, 2, 0, 1, 2)

        self.lineEdit_95 = QLineEdit(self.page_62)
        self.lineEdit_95.setObjectName(u"lineEdit_95")

        self.gridLayout_119.addWidget(self.lineEdit_95, 1, 1, 1, 2)

        self.verticalSpacer_32 = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_119.addItem(self.verticalSpacer_32, 5, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.page_62)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_119.addWidget(self.checkBox_9, 3, 0, 1, 2)

        self.frame_118 = QFrame(self.page_62)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(0, 0))
        self.frame_118.setMaximumSize(QSize(16777215, 16777215))
        self.frame_118.setStyleSheet(u"")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_55 = QSpacerItem(12, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_55)

        self.pushButton_168 = QPushButton(self.frame_118)
        self.pushButton_168.setObjectName(u"pushButton_168")
        self.pushButton_168.setStyleSheet(u"background-color: rgb(0, 198, 0);")
        self.pushButton_168.setIcon(icon16)

        self.horizontalLayout_47.addWidget(self.pushButton_168)

        self.pushButton_169 = QPushButton(self.frame_118)
        self.pushButton_169.setObjectName(u"pushButton_169")
        self.pushButton_169.setStyleSheet(u"background-color: rgb(236, 14, 18);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_169.setIcon(icon18)

        self.horizontalLayout_47.addWidget(self.pushButton_169)

        self.pushButton_170 = QPushButton(self.frame_118)
        self.pushButton_170.setObjectName(u"pushButton_170")
        self.pushButton_170.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_47.addWidget(self.pushButton_170)


        self.gridLayout_119.addWidget(self.frame_118, 4, 0, 1, 3)

        self.verticalSpacer_31 = QSpacerItem(20, 219, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_119.addItem(self.verticalSpacer_31, 0, 2, 1, 1)

        self.horizontalSpacer_57 = QSpacerItem(755, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_119.addItem(self.horizontalSpacer_57, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_62)
        self.page_61 = QWidget()
        self.page_61.setObjectName(u"page_61")
        self.gridLayout_20 = QGridLayout(self.page_61)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_31 = QLabel(self.page_61)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_20.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_379 = QLabel(self.page_61)
        self.label_379.setObjectName(u"label_379")

        self.gridLayout_20.addWidget(self.label_379, 3, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_11, 6, 2, 1, 1)

        self.lineEdit_94 = QLineEdit(self.page_61)
        self.lineEdit_94.setObjectName(u"lineEdit_94")

        self.gridLayout_20.addWidget(self.lineEdit_94, 1, 1, 1, 2)

        self.label_380 = QLabel(self.page_61)
        self.label_380.setObjectName(u"label_380")

        self.gridLayout_20.addWidget(self.label_380, 4, 0, 1, 1)

        self.frame_57 = QFrame(self.page_61)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_53)

        self.pushButton_166 = QPushButton(self.frame_57)
        self.pushButton_166.setObjectName(u"pushButton_166")
        self.pushButton_166.setStyleSheet(u"background-color: rgb(0, 197, 0);")
        self.pushButton_166.setIcon(icon16)
        self.pushButton_166.setIconSize(QSize(16, 35))

        self.horizontalLayout_46.addWidget(self.pushButton_166)

        self.pushButton_167 = QPushButton(self.frame_57)
        self.pushButton_167.setObjectName(u"pushButton_167")

        self.horizontalLayout_46.addWidget(self.pushButton_167)


        self.gridLayout_20.addWidget(self.frame_57, 5, 1, 1, 2)

        self.checkBox_7 = QCheckBox(self.page_61)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_20.addWidget(self.checkBox_7, 4, 1, 1, 2)

        self.verticalSpacer_30 = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_30, 0, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.page_61)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_20.addWidget(self.checkBox_6, 3, 1, 1, 2)

        self.horizontalSpacer_54 = QSpacerItem(1018, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_54, 2, 3, 2, 1)

        self.stackedWidget.addWidget(self.page_61)
        self.page_34 = QWidget()
        self.page_34.setObjectName(u"page_34")
        self.gridLayout_71 = QGridLayout(self.page_34)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.pushButton_63 = QPushButton(self.page_34)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setIcon(icon15)

        self.gridLayout_71.addWidget(self.pushButton_63, 0, 0, 1, 1)

        self.pushButton_53 = QPushButton(self.page_34)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(30, 0))
        self.pushButton_53.setMaximumSize(QSize(87, 16777215))
        self.pushButton_53.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_53.setIcon(icon13)
        self.pushButton_53.setIconSize(QSize(28, 52))

        self.gridLayout_71.addWidget(self.pushButton_53, 3, 0, 2, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_71.addItem(self.horizontalSpacer_13, 3, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_71.addItem(self.horizontalSpacer_32, 3, 4, 1, 1)

        self.frame_93 = QFrame(self.page_34)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMaximumSize(QSize(900, 16777215))
        self.frame_93.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background: transparent;\n"
"	\n"
"	\n"
"	\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.comboBox_25 = QComboBox(self.frame_93)
        self.comboBox_25.setObjectName(u"comboBox_25")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_25.setPalette(palette4)
        self.comboBox_25.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_28.addWidget(self.comboBox_25)

        self.lineEdit_64 = QLineEdit(self.frame_93)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        self.lineEdit_64.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_64.sizePolicy().hasHeightForWidth())
        self.lineEdit_64.setSizePolicy(sizePolicy)
        self.lineEdit_64.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_28.addWidget(self.lineEdit_64)

        self.pushButton_123 = QPushButton(self.frame_93)
        self.pushButton_123.setObjectName(u"pushButton_123")
        self.pushButton_123.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_123.setIcon(icon14)
        self.pushButton_123.setIconSize(QSize(28, 30))

        self.horizontalLayout_28.addWidget(self.pushButton_123)


        self.gridLayout_71.addWidget(self.frame_93, 4, 3, 1, 2)

        self.tableWidget_27 = QTableWidget(self.page_34)
        if (self.tableWidget_27.columnCount() < 7):
            self.tableWidget_27.setColumnCount(7)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_27.setHorizontalHeaderItem(6, __qtablewidgetitem54)
        self.tableWidget_27.setObjectName(u"tableWidget_27")
        self.tableWidget_27.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_27.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_27.setAlternatingRowColors(True)
        self.tableWidget_27.setGridStyle(Qt.NoPen)
        self.tableWidget_27.verticalHeader().setVisible(False)

        self.gridLayout_71.addWidget(self.tableWidget_27, 5, 0, 1, 4)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_71.addItem(self.horizontalSpacer_35, 3, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_71.addItem(self.horizontalSpacer_20, 3, 3, 1, 1)

        self.label_45 = QLabel(self.page_34)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_71.addWidget(self.label_45, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_34)
        self.page_35 = QWidget()
        self.page_35.setObjectName(u"page_35")
        self.gridLayout_74 = QGridLayout(self.page_35)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.frame_71 = QFrame(self.page_35)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout_73 = QGridLayout(self.frame_71)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_73.addItem(self.verticalSpacer_19, 3, 0, 1, 1)

        self.frame_61 = QFrame(self.frame_71)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Sunken)
        self.frame_61.setLineWidth(-4)
        self.gridLayout_72 = QGridLayout(self.frame_61)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.label_60 = QLabel(self.frame_61)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_72.addWidget(self.label_60, 3, 0, 1, 1)

        self.label_50 = QLabel(self.frame_61)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_72.addWidget(self.label_50, 0, 0, 1, 2)

        self.label_71 = QLabel(self.frame_61)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_72.addWidget(self.label_71, 2, 1, 1, 1)

        self.label_58 = QLabel(self.frame_61)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_72.addWidget(self.label_58, 2, 0, 1, 1)

        self.label_65 = QLabel(self.frame_61)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_72.addWidget(self.label_65, 3, 1, 1, 1)

        self.label_57 = QLabel(self.frame_61)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_72.addWidget(self.label_57, 1, 0, 1, 2)

        self.pushButton_98 = QPushButton(self.frame_61)
        self.pushButton_98.setObjectName(u"pushButton_98")

        self.gridLayout_72.addWidget(self.pushButton_98, 4, 1, 1, 1)

        self.pushButton_95 = QPushButton(self.frame_61)
        self.pushButton_95.setObjectName(u"pushButton_95")

        self.gridLayout_72.addWidget(self.pushButton_95, 4, 0, 1, 1)


        self.gridLayout_73.addWidget(self.frame_61, 1, 0, 1, 2)

        self.pushButton_76 = QPushButton(self.frame_71)
        self.pushButton_76.setObjectName(u"pushButton_76")

        self.gridLayout_73.addWidget(self.pushButton_76, 0, 0, 1, 1)


        self.gridLayout_74.addWidget(self.frame_71, 0, 0, 1, 1)

        self.frame_72 = QFrame(self.page_35)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.gridLayout_75 = QGridLayout(self.frame_72)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.label_83 = QLabel(self.frame_72)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_75.addWidget(self.label_83, 0, 0, 1, 1)

        self.label_101 = QLabel(self.frame_72)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_75.addWidget(self.label_101, 1, 0, 1, 1)

        self.label_127 = QLabel(self.frame_72)
        self.label_127.setObjectName(u"label_127")

        self.gridLayout_75.addWidget(self.label_127, 1, 1, 1, 1)

        self.label_121 = QLabel(self.frame_72)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_75.addWidget(self.label_121, 0, 1, 1, 1)

        self.label_135 = QLabel(self.frame_72)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_75.addWidget(self.label_135, 2, 0, 1, 1)

        self.plainTextEdit_8 = QPlainTextEdit(self.frame_72)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setReadOnly(True)

        self.gridLayout_75.addWidget(self.plainTextEdit_8, 4, 0, 1, 2)

        self.tableWidget_28 = QTableWidget(self.frame_72)
        if (self.tableWidget_28.columnCount() < 6):
            self.tableWidget_28.setColumnCount(6)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_28.setHorizontalHeaderItem(5, __qtablewidgetitem60)
        self.tableWidget_28.setObjectName(u"tableWidget_28")
        self.tableWidget_28.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_28.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_28.setAlternatingRowColors(True)
        self.tableWidget_28.setGridStyle(Qt.NoPen)
        self.tableWidget_28.verticalHeader().setVisible(False)

        self.gridLayout_75.addWidget(self.tableWidget_28, 3, 0, 1, 1)


        self.gridLayout_74.addWidget(self.frame_72, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_35)
        self.page_33 = QWidget()
        self.page_33.setObjectName(u"page_33")
        self.gridLayout_70 = QGridLayout(self.page_33)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.pushButton_52 = QPushButton(self.page_33)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setStyleSheet(u"")
        self.pushButton_52.setIcon(icon15)

        self.gridLayout_70.addWidget(self.pushButton_52, 0, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.page_33)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_23.setIcon(icon13)
        self.pushButton_23.setIconSize(QSize(51, 47))

        self.gridLayout_70.addWidget(self.pushButton_23, 3, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_70.addItem(self.horizontalSpacer_12, 3, 2, 1, 1)

        self.label_44 = QLabel(self.page_33)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_70.addWidget(self.label_44, 1, 0, 1, 1)

        self.frame_109 = QFrame(self.page_33)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.comboBox_40 = QComboBox(self.frame_109)
        self.comboBox_40.setObjectName(u"comboBox_40")
        self.comboBox_40.setMinimumSize(QSize(143, 0))
        self.comboBox_40.setMaximumSize(QSize(119, 28))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_40.setPalette(palette5)
        self.comboBox_40.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_37.addWidget(self.comboBox_40)

        self.lineEdit_81 = QLineEdit(self.frame_109)
        self.lineEdit_81.setObjectName(u"lineEdit_81")
        self.lineEdit_81.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_81.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_37.addWidget(self.lineEdit_81)

        self.pushButton_152 = QPushButton(self.frame_109)
        self.pushButton_152.setObjectName(u"pushButton_152")
        self.pushButton_152.setMaximumSize(QSize(16777215, 20))
        self.pushButton_152.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_152.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_152.setIcon(icon14)
        self.pushButton_152.setIconSize(QSize(28, 30))

        self.horizontalLayout_37.addWidget(self.pushButton_152)


        self.gridLayout_70.addWidget(self.frame_109, 3, 3, 1, 1)

        self.tableWidget_26 = QTableWidget(self.page_33)
        if (self.tableWidget_26.columnCount() < 6):
            self.tableWidget_26.setColumnCount(6)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_26.setHorizontalHeaderItem(5, __qtablewidgetitem66)
        self.tableWidget_26.setObjectName(u"tableWidget_26")
        self.tableWidget_26.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_26.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_26.setAlternatingRowColors(True)
        self.tableWidget_26.setGridStyle(Qt.NoPen)
        self.tableWidget_26.verticalHeader().setVisible(False)

        self.gridLayout_70.addWidget(self.tableWidget_26, 4, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_33)
        self.page_63 = QWidget()
        self.page_63.setObjectName(u"page_63")
        self.gridLayout_121 = QGridLayout(self.page_63)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.label_402 = QLabel(self.page_63)
        self.label_402.setObjectName(u"label_402")

        self.gridLayout_121.addWidget(self.label_402, 1, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.page_63)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_121.addWidget(self.lineEdit_22, 1, 1, 1, 2)

        self.checkBox_4 = QCheckBox(self.page_63)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_121.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(676, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_121.addItem(self.horizontalSpacer_61, 4, 3, 1, 1)

        self.label_403 = QLabel(self.page_63)
        self.label_403.setObjectName(u"label_403")

        self.gridLayout_121.addWidget(self.label_403, 2, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_121.addItem(self.verticalSpacer_23, 6, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_121.addItem(self.verticalSpacer_18, 0, 2, 1, 1)

        self.frame_60 = QFrame(self.page_63)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.pushButton_173 = QPushButton(self.frame_60)
        self.pushButton_173.setObjectName(u"pushButton_173")
        self.pushButton_173.setIcon(icon16)

        self.horizontalLayout_48.addWidget(self.pushButton_173)

        self.pushButton_174 = QPushButton(self.frame_60)
        self.pushButton_174.setObjectName(u"pushButton_174")

        self.horizontalLayout_48.addWidget(self.pushButton_174)

        self.pushButton_175 = QPushButton(self.frame_60)
        self.pushButton_175.setObjectName(u"pushButton_175")
        self.pushButton_175.setStyleSheet(u"background-color: rgb(240, 0, 0);")

        self.horizontalLayout_48.addWidget(self.pushButton_175)


        self.gridLayout_121.addWidget(self.frame_60, 5, 1, 1, 2)

        self.comboBox_53 = QComboBox(self.page_63)
        self.comboBox_53.setObjectName(u"comboBox_53")

        self.gridLayout_121.addWidget(self.comboBox_53, 2, 1, 1, 2)

        self.checkBox_10 = QCheckBox(self.page_63)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_121.addWidget(self.checkBox_10, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_63)
        self.page_36 = QWidget()
        self.page_36.setObjectName(u"page_36")
        self.gridLayout_83 = QGridLayout(self.page_36)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.label_174 = QLabel(self.page_36)
        self.label_174.setObjectName(u"label_174")

        self.gridLayout_83.addWidget(self.label_174, 2, 0, 1, 1)

        self.frame_77 = QFrame(self.page_36)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Sunken)
        self.gridLayout_81 = QGridLayout(self.frame_77)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.checkBox = QCheckBox(self.frame_77)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_81.addWidget(self.checkBox, 7, 1, 1, 2)

        self.label_142 = QLabel(self.frame_77)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_81.addWidget(self.label_142, 4, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_77)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_81.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.comboBox_13 = QComboBox(self.frame_77)
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.gridLayout_81.addWidget(self.comboBox_13, 5, 2, 1, 1)

        self.dateEdit_2 = QDateEdit(self.frame_77)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.dateEdit_2.setCalendarPopup(True)

        self.gridLayout_81.addWidget(self.dateEdit_2, 6, 2, 1, 1)

        self.label_146 = QLabel(self.frame_77)
        self.label_146.setObjectName(u"label_146")

        self.gridLayout_81.addWidget(self.label_146, 5, 0, 1, 1)

        self.label_175 = QLabel(self.frame_77)
        self.label_175.setObjectName(u"label_175")

        self.gridLayout_81.addWidget(self.label_175, 6, 0, 1, 1)

        self.dateEdit = QDateEdit(self.frame_77)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_81.addWidget(self.dateEdit, 4, 2, 1, 1)

        self.pushButton_114 = QPushButton(self.frame_77)
        self.pushButton_114.setObjectName(u"pushButton_114")
        self.pushButton_114.setStyleSheet(u"background-color: rgb(48, 143, 0);")

        self.gridLayout_81.addWidget(self.pushButton_114, 2, 0, 1, 1)

        self.label_137 = QLabel(self.frame_77)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_81.addWidget(self.label_137, 3, 0, 1, 2)


        self.gridLayout_83.addWidget(self.frame_77, 1, 0, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.page_36)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout_83.addWidget(self.plainTextEdit_4, 3, 0, 1, 1)

        self.pushButton_77 = QPushButton(self.page_36)
        self.pushButton_77.setObjectName(u"pushButton_77")
        self.pushButton_77.setMinimumSize(QSize(82, 0))
        self.pushButton_77.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_83.addWidget(self.pushButton_77, 0, 0, 1, 1)

        self.tableWidget_29 = QTableWidget(self.page_36)
        if (self.tableWidget_29.columnCount() < 6):
            self.tableWidget_29.setColumnCount(6)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_29.setHorizontalHeaderItem(5, __qtablewidgetitem72)
        self.tableWidget_29.setObjectName(u"tableWidget_29")
        self.tableWidget_29.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_29.setFrameShadow(QFrame.Plain)
        self.tableWidget_29.setAlternatingRowColors(True)
        self.tableWidget_29.setGridStyle(Qt.NoPen)
        self.tableWidget_29.verticalHeader().setVisible(False)

        self.gridLayout_83.addWidget(self.tableWidget_29, 2, 1, 2, 1)

        self.frame_85 = QFrame(self.page_36)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_184 = QLabel(self.frame_85)
        self.label_184.setObjectName(u"label_184")

        self.horizontalLayout_27.addWidget(self.label_184)

        self.label_260 = QLabel(self.frame_85)
        self.label_260.setObjectName(u"label_260")

        self.horizontalLayout_27.addWidget(self.label_260)


        self.gridLayout_83.addWidget(self.frame_85, 4, 1, 1, 1)

        self.frame_78 = QFrame(self.page_36)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Sunken)
        self.gridLayout_82 = QGridLayout(self.frame_78)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.label_187 = QLabel(self.frame_78)
        self.label_187.setObjectName(u"label_187")

        self.gridLayout_82.addWidget(self.label_187, 1, 0, 1, 1)

        self.comboBox_16 = QComboBox(self.frame_78)
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.gridLayout_82.addWidget(self.comboBox_16, 3, 1, 1, 2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_82.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)

        self.pushButton_116 = QPushButton(self.frame_78)
        self.pushButton_116.setObjectName(u"pushButton_116")
        self.pushButton_116.setIcon(icon13)

        self.gridLayout_82.addWidget(self.pushButton_116, 5, 2, 1, 1)

        self.label_191 = QLabel(self.frame_78)
        self.label_191.setObjectName(u"label_191")

        self.gridLayout_82.addWidget(self.label_191, 2, 0, 1, 1)

        self.label_203 = QLabel(self.frame_78)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout_82.addWidget(self.label_203, 3, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.frame_78)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_82.addWidget(self.lineEdit_18, 2, 1, 1, 2)

        self.comboBox_15 = QComboBox(self.frame_78)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout_82.addWidget(self.comboBox_15, 1, 1, 1, 2)

        self.pushButton_115 = QPushButton(self.frame_78)
        self.pushButton_115.setObjectName(u"pushButton_115")
        self.pushButton_115.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.pushButton_115.setIconSize(QSize(72, 67))

        self.gridLayout_82.addWidget(self.pushButton_115, 0, 2, 1, 1)

        self.label_297 = QLabel(self.frame_78)
        self.label_297.setObjectName(u"label_297")

        self.gridLayout_82.addWidget(self.label_297, 4, 0, 1, 1)

        self.lineEdit_61 = QLineEdit(self.frame_78)
        self.lineEdit_61.setObjectName(u"lineEdit_61")

        self.gridLayout_82.addWidget(self.lineEdit_61, 4, 1, 1, 1)


        self.gridLayout_83.addWidget(self.frame_78, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_36)
        self.page_43 = QWidget()
        self.page_43.setObjectName(u"page_43")
        self.gridLayout_96 = QGridLayout(self.page_43)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.frame_92 = QFrame(self.page_43)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.gridLayout_95 = QGridLayout(self.frame_92)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.label_304 = QLabel(self.frame_92)
        self.label_304.setObjectName(u"label_304")

        self.gridLayout_95.addWidget(self.label_304, 1, 0, 1, 1)

        self.pushButton_122 = QPushButton(self.frame_92)
        self.pushButton_122.setObjectName(u"pushButton_122")

        self.gridLayout_95.addWidget(self.pushButton_122, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_95.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)


        self.gridLayout_96.addWidget(self.frame_92, 0, 0, 1, 1)

        self.frame_39 = QFrame(self.page_43)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.gridLayout_97 = QGridLayout(self.frame_39)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.comboBox_23 = QComboBox(self.frame_39)
        self.comboBox_23.setObjectName(u"comboBox_23")

        self.gridLayout_97.addWidget(self.comboBox_23, 0, 3, 1, 1)

        self.comboBox_22 = QComboBox(self.frame_39)
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.gridLayout_97.addWidget(self.comboBox_22, 0, 1, 1, 1)

        self.lineEdit_63 = QLineEdit(self.frame_39)
        self.lineEdit_63.setObjectName(u"lineEdit_63")

        self.gridLayout_97.addWidget(self.lineEdit_63, 0, 7, 1, 1)

        self.pushButton_121 = QPushButton(self.frame_39)
        self.pushButton_121.setObjectName(u"pushButton_121")
        self.pushButton_121.setIcon(icon13)
        self.pushButton_121.setIconSize(QSize(42, 36))

        self.gridLayout_97.addWidget(self.pushButton_121, 0, 8, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_39)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_97.addWidget(self.lineEdit_16, 0, 5, 1, 1)

        self.label_300 = QLabel(self.frame_39)
        self.label_300.setObjectName(u"label_300")

        self.gridLayout_97.addWidget(self.label_300, 0, 2, 1, 1)

        self.label_126 = QLabel(self.frame_39)
        self.label_126.setObjectName(u"label_126")

        self.gridLayout_97.addWidget(self.label_126, 0, 0, 1, 1)

        self.label_303 = QLabel(self.frame_39)
        self.label_303.setObjectName(u"label_303")

        self.gridLayout_97.addWidget(self.label_303, 0, 4, 1, 1)

        self.label_307 = QLabel(self.frame_39)
        self.label_307.setObjectName(u"label_307")

        self.gridLayout_97.addWidget(self.label_307, 0, 6, 1, 1)


        self.gridLayout_96.addWidget(self.frame_39, 1, 0, 1, 1)

        self.frame_91 = QFrame(self.page_43)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Plain)
        self.verticalLayout_40 = QVBoxLayout(self.frame_91)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.tableWidget_37 = QTableWidget(self.frame_91)
        if (self.tableWidget_37.columnCount() < 6):
            self.tableWidget_37.setColumnCount(6)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_37.setHorizontalHeaderItem(5, __qtablewidgetitem78)
        self.tableWidget_37.setObjectName(u"tableWidget_37")
        self.tableWidget_37.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_37.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_37.setAlternatingRowColors(True)
        self.tableWidget_37.setGridStyle(Qt.NoPen)

        self.verticalLayout_40.addWidget(self.tableWidget_37)


        self.gridLayout_96.addWidget(self.frame_91, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_43)
        self.page_60 = QWidget()
        self.page_60.setObjectName(u"page_60")
        self.gridLayout_117 = QGridLayout(self.page_60)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.frame_116 = QFrame(self.page_60)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.gridLayout_118 = QGridLayout(self.frame_116)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.label_374 = QLabel(self.frame_116)
        self.label_374.setObjectName(u"label_374")

        self.gridLayout_118.addWidget(self.label_374, 2, 0, 1, 1)

        self.label_104 = QLabel(self.frame_116)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_118.addWidget(self.label_104, 1, 0, 1, 1)

        self.comboBox_47 = QComboBox(self.frame_116)
        self.comboBox_47.setObjectName(u"comboBox_47")

        self.gridLayout_118.addWidget(self.comboBox_47, 2, 1, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_118.addItem(self.horizontalSpacer_49, 2, 2, 1, 1)

        self.comboBox_46 = QComboBox(self.frame_116)
        self.comboBox_46.setObjectName(u"comboBox_46")

        self.gridLayout_118.addWidget(self.comboBox_46, 1, 1, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_118.addItem(self.verticalSpacer_26, 6, 1, 1, 1)

        self.label_375 = QLabel(self.frame_116)
        self.label_375.setObjectName(u"label_375")

        self.gridLayout_118.addWidget(self.label_375, 3, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_116)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_118.addWidget(self.lineEdit_12, 3, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.frame_116)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_118.addWidget(self.lineEdit_15, 4, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_118.addItem(self.verticalSpacer_27, 0, 1, 1, 1)

        self.label_170 = QLabel(self.frame_116)
        self.label_170.setObjectName(u"label_170")

        self.gridLayout_118.addWidget(self.label_170, 4, 0, 1, 1)

        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_50)

        self.pushButton_162 = QPushButton(self.frame_117)
        self.pushButton_162.setObjectName(u"pushButton_162")
        self.pushButton_162.setStyleSheet(u"background-color: rgb(0, 198, 0);")
        self.pushButton_162.setIcon(icon16)
        self.pushButton_162.setIconSize(QSize(25, 30))

        self.horizontalLayout_44.addWidget(self.pushButton_162)

        self.pushButton_164 = QPushButton(self.frame_117)
        self.pushButton_164.setObjectName(u"pushButton_164")
        self.pushButton_164.setStyleSheet(u"background-color: rgb(231, 0, 23);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/images/icons/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_164.setIcon(icon19)
        self.pushButton_164.setIconSize(QSize(16, 30))

        self.horizontalLayout_44.addWidget(self.pushButton_164)

        self.pushButton_163 = QPushButton(self.frame_117)
        self.pushButton_163.setObjectName(u"pushButton_163")
        self.pushButton_163.setStyleSheet(u"")

        self.horizontalLayout_44.addWidget(self.pushButton_163)


        self.gridLayout_118.addWidget(self.frame_117, 5, 1, 1, 1)


        self.gridLayout_117.addWidget(self.frame_116, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_60)
        self.page_37 = QWidget()
        self.page_37.setObjectName(u"page_37")
        self.gridLayout_115 = QGridLayout(self.page_37)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.tableWidget_30 = QTableWidget(self.page_37)
        if (self.tableWidget_30.columnCount() < 7):
            self.tableWidget_30.setColumnCount(7)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(5, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_30.setHorizontalHeaderItem(6, __qtablewidgetitem85)
        self.tableWidget_30.setObjectName(u"tableWidget_30")
        self.tableWidget_30.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_30.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_30.setAlternatingRowColors(True)
        self.tableWidget_30.setGridStyle(Qt.NoPen)
        self.tableWidget_30.verticalHeader().setVisible(False)

        self.gridLayout_115.addWidget(self.tableWidget_30, 4, 1, 1, 4)

        self.label_238 = QLabel(self.page_37)
        self.label_238.setObjectName(u"label_238")

        self.gridLayout_115.addWidget(self.label_238, 1, 1, 1, 1)

        self.pushButton_100 = QPushButton(self.page_37)
        self.pushButton_100.setObjectName(u"pushButton_100")
        self.pushButton_100.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_100.setIcon(icon13)
        self.pushButton_100.setIconSize(QSize(51, 47))

        self.gridLayout_115.addWidget(self.pushButton_100, 2, 1, 1, 1)

        self.pushButton_99 = QPushButton(self.page_37)
        self.pushButton_99.setObjectName(u"pushButton_99")
        self.pushButton_99.setIcon(icon15)

        self.gridLayout_115.addWidget(self.pushButton_99, 0, 1, 1, 1)

        self.frame_110 = QFrame(self.page_37)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.comboBox_41 = QComboBox(self.frame_110)
        self.comboBox_41.setObjectName(u"comboBox_41")
        self.comboBox_41.setMinimumSize(QSize(143, 0))
        self.comboBox_41.setMaximumSize(QSize(119, 28))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_41.setPalette(palette6)
        self.comboBox_41.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_38.addWidget(self.comboBox_41)

        self.lineEdit_82 = QLineEdit(self.frame_110)
        self.lineEdit_82.setObjectName(u"lineEdit_82")
        self.lineEdit_82.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_82.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_38.addWidget(self.lineEdit_82)

        self.pushButton_153 = QPushButton(self.frame_110)
        self.pushButton_153.setObjectName(u"pushButton_153")
        self.pushButton_153.setMaximumSize(QSize(16777215, 20))
        self.pushButton_153.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_153.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_153.setIcon(icon14)
        self.pushButton_153.setIconSize(QSize(28, 30))

        self.horizontalLayout_38.addWidget(self.pushButton_153)


        self.gridLayout_115.addWidget(self.frame_110, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_115.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_37)
        self.page_38 = QWidget()
        self.page_38.setObjectName(u"page_38")
        self.gridLayout_84 = QGridLayout(self.page_38)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.textEdit_4 = QTextEdit(self.page_38)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(400, 16777215))
        self.textEdit_4.setReadOnly(True)

        self.gridLayout_84.addWidget(self.textEdit_4, 7, 0, 1, 2)

        self.frame_80 = QFrame(self.page_38)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Sunken)
        self.gridLayout_79 = QGridLayout(self.frame_80)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.label_292 = QLabel(self.frame_80)
        self.label_292.setObjectName(u"label_292")

        self.gridLayout_79.addWidget(self.label_292, 1, 2, 1, 1)

        self.label_273 = QLabel(self.frame_80)
        self.label_273.setObjectName(u"label_273")

        self.gridLayout_79.addWidget(self.label_273, 1, 1, 1, 1)

        self.label_272 = QLabel(self.frame_80)
        self.label_272.setObjectName(u"label_272")

        self.gridLayout_79.addWidget(self.label_272, 1, 0, 1, 1)

        self.label_294 = QLabel(self.frame_80)
        self.label_294.setObjectName(u"label_294")

        self.gridLayout_79.addWidget(self.label_294, 1, 3, 1, 1)

        self.label_293 = QLabel(self.frame_80)
        self.label_293.setObjectName(u"label_293")

        self.gridLayout_79.addWidget(self.label_293, 2, 3, 1, 1)

        self.label_269 = QLabel(self.frame_80)
        self.label_269.setObjectName(u"label_269")

        self.gridLayout_79.addWidget(self.label_269, 2, 1, 1, 1)

        self.label_268 = QLabel(self.frame_80)
        self.label_268.setObjectName(u"label_268")

        self.gridLayout_79.addWidget(self.label_268, 2, 0, 1, 1)

        self.label_291 = QLabel(self.frame_80)
        self.label_291.setObjectName(u"label_291")

        self.gridLayout_79.addWidget(self.label_291, 2, 2, 1, 1)

        self.label_298 = QLabel(self.frame_80)
        self.label_298.setObjectName(u"label_298")

        self.gridLayout_79.addWidget(self.label_298, 0, 1, 1, 1)


        self.gridLayout_84.addWidget(self.frame_80, 0, 2, 1, 1)

        self.tableWidget_31 = QTableWidget(self.page_38)
        if (self.tableWidget_31.columnCount() < 5):
            self.tableWidget_31.setColumnCount(5)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_31.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_31.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_31.setHorizontalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_31.setHorizontalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_31.setHorizontalHeaderItem(4, __qtablewidgetitem90)
        self.tableWidget_31.setObjectName(u"tableWidget_31")
        self.tableWidget_31.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_31.setFrameShape(QFrame.Box)
        self.tableWidget_31.setFrameShadow(QFrame.Raised)
        self.tableWidget_31.setAlternatingRowColors(True)
        self.tableWidget_31.setGridStyle(Qt.NoPen)

        self.gridLayout_84.addWidget(self.tableWidget_31, 2, 2, 2, 1)

        self.label_267 = QLabel(self.page_38)
        self.label_267.setObjectName(u"label_267")

        self.gridLayout_84.addWidget(self.label_267, 1, 2, 1, 1)

        self.label_274 = QLabel(self.page_38)
        self.label_274.setObjectName(u"label_274")

        self.gridLayout_84.addWidget(self.label_274, 6, 0, 1, 1)

        self.label_296 = QLabel(self.page_38)
        self.label_296.setObjectName(u"label_296")

        self.gridLayout_84.addWidget(self.label_296, 4, 2, 1, 1)

        self.frame_73 = QFrame(self.page_38)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Sunken)
        self.gridLayout_77 = QGridLayout(self.frame_73)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.pushButton_103 = QPushButton(self.frame_73)
        self.pushButton_103.setObjectName(u"pushButton_103")

        self.gridLayout_77.addWidget(self.pushButton_103, 3, 1, 1, 1)

        self.label_239 = QLabel(self.frame_73)
        self.label_239.setObjectName(u"label_239")

        self.gridLayout_77.addWidget(self.label_239, 0, 0, 1, 2)

        self.label_241 = QLabel(self.frame_73)
        self.label_241.setObjectName(u"label_241")

        self.gridLayout_77.addWidget(self.label_241, 1, 1, 1, 1)

        self.label_240 = QLabel(self.frame_73)
        self.label_240.setObjectName(u"label_240")

        self.gridLayout_77.addWidget(self.label_240, 1, 0, 1, 1)

        self.label_249 = QLabel(self.frame_73)
        self.label_249.setObjectName(u"label_249")

        self.gridLayout_77.addWidget(self.label_249, 2, 0, 1, 1)

        self.pushButton_102 = QPushButton(self.frame_73)
        self.pushButton_102.setObjectName(u"pushButton_102")

        self.gridLayout_77.addWidget(self.pushButton_102, 3, 0, 1, 1)

        self.label_250 = QLabel(self.frame_73)
        self.label_250.setObjectName(u"label_250")

        self.gridLayout_77.addWidget(self.label_250, 2, 1, 1, 1)


        self.gridLayout_84.addWidget(self.frame_73, 0, 0, 3, 2)

        self.tableWidget_32 = QTableWidget(self.page_38)
        if (self.tableWidget_32.columnCount() < 6):
            self.tableWidget_32.setColumnCount(6)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_32.setHorizontalHeaderItem(5, __qtablewidgetitem96)
        self.tableWidget_32.setObjectName(u"tableWidget_32")
        self.tableWidget_32.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_32.setAlternatingRowColors(True)
        self.tableWidget_32.setGridStyle(Qt.NoPen)
        self.tableWidget_32.verticalHeader().setVisible(False)

        self.gridLayout_84.addWidget(self.tableWidget_32, 5, 2, 3, 1)

        self.frame_74 = QFrame(self.page_38)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Sunken)
        self.gridLayout_78 = QGridLayout(self.frame_74)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.label_255 = QLabel(self.frame_74)
        self.label_255.setObjectName(u"label_255")

        self.gridLayout_78.addWidget(self.label_255, 3, 0, 1, 1)

        self.label_259 = QLabel(self.frame_74)
        self.label_259.setObjectName(u"label_259")

        self.gridLayout_78.addWidget(self.label_259, 5, 0, 1, 1)

        self.label_254 = QLabel(self.frame_74)
        self.label_254.setObjectName(u"label_254")

        self.gridLayout_78.addWidget(self.label_254, 2, 0, 1, 1)

        self.pushButton_104 = QPushButton(self.frame_74)
        self.pushButton_104.setObjectName(u"pushButton_104")

        self.gridLayout_78.addWidget(self.pushButton_104, 6, 0, 1, 1)

        self.label_251 = QLabel(self.frame_74)
        self.label_251.setObjectName(u"label_251")

        self.gridLayout_78.addWidget(self.label_251, 0, 0, 1, 1)

        self.label_253 = QLabel(self.frame_74)
        self.label_253.setObjectName(u"label_253")

        self.gridLayout_78.addWidget(self.label_253, 1, 0, 1, 1)

        self.label_258 = QLabel(self.frame_74)
        self.label_258.setObjectName(u"label_258")

        self.gridLayout_78.addWidget(self.label_258, 4, 0, 1, 1)


        self.gridLayout_84.addWidget(self.frame_74, 3, 0, 3, 2)

        self.stackedWidget.addWidget(self.page_38)
        self.page_39 = QWidget()
        self.page_39.setObjectName(u"page_39")
        self.gridLayout_89 = QGridLayout(self.page_39)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.frame_76 = QFrame(self.page_39)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Plain)
        self.frame_76.setLineWidth(1)
        self.frame_76.setMidLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.frame_76)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_281 = QLabel(self.frame_76)
        self.label_281.setObjectName(u"label_281")

        self.verticalLayout_18.addWidget(self.label_281)

        self.label_282 = QLabel(self.frame_76)
        self.label_282.setObjectName(u"label_282")

        self.verticalLayout_18.addWidget(self.label_282)

        self.label_382 = QLabel(self.frame_76)
        self.label_382.setObjectName(u"label_382")

        self.verticalLayout_18.addWidget(self.label_382)

        self.label_383 = QLabel(self.frame_76)
        self.label_383.setObjectName(u"label_383")

        self.verticalLayout_18.addWidget(self.label_383)

        self.lineEdit_45 = QLineEdit(self.frame_76)
        self.lineEdit_45.setObjectName(u"lineEdit_45")

        self.verticalLayout_18.addWidget(self.lineEdit_45)

        self.checkBox_3 = QCheckBox(self.frame_76)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_18.addWidget(self.checkBox_3)

        self.label_283 = QLabel(self.frame_76)
        self.label_283.setObjectName(u"label_283")

        self.verticalLayout_18.addWidget(self.label_283)

        self.dateEdit_8 = QDateEdit(self.frame_76)
        self.dateEdit_8.setObjectName(u"dateEdit_8")
        self.dateEdit_8.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.dateEdit_8.setCalendarPopup(True)

        self.verticalLayout_18.addWidget(self.dateEdit_8)

        self.pushButton_78 = QPushButton(self.frame_76)
        self.pushButton_78.setObjectName(u"pushButton_78")
        self.pushButton_78.setStyleSheet(u"background-color: rgb(0, 198, 0);")

        self.verticalLayout_18.addWidget(self.pushButton_78)


        self.gridLayout_89.addWidget(self.frame_76, 3, 0, 2, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.page_39)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout_89.addWidget(self.plainTextEdit_3, 2, 3, 1, 1)

        self.frame_83 = QFrame(self.page_39)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Sunken)
        self.gridLayout_86 = QGridLayout(self.frame_83)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.stackedWidget_3 = QStackedWidget(self.frame_83)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_40 = QWidget()
        self.page_40.setObjectName(u"page_40")
        self.gridLayout_87 = QGridLayout(self.page_40)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.tableWidget_33 = QTableWidget(self.page_40)
        if (self.tableWidget_33.columnCount() < 5):
            self.tableWidget_33.setColumnCount(5)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_33.setHorizontalHeaderItem(0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_33.setHorizontalHeaderItem(1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_33.setHorizontalHeaderItem(2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_33.setHorizontalHeaderItem(3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_33.setHorizontalHeaderItem(4, __qtablewidgetitem101)
        self.tableWidget_33.setObjectName(u"tableWidget_33")
        self.tableWidget_33.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_33.setAlternatingRowColors(True)
        self.tableWidget_33.setGridStyle(Qt.NoPen)
        self.tableWidget_33.verticalHeader().setVisible(False)

        self.gridLayout_87.addWidget(self.tableWidget_33, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_40)
        self.page_41 = QWidget()
        self.page_41.setObjectName(u"page_41")
        self.gridLayout_88 = QGridLayout(self.page_41)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.tableWidget_34 = QTableWidget(self.page_41)
        if (self.tableWidget_34.columnCount() < 3):
            self.tableWidget_34.setColumnCount(3)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(0, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(1, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_34.setHorizontalHeaderItem(2, __qtablewidgetitem104)
        self.tableWidget_34.setObjectName(u"tableWidget_34")

        self.gridLayout_88.addWidget(self.tableWidget_34, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_41)

        self.gridLayout_86.addWidget(self.stackedWidget_3, 0, 0, 1, 1)


        self.gridLayout_89.addWidget(self.frame_83, 4, 1, 1, 4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_89.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)

        self.frame_75 = QFrame(self.page_39)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Sunken)
        self.gridLayout_80 = QGridLayout(self.frame_75)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.label_280 = QLabel(self.frame_75)
        self.label_280.setObjectName(u"label_280")

        self.gridLayout_80.addWidget(self.label_280, 0, 0, 1, 1)

        self.label_277 = QLabel(self.frame_75)
        self.label_277.setObjectName(u"label_277")

        self.gridLayout_80.addWidget(self.label_277, 2, 0, 1, 1)

        self.label_279 = QLabel(self.frame_75)
        self.label_279.setObjectName(u"label_279")

        self.gridLayout_80.addWidget(self.label_279, 5, 0, 1, 1)

        self.label_278 = QLabel(self.frame_75)
        self.label_278.setObjectName(u"label_278")

        self.gridLayout_80.addWidget(self.label_278, 4, 0, 1, 1)

        self.label_275 = QLabel(self.frame_75)
        self.label_275.setObjectName(u"label_275")

        self.gridLayout_80.addWidget(self.label_275, 1, 0, 1, 1)

        self.label_276 = QLabel(self.frame_75)
        self.label_276.setObjectName(u"label_276")

        self.gridLayout_80.addWidget(self.label_276, 3, 0, 1, 1)


        self.gridLayout_89.addWidget(self.frame_75, 2, 0, 1, 1)

        self.frame_84 = QFrame(self.page_39)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_176 = QPushButton(self.frame_84)
        self.pushButton_176.setObjectName(u"pushButton_176")

        self.horizontalLayout_26.addWidget(self.pushButton_176)

        self.pushButton_110 = QPushButton(self.frame_84)
        self.pushButton_110.setObjectName(u"pushButton_110")
        self.pushButton_110.setMinimumSize(QSize(0, 31))
        self.pushButton_110.setMaximumSize(QSize(16777215, 31))
        self.pushButton_110.setStyleSheet(u"background-color: rgb(39, 168, 0);")

        self.horizontalLayout_26.addWidget(self.pushButton_110)


        self.gridLayout_89.addWidget(self.frame_84, 1, 0, 1, 1)

        self.label_290 = QLabel(self.page_39)
        self.label_290.setObjectName(u"label_290")

        self.gridLayout_89.addWidget(self.label_290, 1, 3, 1, 1)

        self.frame_82 = QFrame(self.page_39)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_288 = QLabel(self.frame_82)
        self.label_288.setObjectName(u"label_288")

        self.horizontalLayout_20.addWidget(self.label_288)

        self.comboBox_19 = QComboBox(self.frame_82)
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(297, 0))
        self.comboBox_19.setMaximumSize(QSize(300, 16777215))
        self.comboBox_19.setEditable(True)

        self.horizontalLayout_20.addWidget(self.comboBox_19)

        self.label_289 = QLabel(self.frame_82)
        self.label_289.setObjectName(u"label_289")

        self.horizontalLayout_20.addWidget(self.label_289)

        self.lineEdit_60 = QLineEdit(self.frame_82)
        self.lineEdit_60.setObjectName(u"lineEdit_60")

        self.horizontalLayout_20.addWidget(self.lineEdit_60)

        self.pushButton_109 = QPushButton(self.frame_82)
        self.pushButton_109.setObjectName(u"pushButton_109")

        self.horizontalLayout_20.addWidget(self.pushButton_109)


        self.gridLayout_89.addWidget(self.frame_82, 3, 1, 1, 4)

        self.frame_81 = QFrame(self.page_39)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.gridLayout_85 = QGridLayout(self.frame_81)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.pushButton_106 = QPushButton(self.frame_81)
        self.pushButton_106.setObjectName(u"pushButton_106")
        self.pushButton_106.setStyleSheet(u"background-color: rgb(0, 158, 0);")

        self.gridLayout_85.addWidget(self.pushButton_106, 0, 0, 1, 1)

        self.pushButton_107 = QPushButton(self.frame_81)
        self.pushButton_107.setObjectName(u"pushButton_107")
        self.pushButton_107.setStyleSheet(u"background-color: rgb(204, 21, 45);")

        self.gridLayout_85.addWidget(self.pushButton_107, 1, 0, 1, 1)

        self.pushButton_108 = QPushButton(self.frame_81)
        self.pushButton_108.setObjectName(u"pushButton_108")
        self.pushButton_108.setStyleSheet(u"background-color: rgb(0, 158, 158);")

        self.gridLayout_85.addWidget(self.pushButton_108, 2, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_85.addItem(self.verticalSpacer_21, 4, 0, 1, 1)

        self.pushButton_111 = QPushButton(self.frame_81)
        self.pushButton_111.setObjectName(u"pushButton_111")
        self.pushButton_111.setStyleSheet(u"background-color: rgb(85, 0, 255);")

        self.gridLayout_85.addWidget(self.pushButton_111, 3, 0, 1, 1)


        self.gridLayout_89.addWidget(self.frame_81, 2, 4, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_89.addItem(self.horizontalSpacer_16, 1, 1, 1, 1)

        self.frame_79 = QFrame(self.page_39)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_38 = QVBoxLayout(self.frame_79)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_284 = QLabel(self.frame_79)
        self.label_284.setObjectName(u"label_284")

        self.verticalLayout_38.addWidget(self.label_284)

        self.lineEdit_58 = QLineEdit(self.frame_79)
        self.lineEdit_58.setObjectName(u"lineEdit_58")

        self.verticalLayout_38.addWidget(self.lineEdit_58)

        self.label_110 = QLabel(self.frame_79)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_38.addWidget(self.label_110)

        self.comboBox_52 = QComboBox(self.frame_79)
        self.comboBox_52.setObjectName(u"comboBox_52")

        self.verticalLayout_38.addWidget(self.comboBox_52)

        self.label_285 = QLabel(self.frame_79)
        self.label_285.setObjectName(u"label_285")

        self.verticalLayout_38.addWidget(self.label_285)

        self.lineEdit_59 = QLineEdit(self.frame_79)
        self.lineEdit_59.setObjectName(u"lineEdit_59")

        self.verticalLayout_38.addWidget(self.lineEdit_59)

        self.label_286 = QLabel(self.frame_79)
        self.label_286.setObjectName(u"label_286")

        self.verticalLayout_38.addWidget(self.label_286)

        self.comboBox_17 = QComboBox(self.frame_79)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.verticalLayout_38.addWidget(self.comboBox_17)

        self.label_287 = QLabel(self.frame_79)
        self.label_287.setObjectName(u"label_287")

        self.verticalLayout_38.addWidget(self.label_287)

        self.comboBox_18 = QComboBox(self.frame_79)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.verticalLayout_38.addWidget(self.comboBox_18)


        self.gridLayout_89.addWidget(self.frame_79, 2, 1, 1, 2)

        self.stackedWidget.addWidget(self.page_39)
        self.page_52 = QWidget()
        self.page_52.setObjectName(u"page_52")
        self.stackedWidget.addWidget(self.page_52)
        self.page_42 = QWidget()
        self.page_42.setObjectName(u"page_42")
        self.gridLayout_90 = QGridLayout(self.page_42)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.label_295 = QLabel(self.page_42)
        self.label_295.setObjectName(u"label_295")

        self.gridLayout_90.addWidget(self.label_295, 1, 0, 1, 1)

        self.tableWidget_35 = QTableWidget(self.page_42)
        if (self.tableWidget_35.columnCount() < 5):
            self.tableWidget_35.setColumnCount(5)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_35.setHorizontalHeaderItem(0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_35.setHorizontalHeaderItem(1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_35.setHorizontalHeaderItem(2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_35.setHorizontalHeaderItem(3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_35.setHorizontalHeaderItem(4, __qtablewidgetitem109)
        self.tableWidget_35.setObjectName(u"tableWidget_35")

        self.gridLayout_90.addWidget(self.tableWidget_35, 3, 0, 1, 1)

        self.pushButton_112 = QPushButton(self.page_42)
        self.pushButton_112.setObjectName(u"pushButton_112")

        self.gridLayout_90.addWidget(self.pushButton_112, 0, 0, 1, 1)

        self.pushButton_113 = QPushButton(self.page_42)
        self.pushButton_113.setObjectName(u"pushButton_113")

        self.gridLayout_90.addWidget(self.pushButton_113, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_42)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayoutWidget_2 = QWidget(self.page_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1291, 531))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_7.setIcon(icon16)
        self.pushButton_7.setIconSize(QSize(42, 35))

        self.horizontalLayout_10.addWidget(self.pushButton_7)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_27)


        self.gridLayout_25.addLayout(self.horizontalLayout_10, 7, 2, 1, 1)

        self.dateEdit_3 = QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMaximumSize(QSize(400, 16777215))
        self.dateEdit_3.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.dateEdit_3.setFrame(True)
        self.dateEdit_3.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setTimeSpec(Qt.LocalTime)
        self.dateEdit_3.setDate(QDate(2000, 4, 1))

        self.gridLayout_25.addWidget(self.dateEdit_3, 3, 2, 1, 1)

        self.label_133 = QLabel(self.gridLayoutWidget_2)
        self.label_133.setObjectName(u"label_133")

        self.gridLayout_25.addWidget(self.label_133, 1, 1, 1, 2)

        self.tableWidget_12 = QTableWidget(self.gridLayoutWidget_2)
        if (self.tableWidget_12.columnCount() < 5):
            self.tableWidget_12.setColumnCount(5)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, __qtablewidgetitem114)
        self.tableWidget_12.setObjectName(u"tableWidget_12")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 0))
        brush5.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_12.setPalette(palette7)
        self.tableWidget_12.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical"
                        "\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")

        self.gridLayout_25.addWidget(self.tableWidget_12, 2, 0, 1, 3)

        self.label_132 = QLabel(self.gridLayoutWidget_2)
        self.label_132.setObjectName(u"label_132")

        self.gridLayout_25.addWidget(self.label_132, 6, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_17.setStyleSheet(u"QLineEdit {\n"
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
"}")

        self.gridLayout_25.addWidget(self.lineEdit_17, 6, 2, 1, 1)

        self.label_130 = QLabel(self.gridLayoutWidget_2)
        self.label_130.setObjectName(u"label_130")

        self.gridLayout_25.addWidget(self.label_130, 3, 0, 1, 1)

        self.label_129 = QLabel(self.gridLayoutWidget_2)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_25.addWidget(self.label_129, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(30, 0))
        self.pushButton_13.setMaximumSize(QSize(30, 16777215))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"")
        self.pushButton_13.setIcon(icon15)
        self.pushButton_13.setIconSize(QSize(26, 30))

        self.gridLayout_25.addWidget(self.pushButton_13, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.gridLayout_62 = QGridLayout(self.page_27)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_61 = QGridLayout()
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.pushButton_73 = QPushButton(self.page_27)
        self.pushButton_73.setObjectName(u"pushButton_73")
        self.pushButton_73.setMinimumSize(QSize(30, 0))
        self.pushButton_73.setMaximumSize(QSize(30, 16777215))
        self.pushButton_73.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_73.setStyleSheet(u"")
        self.pushButton_73.setIcon(icon15)
        self.pushButton_73.setIconSize(QSize(26, 30))

        self.gridLayout_61.addWidget(self.pushButton_73, 0, 0, 1, 1)

        self.lineEdit_44 = QLineEdit(self.page_27)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_44.setStyleSheet(u"QLineEdit {\n"
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
"}")

        self.gridLayout_61.addWidget(self.lineEdit_44, 7, 2, 1, 1)

        self.tableWidget_23 = QTableWidget(self.page_27)
        if (self.tableWidget_23.columnCount() < 5):
            self.tableWidget_23.setColumnCount(5)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(3, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_23.setHorizontalHeaderItem(4, __qtablewidgetitem119)
        self.tableWidget_23.setObjectName(u"tableWidget_23")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_23.setPalette(palette8)
        self.tableWidget_23.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical"
                        "\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")

        self.gridLayout_61.addWidget(self.tableWidget_23, 2, 0, 1, 3)

        self.comboBox_10 = QComboBox(self.page_27)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMaximumSize(QSize(392, 16777215))
        self.comboBox_10.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout_61.addWidget(self.comboBox_10, 6, 2, 1, 1)

        self.label_205 = QLabel(self.page_27)
        self.label_205.setObjectName(u"label_205")

        self.gridLayout_61.addWidget(self.label_205, 6, 0, 1, 1)

        self.label_204 = QLabel(self.page_27)
        self.label_204.setObjectName(u"label_204")

        self.gridLayout_61.addWidget(self.label_204, 1, 1, 1, 2)

        self.label_138 = QLabel(self.page_27)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_61.addWidget(self.label_138, 1, 0, 1, 1)

        self.label_202 = QLabel(self.page_27)
        self.label_202.setObjectName(u"label_202")

        self.gridLayout_61.addWidget(self.label_202, 7, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_30)

        self.pushButton_72 = QPushButton(self.page_27)
        self.pushButton_72.setObjectName(u"pushButton_72")
        self.pushButton_72.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_72.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_72.setIcon(icon16)
        self.pushButton_72.setIconSize(QSize(42, 35))

        self.horizontalLayout_19.addWidget(self.pushButton_72)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_31)


        self.gridLayout_61.addLayout(self.horizontalLayout_19, 8, 2, 1, 1)

        self.dateEdit_7 = QDateEdit(self.page_27)
        self.dateEdit_7.setObjectName(u"dateEdit_7")
        self.dateEdit_7.setMaximumSize(QSize(400, 16777215))
        self.dateEdit_7.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.dateEdit_7.setFrame(True)
        self.dateEdit_7.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_7.setCalendarPopup(True)
        self.dateEdit_7.setTimeSpec(Qt.LocalTime)
        self.dateEdit_7.setDate(QDate(2000, 4, 1))

        self.gridLayout_61.addWidget(self.dateEdit_7, 3, 2, 1, 1)

        self.label_131 = QLabel(self.page_27)
        self.label_131.setObjectName(u"label_131")

        self.gridLayout_61.addWidget(self.label_131, 3, 0, 1, 1)


        self.gridLayout_62.addLayout(self.gridLayout_61, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_27)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_22 = QGridLayout(self.page_4)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)

        self.comboBox_3 = QComboBox(self.page_4)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(110, 0))
        self.comboBox_3.setMaximumSize(QSize(100, 27))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_3.setPalette(palette9)
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_8.addWidget(self.comboBox_3)

        self.lineEdit_11 = QLineEdit(self.page_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_8.addWidget(self.lineEdit_11)

        self.pushButton_22 = QPushButton(self.page_4)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(16777215, 20))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_22.setIcon(icon14)
        self.pushButton_22.setIconSize(QSize(28, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_22)


        self.gridLayout_22.addLayout(self.horizontalLayout_8, 1, 1, 1, 2)

        self.tableWidget_11 = QTableWidget(self.page_4)
        if (self.tableWidget_11.columnCount() < 9):
            self.tableWidget_11.setColumnCount(9)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(6, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(7, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(8, __qtablewidgetitem128)
        self.tableWidget_11.setObjectName(u"tableWidget_11")
        self.tableWidget_11.setMaximumSize(QSize(16777215, 500))
        self.tableWidget_11.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_22.addWidget(self.tableWidget_11, 2, 0, 1, 3)

        self.frame_47 = QFrame(self.page_4)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_47)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.lib_btn4_5 = QPushButton(self.frame_47)
        self.lib_btn4_5.setObjectName(u"lib_btn4_5")
        self.lib_btn4_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn4_5.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.lib_btn4_5.setIcon(icon2)
        self.lib_btn4_5.setIconSize(QSize(44, 38))

        self.gridLayout_24.addWidget(self.lib_btn4_5, 0, 1, 1, 1)

        self.client_btn = QPushButton(self.frame_47)
        self.client_btn.setObjectName(u"client_btn")
        self.client_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.client_btn.setIcon(icon13)
        self.client_btn.setIconSize(QSize(49, 41))

        self.gridLayout_24.addWidget(self.client_btn, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.gridLayout_22.addWidget(self.frame_47, 1, 0, 1, 1)

        self.label_94 = QLabel(self.page_4)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(0, 30))
        self.label_94.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_22.addWidget(self.label_94, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_53 = QWidget()
        self.page_53.setObjectName(u"page_53")
        self.gridLayout_108 = QGridLayout(self.page_53)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.stackedWidget.addWidget(self.page_53)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.gridLayout_2 = QGridLayout(self.widgets)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_105 = QFrame(self.widgets)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.widget_10 = QWidget(self.frame_105)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(430, 20, 500, 300))
        self.widget_10.setMinimumSize(QSize(300, 300))
        self.widget_10.setMaximumSize(QSize(500, 600))
        self.widget_10.setStyleSheet(u"background-color: rgb(27, 27, 27);")
        self.label_330 = QLabel(self.frame_105)
        self.label_330.setObjectName(u"label_330")
        self.label_330.setGeometry(QRect(40, 30, 241, 251))

        self.gridLayout_2.addWidget(self.frame_105, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.widgets)
        self.page_30 = QWidget()
        self.page_30.setObjectName(u"page_30")
        self.gridLayout_66 = QGridLayout(self.page_30)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.widget_6 = QWidget(self.page_30)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_66.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.page_30)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_66.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.page_30)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(300, 264))
        self.widget_9.setMaximumSize(QSize(500, 600))
        self.widget_9.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_66.addWidget(self.widget_9, 1, 1, 1, 1)

        self.widget_7 = QWidget(self.page_30)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(300, 300))
        self.widget_7.setMaximumSize(QSize(500, 600))
        self.widget_7.setStyleSheet(u"background-color: rgb(27, 27, 27);")

        self.gridLayout_66.addWidget(self.widget_7, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_30)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_35 = QGridLayout(self.page_9)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_3 = QFrame(self.page_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(148, 0))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 21, -1, 21)
        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(16777215, 30))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_17 = QPushButton(self.frame_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMaximumSize(QSize(16777215, 30))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_17)

        self.pushButton_19 = QPushButton(self.frame_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMaximumSize(QSize(16777215, 30))
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_19)

        self.pushButton_28 = QPushButton(self.frame_3)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMaximumSize(QSize(16777215, 30))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.frame_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMaximumSize(QSize(16777215, 30))
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_29)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_30 = QPushButton(self.frame_3)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMaximumSize(QSize(16777215, 30))
        self.pushButton_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_30.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_30)


        self.gridLayout_35.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_38 = QFrame(self.page_9)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.gridLayout_35.addWidget(self.frame_38, 1, 1, 1, 1)

        self.label_5 = QLabel(self.page_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 37))

        self.gridLayout_35.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.page_9)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_7 = QGridLayout(self.page_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_120 = QLabel(self.page_11)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_7.addWidget(self.label_120, 2, 1, 1, 1)

        self.label_81 = QLabel(self.page_11)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_7.addWidget(self.label_81, 0, 3, 1, 1)

        self.dateEdit_5 = QDateEdit(self.page_11)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setMinimumSize(QSize(330, 0))
        self.dateEdit_5.setMaximumSize(QSize(351, 16777215))
        self.dateEdit_5.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.dateEdit_5, 2, 5, 1, 1)

        self.treeWidget = QTreeWidget(self.page_11)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setAnimated(True)
        self.treeWidget.header().setDefaultSectionSize(200)

        self.gridLayout_7.addWidget(self.treeWidget, 4, 0, 1, 8)

        self.pushButton_64 = QPushButton(self.page_11)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/images/icons/cil-print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_64.setIcon(icon20)

        self.gridLayout_7.addWidget(self.pushButton_64, 2, 7, 1, 1)

        self.label_53 = QLabel(self.page_11)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_7.addWidget(self.label_53, 2, 4, 1, 1)

        self.dateEdit_4 = QDateEdit(self.page_11)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setMinimumSize(QSize(468, 0))
        self.dateEdit_4.setMaximumSize(QSize(396, 16777215))
        self.dateEdit_4.setCalendarPopup(True)

        self.gridLayout_7.addWidget(self.dateEdit_4, 2, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.page_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(76, 16777215))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setIcon(icon14)

        self.gridLayout_7.addWidget(self.pushButton_9, 2, 6, 1, 1)

        self.frame_63 = QFrame(self.page_11)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_96 = QPushButton(self.frame_63)
        self.pushButton_96.setObjectName(u"pushButton_96")
        self.pushButton_96.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_25.addWidget(self.pushButton_96)

        self.pushButton_97 = QPushButton(self.frame_63)
        self.pushButton_97.setObjectName(u"pushButton_97")
        self.pushButton_97.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_97.setFlat(True)

        self.horizontalLayout_25.addWidget(self.pushButton_97)


        self.gridLayout_7.addWidget(self.frame_63, 3, 1, 1, 2)

        self.stackedWidget_2.addWidget(self.page_11)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.gridLayout_43 = QGridLayout(self.page_19)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.tableWidget_10 = QTableWidget(self.page_19)
        if (self.tableWidget_10.columnCount() < 5):
            self.tableWidget_10.setColumnCount(5)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(4, __qtablewidgetitem133)
        self.tableWidget_10.setObjectName(u"tableWidget_10")
        self.tableWidget_10.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_10.setAlternatingRowColors(True)
        self.tableWidget_10.setGridStyle(Qt.NoPen)
        self.tableWidget_10.verticalHeader().setVisible(False)

        self.gridLayout_43.addWidget(self.tableWidget_10, 3, 0, 1, 6)

        self.label_102 = QLabel(self.page_19)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_43.addWidget(self.label_102, 0, 1, 1, 3)

        self.label_122 = QLabel(self.page_19)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_43.addWidget(self.label_122, 1, 2, 1, 1)

        self.label_128 = QLabel(self.page_19)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_43.addWidget(self.label_128, 1, 0, 1, 1)

        self.pushButton_65 = QPushButton(self.page_19)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMaximumSize(QSize(56, 16777215))
        self.pushButton_65.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_65.setIcon(icon20)

        self.gridLayout_43.addWidget(self.pushButton_65, 1, 5, 1, 1)

        self.dateEdit_10 = QDateEdit(self.page_19)
        self.dateEdit_10.setObjectName(u"dateEdit_10")
        self.dateEdit_10.setCalendarPopup(True)

        self.gridLayout_43.addWidget(self.dateEdit_10, 1, 1, 1, 1)

        self.pushButton_42 = QPushButton(self.page_19)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMaximumSize(QSize(60, 16777215))
        self.pushButton_42.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_42.setIcon(icon14)

        self.gridLayout_43.addWidget(self.pushButton_42, 1, 4, 1, 1)

        self.dateEdit_9 = QDateEdit(self.page_19)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setCalendarPopup(True)

        self.gridLayout_43.addWidget(self.dateEdit_9, 1, 3, 1, 1)

        self.frame_46 = QFrame(self.page_19)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pushButton_92 = QPushButton(self.frame_46)
        self.pushButton_92.setObjectName(u"pushButton_92")
        self.pushButton_92.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton_92)

        self.pushButton_93 = QPushButton(self.frame_46)
        self.pushButton_93.setObjectName(u"pushButton_93")
        self.pushButton_93.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_24.addWidget(self.pushButton_93)

        self.pushButton_94 = QPushButton(self.frame_46)
        self.pushButton_94.setObjectName(u"pushButton_94")
        self.pushButton_94.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_94.setFlat(True)

        self.horizontalLayout_24.addWidget(self.pushButton_94)


        self.gridLayout_43.addWidget(self.frame_46, 2, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.page_19)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.gridLayout_45 = QGridLayout(self.page_22)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_183 = QLabel(self.page_22)
        self.label_183.setObjectName(u"label_183")

        self.gridLayout_45.addWidget(self.label_183, 0, 2, 1, 1)

        self.label_17 = QLabel(self.page_22)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_45.addWidget(self.label_17, 2, 0, 1, 1)

        self.dateEdit_11 = QDateEdit(self.page_22)
        self.dateEdit_11.setObjectName(u"dateEdit_11")
        self.dateEdit_11.setCalendarPopup(True)

        self.gridLayout_45.addWidget(self.dateEdit_11, 2, 3, 1, 1)

        self.label_40 = QLabel(self.page_22)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_45.addWidget(self.label_40, 2, 2, 1, 1)

        self.tableWidget_19 = QTableWidget(self.page_22)
        if (self.tableWidget_19.columnCount() < 9):
            self.tableWidget_19.setColumnCount(9)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(1, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(2, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(3, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(4, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(5, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(6, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(7, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_19.setHorizontalHeaderItem(8, __qtablewidgetitem142)
        self.tableWidget_19.setObjectName(u"tableWidget_19")
        self.tableWidget_19.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_19.setAlternatingRowColors(True)
        self.tableWidget_19.setGridStyle(Qt.NoPen)
        self.tableWidget_19.verticalHeader().setVisible(False)

        self.gridLayout_45.addWidget(self.tableWidget_19, 5, 0, 1, 6)

        self.pushButton_34 = QPushButton(self.page_22)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMaximumSize(QSize(42, 16777215))
        self.pushButton_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_34.setIcon(icon14)

        self.gridLayout_45.addWidget(self.pushButton_34, 2, 4, 1, 1)

        self.pushButton_59 = QPushButton(self.page_22)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setMaximumSize(QSize(45, 16777215))
        self.pushButton_59.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_59.setIcon(icon20)

        self.gridLayout_45.addWidget(self.pushButton_59, 2, 5, 1, 1)

        self.dateEdit_12 = QDateEdit(self.page_22)
        self.dateEdit_12.setObjectName(u"dateEdit_12")
        self.dateEdit_12.setCalendarPopup(True)

        self.gridLayout_45.addWidget(self.dateEdit_12, 2, 1, 1, 1)

        self.frame_14 = QFrame(self.page_22)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_43 = QPushButton(self.frame_14)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_43)

        self.pushButton_14 = QPushButton(self.frame_14)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.pushButton_14)

        self.pushButton_38 = QPushButton(self.frame_14)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_38.setFlat(True)

        self.horizontalLayout_15.addWidget(self.pushButton_38)


        self.gridLayout_45.addWidget(self.frame_14, 3, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.page_22)
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.gridLayout_49 = QGridLayout(self.page_23)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.frame_9 = QFrame(self.page_23)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_9)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.tableWidget_20 = QTableWidget(self.frame_9)
        if (self.tableWidget_20.columnCount() < 10):
            self.tableWidget_20.setColumnCount(10)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(0, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(1, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(2, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(3, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(4, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(5, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(6, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(7, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(8, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_20.setHorizontalHeaderItem(9, __qtablewidgetitem152)
        self.tableWidget_20.setObjectName(u"tableWidget_20")
        self.tableWidget_20.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_20.setAlternatingRowColors(True)
        self.tableWidget_20.setGridStyle(Qt.NoPen)

        self.gridLayout_50.addWidget(self.tableWidget_20, 3, 0, 1, 6)

        self.pushButton_56 = QPushButton(self.frame_9)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setMaximumSize(QSize(60, 16777215))
        self.pushButton_56.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_56.setIcon(icon14)

        self.gridLayout_50.addWidget(self.pushButton_56, 1, 4, 1, 1)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(36, 16777215))

        self.gridLayout_50.addWidget(self.label_41, 1, 0, 1, 1)

        self.pushButton_60 = QPushButton(self.frame_9)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setMaximumSize(QSize(38, 16777215))
        self.pushButton_60.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_60.setIcon(icon20)

        self.gridLayout_50.addWidget(self.pushButton_60, 1, 5, 1, 1)

        self.dateEdit_15 = QDateEdit(self.frame_9)
        self.dateEdit_15.setObjectName(u"dateEdit_15")
        self.dateEdit_15.setCalendarPopup(True)

        self.gridLayout_50.addWidget(self.dateEdit_15, 1, 3, 1, 1)

        self.label_185 = QLabel(self.frame_9)
        self.label_185.setObjectName(u"label_185")

        self.gridLayout_50.addWidget(self.label_185, 0, 1, 1, 3)

        self.dateEdit_16 = QDateEdit(self.frame_9)
        self.dateEdit_16.setObjectName(u"dateEdit_16")
        self.dateEdit_16.setMaximumSize(QSize(445, 16777215))
        self.dateEdit_16.setCalendarPopup(True)

        self.gridLayout_50.addWidget(self.dateEdit_16, 1, 1, 1, 1)

        self.label_43 = QLabel(self.frame_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_50.addWidget(self.label_43, 1, 2, 1, 1)

        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_66 = QPushButton(self.frame_19)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")

        self.horizontalLayout_21.addWidget(self.pushButton_66)

        self.pushButton_84 = QPushButton(self.frame_19)
        self.pushButton_84.setObjectName(u"pushButton_84")
        self.pushButton_84.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.pushButton_84)

        self.pushButton_85 = QPushButton(self.frame_19)
        self.pushButton_85.setObjectName(u"pushButton_85")
        self.pushButton_85.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_85.setFlat(True)

        self.horizontalLayout_21.addWidget(self.pushButton_85)


        self.gridLayout_50.addWidget(self.frame_19, 2, 0, 1, 2)


        self.gridLayout_49.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_23)
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.gridLayout_52 = QGridLayout(self.page_24)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.frame_26 = QFrame(self.page_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_26)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_229 = QLabel(self.frame_26)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_51.addWidget(self.label_229, 4, 2, 1, 1)

        self.dateEdit_17 = QDateEdit(self.frame_26)
        self.dateEdit_17.setObjectName(u"dateEdit_17")
        self.dateEdit_17.setCalendarPopup(True)

        self.gridLayout_51.addWidget(self.dateEdit_17, 1, 3, 1, 1)

        self.dateEdit_18 = QDateEdit(self.frame_26)
        self.dateEdit_18.setObjectName(u"dateEdit_18")
        self.dateEdit_18.setMaximumSize(QSize(445, 16777215))
        self.dateEdit_18.setCalendarPopup(True)

        self.gridLayout_51.addWidget(self.dateEdit_18, 1, 1, 1, 1)

        self.pushButton_61 = QPushButton(self.frame_26)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMaximumSize(QSize(47, 16777215))
        self.pushButton_61.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_61.setIcon(icon20)

        self.gridLayout_51.addWidget(self.pushButton_61, 1, 5, 1, 1)

        self.label_231 = QLabel(self.frame_26)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_51.addWidget(self.label_231, 4, 4, 1, 2)

        self.label_48 = QLabel(self.frame_26)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(36, 16777215))

        self.gridLayout_51.addWidget(self.label_48, 1, 0, 1, 1)

        self.pushButton_57 = QPushButton(self.frame_26)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setMaximumSize(QSize(60, 16777215))
        self.pushButton_57.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_57.setIcon(icon14)

        self.gridLayout_51.addWidget(self.pushButton_57, 1, 4, 1, 1)

        self.label_227 = QLabel(self.frame_26)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_51.addWidget(self.label_227, 4, 0, 1, 1)

        self.tableWidget_21 = QTableWidget(self.frame_26)
        if (self.tableWidget_21.columnCount() < 7):
            self.tableWidget_21.setColumnCount(7)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(1, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(2, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(3, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(4, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(5, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_21.setHorizontalHeaderItem(6, __qtablewidgetitem159)
        self.tableWidget_21.setObjectName(u"tableWidget_21")
        self.tableWidget_21.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_21.setAlternatingRowColors(True)
        self.tableWidget_21.setGridStyle(Qt.NoPen)

        self.gridLayout_51.addWidget(self.tableWidget_21, 3, 0, 1, 6)

        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_51.addWidget(self.label_46, 1, 2, 1, 1)

        self.label_186 = QLabel(self.frame_26)
        self.label_186.setObjectName(u"label_186")

        self.gridLayout_51.addWidget(self.label_186, 0, 1, 1, 3)

        self.label_228 = QLabel(self.frame_26)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_51.addWidget(self.label_228, 4, 1, 1, 1)

        self.label_230 = QLabel(self.frame_26)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_51.addWidget(self.label_230, 4, 3, 1, 1)

        self.frame_17 = QFrame(self.frame_26)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_86 = QPushButton(self.frame_17)
        self.pushButton_86.setObjectName(u"pushButton_86")
        self.pushButton_86.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_86)

        self.pushButton_87 = QPushButton(self.frame_17)
        self.pushButton_87.setObjectName(u"pushButton_87")
        self.pushButton_87.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_22.addWidget(self.pushButton_87)

        self.pushButton_88 = QPushButton(self.frame_17)
        self.pushButton_88.setObjectName(u"pushButton_88")
        self.pushButton_88.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_88.setFlat(True)

        self.horizontalLayout_22.addWidget(self.pushButton_88)


        self.gridLayout_51.addWidget(self.frame_17, 2, 0, 1, 2)


        self.gridLayout_52.addWidget(self.frame_26, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_24)
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.gridLayout_58 = QGridLayout(self.page_25)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.frame_27 = QFrame(self.page_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_27)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.dateEdit_19 = QDateEdit(self.frame_27)
        self.dateEdit_19.setObjectName(u"dateEdit_19")
        self.dateEdit_19.setCalendarPopup(True)

        self.gridLayout_57.addWidget(self.dateEdit_19, 1, 3, 1, 1)

        self.pushButton_58 = QPushButton(self.frame_27)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setMaximumSize(QSize(60, 16777215))
        self.pushButton_58.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_58.setIcon(icon14)

        self.gridLayout_57.addWidget(self.pushButton_58, 1, 4, 1, 1)

        self.pushButton_62 = QPushButton(self.frame_27)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMaximumSize(QSize(48, 16777215))
        self.pushButton_62.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_62.setIcon(icon20)

        self.gridLayout_57.addWidget(self.pushButton_62, 1, 5, 1, 1)

        self.label_189 = QLabel(self.frame_27)
        self.label_189.setObjectName(u"label_189")

        self.gridLayout_57.addWidget(self.label_189, 0, 1, 1, 3)

        self.dateEdit_20 = QDateEdit(self.frame_27)
        self.dateEdit_20.setObjectName(u"dateEdit_20")
        self.dateEdit_20.setMaximumSize(QSize(445, 16777215))
        self.dateEdit_20.setCalendarPopup(True)

        self.gridLayout_57.addWidget(self.dateEdit_20, 1, 1, 1, 1)

        self.label_190 = QLabel(self.frame_27)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMaximumSize(QSize(36, 16777215))

        self.gridLayout_57.addWidget(self.label_190, 1, 0, 1, 1)

        self.label_188 = QLabel(self.frame_27)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_57.addWidget(self.label_188, 1, 2, 1, 1)

        self.tableWidget_22 = QTableWidget(self.frame_27)
        if (self.tableWidget_22.columnCount() < 7):
            self.tableWidget_22.setColumnCount(7)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(0, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(1, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(2, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(3, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(4, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(5, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_22.setHorizontalHeaderItem(6, __qtablewidgetitem166)
        self.tableWidget_22.setObjectName(u"tableWidget_22")
        self.tableWidget_22.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_22.setAlternatingRowColors(True)
        self.tableWidget_22.setGridStyle(Qt.NoPen)

        self.gridLayout_57.addWidget(self.tableWidget_22, 3, 0, 1, 5)

        self.frame_23 = QFrame(self.frame_27)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_89 = QPushButton(self.frame_23)
        self.pushButton_89.setObjectName(u"pushButton_89")
        self.pushButton_89.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")

        self.horizontalLayout_23.addWidget(self.pushButton_89)

        self.pushButton_90 = QPushButton(self.frame_23)
        self.pushButton_90.setObjectName(u"pushButton_90")
        self.pushButton_90.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.pushButton_90)

        self.pushButton_91 = QPushButton(self.frame_23)
        self.pushButton_91.setObjectName(u"pushButton_91")
        self.pushButton_91.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}")
        self.pushButton_91.setFlat(True)

        self.horizontalLayout_23.addWidget(self.pushButton_91)


        self.gridLayout_57.addWidget(self.frame_23, 2, 0, 1, 2)


        self.gridLayout_58.addWidget(self.frame_27, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_25)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.gridLayout_44 = QGridLayout(self.page_12)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(4)
        self.formLayout_4.setVerticalSpacing(11)
        self.formLayout_4.setContentsMargins(20, 0, -1, -1)
        self.label_173 = QLabel(self.page_12)
        self.label_173.setObjectName(u"label_173")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_173)

        self.label_180 = QLabel(self.page_12)
        self.label_180.setObjectName(u"label_180")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_180)

        self.label_211 = QLabel(self.page_12)
        self.label_211.setObjectName(u"label_211")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_211)

        self.label_214 = QLabel(self.page_12)
        self.label_214.setObjectName(u"label_214")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.label_214)

        self.label_212 = QLabel(self.page_12)
        self.label_212.setObjectName(u"label_212")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_212)

        self.label_213 = QLabel(self.page_12)
        self.label_213.setObjectName(u"label_213")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.label_213)

        self.label_218 = QLabel(self.page_12)
        self.label_218.setObjectName(u"label_218")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_218)

        self.label_219 = QLabel(self.page_12)
        self.label_219.setObjectName(u"label_219")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_219)

        self.label_242 = QLabel(self.page_12)
        self.label_242.setObjectName(u"label_242")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.label_242)

        self.label_220 = QLabel(self.page_12)
        self.label_220.setObjectName(u"label_220")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_220)

        self.label_243 = QLabel(self.page_12)
        self.label_243.setObjectName(u"label_243")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.label_243)

        self.label_221 = QLabel(self.page_12)
        self.label_221.setObjectName(u"label_221")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.label_221)

        self.label_244 = QLabel(self.page_12)
        self.label_244.setObjectName(u"label_244")

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.label_244)

        self.label_222 = QLabel(self.page_12)
        self.label_222.setObjectName(u"label_222")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.label_222)

        self.label_223 = QLabel(self.page_12)
        self.label_223.setObjectName(u"label_223")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.label_223)

        self.label_246 = QLabel(self.page_12)
        self.label_246.setObjectName(u"label_246")

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.label_246)

        self.label_224 = QLabel(self.page_12)
        self.label_224.setObjectName(u"label_224")

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.label_224)

        self.label_247 = QLabel(self.page_12)
        self.label_247.setObjectName(u"label_247")

        self.formLayout_4.setWidget(11, QFormLayout.FieldRole, self.label_247)

        self.label_225 = QLabel(self.page_12)
        self.label_225.setObjectName(u"label_225")

        self.formLayout_4.setWidget(12, QFormLayout.LabelRole, self.label_225)

        self.label_248 = QLabel(self.page_12)
        self.label_248.setObjectName(u"label_248")

        self.formLayout_4.setWidget(12, QFormLayout.FieldRole, self.label_248)

        self.label_217 = QLabel(self.page_12)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setMinimumSize(QSize(0, 26))
        self.label_217.setMaximumSize(QSize(16777215, 60))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.label_217)


        self.gridLayout_44.addLayout(self.formLayout_4, 4, 1, 1, 1)

        self.label_151 = QLabel(self.page_12)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_44.addWidget(self.label_151, 1, 2, 1, 1)

        self.dateEdit_14 = QDateEdit(self.page_12)
        self.dateEdit_14.setObjectName(u"dateEdit_14")
        self.dateEdit_14.setCalendarPopup(True)

        self.gridLayout_44.addWidget(self.dateEdit_14, 1, 3, 1, 1)

        self.dateEdit_13 = QDateEdit(self.page_12)
        self.dateEdit_13.setObjectName(u"dateEdit_13")
        self.dateEdit_13.setCalendarPopup(True)

        self.gridLayout_44.addWidget(self.dateEdit_13, 1, 1, 1, 1)

        self.pushButton_45 = QPushButton(self.page_12)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMaximumSize(QSize(60, 16777215))
        self.pushButton_45.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_45.setIcon(icon14)

        self.gridLayout_44.addWidget(self.pushButton_45, 1, 4, 1, 1)

        self.label_141 = QLabel(self.page_12)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_44.addWidget(self.label_141, 1, 0, 1, 1)

        self.label_147 = QLabel(self.page_12)
        self.label_147.setObjectName(u"label_147")

        self.gridLayout_44.addWidget(self.label_147, 0, 2, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(4)
        self.formLayout_5.setVerticalSpacing(18)
        self.formLayout_5.setContentsMargins(21, 0, -1, -1)
        self.label_245 = QLabel(self.page_12)
        self.label_245.setObjectName(u"label_245")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_245)

        self.label_263 = QLabel(self.page_12)
        self.label_263.setObjectName(u"label_263")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.label_263)

        self.label_252 = QLabel(self.page_12)
        self.label_252.setObjectName(u"label_252")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_252)

        self.label_264 = QLabel(self.page_12)
        self.label_264.setObjectName(u"label_264")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.label_264)

        self.label_256 = QLabel(self.page_12)
        self.label_256.setObjectName(u"label_256")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_256)

        self.label_265 = QLabel(self.page_12)
        self.label_265.setObjectName(u"label_265")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.label_265)

        self.label_257 = QLabel(self.page_12)
        self.label_257.setObjectName(u"label_257")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_257)

        self.label_266 = QLabel(self.page_12)
        self.label_266.setObjectName(u"label_266")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.label_266)

        self.label_261 = QLabel(self.page_12)
        self.label_261.setObjectName(u"label_261")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_261)

        self.label_270 = QLabel(self.page_12)
        self.label_270.setObjectName(u"label_270")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.label_270)

        self.label_262 = QLabel(self.page_12)
        self.label_262.setObjectName(u"label_262")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_262)

        self.label_271 = QLabel(self.page_12)
        self.label_271.setObjectName(u"label_271")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.label_271)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(10, QFormLayout.FieldRole, self.verticalSpacer_15)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_16)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_5.setItem(8, QFormLayout.FieldRole, self.verticalSpacer_17)


        self.gridLayout_44.addLayout(self.formLayout_5, 3, 3, 2, 1)

        self.stackedWidget_2.addWidget(self.page_12)

        self.gridLayout_35.addWidget(self.stackedWidget_2, 0, 2, 2, 1)

        self.stackedWidget.addWidget(self.page_9)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.gridLayout = QGridLayout(self.new_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_92 = QLabel(self.new_page)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout.addWidget(self.label_92, 0, 0, 1, 1)

        self.frame_40 = QFrame(self.new_page)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(297, 0))
        self.frame_40.setMaximumSize(QSize(700, 105))
        self.frame_40.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_40)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 66))
        self.frame_41.setMaximumSize(QSize(16777215, 143))
        self.frame_41.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_41)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_176 = QLabel(self.frame_41)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setFont(font)

        self.verticalLayout_35.addWidget(self.label_176)


        self.gridLayout_46.addWidget(self.frame_41, 1, 0, 1, 1)

        self.label_177 = QLabel(self.frame_40)
        self.label_177.setObjectName(u"label_177")

        self.gridLayout_46.addWidget(self.label_177, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_40, 3, 3, 1, 1)

        self.frame_6 = QFrame(self.new_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(617, 0))
        self.frame_6.setMaximumSize(QSize(644, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(70, 16777215))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"")
        self.pushButton_12.setIcon(icon13)
        self.pushButton_12.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_12)

        self.pushButton_16 = QPushButton(self.frame_6)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMaximumSize(QSize(70, 16777215))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"")
        icon21 = QIcon()
        icon21.addFile(u":/icons/images/icons/cil-pen-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon21)
        self.pushButton_16.setIconSize(QSize(37, 37))

        self.horizontalLayout_7.addWidget(self.pushButton_16)

        self.pushButton_11 = QPushButton(self.frame_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(70, 16777215))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"")
        self.pushButton_11.setIcon(icon19)
        self.pushButton_11.setIconSize(QSize(37, 37))

        self.horizontalLayout_7.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.frame_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(70, 16777215))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"")
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QSize(41, 41))

        self.horizontalLayout_7.addWidget(self.pushButton_10)

        self.pushButton_54 = QPushButton(self.frame_6)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setMaximumSize(QSize(70, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_54.setPalette(palette10)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_54.setStyleSheet(u"")
        icon22 = QIcon()
        icon22.addFile(u":/images/images/images/tax.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_54.setIcon(icon22)
        self.pushButton_54.setIconSize(QSize(32, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_54)

        self.pushButton_149 = QPushButton(self.frame_6)
        self.pushButton_149.setObjectName(u"pushButton_149")
        self.pushButton_149.setMinimumSize(QSize(20, 42))
        self.pushButton_149.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_149)


        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.new_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(900, 16777215))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background: transparent;\n"
"	\n"
"	\n"
"	\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox.setPalette(palette11)
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.lineEdit_10 = QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_6.addWidget(self.lineEdit_10)

        self.pushButton_18 = QPushButton(self.frame_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setIcon(icon14)
        self.pushButton_18.setIconSize(QSize(28, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_18)


        self.gridLayout.addWidget(self.frame_2, 7, 0, 1, 5)

        self.tableWidget_4 = QTableWidget(self.new_page)
        if (self.tableWidget_4.columnCount() < 11):
            self.tableWidget_4.setColumnCount(11)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, __qtablewidgetitem177)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMinimumSize(QSize(1230, 304))
        self.tableWidget_4.setMaximumSize(QSize(1208, 500))
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"alternate-background-color: rgb(33, 37, 43);\n"
"selection-color: rgb(85, 170, 0);")
        self.tableWidget_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setGridStyle(Qt.NoPen)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget_4, 8, 0, 1, 1)

        self.frame_42 = QFrame(self.new_page)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(283, 0))
        self.frame_42.setMaximumSize(QSize(697, 105))
        self.frame_42.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_42)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 64))
        self.frame_43.setMaximumSize(QSize(16777215, 126))
        self.frame_43.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_178 = QLabel(self.frame_43)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMinimumSize(QSize(0, 51))
        self.label_178.setMaximumSize(QSize(16777215, 76))
        self.label_178.setFont(font)
        self.label_178.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_178)


        self.gridLayout_47.addWidget(self.frame_43, 1, 0, 1, 1)

        self.label_179 = QLabel(self.frame_42)
        self.label_179.setObjectName(u"label_179")

        self.gridLayout_47.addWidget(self.label_179, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_42, 3, 2, 1, 1)

        self.frame_44 = QFrame(self.new_page)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(272, 0))
        self.frame_44.setMaximumSize(QSize(369, 106))
        self.frame_44.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_44)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 66))
        self.frame_45.setMaximumSize(QSize(16777215, 200))
        self.frame_45.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_45)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_181 = QLabel(self.frame_45)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setFont(font)

        self.verticalLayout_37.addWidget(self.label_181)


        self.gridLayout_48.addWidget(self.frame_45, 1, 0, 1, 1)

        self.label_182 = QLabel(self.frame_44)
        self.label_182.setObjectName(u"label_182")

        self.gridLayout_48.addWidget(self.label_182, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_44, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.new_page)
        self.page_57 = QWidget()
        self.page_57.setObjectName(u"page_57")
        self.gridLayout_114 = QGridLayout(self.page_57)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_114.addItem(self.horizontalSpacer_48, 1, 1, 1, 1)

        self.pushButton_150 = QPushButton(self.page_57)
        self.pushButton_150.setObjectName(u"pushButton_150")
        self.pushButton_150.setMinimumSize(QSize(40, 40))
        self.pushButton_150.setMaximumSize(QSize(89, 16777215))
        self.pushButton_150.setIcon(icon13)

        self.gridLayout_114.addWidget(self.pushButton_150, 1, 0, 1, 1)

        self.label_367 = QLabel(self.page_57)
        self.label_367.setObjectName(u"label_367")

        self.gridLayout_114.addWidget(self.label_367, 0, 0, 1, 1)

        self.frame_111 = QFrame(self.page_57)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.comboBox_42 = QComboBox(self.frame_111)
        self.comboBox_42.setObjectName(u"comboBox_42")
        self.comboBox_42.setMinimumSize(QSize(143, 0))
        self.comboBox_42.setMaximumSize(QSize(119, 28))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_42.setPalette(palette12)
        self.comboBox_42.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_39.addWidget(self.comboBox_42)

        self.lineEdit_83 = QLineEdit(self.frame_111)
        self.lineEdit_83.setObjectName(u"lineEdit_83")
        self.lineEdit_83.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_83.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_39.addWidget(self.lineEdit_83)

        self.pushButton_154 = QPushButton(self.frame_111)
        self.pushButton_154.setObjectName(u"pushButton_154")
        self.pushButton_154.setMaximumSize(QSize(16777215, 20))
        self.pushButton_154.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_154.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_154.setIcon(icon14)
        self.pushButton_154.setIconSize(QSize(28, 30))

        self.horizontalLayout_39.addWidget(self.pushButton_154)


        self.gridLayout_114.addWidget(self.frame_111, 1, 2, 1, 1)

        self.tableWidget_42 = QTableWidget(self.page_57)
        if (self.tableWidget_42.columnCount() < 4):
            self.tableWidget_42.setColumnCount(4)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_42.setHorizontalHeaderItem(0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_42.setHorizontalHeaderItem(1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_42.setHorizontalHeaderItem(2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_42.setHorizontalHeaderItem(3, __qtablewidgetitem181)
        self.tableWidget_42.setObjectName(u"tableWidget_42")
        self.tableWidget_42.setStyleSheet(u"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_42.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_42.setAlternatingRowColors(True)
        self.tableWidget_42.setGridStyle(Qt.NoPen)
        self.tableWidget_42.verticalHeader().setVisible(False)

        self.gridLayout_114.addWidget(self.tableWidget_42, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_57)
        self.page_58 = QWidget()
        self.page_58.setObjectName(u"page_58")
        self.gridLayout_76 = QGridLayout(self.page_58)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.horizontalSpacer_9 = QSpacerItem(500, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_76.addItem(self.horizontalSpacer_9, 2, 3, 2, 1)

        self.label_370 = QLabel(self.page_58)
        self.label_370.setObjectName(u"label_370")

        self.gridLayout_76.addWidget(self.label_370, 3, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_76.addItem(self.verticalSpacer_25, 8, 1, 1, 1)

        self.label_368 = QLabel(self.page_58)
        self.label_368.setObjectName(u"label_368")

        self.gridLayout_76.addWidget(self.label_368, 1, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_76.addItem(self.verticalSpacer_24, 0, 1, 1, 1)

        self.lineEdit_87 = QLineEdit(self.page_58)
        self.lineEdit_87.setObjectName(u"lineEdit_87")
        self.lineEdit_87.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_76.addWidget(self.lineEdit_87, 1, 1, 2, 2)

        self.lineEdit_88 = QLineEdit(self.page_58)
        self.lineEdit_88.setObjectName(u"lineEdit_88")
        self.lineEdit_88.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_76.addWidget(self.lineEdit_88, 3, 1, 1, 2)

        self.lineEdit_89 = QLineEdit(self.page_58)
        self.lineEdit_89.setObjectName(u"lineEdit_89")

        self.gridLayout_76.addWidget(self.lineEdit_89, 4, 1, 1, 1)

        self.label_369 = QLabel(self.page_58)
        self.label_369.setObjectName(u"label_369")

        self.gridLayout_76.addWidget(self.label_369, 4, 0, 1, 1)

        self.frame_115 = QFrame(self.page_58)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 0))
        self.frame_115.setMaximumSize(QSize(16777215, 16777215))
        self.frame_115.setStyleSheet(u"")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_10 = QSpacerItem(12, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_10)

        self.pushButton_159 = QPushButton(self.frame_115)
        self.pushButton_159.setObjectName(u"pushButton_159")
        self.pushButton_159.setStyleSheet(u"background-color: rgb(0, 198, 0);")
        self.pushButton_159.setIcon(icon16)

        self.horizontalLayout_43.addWidget(self.pushButton_159)

        self.pushButton_160 = QPushButton(self.frame_115)
        self.pushButton_160.setObjectName(u"pushButton_160")
        self.pushButton_160.setStyleSheet(u"background-color: rgb(236, 14, 18);")
        self.pushButton_160.setIcon(icon18)

        self.horizontalLayout_43.addWidget(self.pushButton_160)

        self.pushButton_158 = QPushButton(self.frame_115)
        self.pushButton_158.setObjectName(u"pushButton_158")
        self.pushButton_158.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_43.addWidget(self.pushButton_158)


        self.gridLayout_76.addWidget(self.frame_115, 7, 1, 1, 2)

        self.stackedWidget.addWidget(self.page_58)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 556, 307, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_134 = QLabel(self.frame_5)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(323, 426, 16, 43))
        self.label_134.setMinimumSize(QSize(0, 43))
        self.gridLayout_94 = QGridLayout(self.frame_5)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.label_172 = QLabel(self.frame_5)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMaximumSize(QSize(16777215, 34))

        self.gridLayout_94.addWidget(self.label_172, 0, 0, 1, 1)

        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_94.addWidget(self.line_2, 4, 1, 1, 1)

        self.tableWidget_16 = QTableWidget(self.frame_5)
        if (self.tableWidget_16.columnCount() < 8):
            self.tableWidget_16.setColumnCount(8)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(0, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(1, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(2, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(3, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(4, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(5, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(6, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_16.setHorizontalHeaderItem(7, __qtablewidgetitem189)
        self.tableWidget_16.setObjectName(u"tableWidget_16")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_16.setPalette(palette13)
        self.tableWidget_16.setStyleSheet(u"background-color: rgb(29, 29, 29);\n"
"alternate-background-color: rgb(33, 37, 43);")
        self.tableWidget_16.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_16.setAlternatingRowColors(True)
        self.tableWidget_16.setShowGrid(False)
        self.tableWidget_16.setGridStyle(Qt.NoPen)
        self.tableWidget_16.verticalHeader().setVisible(False)

        self.gridLayout_94.addWidget(self.tableWidget_16, 1, 0, 3, 1)

        self.frame_89 = QFrame(self.frame_5)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.frame_89.setFrameShape(QFrame.WinPanel)
        self.frame_89.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_89)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_123 = QLabel(self.frame_89)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.label_123.setFrameShape(QFrame.Box)
        self.label_123.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.label_123, 0, 4, 1, 1)

        self.lineEdit_13 = QLineEdit(self.frame_89)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_9.addWidget(self.lineEdit_13, 3, 4, 1, 1)

        self.label_125 = QLabel(self.frame_89)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_9.addWidget(self.label_125, 4, 3, 1, 1)

        self.label_113 = QLabel(self.frame_89)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_9.addWidget(self.label_113, 5, 3, 1, 1)

        self.label_112 = QLabel(self.frame_89)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_9.addWidget(self.label_112, 3, 3, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_89)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout_9.addWidget(self.comboBox_4, 5, 1, 1, 1)

        self.label_124 = QLabel(self.frame_89)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_9.addWidget(self.label_124, 0, 3, 1, 1)

        self.label_116 = QLabel(self.frame_89)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_9.addWidget(self.label_116, 5, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_89)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout_9.addWidget(self.comboBox_5, 4, 4, 1, 1)

        self.label_114 = QLabel(self.frame_89)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_9.addWidget(self.label_114, 5, 4, 1, 1)

        self.pushButton_24 = QPushButton(self.frame_89)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 0))
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 20px;\n"
"}QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.pushButton_24.setIcon(icon20)
        self.pushButton_24.setIconSize(QSize(60, 44))
        self.pushButton_24.setFlat(False)

        self.gridLayout_9.addWidget(self.pushButton_24, 6, 4, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_89)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMaximumSize(QSize(100, 40))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"")
        self.pushButton_20.setIcon(icon16)
        self.pushButton_20.setIconSize(QSize(77, 68))

        self.gridLayout_9.addWidget(self.pushButton_20, 6, 3, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_89)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_9.addWidget(self.lineEdit_14, 4, 1, 1, 1)

        self.label_117 = QLabel(self.frame_89)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_9.addWidget(self.label_117, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_89)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(88, 16777215))
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setIconSize(QSize(22, 24))

        self.gridLayout_9.addWidget(self.pushButton_2, 4, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_89)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_9.addWidget(self.lineEdit_8, 3, 1, 1, 1)

        self.label_76 = QLabel(self.frame_89)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_9.addWidget(self.label_76, 3, 0, 1, 1)


        self.gridLayout_94.addWidget(self.frame_89, 3, 1, 1, 1)

        self.frame_90 = QFrame(self.frame_5)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 0))
        self.frame_90.setMaximumSize(QSize(16777215, 16777215))
        self.frame_90.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.frame_90.setFrameShape(QFrame.Box)
        self.frame_90.setFrameShadow(QFrame.Plain)
        self.gridLayout_93 = QGridLayout(self.frame_90)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.label_86 = QLabel(self.frame_90)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_93.addWidget(self.label_86, 0, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.frame_90)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMaximumSize(QSize(86, 16777215))
        self.lineEdit_33.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.lineEdit_33.setReadOnly(True)

        self.gridLayout_93.addWidget(self.lineEdit_33, 0, 7, 1, 1)

        self.label_305 = QLabel(self.frame_90)
        self.label_305.setObjectName(u"label_305")

        self.gridLayout_93.addWidget(self.label_305, 3, 0, 1, 1)

        self.comboBox_12 = QComboBox(self.frame_90)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.comboBox_12.setEditable(True)

        self.gridLayout_93.addWidget(self.comboBox_12, 0, 1, 1, 1)

        self.pushButton_71 = QPushButton(self.frame_90)
        self.pushButton_71.setObjectName(u"pushButton_71")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(0, 198, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_71.setPalette(palette14)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_71.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 198, 0);\n"
"border-radius : 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_71.setIcon(icon13)
        self.pushButton_71.setIconSize(QSize(42, 39))

        self.gridLayout_93.addWidget(self.pushButton_71, 2, 1, 1, 1)

        self.comboBox_14 = QComboBox(self.frame_90)
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setMinimumSize(QSize(361, 0))
        self.comboBox_14.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_93.addWidget(self.comboBox_14, 3, 1, 1, 1)

        self.label_90 = QLabel(self.frame_90)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_93.addWidget(self.label_90, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_90)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush13 = QBrush(QColor(0, 0, 235, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.Highlight, brush13)
        brush14 = QBrush(QColor(255, 255, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Highlight, brush13)
        palette15.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette15.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.lineEdit_7.setPalette(palette15)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_93.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.label_161 = QLabel(self.frame_90)
        self.label_161.setObjectName(u"label_161")

        self.gridLayout_93.addWidget(self.label_161, 0, 6, 1, 1)

        self.label_306 = QLabel(self.frame_90)
        self.label_306.setObjectName(u"label_306")

        self.gridLayout_93.addWidget(self.label_306, 4, 0, 1, 1)

        self.comboBox_24 = QComboBox(self.frame_90)
        self.comboBox_24.setObjectName(u"comboBox_24")

        self.gridLayout_93.addWidget(self.comboBox_24, 4, 1, 1, 1)


        self.gridLayout_94.addWidget(self.frame_90, 1, 1, 2, 1)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_19 = QGridLayout(self.page_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.stackedWidget_5 = QStackedWidget(self.page_10)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_54 = QWidget()
        self.page_54.setObjectName(u"page_54")
        self.gridLayout_111 = QGridLayout(self.page_54)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.frame_36 = QFrame(self.page_54)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(797, 0))
        self.frame_36.setMaximumSize(QSize(500, 16777215))
        self.frame_36.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_36)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setVerticalSpacing(6)
        self.label_143 = QLabel(self.frame_36)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_33.addWidget(self.label_143, 11, 0, 1, 1)

        self.lineEdit_42 = QLineEdit(self.frame_36)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.lineEdit_42, 5, 1, 1, 2)

        self.lineEdit_41 = QLineEdit(self.frame_36)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.lineEdit_41, 4, 1, 1, 2)

        self.label_149 = QLabel(self.frame_36)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_33.addWidget(self.label_149, 6, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.frame_36)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.lineEdit_27, 7, 1, 1, 2)

        self.label_115 = QLabel(self.frame_36)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_33.addWidget(self.label_115, 10, 0, 1, 1)

        self.label_139 = QLabel(self.frame_36)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_33.addWidget(self.label_139, 3, 0, 1, 1)

        self.label_150 = QLabel(self.frame_36)
        self.label_150.setObjectName(u"label_150")

        self.gridLayout_33.addWidget(self.label_150, 5, 0, 1, 1)

        self.lineEdit_43 = QLineEdit(self.frame_36)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.lineEdit_43, 6, 1, 1, 2)

        self.frame_106 = QFrame(self.frame_36)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(300, 0))
        self.frame_106.setMaximumSize(QSize(306, 16777215))
        self.frame_106.setStyleSheet(u"")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_31 = QPushButton(self.frame_106)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 31))
        self.pushButton_31.setMaximumSize(QSize(100, 50))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush15 = QBrush(QColor(95, 95, 95, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_31.setPalette(palette16)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_31.setStyleSheet(u"QPushButton{\n"
"    border-radius : 15px;	\n"
"	\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_17.addWidget(self.pushButton_31)

        self.pushButton_44 = QPushButton(self.frame_106)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setMinimumSize(QSize(100, 0))
        self.pushButton_44.setMaximumSize(QSize(116, 50))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_44.setPalette(palette17)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_44.setStyleSheet(u"QPushButton{\n"
"    border-radius : 15px;	\n"
"	\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"}")

        self.horizontalLayout_17.addWidget(self.pushButton_44)


        self.gridLayout_33.addWidget(self.frame_106, 15, 1, 1, 1)

        self.label = QLabel(self.frame_36)
        self.label.setObjectName(u"label")

        self.gridLayout_33.addWidget(self.label, 8, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.frame_36)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.plainTextEdit, 10, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.frame_36)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")
        self.comboBox_8.setEditable(True)

        self.gridLayout_33.addWidget(self.comboBox_8, 8, 1, 1, 1)

        self.lineEdit_40 = QLineEdit(self.frame_36)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.lineEdit_40, 3, 1, 1, 2)

        self.plainTextEdit_2 = QPlainTextEdit(self.frame_36)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_33.addWidget(self.plainTextEdit_2, 11, 1, 1, 1)

        self.label_111 = QLabel(self.frame_36)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_33.addWidget(self.label_111, 7, 0, 1, 1)

        self.label_118 = QLabel(self.frame_36)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_33.addWidget(self.label_118, 9, 1, 1, 1)

        self.label_136 = QLabel(self.frame_36)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMaximumSize(QSize(16777215, 90))

        self.gridLayout_33.addWidget(self.label_136, 0, 0, 1, 1)

        self.label_140 = QLabel(self.frame_36)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_33.addWidget(self.label_140, 4, 0, 1, 1)


        self.gridLayout_111.addWidget(self.frame_36, 0, 0, 1, 1)

        self.stackedWidget_5.addWidget(self.page_54)
        self.page_55 = QWidget()
        self.page_55.setObjectName(u"page_55")
        self.gridLayout_112 = QGridLayout(self.page_55)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.label_356 = QLabel(self.page_55)
        self.label_356.setObjectName(u"label_356")

        self.gridLayout_112.addWidget(self.label_356, 0, 0, 1, 1)

        self.pushButton_143 = QPushButton(self.page_55)
        self.pushButton_143.setObjectName(u"pushButton_143")
        self.pushButton_143.setIcon(icon13)
        self.pushButton_143.setIconSize(QSize(48, 47))

        self.gridLayout_112.addWidget(self.pushButton_143, 1, 0, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_112.addItem(self.horizontalSpacer_46, 1, 1, 1, 1)

        self.tableWidget_41 = QTableWidget(self.page_55)
        if (self.tableWidget_41.columnCount() < 6):
            self.tableWidget_41.setColumnCount(6)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(0, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(1, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(2, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(3, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(4, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_41.setHorizontalHeaderItem(5, __qtablewidgetitem195)
        self.tableWidget_41.setObjectName(u"tableWidget_41")

        self.gridLayout_112.addWidget(self.tableWidget_41, 2, 0, 1, 2)

        self.stackedWidget_5.addWidget(self.page_55)
        self.page_56 = QWidget()
        self.page_56.setObjectName(u"page_56")
        self.gridLayout_113 = QGridLayout(self.page_56)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.comboBox_37 = QComboBox(self.page_56)
        self.comboBox_37.setObjectName(u"comboBox_37")
        self.comboBox_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_113.addWidget(self.comboBox_37, 5, 1, 1, 1)

        self.lineEdit_78 = QLineEdit(self.page_56)
        self.lineEdit_78.setObjectName(u"lineEdit_78")
        self.lineEdit_78.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_78.setEchoMode(QLineEdit.Password)

        self.gridLayout_113.addWidget(self.lineEdit_78, 3, 1, 1, 1)

        self.comboBox_38 = QComboBox(self.page_56)
        self.comboBox_38.setObjectName(u"comboBox_38")
        self.comboBox_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_113.addWidget(self.comboBox_38, 0, 1, 1, 1)

        self.frame_107 = QFrame(self.page_56)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.pushButton_146 = QPushButton(self.frame_107)
        self.pushButton_146.setObjectName(u"pushButton_146")
        self.pushButton_146.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.pushButton_146)

        self.pushButton_148 = QPushButton(self.frame_107)
        self.pushButton_148.setObjectName(u"pushButton_148")

        self.horizontalLayout_35.addWidget(self.pushButton_148)

        self.pushButton_147 = QPushButton(self.frame_107)
        self.pushButton_147.setObjectName(u"pushButton_147")
        self.pushButton_147.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.pushButton_147)


        self.gridLayout_113.addWidget(self.frame_107, 7, 0, 1, 2)

        self.comboBox_35 = QComboBox(self.page_56)
        self.comboBox_35.setObjectName(u"comboBox_35")
        self.comboBox_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_113.addWidget(self.comboBox_35, 4, 1, 1, 1)

        self.label_366 = QLabel(self.page_56)
        self.label_366.setObjectName(u"label_366")

        self.gridLayout_113.addWidget(self.label_366, 2, 0, 1, 1)

        self.label_361 = QLabel(self.page_56)
        self.label_361.setObjectName(u"label_361")

        self.gridLayout_113.addWidget(self.label_361, 0, 0, 1, 1)

        self.lineEdit_77 = QLineEdit(self.page_56)
        self.lineEdit_77.setObjectName(u"lineEdit_77")
        self.lineEdit_77.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_77.setEchoMode(QLineEdit.Password)

        self.gridLayout_113.addWidget(self.lineEdit_77, 2, 1, 1, 1)

        self.label_365 = QLabel(self.page_56)
        self.label_365.setObjectName(u"label_365")

        self.gridLayout_113.addWidget(self.label_365, 4, 0, 1, 1)

        self.label_363 = QLabel(self.page_56)
        self.label_363.setObjectName(u"label_363")

        self.gridLayout_113.addWidget(self.label_363, 5, 0, 1, 1)

        self.label_362 = QLabel(self.page_56)
        self.label_362.setObjectName(u"label_362")

        self.gridLayout_113.addWidget(self.label_362, 3, 0, 1, 1)

        self.label_364 = QLabel(self.page_56)
        self.label_364.setObjectName(u"label_364")

        self.gridLayout_113.addWidget(self.label_364, 6, 0, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_113.addItem(self.horizontalSpacer_47, 3, 2, 1, 1)

        self.label_360 = QLabel(self.page_56)
        self.label_360.setObjectName(u"label_360")

        self.gridLayout_113.addWidget(self.label_360, 1, 0, 1, 1)

        self.comboBox_36 = QComboBox(self.page_56)
        self.comboBox_36.setObjectName(u"comboBox_36")
        self.comboBox_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_113.addWidget(self.comboBox_36, 6, 1, 1, 1)

        self.lineEdit_79 = QLineEdit(self.page_56)
        self.lineEdit_79.setObjectName(u"lineEdit_79")
        self.lineEdit_79.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_113.addWidget(self.lineEdit_79, 1, 1, 1, 1)

        self.stackedWidget_5.addWidget(self.page_56)

        self.gridLayout_19.addWidget(self.stackedWidget_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_10)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.gridLayout_37 = QGridLayout(self.page_15)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_29 = QLabel(self.page_15)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_37.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_80 = QLabel(self.page_15)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_37.addWidget(self.label_80, 3, 1, 1, 1)

        self.pushButton_35 = QPushButton(self.page_15)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(0, 228))
        self.pushButton_35.setMaximumSize(QSize(16777215, 243))
        self.pushButton_35.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_35.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(33, 37, 43);\n"
"border-radius : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u"../Downloads/payment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_35.setIcon(icon23)
        self.pushButton_35.setIconSize(QSize(65, 72))

        self.gridLayout_37.addWidget(self.pushButton_35, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.gridLayout_38 = QGridLayout(self.page_16)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.lineEdit_21 = QLineEdit(self.page_16)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_38.addWidget(self.lineEdit_21, 4, 3, 1, 1)

        self.comboBox_7 = QComboBox(self.page_16)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout_38.addWidget(self.comboBox_7, 4, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.page_16)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")
        self.comboBox_6.setEditable(True)

        self.gridLayout_38.addWidget(self.comboBox_6, 4, 0, 1, 1)

        self.label_68 = QLabel(self.page_16)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_38.addWidget(self.label_68, 3, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.page_16)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 0))
        self.pushButton_15.setMaximumSize(QSize(30, 16777215))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius : 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_15.setIcon(icon15)
        self.pushButton_15.setIconSize(QSize(26, 30))

        self.gridLayout_38.addWidget(self.pushButton_15, 0, 0, 1, 1)

        self.label_38 = QLabel(self.page_16)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_38.addWidget(self.label_38, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.page_16)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(30, 0))
        self.lineEdit_20.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_20.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_38.addWidget(self.lineEdit_20, 4, 2, 1, 1)

        self.label_39 = QLabel(self.page_16)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_38.addWidget(self.label_39, 3, 0, 1, 1)

        self.tableWidget_17 = QTableWidget(self.page_16)
        if (self.tableWidget_17.columnCount() < 7):
            self.tableWidget_17.setColumnCount(7)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(0, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(3, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(4, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(5, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget_17.setHorizontalHeaderItem(6, __qtablewidgetitem202)
        self.tableWidget_17.setObjectName(u"tableWidget_17")
        self.tableWidget_17.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_38.addWidget(self.tableWidget_17, 6, 0, 1, 5)

        self.pushButton_40 = QPushButton(self.page_16)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_40.setIcon(icon16)

        self.gridLayout_38.addWidget(self.pushButton_40, 4, 4, 1, 1)

        self.label_56 = QLabel(self.page_16)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_38.addWidget(self.label_56, 3, 1, 1, 1)

        self.label_73 = QLabel(self.page_16)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_38.addWidget(self.label_73, 5, 0, 1, 1)

        self.label_72 = QLabel(self.page_16)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_38.addWidget(self.label_72, 3, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_16)
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.gridLayout_64 = QGridLayout(self.page_26)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_64.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_64.addItem(self.verticalSpacer_5, 12, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_64.addItem(self.verticalSpacer_4, 13, 1, 1, 1)

        self.label_210 = QLabel(self.page_26)
        self.label_210.setObjectName(u"label_210")

        self.gridLayout_64.addWidget(self.label_210, 5, 0, 1, 1)

        self.label_208 = QLabel(self.page_26)
        self.label_208.setObjectName(u"label_208")

        self.gridLayout_64.addWidget(self.label_208, 3, 0, 1, 1)

        self.lineEdit_51 = QLineEdit(self.page_26)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_51, 8, 1, 1, 1)

        self.lineEdit_50 = QLineEdit(self.page_26)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_50, 7, 1, 1, 1)

        self.lineEdit_46 = QLineEdit(self.page_26)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_46, 3, 1, 1, 1)

        self.lineEdit_48 = QLineEdit(self.page_26)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_48, 5, 1, 1, 1)

        self.label_209 = QLabel(self.page_26)
        self.label_209.setObjectName(u"label_209")

        self.gridLayout_64.addWidget(self.label_209, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_64.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)

        self.label_215 = QLabel(self.page_26)
        self.label_215.setObjectName(u"label_215")

        self.gridLayout_64.addWidget(self.label_215, 6, 0, 1, 1)

        self.label_226 = QLabel(self.page_26)
        self.label_226.setObjectName(u"label_226")

        self.gridLayout_64.addWidget(self.label_226, 8, 0, 1, 1)

        self.label_216 = QLabel(self.page_26)
        self.label_216.setObjectName(u"label_216")

        self.gridLayout_64.addWidget(self.label_216, 7, 0, 1, 1)

        self.pushButton_79 = QPushButton(self.page_26)
        self.pushButton_79.setObjectName(u"pushButton_79")
        self.pushButton_79.setMaximumSize(QSize(70, 16777215))
        self.pushButton_79.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_79.setIcon(icon16)

        self.gridLayout_64.addWidget(self.pushButton_79, 11, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_64.addItem(self.verticalSpacer_2, 14, 1, 1, 1)

        self.lineEdit_49 = QLineEdit(self.page_26)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_49, 6, 1, 1, 1)

        self.pushButton_80 = QPushButton(self.page_26)
        self.pushButton_80.setObjectName(u"pushButton_80")
        self.pushButton_80.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_80.setIcon(icon15)

        self.gridLayout_64.addWidget(self.pushButton_80, 0, 0, 1, 1)

        self.lineEdit_90 = QLineEdit(self.page_26)
        self.lineEdit_90.setObjectName(u"lineEdit_90")
        self.lineEdit_90.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_90, 9, 1, 1, 1)

        self.lineEdit_47 = QLineEdit(self.page_26)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_47, 4, 1, 1, 1)

        self.lineEdit_91 = QLineEdit(self.page_26)
        self.lineEdit_91.setObjectName(u"lineEdit_91")
        self.lineEdit_91.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_64.addWidget(self.lineEdit_91, 10, 1, 1, 1)

        self.label_371 = QLabel(self.page_26)
        self.label_371.setObjectName(u"label_371")

        self.gridLayout_64.addWidget(self.label_371, 9, 0, 1, 1)

        self.label_372 = QLabel(self.page_26)
        self.label_372.setObjectName(u"label_372")

        self.gridLayout_64.addWidget(self.label_372, 10, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_26)
        self.page_29 = QWidget()
        self.page_29.setObjectName(u"page_29")
        self.gridLayout_65 = QGridLayout(self.page_29)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.lineEdit_55 = QLineEdit(self.page_29)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_55, 3, 1, 1, 1)

        self.lineEdit_56 = QLineEdit(self.page_29)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_56, 2, 1, 1, 1)

        self.lineEdit_52 = QLineEdit(self.page_29)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_52, 5, 1, 1, 1)

        self.pushButton_81 = QPushButton(self.page_29)
        self.pushButton_81.setObjectName(u"pushButton_81")
        self.pushButton_81.setMaximumSize(QSize(70, 16777215))
        self.pushButton_81.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_81.setIcon(icon16)

        self.gridLayout_65.addWidget(self.pushButton_81, 8, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_65.addItem(self.verticalSpacer_13, 9, 1, 1, 1)

        self.label_236 = QLabel(self.page_29)
        self.label_236.setObjectName(u"label_236")

        self.gridLayout_65.addWidget(self.label_236, 4, 0, 1, 1)

        self.label_237 = QLabel(self.page_29)
        self.label_237.setObjectName(u"label_237")

        self.gridLayout_65.addWidget(self.label_237, 5, 0, 1, 1)

        self.label_232 = QLabel(self.page_29)
        self.label_232.setObjectName(u"label_232")

        self.gridLayout_65.addWidget(self.label_232, 7, 0, 1, 1)

        self.label_235 = QLabel(self.page_29)
        self.label_235.setObjectName(u"label_235")

        self.gridLayout_65.addWidget(self.label_235, 3, 0, 1, 1)

        self.label_233 = QLabel(self.page_29)
        self.label_233.setObjectName(u"label_233")

        self.gridLayout_65.addWidget(self.label_233, 2, 0, 1, 1)

        self.label_234 = QLabel(self.page_29)
        self.label_234.setObjectName(u"label_234")

        self.gridLayout_65.addWidget(self.label_234, 6, 0, 1, 1)

        self.lineEdit_53 = QLineEdit(self.page_29)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_53, 6, 1, 1, 1)

        self.pushButton_82 = QPushButton(self.page_29)
        self.pushButton_82.setObjectName(u"pushButton_82")
        self.pushButton_82.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_82.setIcon(icon15)

        self.gridLayout_65.addWidget(self.pushButton_82, 0, 0, 1, 1)

        self.lineEdit_54 = QLineEdit(self.page_29)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_54, 4, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_65.addItem(self.verticalSpacer_14, 1, 1, 1, 1)

        self.lineEdit_57 = QLineEdit(self.page_29)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_65.addWidget(self.lineEdit_57, 7, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_65.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_29)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.gridLayout_14 = QGridLayout(self.page_18)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_99 = QLabel(self.page_18)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_14.addWidget(self.label_99, 4, 0, 1, 2)

        self.label_98 = QLabel(self.page_18)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_14.addWidget(self.label_98, 3, 0, 1, 2)

        self.lineEdit_38 = QLineEdit(self.page_18)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_38, 3, 2, 1, 1)

        self.label_97 = QLabel(self.page_18)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_14.addWidget(self.label_97, 5, 0, 1, 2)

        self.pushButton_67 = QPushButton(self.page_18)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(30, 0))
        self.pushButton_67.setMaximumSize(QSize(30, 16777215))
        self.pushButton_67.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_67.setStyleSheet(u"")
        self.pushButton_67.setIcon(icon15)
        self.pushButton_67.setIconSize(QSize(26, 30))

        self.gridLayout_14.addWidget(self.pushButton_67, 0, 0, 1, 1)

        self.lineEdit_37 = QLineEdit(self.page_18)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_37, 2, 2, 1, 1)

        self.lineEdit_36 = QLineEdit(self.page_18)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_36, 4, 2, 1, 1)

        self.comboBox_11 = QComboBox(self.page_18)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.gridLayout_14.addWidget(self.comboBox_11, 8, 2, 1, 1)

        self.dateEdit_6 = QDateEdit(self.page_18)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.dateEdit_6.setCalendarPopup(True)

        self.gridLayout_14.addWidget(self.dateEdit_6, 5, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 4, 5, 1, 1)

        self.label_206 = QLabel(self.page_18)
        self.label_206.setObjectName(u"label_206")

        self.gridLayout_14.addWidget(self.label_206, 8, 0, 1, 1)

        self.pushButton_41 = QPushButton(self.page_18)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setMaximumSize(QSize(78, 34))
        self.pushButton_41.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_14.addWidget(self.pushButton_41, 11, 2, 1, 1)

        self.tableWidget_18 = QTableWidget(self.page_18)
        if (self.tableWidget_18.columnCount() < 7):
            self.tableWidget_18.setColumnCount(7)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(0, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(1, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(2, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(3, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(4, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(5, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_18.setHorizontalHeaderItem(6, __qtablewidgetitem209)
        self.tableWidget_18.setObjectName(u"tableWidget_18")
        self.tableWidget_18.setStyleSheet(u"background-color: rgb(29, 29, 29);")

        self.gridLayout_14.addWidget(self.tableWidget_18, 12, 0, 1, 6)

        self.label_87 = QLabel(self.page_18)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_14.addWidget(self.label_87, 1, 0, 1, 2)

        self.label_91 = QLabel(self.page_18)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_14.addWidget(self.label_91, 2, 0, 1, 2)

        self.label_200 = QLabel(self.page_18)
        self.label_200.setObjectName(u"label_200")

        self.gridLayout_14.addWidget(self.label_200, 2, 3, 1, 1)

        self.lineEdit_34 = QLineEdit(self.page_18)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_34, 2, 4, 1, 1)

        self.label_100 = QLabel(self.page_18)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_14.addWidget(self.label_100, 3, 3, 1, 1)

        self.lineEdit_26 = QLineEdit(self.page_18)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_26, 3, 4, 1, 1)

        self.label_207 = QLabel(self.page_18)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout_14.addWidget(self.label_207, 4, 3, 1, 1)

        self.lineEdit = QLineEdit(self.page_18)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit, 4, 4, 1, 1)

        self.label_201 = QLabel(self.page_18)
        self.label_201.setObjectName(u"label_201")

        self.gridLayout_14.addWidget(self.label_201, 5, 3, 1, 1)

        self.lineEdit_35 = QLineEdit(self.page_18)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.gridLayout_14.addWidget(self.lineEdit_35, 5, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_18)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_10 = QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.stackedwidget_3 = QStackedWidget(self.page_2)
        self.stackedwidget_3.setObjectName(u"stackedwidget_3")
        self.stackedwidget_3.setMinimumSize(QSize(0, 580))
        self.stackedwidget_3.setMaximumSize(QSize(1150, 580))
        self.stackedwidget_3.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.gridLayout_18 = QGridLayout(self.page_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.stackedwidget_3.addWidget(self.page_14)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_36 = QGridLayout(self.page_13)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.tableWidget_13 = QTableWidget(self.page_13)
        if (self.tableWidget_13.columnCount() < 6):
            self.tableWidget_13.setColumnCount(6)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(5, __qtablewidgetitem215)
        self.tableWidget_13.setObjectName(u"tableWidget_13")
        self.tableWidget_13.setMinimumSize(QSize(0, 431))
        self.tableWidget_13.setMaximumSize(QSize(16777215, 1000))

        self.gridLayout_36.addWidget(self.tableWidget_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.page_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_36.addWidget(self.label_14, 0, 0, 1, 1)

        self.frame_59 = QFrame(self.page_13)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(100, 276))
        self.frame_59.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_59)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(12, 9, 5, 0)
        self.lib_btn2_5 = QPushButton(self.frame_59)
        self.lib_btn2_5.setObjectName(u"lib_btn2_5")
        self.lib_btn2_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn2_5.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn2_5.setIcon(icon13)
        self.lib_btn2_5.setIconSize(QSize(46, 42))

        self.verticalLayout_33.addWidget(self.lib_btn2_5)

        self.lib_btn3_6 = QPushButton(self.frame_59)
        self.lib_btn3_6.setObjectName(u"lib_btn3_6")
        self.lib_btn3_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn3_6.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn3_6.setIcon(icon19)
        self.lib_btn3_6.setIconSize(QSize(43, 43))

        self.verticalLayout_33.addWidget(self.lib_btn3_6)

        self.pushButton_55 = QPushButton(self.frame_59)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_55.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_55.setIcon(icon21)
        self.pushButton_55.setIconSize(QSize(53, 40))

        self.verticalLayout_33.addWidget(self.pushButton_55)

        self.lib_btn4_6 = QPushButton(self.frame_59)
        self.lib_btn4_6.setObjectName(u"lib_btn4_6")
        self.lib_btn4_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn4_6.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn4_6.setIcon(icon2)
        self.lib_btn4_6.setIconSize(QSize(52, 38))

        self.verticalLayout_33.addWidget(self.lib_btn4_6)


        self.gridLayout_36.addWidget(self.frame_59, 1, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.stackedwidget_3.addWidget(self.page_13)
        self.asset_page = QWidget()
        self.asset_page.setObjectName(u"asset_page")
        self.gridLayout_11 = QGridLayout(self.asset_page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_30 = QFrame(self.asset_page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(100, 276))
        self.frame_30.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_30)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(12, 9, 5, 0)
        self.addbutton = QPushButton(self.frame_30)
        self.addbutton.setObjectName(u"addbutton")
        self.addbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addbutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.addbutton.setIcon(icon13)
        self.addbutton.setIconSize(QSize(46, 42))

        self.verticalLayout_23.addWidget(self.addbutton)

        self.deletebutton = QPushButton(self.frame_30)
        self.deletebutton.setObjectName(u"deletebutton")
        self.deletebutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletebutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.deletebutton.setIcon(icon19)
        self.deletebutton.setIconSize(QSize(43, 43))

        self.verticalLayout_23.addWidget(self.deletebutton)

        self.pushButton_47 = QPushButton(self.frame_30)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_47.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_47.setIcon(icon21)
        self.pushButton_47.setIconSize(QSize(53, 40))

        self.verticalLayout_23.addWidget(self.pushButton_47)

        self.savebutton = QPushButton(self.frame_30)
        self.savebutton.setObjectName(u"savebutton")
        self.savebutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.savebutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.savebutton.setIcon(icon2)
        self.savebutton.setIconSize(QSize(52, 38))

        self.verticalLayout_23.addWidget(self.savebutton)


        self.gridLayout_11.addWidget(self.frame_30, 3, 2, 1, 1)

        self.label_13 = QLabel(self.asset_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(127, 20))

        self.gridLayout_11.addWidget(self.label_13, 0, 0, 1, 1)

        self.tableAsset = QTableWidget(self.asset_page)
        if (self.tableAsset.columnCount() < 7):
            self.tableAsset.setColumnCount(7)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(2, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(3, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(4, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(5, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        self.tableAsset.setHorizontalHeaderItem(6, __qtablewidgetitem222)
        self.tableAsset.setObjectName(u"tableAsset")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableAsset.sizePolicy().hasHeightForWidth())
        self.tableAsset.setSizePolicy(sizePolicy3)
        self.tableAsset.setMinimumSize(QSize(0, 442))
        self.tableAsset.setMaximumSize(QSize(16777215, 900))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush16 = QBrush(QColor(34, 34, 34, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableAsset.setPalette(palette18)
        self.tableAsset.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableAsset.setMouseTracking(True)
        self.tableAsset.setAutoFillBackground(False)
        self.tableAsset.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.tableAsset.setFrameShape(QFrame.Box)
        self.tableAsset.setFrameShadow(QFrame.Sunken)
        self.tableAsset.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableAsset.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableAsset.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableAsset.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableAsset.setDragEnabled(True)
        self.tableAsset.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableAsset.setDefaultDropAction(Qt.CopyAction)
        self.tableAsset.setAlternatingRowColors(False)
        self.tableAsset.setGridStyle(Qt.SolidLine)
        self.tableAsset.setRowCount(0)
        self.tableAsset.horizontalHeader().setVisible(True)
        self.tableAsset.horizontalHeader().setCascadingSectionResizes(True)
        self.tableAsset.verticalHeader().setVisible(False)

        self.gridLayout_11.addWidget(self.tableAsset, 3, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.stackedwidget_3.addWidget(self.asset_page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_21 = QGridLayout(self.page_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.fixed_assets_tb = QTableWidget(self.page_6)
        if (self.fixed_assets_tb.columnCount() < 7):
            self.fixed_assets_tb.setColumnCount(7)
        __qtablewidgetitem223 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(0, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        __qtablewidgetitem224.setBackground(QColor(255, 255, 255));
        self.fixed_assets_tb.setHorizontalHeaderItem(1, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(2, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(3, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(4, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(5, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.fixed_assets_tb.setHorizontalHeaderItem(6, __qtablewidgetitem229)
        self.fixed_assets_tb.setObjectName(u"fixed_assets_tb")
        self.fixed_assets_tb.setMinimumSize(QSize(0, 442))
        self.fixed_assets_tb.setMaximumSize(QSize(16777215, 1030))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.fixed_assets_tb.setPalette(palette19)
        self.fixed_assets_tb.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.fixed_assets_tb.setFrameShape(QFrame.Box)
        self.fixed_assets_tb.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.fixed_assets_tb.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.fixed_assets_tb.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.fixed_assets_tb.horizontalHeader().setVisible(True)
        self.fixed_assets_tb.horizontalHeader().setCascadingSectionResizes(True)
        self.fixed_assets_tb.verticalHeader().setVisible(False)
        self.fixed_assets_tb.verticalHeader().setStretchLastSection(False)

        self.gridLayout_21.addWidget(self.fixed_assets_tb, 1, 0, 1, 1)

        self.frame_54 = QFrame(self.page_6)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(100, 276))
        self.frame_54.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_54)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(12, 9, 5, 0)
        self.pushButton_4 = QPushButton(self.frame_54)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_4.setIcon(icon13)
        self.pushButton_4.setIconSize(QSize(46, 42))

        self.verticalLayout_24.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_54)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_5.setIcon(icon19)
        self.pushButton_5.setIconSize(QSize(43, 43))

        self.verticalLayout_24.addWidget(self.pushButton_5)

        self.pushButton_46 = QPushButton(self.frame_54)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_46.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_46.setIcon(icon21)
        self.pushButton_46.setIconSize(QSize(53, 40))

        self.verticalLayout_24.addWidget(self.pushButton_46)

        self.pushButton_6 = QPushButton(self.frame_54)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(52, 38))

        self.verticalLayout_24.addWidget(self.pushButton_6)


        self.gridLayout_21.addWidget(self.frame_54, 1, 1, 1, 1)

        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 19))

        self.gridLayout_21.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.stackedwidget_3.addWidget(self.page_6)
        self.page_28 = QWidget()
        self.page_28.setObjectName(u"page_28")
        self.gridLayout_63 = QGridLayout(self.page_28)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_63.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.pushButton_75 = QPushButton(self.page_28)
        self.pushButton_75.setObjectName(u"pushButton_75")
        self.pushButton_75.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_75.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_75.setIcon(icon13)
        self.pushButton_75.setIconSize(QSize(46, 42))

        self.gridLayout_63.addWidget(self.pushButton_75, 1, 0, 1, 1)

        self.label_82 = QLabel(self.page_28)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_63.addWidget(self.label_82, 0, 0, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_63.addItem(self.horizontalSpacer_56, 1, 1, 1, 1)

        self.chart_of_accounts_tb = QTableWidget(self.page_28)
        if (self.chart_of_accounts_tb.columnCount() < 6):
            self.chart_of_accounts_tb.setColumnCount(6)
        __qtablewidgetitem230 = QTableWidgetItem()
        self.chart_of_accounts_tb.setHorizontalHeaderItem(0, __qtablewidgetitem230)
        __qtablewidgetitem231 = QTableWidgetItem()
        self.chart_of_accounts_tb.setHorizontalHeaderItem(1, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        __qtablewidgetitem232.setBackground(QColor(255, 255, 255));
        self.chart_of_accounts_tb.setHorizontalHeaderItem(2, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.chart_of_accounts_tb.setHorizontalHeaderItem(3, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        self.chart_of_accounts_tb.setHorizontalHeaderItem(4, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        self.chart_of_accounts_tb.setHorizontalHeaderItem(5, __qtablewidgetitem235)
        self.chart_of_accounts_tb.setObjectName(u"chart_of_accounts_tb")
        self.chart_of_accounts_tb.setMinimumSize(QSize(0, 424))
        self.chart_of_accounts_tb.setMaximumSize(QSize(16777215, 435))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush17 = QBrush(QColor(43, 43, 43, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.chart_of_accounts_tb.setPalette(palette20)
        self.chart_of_accounts_tb.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"alternate-background-color: rgb(43, 43, 43);\n"
"")
        self.chart_of_accounts_tb.setFrameShape(QFrame.Box)
        self.chart_of_accounts_tb.setFrameShadow(QFrame.Plain)
        self.chart_of_accounts_tb.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.chart_of_accounts_tb.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.chart_of_accounts_tb.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.chart_of_accounts_tb.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.chart_of_accounts_tb.setAlternatingRowColors(True)
        self.chart_of_accounts_tb.setShowGrid(True)
        self.chart_of_accounts_tb.setGridStyle(Qt.NoPen)
        self.chart_of_accounts_tb.horizontalHeader().setVisible(True)
        self.chart_of_accounts_tb.horizontalHeader().setCascadingSectionResizes(False)
        self.chart_of_accounts_tb.verticalHeader().setVisible(False)
        self.chart_of_accounts_tb.verticalHeader().setHighlightSections(True)
        self.chart_of_accounts_tb.verticalHeader().setStretchLastSection(False)

        self.gridLayout_63.addWidget(self.chart_of_accounts_tb, 2, 0, 1, 2)

        self.stackedwidget_3.addWidget(self.page_28)
        self.liabilities_page = QWidget()
        self.liabilities_page.setObjectName(u"liabilities_page")
        self.gridLayout_12 = QGridLayout(self.liabilities_page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_56 = QFrame(self.liabilities_page)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(100, 276))
        self.frame_56.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_56)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(12, 9, 5, 0)
        self.lib_addbutton = QPushButton(self.frame_56)
        self.lib_addbutton.setObjectName(u"lib_addbutton")
        self.lib_addbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_addbutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_addbutton.setIcon(icon13)
        self.lib_addbutton.setIconSize(QSize(46, 42))

        self.verticalLayout_30.addWidget(self.lib_addbutton)

        self.lib_deletebutton = QPushButton(self.frame_56)
        self.lib_deletebutton.setObjectName(u"lib_deletebutton")
        self.lib_deletebutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_deletebutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_deletebutton.setIcon(icon19)
        self.lib_deletebutton.setIconSize(QSize(43, 43))

        self.verticalLayout_30.addWidget(self.lib_deletebutton)

        self.pushButton_51 = QPushButton(self.frame_56)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pushButton_51.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_51.setIcon(icon21)
        self.pushButton_51.setIconSize(QSize(53, 40))

        self.verticalLayout_30.addWidget(self.pushButton_51)

        self.pushButton_33 = QPushButton(self.frame_56)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_33.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_33.setIcon(icon2)
        self.pushButton_33.setIconSize(QSize(52, 38))

        self.verticalLayout_30.addWidget(self.pushButton_33)


        self.gridLayout_12.addWidget(self.frame_56, 3, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_8, 4, 1, 1, 1)

        self.label_10 = QLabel(self.liabilities_page)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_12.addWidget(self.label_10, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.liabilities_page)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem239)
        __qtablewidgetitem240 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem241)
        __qtablewidgetitem242 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem242)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(0, 436))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 800))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_2.setPalette(palette21)
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.tableWidget_2.setFrameShape(QFrame.Box)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.tableWidget_2, 3, 0, 1, 2)

        self.stackedwidget_3.addWidget(self.liabilities_page)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_15 = QGridLayout(self.page_7)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_11 = QLabel(self.page_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(167, 16777215))

        self.gridLayout_15.addWidget(self.label_11, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 3, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.page_7)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem243 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem248)
        __qtablewidgetitem249 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem249)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(0, 421))
        self.tableWidget_3.setMaximumSize(QSize(16777215, 382))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget_3.setPalette(palette22)
        self.tableWidget_3.setAutoFillBackground(False)
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.tableWidget_3.setFrameShape(QFrame.Box)
        self.tableWidget_3.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.gridLayout_15.addWidget(self.tableWidget_3, 1, 0, 1, 1)

        self.frame_55 = QFrame(self.page_7)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(100, 276))
        self.frame_55.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_55)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(12, 9, 5, 0)
        self.lib_btn2 = QPushButton(self.frame_55)
        self.lib_btn2.setObjectName(u"lib_btn2")
        self.lib_btn2.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn2.setIcon(icon13)
        self.lib_btn2.setIconSize(QSize(46, 42))

        self.verticalLayout_25.addWidget(self.lib_btn2)

        self.lib_btn3 = QPushButton(self.frame_55)
        self.lib_btn3.setObjectName(u"lib_btn3")
        self.lib_btn3.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn3.setIcon(icon19)
        self.lib_btn3.setIconSize(QSize(43, 43))

        self.verticalLayout_25.addWidget(self.lib_btn3)

        self.pushButton_50 = QPushButton(self.frame_55)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_50.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_50.setIcon(icon21)
        self.pushButton_50.setIconSize(QSize(53, 40))

        self.verticalLayout_25.addWidget(self.pushButton_50)

        self.lib_btn4 = QPushButton(self.frame_55)
        self.lib_btn4.setObjectName(u"lib_btn4")
        self.lib_btn4.setCursor(QCursor(Qt.PointingHandCursor))
        self.lib_btn4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.lib_btn4.setIcon(icon2)
        self.lib_btn4.setIconSize(QSize(52, 38))

        self.verticalLayout_25.addWidget(self.lib_btn4)


        self.gridLayout_15.addWidget(self.frame_55, 1, 1, 1, 1)

        self.stackedwidget_3.addWidget(self.page_7)
        self.debts_page_2 = QWidget()
        self.debts_page_2.setObjectName(u"debts_page_2")
        self.gridLayout_13 = QGridLayout(self.debts_page_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.checkBox_5 = QCheckBox(self.debts_page_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_13.addWidget(self.checkBox_5, 5, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 149, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_10, 9, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.debts_page_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_13.addWidget(self.checkBox_2, 6, 1, 1, 1)

        self.comboBox_50 = QComboBox(self.debts_page_2)
        self.comboBox_50.setObjectName(u"comboBox_50")
        self.comboBox_50.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_13.addWidget(self.comboBox_50, 4, 1, 1, 1)

        self.label_376 = QLabel(self.debts_page_2)
        self.label_376.setObjectName(u"label_376")

        self.gridLayout_13.addWidget(self.label_376, 3, 0, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_51, 4, 2, 1, 1)

        self.label_377 = QLabel(self.debts_page_2)
        self.label_377.setObjectName(u"label_377")

        self.gridLayout_13.addWidget(self.label_377, 5, 0, 1, 1)

        self.label_49 = QLabel(self.debts_page_2)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_13.addWidget(self.label_49, 4, 0, 1, 1)

        self.frame_25 = QFrame(self.debts_page_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_52)

        self.pushButton_49 = QPushButton(self.frame_25)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setStyleSheet(u"background-color: rgb(0, 197, 0);")
        self.pushButton_49.setIcon(icon16)
        self.pushButton_49.setIconSize(QSize(16, 35))

        self.horizontalLayout_45.addWidget(self.pushButton_49)

        self.pushButton_165 = QPushButton(self.frame_25)
        self.pushButton_165.setObjectName(u"pushButton_165")
        self.pushButton_165.setMinimumSize(QSize(48, 35))

        self.horizontalLayout_45.addWidget(self.pushButton_165)


        self.gridLayout_13.addWidget(self.frame_25, 7, 1, 1, 1)

        self.label_30 = QLabel(self.debts_page_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_13.addWidget(self.label_30, 2, 0, 1, 1)

        self.lineEdit_93 = QLineEdit(self.debts_page_2)
        self.lineEdit_93.setObjectName(u"lineEdit_93")

        self.gridLayout_13.addWidget(self.lineEdit_93, 2, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_28, 0, 1, 1, 1)

        self.comboBox_48 = QComboBox(self.debts_page_2)
        self.comboBox_48.setObjectName(u"comboBox_48")

        self.gridLayout_13.addWidget(self.comboBox_48, 1, 1, 1, 1)

        self.lineEdit_92 = QLineEdit(self.debts_page_2)
        self.lineEdit_92.setObjectName(u"lineEdit_92")

        self.gridLayout_13.addWidget(self.lineEdit_92, 3, 1, 1, 1)

        self.label_378 = QLabel(self.debts_page_2)
        self.label_378.setObjectName(u"label_378")

        self.gridLayout_13.addWidget(self.label_378, 6, 0, 1, 1)

        self.label_47 = QLabel(self.debts_page_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_13.addWidget(self.label_47, 1, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_29, 8, 2, 1, 1)

        self.stackedwidget_3.addWidget(self.debts_page_2)

        self.gridLayout_10.addWidget(self.stackedwidget_3, 1, 2, 1, 1)

        self.frame_8 = QFrame(self.page_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 106))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_69 = QFrame(self.frame_8)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.gridLayout_56 = QGridLayout(self.frame_69)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 48))
        self.frame_70.setMaximumSize(QSize(16777215, 59))
        self.frame_70.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_70)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_198 = QLabel(self.frame_70)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setFont(font)

        self.verticalLayout_45.addWidget(self.label_198)


        self.gridLayout_56.addWidget(self.frame_70, 1, 0, 1, 1)

        self.label_199 = QLabel(self.frame_69)
        self.label_199.setObjectName(u"label_199")

        self.gridLayout_56.addWidget(self.label_199, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_69)

        self.frame_67 = QFrame(self.frame_8)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.gridLayout_55 = QGridLayout(self.frame_67)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 48))
        self.frame_68.setMaximumSize(QSize(16777215, 59))
        self.frame_68.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_68)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_196 = QLabel(self.frame_68)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setFont(font)

        self.verticalLayout_44.addWidget(self.label_196)


        self.gridLayout_55.addWidget(self.frame_68, 1, 0, 1, 1)

        self.label_197 = QLabel(self.frame_67)
        self.label_197.setObjectName(u"label_197")

        self.gridLayout_55.addWidget(self.label_197, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_67)

        self.frame_65 = QFrame(self.frame_8)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.gridLayout_54 = QGridLayout(self.frame_65)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 48))
        self.frame_66.setMaximumSize(QSize(16777215, 200))
        self.frame_66.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_66)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_194 = QLabel(self.frame_66)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setFont(font)

        self.verticalLayout_43.addWidget(self.label_194)


        self.gridLayout_54.addWidget(self.frame_66, 1, 0, 1, 1)

        self.label_195 = QLabel(self.frame_65)
        self.label_195.setObjectName(u"label_195")

        self.gridLayout_54.addWidget(self.label_195, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_65)

        self.frame_62 = QFrame(self.frame_8)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(16777215, 100))
        self.frame_62.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	background-color: rgb(29, 29, 29);\n"
"}")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_62)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.frame_64 = QFrame(self.frame_62)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 48))
        self.frame_64.setMaximumSize(QSize(16777215, 200))
        self.frame_64.setStyleSheet(u"QFrame{\n"
"border-radius : 15px;\n"
"	\n"
"	\n"
"	background-color: rgb(67, 67, 67);\n"
"}")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_64)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_192 = QLabel(self.frame_64)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font)

        self.verticalLayout_42.addWidget(self.label_192)


        self.gridLayout_53.addWidget(self.frame_64, 1, 0, 1, 1)

        self.label_193 = QLabel(self.frame_62)
        self.label_193.setObjectName(u"label_193")

        self.gridLayout_53.addWidget(self.label_193, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_62)


        self.gridLayout_10.addWidget(self.frame_8, 0, 2, 1, 1)

        self.frame_28 = QFrame(self.page_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(145, 0))
        self.frame_28.setMaximumSize(QSize(154, 548))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(6, 44, 2, 76)
        self.pushButton_74 = QPushButton(self.frame_28)
        self.pushButton_74.setObjectName(u"pushButton_74")
        self.pushButton_74.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_22.addWidget(self.pushButton_74)

        self.ledgers_btn = QPushButton(self.frame_28)
        self.ledgers_btn.setObjectName(u"ledgers_btn")
        self.ledgers_btn.setMinimumSize(QSize(132, 4))
        self.ledgers_btn.setMaximumSize(QSize(16777215, 16777215))
        self.ledgers_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ledgers_btn.setMouseTracking(True)
        self.ledgers_btn.setStyleSheet(u"")
        self.ledgers_btn.setIconSize(QSize(33, 160))

        self.verticalLayout_22.addWidget(self.ledgers_btn)

        self.pushButton_36 = QPushButton(self.frame_28)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.verticalLayout_22.addWidget(self.pushButton_36)

        self.pushButton_101 = QPushButton(self.frame_28)
        self.pushButton_101.setObjectName(u"pushButton_101")

        self.verticalLayout_22.addWidget(self.pushButton_101)

        self.pushButton_124 = QPushButton(self.frame_28)
        self.pushButton_124.setObjectName(u"pushButton_124")

        self.verticalLayout_22.addWidget(self.pushButton_124)


        self.gridLayout_10.addWidget(self.frame_28, 1, 1, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_44 = QWidget()
        self.page_44.setObjectName(u"page_44")
        self.gridLayout_98 = QGridLayout(self.page_44)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.frame_94 = QFrame(self.page_44)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.gridLayout_99 = QGridLayout(self.frame_94)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(145, 0))
        self.frame_95.setMaximumSize(QSize(154, 548))
        self.frame_95.setStyleSheet(u"QFrame{\n"
"background-color: rgb(33, 37, 43);\n"
"}")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_95)
        self.verticalLayout_41.setSpacing(6)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(6, 44, 2, 76)
        self.pushButton_125 = QPushButton(self.frame_95)
        self.pushButton_125.setObjectName(u"pushButton_125")
        self.pushButton_125.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_41.addWidget(self.pushButton_125)

        self.ledgers_btn_2 = QPushButton(self.frame_95)
        self.ledgers_btn_2.setObjectName(u"ledgers_btn_2")
        self.ledgers_btn_2.setMinimumSize(QSize(132, 4))
        self.ledgers_btn_2.setMaximumSize(QSize(16777215, 16777215))
        self.ledgers_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.ledgers_btn_2.setMouseTracking(True)
        self.ledgers_btn_2.setStyleSheet(u"")
        self.ledgers_btn_2.setIconSize(QSize(33, 160))

        self.verticalLayout_41.addWidget(self.ledgers_btn_2)

        self.pushButton_126 = QPushButton(self.frame_95)
        self.pushButton_126.setObjectName(u"pushButton_126")

        self.verticalLayout_41.addWidget(self.pushButton_126)


        self.gridLayout_99.addWidget(self.frame_95, 0, 0, 1, 1)

        self.stackedWidget_4 = QStackedWidget(self.frame_94)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_45 = QWidget()
        self.page_45.setObjectName(u"page_45")
        self.gridLayout_100 = QGridLayout(self.page_45)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.tableWidget_38 = QTableWidget(self.page_45)
        if (self.tableWidget_38.columnCount() < 5):
            self.tableWidget_38.setColumnCount(5)
        __qtablewidgetitem250 = QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(0, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(1, __qtablewidgetitem251)
        __qtablewidgetitem252 = QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(2, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(3, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.tableWidget_38.setHorizontalHeaderItem(4, __qtablewidgetitem254)
        self.tableWidget_38.setObjectName(u"tableWidget_38")
        self.tableWidget_38.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_100.addWidget(self.tableWidget_38, 1, 0, 1, 1)

        self.frame_99 = QFrame(self.page_45)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 45))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_132 = QPushButton(self.frame_99)
        self.pushButton_132.setObjectName(u"pushButton_132")
        self.pushButton_132.setMinimumSize(QSize(51, 45))
        self.pushButton_132.setIcon(icon13)

        self.horizontalLayout_31.addWidget(self.pushButton_132)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_38)

        self.frame_113 = QFrame(self.frame_99)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.comboBox_44 = QComboBox(self.frame_113)
        self.comboBox_44.setObjectName(u"comboBox_44")
        self.comboBox_44.setMinimumSize(QSize(143, 0))
        self.comboBox_44.setMaximumSize(QSize(119, 28))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_44.setPalette(palette23)
        self.comboBox_44.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_41.addWidget(self.comboBox_44)

        self.lineEdit_85 = QLineEdit(self.frame_113)
        self.lineEdit_85.setObjectName(u"lineEdit_85")
        self.lineEdit_85.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_85.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_41.addWidget(self.lineEdit_85)

        self.pushButton_156 = QPushButton(self.frame_113)
        self.pushButton_156.setObjectName(u"pushButton_156")
        self.pushButton_156.setMaximumSize(QSize(16777215, 20))
        self.pushButton_156.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_156.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_156.setIcon(icon14)
        self.pushButton_156.setIconSize(QSize(28, 30))

        self.horizontalLayout_41.addWidget(self.pushButton_156)


        self.horizontalLayout_31.addWidget(self.frame_113)


        self.gridLayout_100.addWidget(self.frame_99, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_45)
        self.page_46 = QWidget()
        self.page_46.setObjectName(u"page_46")
        self.gridLayout_101 = QGridLayout(self.page_46)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.tableWidget_39 = QTableWidget(self.page_46)
        if (self.tableWidget_39.columnCount() < 6):
            self.tableWidget_39.setColumnCount(6)
        __qtablewidgetitem255 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(0, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(1, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(2, __qtablewidgetitem257)
        __qtablewidgetitem258 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(3, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(4, __qtablewidgetitem259)
        __qtablewidgetitem260 = QTableWidgetItem()
        self.tableWidget_39.setHorizontalHeaderItem(5, __qtablewidgetitem260)
        self.tableWidget_39.setObjectName(u"tableWidget_39")

        self.gridLayout_101.addWidget(self.tableWidget_39, 1, 0, 1, 1)

        self.frame_96 = QFrame(self.page_46)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 45))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.gridLayout_102 = QGridLayout(self.frame_96)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.pushButton_128 = QPushButton(self.frame_96)
        self.pushButton_128.setObjectName(u"pushButton_128")
        self.pushButton_128.setMinimumSize(QSize(45, 45))
        self.pushButton_128.setIcon(icon13)

        self.gridLayout_102.addWidget(self.pushButton_128, 0, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_102.addItem(self.horizontalSpacer_34, 0, 1, 1, 1)


        self.gridLayout_101.addWidget(self.frame_96, 0, 0, 1, 1)

        self.frame_114 = QFrame(self.page_46)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.comboBox_45 = QComboBox(self.frame_114)
        self.comboBox_45.setObjectName(u"comboBox_45")
        self.comboBox_45.setMinimumSize(QSize(143, 0))
        self.comboBox_45.setMaximumSize(QSize(119, 28))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_45.setPalette(palette24)
        self.comboBox_45.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_42.addWidget(self.comboBox_45)

        self.lineEdit_86 = QLineEdit(self.frame_114)
        self.lineEdit_86.setObjectName(u"lineEdit_86")
        self.lineEdit_86.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_86.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_42.addWidget(self.lineEdit_86)

        self.pushButton_157 = QPushButton(self.frame_114)
        self.pushButton_157.setObjectName(u"pushButton_157")
        self.pushButton_157.setMaximumSize(QSize(16777215, 20))
        self.pushButton_157.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_157.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_157.setIcon(icon14)
        self.pushButton_157.setIconSize(QSize(28, 30))

        self.horizontalLayout_42.addWidget(self.pushButton_157)


        self.gridLayout_101.addWidget(self.frame_114, 0, 1, 1, 1)

        self.stackedWidget_4.addWidget(self.page_46)
        self.page_47 = QWidget()
        self.page_47.setObjectName(u"page_47")
        self.gridLayout_103 = QGridLayout(self.page_47)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.pushButton_133 = QPushButton(self.page_47)
        self.pushButton_133.setObjectName(u"pushButton_133")
        self.pushButton_133.setMinimumSize(QSize(50, 45))
        self.pushButton_133.setIcon(icon13)

        self.gridLayout_103.addWidget(self.pushButton_133, 0, 0, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_103.addItem(self.horizontalSpacer_39, 0, 1, 1, 1)

        self.frame_112 = QFrame(self.page_47)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.comboBox_43 = QComboBox(self.frame_112)
        self.comboBox_43.setObjectName(u"comboBox_43")
        self.comboBox_43.setMinimumSize(QSize(143, 0))
        self.comboBox_43.setMaximumSize(QSize(119, 28))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.comboBox_43.setPalette(palette25)
        self.comboBox_43.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(48, 48, 48);\n"
"	color: rgb(229, 229, 229);\n"
"}")

        self.horizontalLayout_40.addWidget(self.comboBox_43)

        self.lineEdit_84 = QLineEdit(self.frame_112)
        self.lineEdit_84.setObjectName(u"lineEdit_84")
        self.lineEdit_84.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_84.setStyleSheet(u"background-color: rgb(48, 48, 48);")

        self.horizontalLayout_40.addWidget(self.lineEdit_84)

        self.pushButton_155 = QPushButton(self.frame_112)
        self.pushButton_155.setObjectName(u"pushButton_155")
        self.pushButton_155.setMaximumSize(QSize(16777215, 20))
        self.pushButton_155.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_155.setStyleSheet(u"QPushButton{\n"
"border-radius : 15px;\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.pushButton_155.setIcon(icon14)
        self.pushButton_155.setIconSize(QSize(28, 30))

        self.horizontalLayout_40.addWidget(self.pushButton_155)


        self.gridLayout_103.addWidget(self.frame_112, 0, 2, 1, 1)

        self.tableWidget_40 = QTableWidget(self.page_47)
        if (self.tableWidget_40.columnCount() < 7):
            self.tableWidget_40.setColumnCount(7)
        __qtablewidgetitem261 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(0, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(1, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(2, __qtablewidgetitem263)
        __qtablewidgetitem264 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(3, __qtablewidgetitem264)
        __qtablewidgetitem265 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(4, __qtablewidgetitem265)
        __qtablewidgetitem266 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(5, __qtablewidgetitem266)
        __qtablewidgetitem267 = QTableWidgetItem()
        self.tableWidget_40.setHorizontalHeaderItem(6, __qtablewidgetitem267)
        self.tableWidget_40.setObjectName(u"tableWidget_40")

        self.gridLayout_103.addWidget(self.tableWidget_40, 1, 0, 1, 3)

        self.stackedWidget_4.addWidget(self.page_47)
        self.page_48 = QWidget()
        self.page_48.setObjectName(u"page_48")
        self.gridLayout_104 = QGridLayout(self.page_48)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.lineEdit_70 = QLineEdit(self.page_48)
        self.lineEdit_70.setObjectName(u"lineEdit_70")
        self.lineEdit_70.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.lineEdit_70, 6, 1, 1, 1)

        self.label_312 = QLabel(self.page_48)
        self.label_312.setObjectName(u"label_312")

        self.gridLayout_104.addWidget(self.label_312, 8, 0, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_104.addItem(self.horizontalSpacer_41, 5, 2, 1, 1)

        self.label_315 = QLabel(self.page_48)
        self.label_315.setObjectName(u"label_315")

        self.gridLayout_104.addWidget(self.label_315, 10, 0, 1, 1)

        self.comboBox_27 = QComboBox(self.page_48)
        self.comboBox_27.setObjectName(u"comboBox_27")
        self.comboBox_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.comboBox_27, 8, 1, 1, 1)

        self.frame_100 = QFrame(self.page_48)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 10))
        self.frame_100.setMaximumSize(QSize(16777215, 46))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_40)

        self.pushButton_134 = QPushButton(self.frame_100)
        self.pushButton_134.setObjectName(u"pushButton_134")
        self.pushButton_134.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.pushButton_134)

        self.pushButton_135 = QPushButton(self.frame_100)
        self.pushButton_135.setObjectName(u"pushButton_135")
        self.pushButton_135.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.pushButton_135)

        self.pushButton_141 = QPushButton(self.frame_100)
        self.pushButton_141.setObjectName(u"pushButton_141")
        self.pushButton_141.setStyleSheet(u"background-color: rgb(221, 0, 4);")
        self.pushButton_141.setIcon(icon18)

        self.horizontalLayout_32.addWidget(self.pushButton_141)


        self.gridLayout_104.addWidget(self.frame_100, 12, 1, 1, 1)

        self.lineEdit_66 = QLineEdit(self.page_48)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.lineEdit_66, 2, 1, 1, 1)

        self.lineEdit_69 = QLineEdit(self.page_48)
        self.lineEdit_69.setObjectName(u"lineEdit_69")
        self.lineEdit_69.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.lineEdit_69, 5, 1, 1, 1)

        self.label_314 = QLabel(self.page_48)
        self.label_314.setObjectName(u"label_314")

        self.gridLayout_104.addWidget(self.label_314, 3, 0, 1, 1)

        self.comboBox_28 = QComboBox(self.page_48)
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.comboBox_28, 7, 1, 1, 1)

        self.lineEdit_67 = QLineEdit(self.page_48)
        self.lineEdit_67.setObjectName(u"lineEdit_67")
        self.lineEdit_67.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.lineEdit_67, 3, 1, 1, 1)

        self.comboBox_29 = QComboBox(self.page_48)
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.comboBox_29, 10, 1, 1, 1)

        self.label_308 = QLabel(self.page_48)
        self.label_308.setObjectName(u"label_308")

        self.gridLayout_104.addWidget(self.label_308, 6, 0, 1, 1)

        self.label_318 = QLabel(self.page_48)
        self.label_318.setObjectName(u"label_318")

        self.gridLayout_104.addWidget(self.label_318, 1, 0, 1, 1)

        self.dateEdit_21 = QDateEdit(self.page_48)
        self.dateEdit_21.setObjectName(u"dateEdit_21")
        self.dateEdit_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dateEdit_21.setCalendarPopup(True)

        self.gridLayout_104.addWidget(self.dateEdit_21, 11, 1, 1, 1)

        self.label_317 = QLabel(self.page_48)
        self.label_317.setObjectName(u"label_317")

        self.gridLayout_104.addWidget(self.label_317, 11, 0, 1, 1)

        self.label_310 = QLabel(self.page_48)
        self.label_310.setObjectName(u"label_310")

        self.gridLayout_104.addWidget(self.label_310, 4, 0, 1, 1)

        self.lineEdit_68 = QLineEdit(self.page_48)
        self.lineEdit_68.setObjectName(u"lineEdit_68")

        self.gridLayout_104.addWidget(self.lineEdit_68, 1, 1, 1, 1)

        self.label_316 = QLabel(self.page_48)
        self.label_316.setObjectName(u"label_316")

        self.gridLayout_104.addWidget(self.label_316, 9, 0, 1, 1)

        self.label_309 = QLabel(self.page_48)
        self.label_309.setObjectName(u"label_309")

        self.gridLayout_104.addWidget(self.label_309, 5, 0, 1, 1)

        self.comboBox_26 = QComboBox(self.page_48)
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.comboBox_26, 9, 1, 1, 1)

        self.label_313 = QLabel(self.page_48)
        self.label_313.setObjectName(u"label_313")

        self.gridLayout_104.addWidget(self.label_313, 2, 0, 1, 1)

        self.label_311 = QLabel(self.page_48)
        self.label_311.setObjectName(u"label_311")

        self.gridLayout_104.addWidget(self.label_311, 7, 0, 1, 1)

        self.lineEdit_65 = QLineEdit(self.page_48)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        self.lineEdit_65.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_104.addWidget(self.lineEdit_65, 4, 1, 1, 1)

        self.label_352 = QLabel(self.page_48)
        self.label_352.setObjectName(u"label_352")
        self.label_352.setMinimumSize(QSize(0, 20))
        self.label_352.setMaximumSize(QSize(16777215, 43))

        self.gridLayout_104.addWidget(self.label_352, 0, 1, 1, 1)

        self.stackedWidget_4.addWidget(self.page_48)
        self.page_50 = QWidget()
        self.page_50.setObjectName(u"page_50")
        self.gridLayout_106 = QGridLayout(self.page_50)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.comboBox_32 = QComboBox(self.page_50)
        self.comboBox_32.setObjectName(u"comboBox_32")
        self.comboBox_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.comboBox_32, 4, 1, 1, 1)

        self.label_344 = QLabel(self.page_50)
        self.label_344.setObjectName(u"label_344")

        self.gridLayout_106.addWidget(self.label_344, 3, 0, 1, 1)

        self.comboBox_30 = QComboBox(self.page_50)
        self.comboBox_30.setObjectName(u"comboBox_30")
        self.comboBox_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.comboBox_30, 5, 1, 1, 1)

        self.label_343 = QLabel(self.page_50)
        self.label_343.setObjectName(u"label_343")

        self.gridLayout_106.addWidget(self.label_343, 1, 0, 1, 1)

        self.label_341 = QLabel(self.page_50)
        self.label_341.setObjectName(u"label_341")

        self.gridLayout_106.addWidget(self.label_341, 6, 0, 1, 1)

        self.label_342 = QLabel(self.page_50)
        self.label_342.setObjectName(u"label_342")

        self.gridLayout_106.addWidget(self.label_342, 7, 0, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_106.addItem(self.horizontalSpacer_43, 4, 2, 1, 1)

        self.lineEdit_71 = QLineEdit(self.page_50)
        self.lineEdit_71.setObjectName(u"lineEdit_71")
        self.lineEdit_71.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.lineEdit_71, 2, 1, 1, 1)

        self.frame_101 = QFrame(self.page_50)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_42)

        self.pushButton_136 = QPushButton(self.frame_101)
        self.pushButton_136.setObjectName(u"pushButton_136")
        self.pushButton_136.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.pushButton_136)

        self.pushButton_137 = QPushButton(self.frame_101)
        self.pushButton_137.setObjectName(u"pushButton_137")
        self.pushButton_137.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.pushButton_137)

        self.pushButton_142 = QPushButton(self.frame_101)
        self.pushButton_142.setObjectName(u"pushButton_142")
        self.pushButton_142.setStyleSheet(u"background-color: rgb(221, 0, 4);")
        self.pushButton_142.setIcon(icon18)

        self.horizontalLayout_33.addWidget(self.pushButton_142)


        self.gridLayout_106.addWidget(self.frame_101, 8, 1, 1, 1)

        self.label_320 = QLabel(self.page_50)
        self.label_320.setObjectName(u"label_320")

        self.gridLayout_106.addWidget(self.label_320, 5, 0, 1, 1)

        self.lineEdit_73 = QLineEdit(self.page_50)
        self.lineEdit_73.setObjectName(u"lineEdit_73")
        self.lineEdit_73.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.lineEdit_73, 3, 1, 1, 1)

        self.label_340 = QLabel(self.page_50)
        self.label_340.setObjectName(u"label_340")

        self.gridLayout_106.addWidget(self.label_340, 4, 0, 1, 1)

        self.comboBox_31 = QComboBox(self.page_50)
        self.comboBox_31.setObjectName(u"comboBox_31")
        self.comboBox_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.comboBox_31, 7, 1, 1, 1)

        self.lineEdit_72 = QLineEdit(self.page_50)
        self.lineEdit_72.setObjectName(u"lineEdit_72")
        self.lineEdit_72.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.lineEdit_72, 1, 1, 1, 1)

        self.label_337 = QLabel(self.page_50)
        self.label_337.setObjectName(u"label_337")

        self.gridLayout_106.addWidget(self.label_337, 2, 0, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.page_50)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_106.addWidget(self.plainTextEdit_6, 6, 1, 1, 1)

        self.label_353 = QLabel(self.page_50)
        self.label_353.setObjectName(u"label_353")

        self.gridLayout_106.addWidget(self.label_353, 0, 1, 1, 1)

        self.stackedWidget_4.addWidget(self.page_50)
        self.page_49 = QWidget()
        self.page_49.setObjectName(u"page_49")
        self.gridLayout_105 = QGridLayout(self.page_49)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.label_354 = QLabel(self.page_49)
        self.label_354.setObjectName(u"label_354")
        self.label_354.setMaximumSize(QSize(16777215, 51))

        self.gridLayout_105.addWidget(self.label_354, 0, 0, 1, 2)

        self.frame_104 = QFrame(self.page_49)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.WinPanel)
        self.frame_104.setFrameShadow(QFrame.Plain)
        self.gridLayout_110 = QGridLayout(self.frame_104)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.frame_103 = QFrame(self.frame_104)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.gridLayout_109 = QGridLayout(self.frame_103)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.label_357 = QLabel(self.frame_103)
        self.label_357.setObjectName(u"label_357")
        self.label_357.setMinimumSize(QSize(0, 50))
        self.label_357.setMaximumSize(QSize(153, 153))
        self.label_357.setPixmap(QPixmap(u":/images/images/images/user.png"))
        self.label_357.setScaledContents(True)

        self.gridLayout_109.addWidget(self.label_357, 0, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_109.addItem(self.verticalSpacer_20, 1, 0, 1, 1)


        self.gridLayout_110.addWidget(self.frame_103, 0, 0, 5, 1)

        self.label_319 = QLabel(self.frame_104)
        self.label_319.setObjectName(u"label_319")

        self.gridLayout_110.addWidget(self.label_319, 0, 1, 1, 1)

        self.label_328 = QLabel(self.frame_104)
        self.label_328.setObjectName(u"label_328")

        self.gridLayout_110.addWidget(self.label_328, 0, 2, 1, 1)

        self.label_324 = QLabel(self.frame_104)
        self.label_324.setObjectName(u"label_324")

        self.gridLayout_110.addWidget(self.label_324, 0, 3, 1, 1)

        self.label_335 = QLabel(self.frame_104)
        self.label_335.setObjectName(u"label_335")

        self.gridLayout_110.addWidget(self.label_335, 0, 4, 1, 1)

        self.label_325 = QLabel(self.frame_104)
        self.label_325.setObjectName(u"label_325")

        self.gridLayout_110.addWidget(self.label_325, 1, 1, 1, 1)

        self.label_331 = QLabel(self.frame_104)
        self.label_331.setObjectName(u"label_331")

        self.gridLayout_110.addWidget(self.label_331, 1, 2, 1, 1)

        self.label_329 = QLabel(self.frame_104)
        self.label_329.setObjectName(u"label_329")

        self.gridLayout_110.addWidget(self.label_329, 1, 3, 1, 1)

        self.label_336 = QLabel(self.frame_104)
        self.label_336.setObjectName(u"label_336")

        self.gridLayout_110.addWidget(self.label_336, 1, 4, 1, 1)

        self.label_323 = QLabel(self.frame_104)
        self.label_323.setObjectName(u"label_323")

        self.gridLayout_110.addWidget(self.label_323, 2, 1, 1, 1)

        self.label_332 = QLabel(self.frame_104)
        self.label_332.setObjectName(u"label_332")

        self.gridLayout_110.addWidget(self.label_332, 2, 2, 1, 1)

        self.label_322 = QLabel(self.frame_104)
        self.label_322.setObjectName(u"label_322")

        self.gridLayout_110.addWidget(self.label_322, 2, 3, 1, 1)

        self.label_338 = QLabel(self.frame_104)
        self.label_338.setObjectName(u"label_338")

        self.gridLayout_110.addWidget(self.label_338, 2, 4, 1, 1)

        self.label_327 = QLabel(self.frame_104)
        self.label_327.setObjectName(u"label_327")

        self.gridLayout_110.addWidget(self.label_327, 3, 1, 1, 1)

        self.label_333 = QLabel(self.frame_104)
        self.label_333.setObjectName(u"label_333")

        self.gridLayout_110.addWidget(self.label_333, 3, 2, 1, 1)

        self.label_326 = QLabel(self.frame_104)
        self.label_326.setObjectName(u"label_326")

        self.gridLayout_110.addWidget(self.label_326, 3, 3, 1, 1)

        self.label_339 = QLabel(self.frame_104)
        self.label_339.setObjectName(u"label_339")

        self.gridLayout_110.addWidget(self.label_339, 3, 4, 1, 1)

        self.label_321 = QLabel(self.frame_104)
        self.label_321.setObjectName(u"label_321")

        self.gridLayout_110.addWidget(self.label_321, 4, 1, 1, 1)

        self.label_334 = QLabel(self.frame_104)
        self.label_334.setObjectName(u"label_334")

        self.gridLayout_110.addWidget(self.label_334, 4, 2, 1, 1)


        self.gridLayout_105.addWidget(self.frame_104, 2, 0, 1, 2)

        self.label_355 = QLabel(self.page_49)
        self.label_355.setObjectName(u"label_355")
        self.label_355.setMinimumSize(QSize(0, 20))
        self.label_355.setMaximumSize(QSize(16777215, 60))

        self.gridLayout_105.addWidget(self.label_355, 1, 0, 1, 2)

        self.stackedWidget_4.addWidget(self.page_49)
        self.page_51 = QWidget()
        self.page_51.setObjectName(u"page_51")
        self.gridLayout_107 = QGridLayout(self.page_51)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.lineEdit_74 = QLineEdit(self.page_51)
        self.lineEdit_74.setObjectName(u"lineEdit_74")
        self.lineEdit_74.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.lineEdit_74, 3, 1, 1, 1)

        self.lineEdit_76 = QLineEdit(self.page_51)
        self.lineEdit_76.setObjectName(u"lineEdit_76")
        self.lineEdit_76.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.lineEdit_76, 2, 1, 1, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.page_51)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.plainTextEdit_7, 5, 1, 1, 1)

        self.label_347 = QLabel(self.page_51)
        self.label_347.setObjectName(u"label_347")

        self.gridLayout_107.addWidget(self.label_347, 1, 0, 1, 1)

        self.label_350 = QLabel(self.page_51)
        self.label_350.setObjectName(u"label_350")

        self.gridLayout_107.addWidget(self.label_350, 5, 0, 1, 1)

        self.label_348 = QLabel(self.page_51)
        self.label_348.setObjectName(u"label_348")

        self.gridLayout_107.addWidget(self.label_348, 4, 0, 1, 1)

        self.comboBox_34 = QComboBox(self.page_51)
        self.comboBox_34.setObjectName(u"comboBox_34")
        self.comboBox_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.comboBox_34, 6, 1, 1, 1)

        self.label_345 = QLabel(self.page_51)
        self.label_345.setObjectName(u"label_345")

        self.gridLayout_107.addWidget(self.label_345, 2, 0, 1, 1)

        self.label_346 = QLabel(self.page_51)
        self.label_346.setObjectName(u"label_346")

        self.gridLayout_107.addWidget(self.label_346, 6, 0, 1, 1)

        self.lineEdit_75 = QLineEdit(self.page_51)
        self.lineEdit_75.setObjectName(u"lineEdit_75")
        self.lineEdit_75.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.lineEdit_75, 1, 1, 1, 1)

        self.label_351 = QLabel(self.page_51)
        self.label_351.setObjectName(u"label_351")

        self.gridLayout_107.addWidget(self.label_351, 0, 1, 1, 1)

        self.frame_102 = QFrame(self.page_51)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_44)

        self.pushButton_138 = QPushButton(self.frame_102)
        self.pushButton_138.setObjectName(u"pushButton_138")
        self.pushButton_138.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.pushButton_138)

        self.pushButton_139 = QPushButton(self.frame_102)
        self.pushButton_139.setObjectName(u"pushButton_139")
        self.pushButton_139.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.pushButton_139)

        self.pushButton_140 = QPushButton(self.frame_102)
        self.pushButton_140.setObjectName(u"pushButton_140")
        self.pushButton_140.setStyleSheet(u"background-color: rgb(234, 0, 4);")
        self.pushButton_140.setIcon(icon18)

        self.horizontalLayout_34.addWidget(self.pushButton_140)


        self.gridLayout_107.addWidget(self.frame_102, 7, 1, 1, 1)

        self.comboBox_33 = QComboBox(self.page_51)
        self.comboBox_33.setObjectName(u"comboBox_33")
        self.comboBox_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_107.addWidget(self.comboBox_33, 4, 1, 1, 1)

        self.label_349 = QLabel(self.page_51)
        self.label_349.setObjectName(u"label_349")

        self.gridLayout_107.addWidget(self.label_349, 3, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_107.addItem(self.horizontalSpacer_45, 5, 2, 1, 1)

        self.stackedWidget_4.addWidget(self.page_51)

        self.gridLayout_99.addWidget(self.stackedWidget_4, 0, 2, 1, 1)


        self.gridLayout_98.addWidget(self.frame_94, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_44)

        self.gridLayout_39.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(4)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedwidget_3.setCurrentIndex(4)
        self.stackedWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yobi", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Yobi", None))
        self.titleLeftDescription.setText("")
        self.label_15.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Sale", None))
        self.btn_widgets_2.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.client_btn_2.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Business profile settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Stats</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#b8b8b8;\">stats a point of sale system and finance tool </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#b8b8b8;\">"
                        "get the most of your products with ready to use tools</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">POS</span></p></body></html>", None))
        self.label_28.setText("")
        self.titleRightInfo.setText("")
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"refresh", None))
        self.pushButton_129.setText(QCoreApplication.translate("MainWindow", u"Navigator", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#dfdfdf;\">Total Liabilities</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#e6e6e6;\">Total Assets</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#cbcbcb;\">0%</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#cbcbcb;\">0%</span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#cbcbcb;\">Capital employed</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600; color:#e6e6e6;\">working capital</span></p></body></html>", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#cbcbcb;\">0%</span></p></body></html>", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700; color:#cbcbcb;\">0%</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Reoder limit</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem2 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        self.label_35.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">profit</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#b8b89f;\">NET</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Most sold</p></body></html>", None))
        ___qtablewidgetitem3 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem4 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Item name", None));
        ___qtablewidgetitem5 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">profit</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#b8b89f;\">GROSS</span></p></body></html>", None))
        self.label_23.setText("")
        self.pushButton_127.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.pushButton_171.setText(QCoreApplication.translate("MainWindow", u"Bills", None))
        self.pushButton_145.setText(QCoreApplication.translate("MainWindow", u"purchase orders", None))
        self.pushButton_105.setText(QCoreApplication.translate("MainWindow", u"Vendors", None))
        self.pushButton_172.setText(QCoreApplication.translate("MainWindow", u"Ledgers", None))
        self.pushButton_144.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.label_384.setText(QCoreApplication.translate("MainWindow", u"Quick Links", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Debt percentage", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"current ratio", None))
        self.label_18.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gross profit Margin", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Net profit margin</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#b8b89f;\">Recent orders</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Debt ratio", None))
        self.label_12.setText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#d3d3d3;\">Due</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#cbcbcb;\">0 ksh</span></p></body></html>", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#d3d3d3;\">Total revenue</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#cbcbcb;\">0 ksh</span></p></body></html>", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">0</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL PAID</span></p></body></html>", None))
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"Vendors", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"new order", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.comboBox_2.setCurrentText("")
        self.pushButton_21.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">0</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL ORDERS</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL SALES REVENUE</span></p></body></html>", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">0</span></p></body></html>", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">0</span></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL DUE</span></p></body></html>", None))
        ___qtablewidgetitem6 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"code", None));
        ___qtablewidgetitem7 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"client name", None));
        ___qtablewidgetitem8 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Grand Total", None));
        ___qtablewidgetitem9 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Payment status", None));
        ___qtablewidgetitem10 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"order_date", None));
        ___qtablewidgetitem11 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Due", None));
        ___qtablewidgetitem12 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Take payment", None));
        ___qtablewidgetitem13 = self.tableWidget_6.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"edit", None));
        ___qtablewidgetitem14 = self.tableWidget_6.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"delete", None));
        ___qtablewidgetitem15 = self.tableWidget_6.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"return order", None));
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Invoice Amount</span></p></body></html>", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Terms</span></p></body></html>", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Invoice Status</span></p></body></html>", None))
        self.pushButton_25.setText("")
        self.orders_update_btn.setText(QCoreApplication.translate("MainWindow", u"save", None))
        ___qtablewidgetitem16 = self.tableWidget_36.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"item name", None));
        ___qtablewidgetitem17 = self.tableWidget_36.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem18 = self.tableWidget_36.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        self.pushButton_118.setText(QCoreApplication.translate("MainWindow", u"Unlock Invoice", None))
        self.pushButton_119.setText(QCoreApplication.translate("MainWindow", u"post invoice", None))
        self.pushButton_117.setText(QCoreApplication.translate("MainWindow", u"Ledger Journal Entries", None))
        self.pushButton_120.setText(QCoreApplication.translate("MainWindow", u"Lock Invoice", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">grand total</span></p></body></html>", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">total amount</span></p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">payment status</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#b8b8b8;\">discount</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">order date</span></p></body></html>", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#a3a3a3;\">client name</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">sub total</span></p></body></html>", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">due</span></p></body></html>", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#b8b89f;\">payment type</span></p></body></html>", None))
        self.pushButton_83.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Vendors</span></p></body></html>", None))
        self.comboBox_9.setCurrentText("")
        self.pushButton_39.setText("")
        self.lib_btn4_7.setText("")
        self.client_btn_3.setText("")
        ___qtablewidgetitem19 = self.tableWidget_14.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Supplier name", None));
        ___qtablewidgetitem20 = self.tableWidget_14.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Bills", None));
        ___qtablewidgetitem21 = self.tableWidget_14.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        ___qtablewidgetitem22 = self.tableWidget_14.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"delete", None));
        ___qtablewidgetitem23 = self.tableWidget_14.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        self.label_390.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_388.setText(QCoreApplication.translate("MainWindow", u"Address1", None))
        self.label_389.setText(QCoreApplication.translate("MainWindow", u"phone number 2", None))
        self.label_398.setText("")
        self.label_387.setText(QCoreApplication.translate("MainWindow", u"Address2", None))
        self.label_396.setText("")
        self.label_392.setText(QCoreApplication.translate("MainWindow", u"country", None))
        self.label_399.setText("")
        self.label_385.setText(QCoreApplication.translate("MainWindow", u"website", None))
        self.label_395.setText("")
        self.label_397.setText("")
        self.label_386.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_400.setText("")
        self.label_394.setText("")
        self.label_401.setText("")
        self.label_391.setText(QCoreApplication.translate("MainWindow", u"phone number 1", None))
        self.label_393.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">VENDOR INFO</span></p></body></html>", None))
        self.pushButton_177.setText("")
        self.pushButton_161.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.label_373.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.pushButton_68.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"order code", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">sales return</span></p></body></html>", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Journal Entries", None))
        ___qtablewidgetitem24 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Order code", None));
        ___qtablewidgetitem25 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"item name", None));
        ___qtablewidgetitem26 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem27 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem28 = self.tableWidget_9.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Total Amount ", None));
        ___qtablewidgetitem29 = self.tableWidget_9.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem30 = self.tableWidget_9.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        ___qtablewidgetitem31 = self.tableWidget_9.horizontalHeaderItem(7)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Delete", None));
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Total amount", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"item name", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_169.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"telno", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Payments details</span></p></body></html>", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"client name", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">payment type</span></p></body></html>", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Grand total :</span></p></body></html>", None))
        self.label_159.setText("")
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Billing Address</span></p></body></html>", None))
        self.label_168.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">Sales Order</span></p></body></html>", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Total Amount :</span></p></body></html>", None))
        self.label_166.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Discount :</span></p></body></html>", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Items</span></p></body></html>", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Sub-Total :</span></p></body></html>", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Due</span></p></body></html>", None))
        self.label_157.setText("")
        self.label_167.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"address", None))
        self.pushButton_69.setText("")
        ___qtablewidgetitem32 = self.tableWidget_15.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem33 = self.tableWidget_15.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem34 = self.tableWidget_15.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem35 = self.tableWidget_15.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem36 = self.tableWidget_15.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Return item", None));
        self.label_358.setText(QCoreApplication.translate("MainWindow", u"Teller", None))
        self.label_359.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_130.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Account Transaction List Report</span></p></body></html>", None))
        ___qtablewidgetitem37 = self.tableWidget_24.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Account", None));
        ___qtablewidgetitem38 = self.tableWidget_24.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Trans Action Type", None));
        ___qtablewidgetitem39 = self.tableWidget_24.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem40 = self.tableWidget_24.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem41 = self.tableWidget_24.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.client_btn_4.setText("")
        self.pushButton_131.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Ledgers</span></p></body></html>", None))
        ___qtablewidgetitem42 = self.tableWidget_25.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem43 = self.tableWidget_25.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Journal Date", None));
        ___qtablewidgetitem44 = self.tableWidget_25.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        ___qtablewidgetitem45 = self.tableWidget_25.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Journal entries", None));
        self.comboBox_39.setCurrentText("")
        self.pushButton_151.setText("")
        self.label_381.setText(QCoreApplication.translate("MainWindow", u"Ledger Name", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Locked", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.pushButton_168.setText("")
        self.pushButton_169.setText("")
        self.pushButton_170.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">ledger name</span></p></body></html>", None))
        self.label_379.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">locked</span></p></body></html>", None))
        self.label_380.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">active</span></p></body></html>", None))
        self.pushButton_166.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_167.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.checkBox_7.setText("")
        self.checkBox_6.setText("")
        self.pushButton_63.setText("")
        self.pushButton_53.setText("")
        self.comboBox_25.setCurrentText("")
        self.pushButton_123.setText("")
        ___qtablewidgetitem46 = self.tableWidget_27.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PO Number", None));
        ___qtablewidgetitem47 = self.tableWidget_27.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem48 = self.tableWidget_27.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"PO Date", None));
        ___qtablewidgetitem49 = self.tableWidget_27.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"PO Status", None));
        ___qtablewidgetitem50 = self.tableWidget_27.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Fulfilment Date", None));
        ___qtablewidgetitem51 = self.tableWidget_27.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"PO Amount", None));
        ___qtablewidgetitem52 = self.tableWidget_27.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">Purchase Orders</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Fulfilled</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Purchase order Info</span></p></body></html>", None))
        self.label_71.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Status:</span></p></body></html>", None))
        self.label_65.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Po Number</span></p></body></html>", None))
        self.pushButton_98.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_95.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_76.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Po Amount</span></p></body></html>", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">0$</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">0$</span></p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">AMOUNT RECEIVED:</span></p></body></html>", None))
        self.label_135.setText("")
        ___qtablewidgetitem53 = self.tableWidget_28.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem54 = self.tableWidget_28.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem55 = self.tableWidget_28.horizontalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Unit Cost", None));
        ___qtablewidgetitem56 = self.tableWidget_28.horizontalHeaderItem(3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem57 = self.tableWidget_28.horizontalHeaderItem(4)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem58 = self.tableWidget_28.horizontalHeaderItem(5)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Billed", None));
        self.pushButton_52.setText("")
        self.pushButton_23.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Journal Entries</span></p></body></html>", None))
        self.comboBox_40.setCurrentText("")
        self.pushButton_152.setText("")
        ___qtablewidgetitem59 = self.tableWidget_26.horizontalHeaderItem(1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem60 = self.tableWidget_26.horizontalHeaderItem(2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Journal Entry Date", None));
        ___qtablewidgetitem61 = self.tableWidget_26.horizontalHeaderItem(3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem62 = self.tableWidget_26.horizontalHeaderItem(4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        ___qtablewidgetitem63 = self.tableWidget_26.horizontalHeaderItem(5)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Transactions", None));
        self.label_402.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Posted", None))
        self.label_403.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.pushButton_173.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_174.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.pushButton_175.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Locked", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Notes</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Mark as Fulfilled", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Purchase Order Date</span></p></body></html>", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Purchase Order Status</span></p></body></html>", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Fulfillment Date</span></p></body></html>", None))
        self.pushButton_114.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Purchase Order Title</span></p></body></html>", None))
        self.pushButton_77.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        ___qtablewidgetitem64 = self.tableWidget_29.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"item", None));
        ___qtablewidgetitem65 = self.tableWidget_29.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"cost", None));
        ___qtablewidgetitem66 = self.tableWidget_29.horizontalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem67 = self.tableWidget_29.horizontalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem68 = self.tableWidget_29.horizontalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Delete", None));
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Total</span></p></body></html>", None))
        self.label_260.setText("")
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Item</span></p></body></html>", None))
        self.pushButton_116.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Quantity</span></p></body></html>", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Status</span></p></body></html>", None))
        self.pushButton_115.setText(QCoreApplication.translate("MainWindow", u"Create Bill", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"Unit Cost", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Transactions</span></p></body></html>", None))
        self.pushButton_122.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_121.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">TX Type</p></body></html>", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Account</p></body></html>", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        ___qtablewidgetitem69 = self.tableWidget_37.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Account", None));
        ___qtablewidgetitem70 = self.tableWidget_37.horizontalHeaderItem(2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"TransAction Type", None));
        ___qtablewidgetitem71 = self.tableWidget_37.horizontalHeaderItem(3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem72 = self.tableWidget_37.horizontalHeaderItem(4)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem73 = self.tableWidget_37.horizontalHeaderItem(5)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_374.setText(QCoreApplication.translate("MainWindow", u"TX type", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_375.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.pushButton_162.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_164.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_163.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        ___qtablewidgetitem74 = self.tableWidget_30.horizontalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Bill Number", None));
        ___qtablewidgetitem75 = self.tableWidget_30.horizontalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Bill Date", None));
        ___qtablewidgetitem76 = self.tableWidget_30.horizontalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Bill From", None));
        ___qtablewidgetitem77 = self.tableWidget_30.horizontalHeaderItem(3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem78 = self.tableWidget_30.horizontalHeaderItem(4)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Payments", None));
        ___qtablewidgetitem79 = self.tableWidget_30.horizontalHeaderItem(5)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        ___qtablewidgetitem80 = self.tableWidget_30.horizontalHeaderItem(6)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Update", None));
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">Bills</span></p></body></html>", None))
        self.pushButton_100.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_99.setText("")
        self.comboBox_41.setCurrentText("")
        self.pushButton_153.setText("")
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"PREPAID ACCOUNT", None))
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Owe's</p></body></html>", None))
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Cash Account", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"UNEARNED ACCOUNT", None))
        self.label_293.setText("")
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">0$</p></body></html>", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"$0", None))
        self.label_291.setText("")
        self.label_298.setText("")
        ___qtablewidgetitem81 = self.tableWidget_31.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem82 = self.tableWidget_31.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem83 = self.tableWidget_31.horizontalHeaderItem(2)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Unit Cost", None));
        ___qtablewidgetitem84 = self.tableWidget_31.horizontalHeaderItem(3)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem85 = self.tableWidget_31.horizontalHeaderItem(4)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"PO", None));
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Bill Items</span></p></body></html>", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Bill Transaction</span></p></body></html>", None))
        self.pushButton_103.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Bill Info</span></p></body></html>", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Not Approved", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Status :</span></p></body></html>", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Amount Paid</span></p></body></html>", None))
        self.pushButton_102.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"0$", None))
        ___qtablewidgetitem86 = self.tableWidget_32.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem87 = self.tableWidget_32.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Account", None));
        ___qtablewidgetitem88 = self.tableWidget_32.horizontalHeaderItem(2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Account Name", None));
        ___qtablewidgetitem89 = self.tableWidget_32.horizontalHeaderItem(3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Credit", None));
        ___qtablewidgetitem90 = self.tableWidget_32.horizontalHeaderItem(4)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Debit", None));
        ___qtablewidgetitem91 = self.tableWidget_32.horizontalHeaderItem(5)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.pushButton_104.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Vendor Info</span></p></body></html>", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">vendor name</span></p></body></html>", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Bill state</span></p></body></html>", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None))
        self.label_382.setText("")
        self.label_383.setText(QCoreApplication.translate("MainWindow", u"Make payment", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"paid", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"Paid Date", None))
        self.pushButton_78.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        ___qtablewidgetitem92 = self.tableWidget_33.horizontalHeaderItem(0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem93 = self.tableWidget_33.horizontalHeaderItem(1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Unit cost", None));
        ___qtablewidgetitem94 = self.tableWidget_33.horizontalHeaderItem(2)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem95 = self.tableWidget_33.horizontalHeaderItem(3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"view purchase order", None));
        ___qtablewidgetitem96 = self.tableWidget_33.horizontalHeaderItem(4)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem97 = self.tableWidget_34.horizontalHeaderItem(0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem98 = self.tableWidget_34.horizontalHeaderItem(1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"PO Quantity", None));
        ___qtablewidgetitem99 = self.tableWidget_34.horizontalHeaderItem(2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#8c8c8c;\">Vendor Info</span></p></body></html>", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">vendor name</span></p></body></html>", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.pushButton_176.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_110.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bill Items</span></p></body></html>", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.pushButton_109.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_106.setText(QCoreApplication.translate("MainWindow", u"Bill Ledger", None))
        self.pushButton_107.setText(QCoreApplication.translate("MainWindow", u"Lock Bill", None))
        self.pushButton_108.setText(QCoreApplication.translate("MainWindow", u"Unlock Bill", None))
        self.pushButton_111.setText(QCoreApplication.translate("MainWindow", u"Ledger Journal Entries", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Bill Amount</span></p></body></html>", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">External Refrence Number</span></p></body></html>", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Terms</span></p></body></html>", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Bill Status</span></p></body></html>", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Journal Entry Detail</span></p></body></html>", None))
        ___qtablewidgetitem100 = self.tableWidget_35.horizontalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem101 = self.tableWidget_35.horizontalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Account", None));
        ___qtablewidgetitem102 = self.tableWidget_35.horizontalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Credit", None));
        ___qtablewidgetitem103 = self.tableWidget_35.horizontalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Debit", None));
        ___qtablewidgetitem104 = self.tableWidget_35.horizontalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.pushButton_112.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_113.setText(QCoreApplication.translate("MainWindow", u"New Transaction", None))
        self.pushButton_7.setText("")
        self.dateEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_133.setText("")
        ___qtablewidgetitem105 = self.tableWidget_12.horizontalHeaderItem(0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem106 = self.tableWidget_12.horizontalHeaderItem(1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Client name", None));
        ___qtablewidgetitem107 = self.tableWidget_12.horizontalHeaderItem(2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem108 = self.tableWidget_12.horizontalHeaderItem(3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem109 = self.tableWidget_12.horizontalHeaderItem(4)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Due", None));
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#afafaf;\">Paid Amount</span></p></body></html>", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#cccccc;\">Order Date</span></p></body></html>", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#bfbfbf;\">Payment of Order:</span></p></body></html>", None))
        self.pushButton_13.setText("")
        self.pushButton_73.setText("")
        ___qtablewidgetitem110 = self.tableWidget_23.horizontalHeaderItem(0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem111 = self.tableWidget_23.horizontalHeaderItem(1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Supplier name", None));
        ___qtablewidgetitem112 = self.tableWidget_23.horizontalHeaderItem(2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem113 = self.tableWidget_23.horizontalHeaderItem(3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem114 = self.tableWidget_23.horizontalHeaderItem(4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Due", None));
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"payment source", None))
        self.label_204.setText("")
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#bfbfbf;\">Payment of supplier:</span></p></body></html>", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#afafaf;\">Amount paid</span></p></body></html>", None))
        self.pushButton_72.setText("")
        self.dateEdit_7.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#cccccc;\">Order Date</span></p></body></html>", None))
        self.comboBox_3.setCurrentText("")
        self.pushButton_22.setText("")
        ___qtablewidgetitem115 = self.tableWidget_11.horizontalHeaderItem(0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem116 = self.tableWidget_11.horizontalHeaderItem(1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Client name", None));
        ___qtablewidgetitem117 = self.tableWidget_11.horizontalHeaderItem(2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Tel no.", None));
        ___qtablewidgetitem118 = self.tableWidget_11.horizontalHeaderItem(3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem119 = self.tableWidget_11.horizontalHeaderItem(4)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem120 = self.tableWidget_11.horizontalHeaderItem(5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem121 = self.tableWidget_11.horizontalHeaderItem(6)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Due", None));
        ___qtablewidgetitem122 = self.tableWidget_11.horizontalHeaderItem(7)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"edit", None));
        ___qtablewidgetitem123 = self.tableWidget_11.horizontalHeaderItem(8)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"delete", None));
        self.lib_btn4_5.setText("")
        self.client_btn.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Clients</span></p></body></html>", None))
        self.label_330.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"sales return", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"profit & loss", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"orders", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"General ledger", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Balance sheet", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"sales", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Reports</span></p></body></html>", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Profit &amp; Loss</span></p></body></html>", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"name", None));
        self.pushButton_64.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.pushButton_9.setText("")
        self.pushButton_96.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_97.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        ___qtablewidgetitem124 = self.tableWidget_10.horizontalHeaderItem(0)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"name ", None));
        ___qtablewidgetitem125 = self.tableWidget_10.horizontalHeaderItem(1)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u" Total amount ", None));
        ___qtablewidgetitem126 = self.tableWidget_10.horizontalHeaderItem(2)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Description ", None));
        ___qtablewidgetitem127 = self.tableWidget_10.horizontalHeaderItem(3)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"Tx type", None));
        ___qtablewidgetitem128 = self.tableWidget_10.horizontalHeaderItem(4)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Return date", None));
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">sales returns</span></p></body></html>", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.pushButton_65.setText("")
        self.pushButton_42.setText("")
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_94.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">stock</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        ___qtablewidgetitem129 = self.tableWidget_19.horizontalHeaderItem(0)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"UPC", None));
        ___qtablewidgetitem130 = self.tableWidget_19.horizontalHeaderItem(1)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem131 = self.tableWidget_19.horizontalHeaderItem(2)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"BP", None));
        ___qtablewidgetitem132 = self.tableWidget_19.horizontalHeaderItem(3)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"SP", None));
        ___qtablewidgetitem133 = self.tableWidget_19.horizontalHeaderItem(4)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem134 = self.tableWidget_19.horizontalHeaderItem(5)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Supplier", None));
        ___qtablewidgetitem135 = self.tableWidget_19.horizontalHeaderItem(6)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem136 = self.tableWidget_19.horizontalHeaderItem(7)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Vat", None));
        ___qtablewidgetitem137 = self.tableWidget_19.horizontalHeaderItem(8)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.pushButton_34.setText("")
        self.pushButton_59.setText("")
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        ___qtablewidgetitem138 = self.tableWidget_20.horizontalHeaderItem(0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"Sale No.", None));
        ___qtablewidgetitem139 = self.tableWidget_20.horizontalHeaderItem(1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"UPC", None));
        ___qtablewidgetitem140 = self.tableWidget_20.horizontalHeaderItem(2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem141 = self.tableWidget_20.horizontalHeaderItem(3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem142 = self.tableWidget_20.horizontalHeaderItem(4)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem143 = self.tableWidget_20.horizontalHeaderItem(5)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"KSH ", None));
        ___qtablewidgetitem144 = self.tableWidget_20.horizontalHeaderItem(6)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u" VAT ", None));
        ___qtablewidgetitem145 = self.tableWidget_20.horizontalHeaderItem(7)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u" totalvat", None));
        ___qtablewidgetitem146 = self.tableWidget_20.horizontalHeaderItem(8)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"taxcode", None));
        ___qtablewidgetitem147 = self.tableWidget_20.horizontalHeaderItem(9)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"sale date", None));
        self.pushButton_56.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.pushButton_60.setText("")
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">sales</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton_84.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_85.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"credit", None))
        self.pushButton_61.setText("")
        self.label_231.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.pushButton_57.setText("")
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"debit", None))
        ___qtablewidgetitem148 = self.tableWidget_21.horizontalHeaderItem(0)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem149 = self.tableWidget_21.horizontalHeaderItem(1)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"name ", None));
        ___qtablewidgetitem150 = self.tableWidget_21.horizontalHeaderItem(2)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem151 = self.tableWidget_21.horizontalHeaderItem(3)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"description ", None));
        ___qtablewidgetitem152 = self.tableWidget_21.horizontalHeaderItem(4)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"debit ", None));
        ___qtablewidgetitem153 = self.tableWidget_21.horizontalHeaderItem(5)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"credit", None));
        ___qtablewidgetitem154 = self.tableWidget_21.horizontalHeaderItem(6)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"ledgerdate ", None));
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">General Ledger</span></p></body></html>", None))
        self.label_228.setText("")
        self.label_230.setText("")
        self.pushButton_86.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton_87.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_88.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.pushButton_58.setText("")
        self.pushButton_62.setText("")
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Orders</span></p></body></html>", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        ___qtablewidgetitem155 = self.tableWidget_22.horizontalHeaderItem(0)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem156 = self.tableWidget_22.horizontalHeaderItem(1)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"Client name", None));
        ___qtablewidgetitem157 = self.tableWidget_22.horizontalHeaderItem(2)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"Grand total", None));
        ___qtablewidgetitem158 = self.tableWidget_22.horizontalHeaderItem(3)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Total amount", None));
        ___qtablewidgetitem159 = self.tableWidget_22.horizontalHeaderItem(4)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"Payment  stats", None));
        ___qtablewidgetitem160 = self.tableWidget_22.horizontalHeaderItem(5)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"Order date", None));
        ___qtablewidgetitem161 = self.tableWidget_22.horizontalHeaderItem(6)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"Due", None));
        self.pushButton_89.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.pushButton_90.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.pushButton_91.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ASSETS</span></p></body></html>", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#787878;\">current assets</span></p></body></html>", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#787878;\">fixed assets</span></p></body></html>", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#787878;\">Total assets</span></p></body></html>", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">LIABILITIES</span></p></body></html>", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#767676;\">short term liabilities</span></p></body></html>", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#767676;\">long term liabilities</span></p></body></html>", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#787878;\">Total Liabilities</span></p></body></html>", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">EXPENSES</span></p></body></html>", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#787878;\">fixed expenses</span></p></body></html>", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#787878;\">variable expenses</span></p></body></html>", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#787878;\">Total expenses</span></p></body></html>", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.pushButton_45.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Balance Sheet</span></p></body></html>", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">capital employed</span></p></body></html>", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">working capital</span></p></body></html>", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Gross profit</span></p></body></html>", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Net profit</span></p></body></html>", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">CURRENT RATIO</span></p></body></html>", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">DEBT RATIO</span></p></body></html>", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#888888;\">0</span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Stock</span></p></body></html>", None))
        self.label_176.setText("")
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL ITEMS WORTH</span></p></body></html>", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"refresh", None))
        self.pushButton_54.setText("")
        self.pushButton_149.setText(QCoreApplication.translate("MainWindow", u"UOM", None))
        self.comboBox.setCurrentText("")
        self.pushButton_18.setText("")
        ___qtablewidgetitem162 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"UPC", None));
        ___qtablewidgetitem163 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem164 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"COGS", None));
        ___qtablewidgetitem165 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"Selling price", None));
        ___qtablewidgetitem166 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem167 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"Supplier", None));
        ___qtablewidgetitem168 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem169 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"Reoder limit", None));
        ___qtablewidgetitem170 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        ___qtablewidgetitem171 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"VAT", None));
        ___qtablewidgetitem172 = self.tableWidget_4.horizontalHeaderItem(10)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.label_178.setText("")
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL ITEMS</span></p></body></html>", None))
        self.label_181.setText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TOTAL COGS</span></p></body></html>", None))
        self.pushButton_150.setText("")
        self.label_367.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Unit Of Measure</span></p></body></html>", None))
        self.comboBox_42.setCurrentText("")
        self.pushButton_154.setText("")
        ___qtablewidgetitem173 = self.tableWidget_42.horizontalHeaderItem(0)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem174 = self.tableWidget_42.horizontalHeaderItem(1)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem175 = self.tableWidget_42.horizontalHeaderItem(2)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"Unit Abbreviation", None));
        ___qtablewidgetitem176 = self.tableWidget_42.horizontalHeaderItem(3)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_370.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">UOM Abbreviation</span></p></body></html>", None))
        self.label_368.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>", None))
        self.label_369.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Status</span></p></body></html>", None))
        self.pushButton_159.setText("")
        self.pushButton_160.setText("")
        self.pushButton_158.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.label_134.setText("")
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Create New Order</span></p></body></html>", None))
        ___qtablewidgetitem177 = self.tableWidget_16.horizontalHeaderItem(0)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"UPC", None));
        ___qtablewidgetitem178 = self.tableWidget_16.horizontalHeaderItem(1)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem179 = self.tableWidget_16.horizontalHeaderItem(2)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem180 = self.tableWidget_16.horizontalHeaderItem(3)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem181 = self.tableWidget_16.horizontalHeaderItem(4)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"TOTAL KSH", None));
        ___qtablewidgetitem182 = self.tableWidget_16.horizontalHeaderItem(7)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"Remove", None));
        self.label_123.setText("")
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"payment status", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Grand total", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total</p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"payment type", None))
        self.label_114.setText("")
        self.pushButton_24.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u" save order", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"New client", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#cfcfcf;\">Paid amount</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#9a9a9a;\">item name</span></p></body></html>", None))
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"Bill Status", None))
        self.pushButton_71.setText(QCoreApplication.translate("MainWindow", u"add row", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#cbcbcb;\">Quantity</span></p></body></html>", None))
        self.lineEdit_7.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Sale No:", None))
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"Terms", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Footer</p></body></html>", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">email</p></body></html>", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">notes</p></body></html>", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#bcbcbc;\">Businness name</span></p></body></html>", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#bcbcbc;\">phone number</span></p></body></html>", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Currency</p></body></html>", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">company street address</p></body></html>", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Invoice</span></p></body></html>", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#b3b3b3;\">Company profile</span></p></body></html>", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#bcbcbc;\">P.O BOX</span></p></body></html>", None))
        self.label_356.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Users</span></p></body></html>", None))
        self.pushButton_143.setText("")
        ___qtablewidgetitem183 = self.tableWidget_41.horizontalHeaderItem(0)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"Employee Name", None));
        ___qtablewidgetitem184 = self.tableWidget_41.horizontalHeaderItem(1)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("MainWindow", u"User name", None));
        ___qtablewidgetitem185 = self.tableWidget_41.horizontalHeaderItem(2)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem186 = self.tableWidget_41.horizontalHeaderItem(3)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem187 = self.tableWidget_41.horizontalHeaderItem(4)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("MainWindow", u"Assign", None));
        ___qtablewidgetitem188 = self.tableWidget_41.horizontalHeaderItem(5)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.pushButton_146.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_148.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_147.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_366.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>", None))
        self.label_361.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee name</span></p></body></html>", None))
        self.lineEdit_77.setInputMask("")
        self.label_365.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Assign</span></p></body></html>", None))
        self.label_363.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Role</span></p></body></html>", None))
        self.label_362.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Confirm Password</span></p></body></html>", None))
        self.label_364.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">status</span></p></body></html>", None))
        self.label_360.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Transactions</span></p></body></html>", None))
        self.label_80.setText("")
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Accounts Payable", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.pushButton_15.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Payments</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"what are you paying for", None))
        ___qtablewidgetitem189 = self.tableWidget_17.horizontalHeaderItem(0)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem190 = self.tableWidget_17.horizontalHeaderItem(1)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem191 = self.tableWidget_17.horizontalHeaderItem(2)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem192 = self.tableWidget_17.horizontalHeaderItem(3)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem193 = self.tableWidget_17.horizontalHeaderItem(4)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("MainWindow", u"Credit", None));
        ___qtablewidgetitem194 = self.tableWidget_17.horizontalHeaderItem(5)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("MainWindow", u"Debit", None));
        ___qtablewidgetitem195 = self.tableWidget_17.horizontalHeaderItem(6)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.pushButton_40.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"source of payment", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Recent Transactions", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Tel 2", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Supplier name", None))
#if QT_CONFIG(whatsthis)
        self.lineEdit_46.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>background-color: rgb(48, 48, 48);</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Tel 1", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Addres 2", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Addres 1", None))
        self.pushButton_79.setText("")
        self.pushButton_80.setText("")
        self.label_371.setText(QCoreApplication.translate("MainWindow", u"Site", None))
        self.label_372.setText(QCoreApplication.translate("MainWindow", u"Country", None))
#if QT_CONFIG(whatsthis)
        self.lineEdit_56.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>background-color: rgb(48, 48, 48);</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_81.setText("")
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Due", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"telno", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Client name", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.pushButton_82.setText("")
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Quantiy", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"purchase date", None))
        self.pushButton_67.setText("")
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Source of payment", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Purchase", None))
        ___qtablewidgetitem196 = self.tableWidget_18.horizontalHeaderItem(0)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("MainWindow", u"Purchase code", None));
        ___qtablewidgetitem197 = self.tableWidget_18.horizontalHeaderItem(1)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("MainWindow", u"Supplier", None));
        ___qtablewidgetitem198 = self.tableWidget_18.horizontalHeaderItem(2)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem199 = self.tableWidget_18.horizontalHeaderItem(3)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem200 = self.tableWidget_18.horizontalHeaderItem(4)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("MainWindow", u"Transportation", None));
        ___qtablewidgetitem201 = self.tableWidget_18.horizontalHeaderItem(5)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("MainWindow", u"Unit price", None));
        ___qtablewidgetitem202 = self.tableWidget_18.horizontalHeaderItem(6)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">inventory purchase</span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"supplier", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Transportation", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"purchase code", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"Owe,s", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Cost of items", None))
        ___qtablewidgetitem203 = self.tableWidget_13.horizontalHeaderItem(0)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem204 = self.tableWidget_13.horizontalHeaderItem(1)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem205 = self.tableWidget_13.horizontalHeaderItem(2)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("MainWindow", u"Debit", None));
        ___qtablewidgetitem206 = self.tableWidget_13.horizontalHeaderItem(3)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("MainWindow", u"Credit", None));
        ___qtablewidgetitem207 = self.tableWidget_13.horizontalHeaderItem(4)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem208 = self.tableWidget_13.horizontalHeaderItem(5)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">income</span></p></body></html>", None))
        self.lib_btn2_5.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.lib_btn3_6.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u" Edit", None))
        self.lib_btn4_6.setText(QCoreApplication.translate("MainWindow", u" refresh", None))
        self.addbutton.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.deletebutton.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u" Edit", None))
        self.savebutton.setText(QCoreApplication.translate("MainWindow", u" refresh", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">current assets</span></p></body></html>", None))
        ___qtablewidgetitem209 = self.tableAsset.horizontalHeaderItem(0)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem210 = self.tableAsset.horizontalHeaderItem(1)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem211 = self.tableAsset.horizontalHeaderItem(2)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem212 = self.tableAsset.horizontalHeaderItem(3)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem213 = self.tableAsset.horizontalHeaderItem(4)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("MainWindow", u"debit", None));
        ___qtablewidgetitem214 = self.tableAsset.horizontalHeaderItem(5)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("MainWindow", u"credit", None));
        ___qtablewidgetitem215 = self.tableAsset.horizontalHeaderItem(6)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem216 = self.fixed_assets_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem217 = self.fixed_assets_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem218 = self.fixed_assets_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem219 = self.fixed_assets_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem220 = self.fixed_assets_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("MainWindow", u"debit", None));
        ___qtablewidgetitem221 = self.fixed_assets_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("MainWindow", u"credit", None));
        ___qtablewidgetitem222 = self.fixed_assets_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u" Edit", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" refresh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>fixed assests</p></body></html>", None))
        self.pushButton_75.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"chart of accounts", None))
        ___qtablewidgetitem223 = self.chart_of_accounts_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("MainWindow", u"code", None));
        ___qtablewidgetitem224 = self.chart_of_accounts_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem225 = self.chart_of_accounts_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("MainWindow", u"Account Name", None));
        ___qtablewidgetitem226 = self.chart_of_accounts_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("MainWindow", u"Balance Type", None));
        ___qtablewidgetitem227 = self.chart_of_accounts_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("MainWindow", u"Details", None));
        ___qtablewidgetitem228 = self.chart_of_accounts_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.lib_addbutton.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.lib_deletebutton.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u" Edit", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u" refresh", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">short term liabilities</span></p></body></html>", None))
        ___qtablewidgetitem229 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem230 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem231 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem232 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION", None));
        ___qtablewidgetitem233 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("MainWindow", u"DEBIT", None));
        ___qtablewidgetitem234 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("MainWindow", u"CREDIT", None));
        ___qtablewidgetitem235 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">long term liabilities</span></p></body></html>", None))
        ___qtablewidgetitem236 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem237 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem237.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem238 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem238.setText(QCoreApplication.translate("MainWindow", u"KSH", None));
        ___qtablewidgetitem239 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem239.setText(QCoreApplication.translate("MainWindow", u"DESCRIPTION", None));
        ___qtablewidgetitem240 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem240.setText(QCoreApplication.translate("MainWindow", u"debit", None));
        ___qtablewidgetitem241 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem241.setText(QCoreApplication.translate("MainWindow", u"CREDIT", None));
        ___qtablewidgetitem242 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem242.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        self.lib_btn2.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.lib_btn3.setText(QCoreApplication.translate("MainWindow", u" Delete", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u" Edit", None))
        self.lib_btn4.setText(QCoreApplication.translate("MainWindow", u" refresh", None))
        self.checkBox_5.setText("")
        self.checkBox_2.setText("")
        self.label_376.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Code</span></p></body></html>", None))
        self.label_377.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Locked</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#f9f9f9;\">Balance type</span></p></body></html>", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.pushButton_165.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">account name</span></p></body></html>", None))
        self.label_378.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">active</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">accounts</span></p></body></html>", None))
        self.label_198.setText("")
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Total Assets</span></p></body></html>", None))
        self.label_196.setText("")
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Total Liabilities</span></p></body></html>", None))
        self.label_194.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Total Revenue</span></p></body></html>", None))
        self.label_192.setText("")
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Total Expenses</span></p></body></html>", None))
        self.pushButton_74.setText(QCoreApplication.translate("MainWindow", u"chart of accounts", None))
        self.ledgers_btn.setText(QCoreApplication.translate("MainWindow", u"Ledgers", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Purchase Order", None))
        self.pushButton_101.setText(QCoreApplication.translate("MainWindow", u"Bills", None))
        self.pushButton_124.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Accounts</span></p></body></html>", None))
        self.pushButton_125.setText(QCoreApplication.translate("MainWindow", u"Positions", None))
        self.ledgers_btn_2.setText(QCoreApplication.translate("MainWindow", u"Departments", None))
        self.pushButton_126.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        ___qtablewidgetitem243 = self.tableWidget_38.horizontalHeaderItem(0)
        ___qtablewidgetitem243.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem244 = self.tableWidget_38.horizontalHeaderItem(1)
        ___qtablewidgetitem244.setText(QCoreApplication.translate("MainWindow", u"Position name", None));
        ___qtablewidgetitem245 = self.tableWidget_38.horizontalHeaderItem(2)
        ___qtablewidgetitem245.setText(QCoreApplication.translate("MainWindow", u"Level", None));
        ___qtablewidgetitem246 = self.tableWidget_38.horizontalHeaderItem(3)
        ___qtablewidgetitem246.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem247 = self.tableWidget_38.horizontalHeaderItem(4)
        ___qtablewidgetitem247.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.pushButton_132.setText("")
        self.comboBox_44.setCurrentText("")
        self.pushButton_156.setText("")
        ___qtablewidgetitem248 = self.tableWidget_39.horizontalHeaderItem(0)
        ___qtablewidgetitem248.setText(QCoreApplication.translate("MainWindow", u"Department code", None));
        ___qtablewidgetitem249 = self.tableWidget_39.horizontalHeaderItem(1)
        ___qtablewidgetitem249.setText(QCoreApplication.translate("MainWindow", u"Department name", None));
        ___qtablewidgetitem250 = self.tableWidget_39.horizontalHeaderItem(2)
        ___qtablewidgetitem250.setText(QCoreApplication.translate("MainWindow", u"Department Level", None));
        ___qtablewidgetitem251 = self.tableWidget_39.horizontalHeaderItem(3)
        ___qtablewidgetitem251.setText(QCoreApplication.translate("MainWindow", u"Department Supirior", None));
        ___qtablewidgetitem252 = self.tableWidget_39.horizontalHeaderItem(4)
        ___qtablewidgetitem252.setText(QCoreApplication.translate("MainWindow", u"Department Status", None));
        ___qtablewidgetitem253 = self.tableWidget_39.horizontalHeaderItem(5)
        ___qtablewidgetitem253.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.pushButton_128.setText("")
        self.comboBox_45.setCurrentText("")
        self.pushButton_157.setText("")
        self.pushButton_133.setText("")
        self.comboBox_43.setCurrentText("")
        self.pushButton_155.setText("")
        ___qtablewidgetitem254 = self.tableWidget_40.horizontalHeaderItem(0)
        ___qtablewidgetitem254.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem255 = self.tableWidget_40.horizontalHeaderItem(1)
        ___qtablewidgetitem255.setText(QCoreApplication.translate("MainWindow", u"Employee name", None));
        ___qtablewidgetitem256 = self.tableWidget_40.horizontalHeaderItem(2)
        ___qtablewidgetitem256.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem257 = self.tableWidget_40.horizontalHeaderItem(3)
        ___qtablewidgetitem257.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem258 = self.tableWidget_40.horizontalHeaderItem(4)
        ___qtablewidgetitem258.setText(QCoreApplication.translate("MainWindow", u"Start date", None));
        ___qtablewidgetitem259 = self.tableWidget_40.horizontalHeaderItem(5)
        ___qtablewidgetitem259.setText(QCoreApplication.translate("MainWindow", u"profile", None));
        ___qtablewidgetitem260 = self.tableWidget_40.horizontalHeaderItem(6)
        ___qtablewidgetitem260.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee Position</span></p></body></html>", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Status</span></p></body></html>", None))
        self.pushButton_134.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_135.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_141.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Last name</span></p></body></html>", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Addres</span></p></body></html>", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee code</span></p></body></html>", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Start Date</span></p></body></html>", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Mobile</span></p></body></html>", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee Department</span></p></body></html>", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Email</span></p></body></html>", None))
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">First name</span></p></body></html>", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Gender</span></p></body></html>", None))
        self.label_352.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Employee Update</span></p></body></html>", None))
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department short name</span></p></body></html>", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department code</span></p></body></html>", None))
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department description</span></p></body></html>", None))
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Status</span></p></body></html>", None))
        self.pushButton_136.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_137.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_142.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department supirior</span></p></body></html>", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department level</span></p></body></html>", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">department name</span></p></body></html>", None))
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Department Update</span></p></body></html>", None))
        self.label_354.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Employee:</span></p></body></html>", None))
        self.label_357.setText("")
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">First name :</span></p></body></html>", None))
        self.label_328.setText("")
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee Position :</span></p></body></html>", None))
        self.label_335.setText("")
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Last name :</span></p></body></html>", None))
        self.label_331.setText("")
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Employee Department :</span></p></body></html>", None))
        self.label_336.setText("")
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Mobile :</span></p></body></html>", None))
        self.label_332.setText("")
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Gender :</span></p></body></html>", None))
        self.label_338.setText("")
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Email :</span></p></body></html>", None))
        self.label_333.setText("")
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Start Date :</span></p></body></html>", None))
        self.label_339.setText("")
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Address :</span></p></body></html>", None))
        self.label_334.setText("")
        self.label_355.setText("")
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">position code</span></p></body></html>", None))
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">position description</span></p></body></html>", None))
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">position level</span></p></body></html>", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">position name</span></p></body></html>", None))
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">status</span></p></body></html>", None))
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Position update</span></p></body></html>", None))
        self.pushButton_138.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_139.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_140.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_349.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">position short name</span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

