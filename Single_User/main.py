##############################################################################
#           (Where there is no order, there is confusion) -Luca Pacioli       #
##############################################################################
import json
import logging
import random
import re
import string
import sys
import os
import sqlite3
import csv
import uuid
import hashlib
from datetime import datetime as dt
from datetime import date, timedelta
import babel.numbers
from numpy import who
import requests
import decimal
from PySide6 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QLineEdit, QVBoxLayout
from modules import charts, search_table
from modules.frontend.ui_add_ledger import Ui_Dialog_Add_Ledger
from modules.frontend.ui_bizdetail import Ui_Dialog10
from modules.frontend.ui_uom import Ui_UOM
from modules.frontend.ui_update import Ui_Dialog8
from modules.frontend.ui_salesedit import Ui_Dialog7
from modules.frontend.ui_addstock import Ui_Dialog1
from modules.frontend.ui_taxsettingsui import Ui_Dialog
from modules.frontend.ui_taxsettingsui import Ui_Dialog
from modules import orders_function, uom
from modules import bills
from modules import admin
from modules import st_database
from modules import Table_resizeing
from modules.frontend.ui_income_edit import Ui_Dialog13
from modules.frontend.ui_profile import Ui_Dialog_profile
from modules.frontend.ui_coa import Ui_Dialog_coa
from modules.frontend.ui_journalentry import Ui_Dialog_journal_entry
from modules import payment
from modules.purchase_order import PurchaseOrder
from modules import accounts
from modules import refresh_dashboard
from modules import tests
from invoice import ban
from currencies import curencies
from modules import imageconversion
from modules.frontend.ui_purchase_order import Ui_DialogPurchaseOrder
from modules.frontend.ui_bills import Ui_Dialog_Bills
from modules.frontend.ui_user_managment import Ui_User_managment
from modules.frontend.ui_login_accounts import Ui_Accounts_Login
from circular_progress import CircularProgress
from modules import hrms
from modules.entrance import Ui_Entrance
from modules.frontend.ui_login_admin import Ui_Login_Admin_In
from modules.frontend.ui_login_hr import Ui_Singnup
from modules.frontend.ui_logout import  Ui_logout
from modules.frontend.ui_department import  Ui_Departments
from modules.frontend.ui_position import  Ui_Position
from modules.frontend.ui_employee import  Ui_Employee
from modules.tableclass import TableQt
from modules.update_pages import UPDATE_PAGE_SetWidgetsData
from modules.contextmanager.contex_manager import SQLite_CONTEX_MANAGER
from modules.frontend.ui_main import Ui_MainWindow
from modules.frontend.ui_login import Ui_Login
from modules.ledger_btns import LEDGERBUTTONS
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
counter = 0
jumper = 10
user_UUID = []
auto_num = []
ledger_id = []
invoice_id = []
who_is_logged = []
jr_id_lst = []
current_bill_code_fromTable = []
purchase_order_bill_uuid = []
basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)
try:
    conn = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recip_detail(id_17 INTEGER PRIMARY KEY, business_name TEXT, pobox TEXT, contact TEXT, email TEXT, street_address TEXT, notes TEXT, footer TEXT, currency TEXT, profile_photo BLOB)")
    c.execute("CREATE TABLE IF NOT EXISTS admin(email, salt, hash, token, logged_in, password_set, user_uuid)")
    cash_label = c.execute(
        "SELECT currency FROM recip_detail WHERE id_17=1").fetchone()
    cash_label = (''.join(map(str, cash_label)))
    c.close()
except Exception:
    cash_label = "$"
# ==> YOUR APPLICATION WINDOW



def insert7():
    v = InsertDialog7()
    v.exec()


def insert11():
    v = clientadd()
    v.exec()


def insert14():
    v = supplieradd()
    v.exec()


def insert13():
    v = InsertIncome()
    v.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "yobi"
        description = "Yobi"
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.ui.titleRightInfo.setText(description)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.ui.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # LEFT MENUS
        self.logged_in_user()
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_widgets.clicked.connect(self.buttonClick)
        self.ui.btn_new.clicked.connect(self.buttonClick)
        self.ui.btn_save.clicked.connect(self.buttonClick)
        self.ui.btn_exit.clicked.connect(self.buttonClick)
        self.ui.client_btn_2.clicked.connect(self.buttonClick)
        self.ui.pushButton.clicked.connect(self.buttonClick)
        self.ui.pushButton_8.clicked.connect(self.buttonClick)
        self.ui.pushButton_17.clicked.connect(self.buttonClick)
        self.ui.pushButton_19.clicked.connect(self.buttonClick)
        self.ui.pushButton_28.clicked.connect(self.buttonClick)
        self.ui.pushButton_29.clicked.connect(self.buttonClick)
        self.ui.pushButton_3.clicked.connect(self.buttonClick)
        self.ui.pushButton_30.clicked.connect(self.buttonClick)
        self.ui.pushButton_37.clicked.connect(self.buttonClick)
        self.ui.btn_widgets_2.clicked.connect(self.buttonClick)
        # self.ui.pushButton_127.clicked.connect(self.buttonClick)
        self.ui.btn_logout.clicked.connect(self.buttonClick)
        # self.ui.pushButton_144.clicked.connect(self.buttonClick)
        # self.ui.pushButton_145.clicked.connect(self.buttonClick)
        self.ui.pushButton_129.clicked.connect(self.buttonClick)
        self.ui.pushButton_149.clicked.connect(self.buttonClick)
        self.ui.pushButton_63.clicked.connect(self.buttonClick)
        self.ui.pushButton_131.clicked.connect(self.buttonClick)
        self.ui.pushButton_99.clicked.connect(self.buttonClick)
        self.ui.pushButton_122.clicked.connect(self.buttonClick)
        self.ui.pushButton_52.clicked.connect(self.buttonClick)
        self.ui.pushButton_158.clicked.connect(self.buttonClick)
    
        st_database.stats_database(self)
        
        
        
        self.ui.ledgers_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_32))
        self.ui.pushButton_13.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_3))
        self.ui.pushButton_35.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_16))
        self.ui.pushButton_74.clicked.connect(
            lambda: self.ui.stackedwidget_3.setCurrentWidget(
                self.ui.page_28))
    
        self.ui.pushButton.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_3))
        self.ui.pushButton_69.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_3))
        self.ui.pushButton_25.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_3))
        self.ui.pushButton_68.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_20))
        #self.ui.pushButton_70.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_21))
        self.ui.pushButton_36.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_34))
        self.ui.pushButton_101.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_37))
        self.ui.pushButton_82.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_4))
        self.ui.pushButton_80.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_21))
        self.ui.pushButton_83.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_3))
        self.ui.pushButton_27.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page))
        self.ui.pushButton_76.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_34))
        self.ui.pushButton_15.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_15))
        self.ui.pushButton_67.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_15))
        self.ui.pushButton_158.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_57))
        self.ui.pushButton_125.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(
                self.ui.page_45))
        self.ui.ledgers_btn_2.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(
                self.ui.page_46))
        self.ui.pushButton_126.clicked.connect(
            lambda: self.ui.stackedWidget_4.setCurrentWidget(
                self.ui.page_47))
        self.ui.pushButton_165.clicked.connect(
            lambda: self.ui.stackedwidget_3.setCurrentWidget(
                self.ui.page_28))
        self.ui.pushButton_130.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_2))
        self.ui.pushButton_11.clicked.connect(self.delete)
 
        self.ui.client_btn.clicked.connect(insert11)
        self.ui.pushButton_2.clicked.connect(insert11)
        self.ui.lib_btn2_5.clicked.connect(insert13)
        self.ui.client_btn_3.clicked.connect(insert14)
        self.ui.pushButton_10.clicked.connect(self.loaddata9)
        self.ui.lib_btn4_6.clicked.connect(self.loaddata13)
        self.ui.tableWidget_4.setFont((QFont("Times", 13)))
        self.ui.tableWidget_4.setColumnWidth(0, 140)
        self.ui.tableWidget_4.setColumnWidth(1, 180)
        self.ui.tableWidget_4.setColumnWidth(2, 100)
        self.ui.tableWidget_4.setColumnWidth(3, 100)
        self.ui.tableWidget_4.setColumnWidth(4, 80)
        self.ui.tableWidget_4.setColumnWidth(5, 100)
        self.ui.tableWidget_4.setColumnWidth(6, 100)
        self.ui.tableWidget_4.setColumnWidth(7, 70)
        

        self.ui.tableWidget_4.horizontalHeader().setVisible(True)
   
        self.ui.tableWidget_7.setColumnWidth(0, 100)
        self.ui.tableWidget_7.setColumnWidth(1, 100)
        self.ui.tableWidget_7.setColumnWidth(2, 100)
        # resizes all table columns
        # self.ui.tableAsset.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableAsset.resizeRowsToContents()
        self.ui.tableAsset.setFont((QFont("Times", 13)))
        self.ui.tableAsset.setColumnWidth(0, 30)
        self.ui.tableAsset.setColumnWidth(1, 200)
        self.ui.tableAsset.setColumnWidth(2, 100)
        self.ui.tableAsset.setColumnWidth(3, 200)
        self.ui.tableAsset.setColumnWidth(4, 100)
        self.ui.tableAsset.setColumnWidth(5, 100)
        self.ui.tableAsset.setColumnWidth(6, 100)
        
        self.search_stock_category()
        self.update_client_btn()
        # ban(self)
        self.supplierload()
        self.addstock2()
        self.delete_uom_btn()
        self.delete_tx_btn()
        self.delete_ledger_btn()
        # self.receipt()
        self.Netprofit_Margin()
        self.Margin()
        self.prof_edit()
        self.ui.lineEdit_20.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_36.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_34.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_35.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_4.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_32.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_17.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_24.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_3.setValidator(QtGui.QIntValidator())
        self.onlyInt = QIntValidator()
        # self.ui.lineEdit_12.setValidator(self.onlyInt)
        self.ui.lineEdit_5.setValidator(self.onlyInt)
        self.ui.lineEdit_19.setValidator(self.onlyInt)
        self.ui.lineEdit_31.setValidator(QtGui.QIntValidator())
        # sself.ui.lineEdit_18.setValidator(self.onlyInt)
        self.total_income()
        self.s_c = QShortcut(QKeySequence('ctrl+Q'), self)
        self.s_c.activated.connect(self.act)
        self.poslist = []
        # print(orders_function.total_cogs.__annotations__)
        self.kshpos = []
        self.itempos = []
        self.point_OS = {}
        hrms.load_positions_hrms(self)
        hrms.load_employee_hrms(self)
        self.update_employee_btn()
        self.search_orders()
        self.prev()
        self.search_client_btn()
        self.search_ledger_btn()
        self.search_bills_btn()
        self.search_purchase_orders_btn()
        self.payment_reload()
        self.capital_employed()
        self.scroll()
        self.unlock_bill_ledger_btn()
        self.add_journalentry_btn()
        self.sum_fix_exp()
        self.sum_var_exp()
        self.total_liability()
        self.sum_long_term()
        self.sum_short_term()
        self.sumCurrent_asset()
        self.total_expenses()
        self.sumfixed_asset()
        self.total_asset()
        self.coa_load()
        self.gross_profit()
        self.net_profit()
        self.sales_repo()
        self.sales_btn()
        self.load_ledgers()
        self.addrow()
        self.pay_supplier_button()
        self.working_capital()
        self.debt_ratio()
        self.current_ratio()
        self.total_sales()
        self.add_bill_items_btn()
        self.bill_detail_update_btn()
        self.uppdate_purchase_order_page_btn()
        self.insert_purchase_order_items_btn()
        bills.Bill.bill_load_table(self)
        self.create_bill_from_purchase_order_btn()
        self.update_department_btn()
        # self.openbtn()
        self.export_inv()
        orders_function.total_orders(self)
        orders_function.total_cogs(self)
        
        PurchaseOrder.purchase_order_load_table(self)
        self.update_bill_btn()
        self.pay_bill_btn()
        self.unlock_invoice_ledger_btn()
        self.uppdate_purchase_order_btn()
        # self.Quantity()
        
        # self.s_t()
        self.pos_details()
        self.most_sold_table()
        charts.create_bar(self)
        charts.create_bar2(self)
        self.autocompleter()
        # self.company_name()
        self.invoice_ledger_btn()
        # self.addbtnstock()
        self.auto2()
        self.search_stock_category()
        self.pos_line()
        self.load_supplier_button()
        # self.reset_postable_button()
        self.sales_ret_btn()
        self.bill_journal_entriesr_btn()
        payment.add_coa(self)
        self.coa()
        self.search_sup_btn()
        self.update_transactions_btn()
        self.update_coa_btn()
        self.gr_repobtn()
        self.combo()
        self.reoder_limit()
        self.profit_lossbtn()
        self.po_details_page_btn()
        self.sales_returns_journal_entries_button()
        self.recip_detail()
        # self.receiptload()
        self.keystroke()
        self.save_payment_btn()
        self.add_ledger_btn()
        self.update_supplier_btn()
        self.update_uom_btn()
        self.lock_invoice_ledger_btn()
        # self.sales()
        self.stock_report_btn()
        self.stock_btn()
        self.return_order_btn()
        self.update1()
        self.taxset()
        self.department_btn()
        self.user_managment_btn()
        self.back_ledgers_btn()
        self.reset_solditems_postable()
        self.image_path = []
        self.balance_button()
        self.lock_bill_ledger_btn()
        orders_function.setButtons2(self)
        orders_function.auto_completer(self)
        Table_resizeing.resize_tables(self)
        orders_function.orders_label(self)
        orders_function.items_worth(self)
        orders_function.total_stock(self)
        payment.combo_payments(self)
        hrms.load_department_hrms(self)
        admin.load_user_managment(self)
        uom.load_uom(self)
        self.tx_back_btn()
        #self.ledger_id = []

        self.delete_pos_tb()
        self.jouranal_add_transaction_btn()
        charts.pie(self)
        charts.pie2(self)
        # imageconversion.select_image(self)
        self.combo_pay()
        self.update_order_btn()
        self.update_ledger_btn()
        self.inventory()
        self.order_btn()
        self.ui.comboBox_4.addItems(["cash", "cheque", "credit card"])
        self.ui.comboBox_5.addItems(["Fully paid", "Installments", "Not Paid"])
        self.ui.comboBox_49.addItems(["cash", "cheque", "credit card"])
        self.ui.comboBox_51.addItems(["Fully paid", "Installments", "Not Paid"])
        self.export_table_orders_btn()
        self.refersh_everything()
        self.clientbtn()
        self.income()
        self.debt_percentage()
        self.add_po_btn()
        self.add_bill_btn()
        self.setcombos_bill_update()
        self.bill_ledger_btn()
        self.add_position_btn()
        self.add_employee_btn()
        self.add_uom_btn()
        self.update_position_btn()
        print("user_UUID###########", str(who_is_logged[1]))
        # EXTRA LEFT BOX

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        self.ui.toggleLeftBox.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_10))
        # self.ui.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        self.ui.settingsTopBtn.clicked.connect(openCloseRightBox)
        
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes/py_dracula_dark.qss"
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        # self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(
            UIFunctions.selectMenu(
                self.ui.btn_home.styleSheet()))
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def logged_in_user(self):
        if who_is_logged[0] == "admin":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            print("is admin")
        elif who_is_logged[0] == "Accounts":
            print("::::::::::::::::::::::kkkkkkkk", who_is_logged[0])
            
            self.ui.leftMenuBg.setMinimumSize(QSize(0, 0))
            self.ui.leftMenuBg.setMaximumSize(QSize(0, 16777215))
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        elif who_is_logged[0] == "POS":
            self.ui.leftMenuBg.setMinimumSize(QSize(0, 0))
            self.ui.leftMenuBg.setMaximumSize(QSize(0, 16777215))
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        elif who_is_logged[0] == "Inventory":
            self.ui.leftMenuBg.setMinimumSize(QSize(0, 0))
            self.ui.leftMenuBg.setMaximumSize(QSize(0, 16777215))
            self.ui.stackedWidget.setCurrentWidget(self.ui.pagesContainer)
        elif who_is_logged[0] == "CRM":
            self.ui.leftMenuBg.setMinimumSize(QSize(0, 0))
            self.ui.leftMenuBg.setMaximumSize(QSize(0, 16777215))
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        elif who_is_logged[0] == "HR":
            self.ui.leftMenuBg.setMinimumSize(QSize(0, 0))
            self.ui.leftMenuBg.setMaximumSize(QSize(0, 16777215))
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_44)
    def company_name(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        v = cusr.execute("SELECT business_name FROM recip_detail").fetchone()
        v = (''.join(map(str, v)))
        labels = [
            self.ui.label_82,
            self.ui.label_101,
            self.ui.label_175,
            self.ui.label_184,
            self.ui.label_187,
            self.ui.label_191,
            self.ui.label_146]
        for i in labels:
            i.setText(str(v))
            i.setFont(QFont("Times", 20))
            i.setStyleSheet("QLabel { color : rgb(203, 203, 203); }")

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName == "btn_widgets_2":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_15)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_9)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW NEW PAGE
        if btnName == "btn_new":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.new_page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
        if btnName == "btn_save":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
        if btnName == "btn_exit":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU

        if btnName == "client_btn_2":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)  # SET PAGE
            self.clientdata()
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
        if btnName == "pushButton":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
        if btnName == "pushButton_37":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_30)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
        if btnName == "pushButton_17":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_11)  # SET PAGE
        if btnName == "pushButton_149":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_57)  # SET PAGE
        if btnName == "pushButton_63":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_2)  # SET PAGE
        if btnName == "pushButton_158":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_58)  # SET PAGE
        if btnName == "pushButton_131":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_2)  # SET PAGE
        if btnName == "pushButton_122":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_33)  # SET PAGE
        if btnName == "pushButton_52":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_32)  # SET PAGE
        if btnName == "pushButton_99":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_2)  # SET PAGE
        if btnName == "pushButton_8":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_19)  # SET PAGE
        if btnName == "pushButton_19":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_25)  # SET PAGE
        if btnName == "pushButton_28":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_24)  # SET PAGE
        if btnName == "pushButton_29":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_12)  # SET PAGE
        if btnName == "pushButton_3":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_23)  # SET PAGE
        if btnName == "pushButton_30":
            self.ui.stackedWidget_2.setCurrentWidget(
                self.ui.page_22)  # SET PAGE
        if btnName == "pushButton_129":
            Entrance()
        if btnName == "btn_logout":
            self.logout_dialog() # SET PAGE

    def reset_btns_docs(self):
        list_btn = []
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////

    def update_clients(self):
        pass

    def set_update_company_profile(self):
        # try:
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        var_y = cusr.execute(
            "SELECT business_name FROM recip_detail").fetchone()
        var_y = (''.join(map(str, var_y)))
        self.ui.lineEdit_40.setText((var_y))
        var_t = cusr.execute("SELECT pobox FROM recip_detail ").fetchone()
        var_t = (''.join(map(str, var_t)))
        self.ui.lineEdit_41.setText((var_t))
        var_y = cusr.execute("SELECT contact FROM recip_detail").fetchone()
        var_y = (''.join(map(str, var_y)))
        self.ui.lineEdit_42.setText((var_y))
        var_y = cusr.execute("SELECT email FROM recip_detail").fetchone()
        var_y = (''.join(map(str, var_y)))
        self.ui.lineEdit_43.setText((var_y))
        var_y = cusr.execute(
            "SELECT street_address FROM recip_detail").fetchone()
        var_y = (''.join(map(str, var_y)))
        self.ui.lineEdit_27.setText((var_y))
        notes = cusr.execute("SELECT notes FROM recip_detail").fetchone()
        notes = (''.join(map(str, notes)))
        self.ui.plainTextEdit.insertPlainText(notes)
        foot = cusr.execute("SELECT footer FROM recip_detail").fetchone()
        foot = (''.join(map(str, foot)))
        self.ui.plainTextEdit_2.insertPlainText(foot)
        # except Exception:
        #QMessageBox.warning(QMessageBox(), 'Error', 'an error has occured.')

    def update_company_profile(self):
        try:
            bizname = self.ui.lineEdit_4.text()
            pobox = self.ui.lineEdit.text()
            num = self.ui.lineEdit_2.text()
            other = self.ui.lineEdit_3.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE recip_detail SET business_name=?", (bizname,))
            cusr.execute("UPDATE recip_detail SET pobox=?", (pobox,))
            cusr.execute("UPDATE recip_detail SET contact=?", (num,))
            cusr.execute("UPDATE recip_detail SET other=?", (other,))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'current liability is edited successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not edit.')

    def inventory_purchase_reload(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM Purchase"
        result = database_connection.execute(query).fetchall()
        print(result)
        self.ui.tableWidget_18.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_18.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_18.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def total_income(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            res = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=? AND tx_type=?", ("revenue", "credit")).fetchone()
            res = (''.join(map(str, res)))
            if res == str(None):
                res = 0.0
            else:
                res = float(''.join(map(str, res)))
            items = babel.numbers.format_currency(
                decimal.Decimal(res), cash_label, locale='en_US')
            print(items, " ===============")
            self.ui.label_194.setText(str(items))
            self.ui.label_194.setFont(QFont("Times", 26))
            self.ui.label_194.setStyleSheet(
                "QLabel { color : rgb(203, 203, 203); }")
        except Exception:
            print("labels income")

    def openbtn(self):
        self.ui.pushButton_43.clicked.connect(self.openimage)



    def coa(self):
        self.ui.pushButton_75.clicked.connect(self.chart_of_acc)

    def inventory(self):
        self.ui.pushButton_41.clicked.connect(self.purchase)

    def supplierload(self):
        self.ui.pushButton_70.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_21))
        orders_function.setButtons_suppliers(self)

    def pay_supplier_button(self):
        self.ui.pushButton_72.clicked.connect(self.pay_supplier)
    def sales_returns_journal_entries_button(self):
        self.ui.pushButton_48.clicked.connect(self.sales_returns_journal_entries)

    def pay_supplier(self):
        payment.supllier_payment(self)

    def purchase(self):
        payment.purchase_order_payment(self)
        self.inventory_purchase_reload()

    def profit_lossbtn(self):
        self.ui.pushButton_9.clicked.connect(self.profit_loss)
    def po_details_page_btn(self):
        self.ui.pushButton_77.clicked.connect(self.details_page)

    def gr_repobtn(self):
        self.ui.pushButton_57.clicked.connect(self.gr_repo)

    def gr_repo(self):
        print('its working transactions==================================')
        accounts.general_report(self)

    def load_supplier_button(self):
        self.ui.lib_btn4_7.clicked.connect(self.load_suplier)

    def refersh_everything(self):
        self.ui.pushButton_26.clicked.connect(self.refresh_all)

    def refresh_all(self):
        refresh_dashboard.refreshdashboard(self)

    def balance_button(self):
        self.ui.pushButton_45.clicked.connect(self.balance_sheet)

    def order_btn(self):
        self.ui.pushButton_58.clicked.connect(self.order_repo)

    def sales_repo(self):
        self.ui.pushButton_56.clicked.connect(self.sale_rep)

    def sales_btn(self):
        self.ui.pushButton_60.clicked.connect(self.sales_print)

    def stock_report_btn(self):
        self.ui.pushButton_34.clicked.connect(self.stock_report)
    def department_btn(self):
        self.ui.pushButton_128.clicked.connect(self.add_department)
    def user_managment_btn(self):
        self.ui.pushButton_143.clicked.connect(self.user_managment)

    def stock_btn(self):
        pass
        # self.ui.pushButton_59.clicked.connect(self.stock_print)

    def sales_ret_btn(self):
        self.ui.pushButton_42.clicked.connect(self.sales_return_repo)
    def add_position_btn(self):
        self.ui.pushButton_132.clicked.connect(self.add_position)
    def add_uom_btn(self):
        self.ui.pushButton_150.clicked.connect(self.add_uom)
    def add_employee_btn(self):
        self.ui.pushButton_133.clicked.connect(self.add_employee)

    def export_table_orders_btn(self):
        self.ui.pushButton_62.clicked.connect(self.export_table_order)

    def sales_return_repo(self):
        accounts.salereturns_report(self)

    def profit_loss(self):
        accounts.profit_loss_account(self)

    def order_repo(self):
        accounts.orrders_report(self)

    def sale_rep(self):
        accounts.sales_reports(self)

    def sales_print(self):
        accounts.export_table_sales(self)

    def export_table_order(self):
        accounts.export_table_orders(self)

    def stock_report(self):
        accounts.stock_reports(self)

    def onClicked(self):
        self.webEngineView.page().printToPdf('myfile2345.pdf')
        QMessageBox.information(self, 'info', 'page exported')

    def openimage(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.svg)")
        imagepath = fname[0]
        self.image_path.append(imagepath)
        print(imagepath)
        pix = QPixmap(imagepath)
        self.ui.label_174.setPixmap(QPixmap(pix))
        self.ui.label_174.setScaledContents(True)
        return imagepath

    def insert_company_details(self):
        imageconversion.insertBLOB(self)

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////

    def scroll(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        alltb = cusr.execute(
            "SELECT code, client_name, due FROM orders ORDER BY id_13 DESC LIMIT 10")
        # Widget that contains the collection of Vertical Box
        self.widget = QWidget()
        # The Vertical Box that contains the Horizontal Boxes of  labels and
        # buttons
        self.vbox = QVBoxLayout()
        print("its")
        for vbn, c_name, due2 in (alltb):
            vbn = (''.join(map(str, vbn)))
            due2 = babel.numbers.format_currency(
                decimal.Decimal(due2), cash_label, locale='en_US')
            object = QLabel(
                "<html><head/><body><p><span style=\" font-size:18pt; font-weight:630; color:#00db00;\">{vbn}</span></p><p><span style=\" font-size:13pt; font-weight:600; color:#f0f0f0;\">{c_name}</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\"> {due2}</span></p></body></html>".format(
                    vbn=vbn,
                    c_name=c_name,
                    due2=due2),
                None)
            object.setStyleSheet("QLabel{\n"
                                 "    background-color: rgb(83, 83, 83);;\n"
                                 "color : rgb(7, 7, 7); \n"
                                 "}")
            object.setFixedSize(370, 100)
            object.setAlignment(QtCore.Qt.AlignLeft)
            self.vbox.addWidget(object)
        self.widget.setLayout(self.vbox)
        # Scroll Area Properties
        # self.ui.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.ui.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollArea.setWidget(self.widget)
        self.show()
        return

    def combo_pay(self):
        self.ui.pushButton_40.clicked.connect(self.paying)

    def payment_reload(self):
        self.ui.pushButton_35.clicked.connect(self.paying2)
    
        
    def load_ledgers(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT lg_id, name, ledger_date FROM ledgers ORDER BY id DESC"
        result = database_connection.execute(query).fetchall()

        self.ui.tableWidget_25.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_25.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_25.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                rtn = QPushButton("Details")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                rtn.setFont(font)
                rtn.setStyleSheet(u"QPushButton{\n"
                                "\n"
                                "border-radius : 20px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(85, 170, 255);\n"
                                "}")
                edit = QPushButton("Edit")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                edit.setFont(font)
                edit.setStyleSheet(u"QPushButton{\n"
                                "\n"
                                "border-radius : 20px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "	background-color: rgb(85, 170, 255);\n"
                                "}")
                self.ui.tableWidget_25.setCellWidget(row_number, 4, rtn)
                self.ui.tableWidget_25.setCellWidget(row_number, 3, edit)
                rtn.clicked.connect(self.all_journal_entries)
                edit.clicked.connect(self.set_ledger_update_page)
    def back_ledgers_btn(self):
        self.ui.pushButton_52.clicked.connect(self.back_ledgers)

    def back_ledgers(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_32)
        ledger_id.clear()

    def jouranal_add_transaction_btn(self):
        self.ui.pushButton_121.clicked.connect(self.jouranal_add_transaction)
        

    def load_tx(self):
        row = self.ui.tableWidget_26.currentRow()
        currentcode = (self.ui.tableWidget_26.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        TableQt.loadtable_query(
            tablename = self.ui.tableWidget_37,
            column_num = [4], 
            funccalled = [self.tx_update_page], 
            sqlquery = "SELECT id_4, name, tx_type, KSH, description FROM transactions WHERE journal_entry_id=?",
            btn_name = ["update"],
            query_var = currentcode
            )

    def all_journal_entries(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_25.currentRow()
        currentcode = (self.ui.tableWidget_25.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        b = cusr.execute('SELECT id FROM ledgers WHERE lg_id=?', (currentcode,)).fetchone()
        b = (''.join(map(str, b)))
        # self.ledger_id.append(b)
        ledger_id.append(b)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_33)
        result = database_connection.execute("SELECT id, description, journal_entrydate, activity  FROM journal_entries WHERE ledger_id=?", (b,)).fetchall()

        self.ui.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_26.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("TXS")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                "    background-color: rgb(0, 255, 0);;\n"
                                "border-radius : 25px;\n"
                                "color : rgb(7, 7, 7); \n"
                                "}")
                self.ui.tableWidget_26.setCellWidget(row_number, 4, btn)
                btn.clicked.connect(self.jouranal_entry_transaction)
    def sales_returns_journal_entries(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()

        currentcode = str(self.ui.lineEdit_28.text())
        b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
        b = (''.join(map(str, b)))
        # self.ledger_id.append(b)
        ledger_id.append(b)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_33)
        result = database_connection.execute("SELECT id, description, journal_entrydate, activity  FROM journal_entries WHERE ledger_id=?", (b,)).fetchall()

        self.ui.tableWidget_26.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_26.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_26.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("TXS")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                "    background-color: rgb(0, 255, 0);;\n"
                                "border-radius : 25px;\n"
                                "color : rgb(7, 7, 7); \n"
                                "}")
                self.ui.tableWidget_26.setCellWidget(row_number, 4, btn)
                btn.clicked.connect(self.jouranal_entry_transaction)


    def jouranal_entry_transaction(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_43)
        try:
            row = self.ui.tableWidget_26.currentRow()
            currentcode = (self.ui.tableWidget_26.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            query = "SELECT id_4, name, tx_type, KSH, description FROM transactions WHERE journal_entry_id=?"
            result = cusr.execute(query, (currentcode,)).fetchall()
            self.ui.tableWidget_37.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_37.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_37.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
                    btn = QPushButton("Edit")
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)
                    # font.setWeight(75)
                    btn.setFont(font)
                    btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: rgb(0, 255, 0);;\n"
                                    "border-radius : 25px;\n"
                                    "color : rgb(7, 7, 7); \n"
                                    "}")
                    icon5 = QIcon()
                    icon5.addFile(
                        u":/icons/images/icons/cil-pen-alt.png",
                        QSize(),
                        QIcon.Normal,
                        QIcon.Off)
                    btn.setIcon(icon5)
                    btn.setIconSize(QSize(40, 40))
                    self.ui.tableWidget_37.setCellWidget(row_number, 5, btn)
                    btn.clicked.connect(self.update_tx_page)
        except Exception:
            print("transactions loading")

    def jouranal_add_transaction(self):
        try:
            database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_26.currentRow()
            currentcode = (self.ui.tableWidget_26.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            updated = dt.today()
            created = dt.today()
            transactionsdate = date.today()

            coa_acc = str(self.ui.comboBox_22.currentText())
            coa_id = cusr.execute("SELECT role FROM chart_of_accounts WHERE account=?", (coa_acc,)).fetchone()
            ledger_id = cusr.execute("SELECT ledger_id FROM journal_entries WHERE id=?", (currentcode,)).fetchone()
            coa_id = (''.join(map(str, coa_id)))
            ledger_id = (''.join(map(str, ledger_id)))

            tx_type = str(self.ui.comboBox_23.currentText())
            uuid1 = uuid.uuid4().hex

            name = str(self.ui.lineEdit_63.text())
            amount =  float(str(self.ui.lineEdit_16.text()))
            cusr.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                ((uuid1,
                updated,
                created,
                coa_id,
                currentcode,
                ledger_id,
                coa_acc,
                amount,
                name,
                tx_type,
                transactionsdate)))
            database_connection.commit()
            QMessageBox.information(QMessageBox(),'Successfull', "Transaction added Successfully")
            self.jouranal_entry_transaction()
        except Exception:
            print(Exception)
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add transaction.')

    def paying2(self):
        payment.ledger_load(self)

    def paying(self):
        payment.automatic_acc(self)
        payment.ledger_load(self)

    def set_return_orders(self):
        cash_label = str(self.ui.comboBox_8.currentText())
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_20)
        row = self.ui.tableWidget_6.currentRow()
        currentcode = (self.ui.tableWidget_6.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        sale_no = cusr.execute(
            "SELECT sale_no FROM orders WHERE code=?", (currentcode,)).fetchone()
        sale_no = (''.join(map(str, sale_no)))
        print('this is the sale number', sale_no)
        result = cusr.execute(
            "SELECT name , Quantity, KSH, sale_date FROM sales WHERE sale_no=?",
            (sale_no,
             )).fetchall()
        print(result)
        self.ui.tableWidget_15.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_15.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_15.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("Return Item")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet(u"QPushButton{\n"
                                  "\n"
                                  "border-radius : 20px;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(85, 170, 255);\n"
                                  "}")
                btn.clicked.connect(self.sales_return_page)
                self.ui.tableWidget_15.setCellWidget(row_number, 4, btn)
        c_n = cusr.execute(
            "SELECT client_name FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        c_n = (''.join(map(str, c_n)))
        p_a = cusr.execute(
            "SELECT paid_amount FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        p_a = float(''.join(map(str, p_a)))
        c_d = cusr.execute(
            "SELECT code FROM orders WHERE code=? ", (currentcode,)).fetchone()
        c_d = (''.join(map(str, c_d)))
        d_t = cusr.execute(
            "SELECT discount FROM orders WHERE code=? ", (currentcode,)).fetchone()
        d_t = float(''.join(map(str, d_t)))
        g_t = cusr.execute(
            "SELECT grand_total FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        g_t = float(''.join(map(str, g_t)))
        t_a = cusr.execute(
            "SELECT total_amount FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        t_a = float(''.join(map(str, t_a)))
        p_t = cusr.execute(
            "SELECT payment_type FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        p_t = (''.join(map(str, p_t)))
        o_d = cusr.execute(
            "SELECT order_date FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        o_d = (''.join(map(str, o_d)))
        d_u = cusr.execute(
            "SELECT due FROM orders WHERE code=? ", (currentcode,)).fetchone()
        d_u = float(''.join(map(str, d_u)))
        s_b = cusr.execute(
            "SELECT sub_total FROM orders WHERE code=? ", (currentcode,)).fetchone()
        s_b = float(''.join(map(str, s_b)))
        p_s = cusr.execute(
            "SELECT payment_status FROM orders WHERE code=? ",
            (currentcode,
             )).fetchone()
        p_s = (''.join(map(str, p_s)))
        tel = cusr.execute(
            "SELECT telno FROM clients WHERE name=? ", (c_n,)).fetchone()
        tel = (''.join(map(str, tel)))
        addr = cusr.execute(
            "SELECT address FROM clients WHERE name=? ", (c_n,)).fetchone()
        addr = (''.join(map(str, addr)))
        e_addr = cusr.execute(
            "SELECT email FROM clients WHERE name=? ", (c_n,)).fetchone()
        e_addr = (''.join(map(str, e_addr)))
        t_a_k = babel.numbers.format_currency(decimal.Decimal(t_a), cash_label)
        s_b_k = babel.numbers.format_currency(decimal.Decimal(s_b), cash_label)
        d_u_k = babel.numbers.format_currency(decimal.Decimal(d_u), cash_label)
        g_t_k = babel.numbers.format_currency(decimal.Decimal(g_t), cash_label)
        d_t_k = babel.numbers.format_currency(decimal.Decimal(d_t), cash_label)
        self.ui.label_148.setText(str(c_n))
        self.ui.label_157.setText(str(d_u_k))
        self.ui.label_159.setText(str(p_t))
        self.ui.label_166.setText(str(g_t_k))
        self.ui.label_166.setStyleSheet(
            "QLabel { color : rgb(0, 170, 0); }")
        self.ui.label_167.setText(str(s_b_k))
        self.ui.label_167.setStyleSheet(
            "QLabel { color : rgb(0, 170, 0); }")
        self.ui.label_168.setText(str(t_a_k))
        self.ui.label_168.setStyleSheet(
            "QLabel { color : rgb(0, 170, 0); }")
        self.ui.label_169.setText(str(d_t_k))
        self.ui.label_169.setStyleSheet(
            "QLabel { color : rgb(0, 170, 0); }")
        self.ui.label_160.setText(str(o_d))
        self.ui.label_152.setText(str(addr))
        self.ui.label_153.setText(str(tel))
        self.ui.label_154.setText(str(e_addr))
        # var_y = (''.join(map(str, var_y)))
        self.ui.lineEdit_28.setText((currentcode))

    def sales_return_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_8)
        row = self.ui.tableWidget_15.currentRow()
        currentcode = (self.ui.tableWidget_15.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        currentcode2 = (self.ui.tableWidget_15.item(row, 1).text())
        currentcode2 = (''.join(map(str, currentcode2)))
        self.ui.lineEdit_29.setText((currentcode))
        self.ui.lineEdit_31.setText((currentcode2))
    def delete_uom_btn(self):
        self.ui.pushButton_160.clicked.connect(self.delete_uom)
    def delete_tx_btn(self):
        self.ui.pushButton_164.clicked.connect(self.delete_tx)
    def delete_ledger_btn(self):
        self.ui.pushButton_169.clicked.connect(self.delete_ledger)


    def delete_uom(self):
        row = self.ui.tableWidget_42.currentRow()
        currentcode = (self.ui.tableWidget_42.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from uom WHERE uom_id=?", (currentcode,))
        database_connection.commit()
        uom.load_uom(self)
        self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_57)
        cusr.close()
        database_connection.close()
    def delete_purchase_order(self):
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        row2 = self.ui.tableWidget_29.currentRow()
        currentcode2 = (self.ui.tableWidget_29.item(row2, 1).text())
        currentcode2 = (''.join(map(str, currentcode2)))

        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from purchase_order_items WHERE purchase_order_uuid=? AND po_items_id=?", (currentcode, currentcode2))
        database_connection.commit()
        PurchaseOrder.purchase_order_items_load_table(self)
        cusr.close()
        database_connection.close()


    def delete_ledger(self):
        row = self.ui.tableWidget_25.currentRow()
        currentcode = (self.ui.tableWidget_25.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from ledgers WHERE lg_id=?", (currentcode,))
        database_connection.commit()
        self.load_ledgers()
        self.ui.stackedWidget.setCurrentWidget(
                self.ui.page_62)
        cusr.close()
        database_connection.close()
    def delete_tx(self):
        try:
            currentcode = jr_id_lst[1]
            print("this is currentcode", currentcode)
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("DELETE from transactions WHERE id_4=?", (currentcode,))
            database_connection.commit()
            uom.load_uom(self)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_60)
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'deleted transaction.')
        except Exception:
            print("deleted trans")


    def delete_supplier(self):
        row = self.ui.tableWidget_14.currentRow()
        currentcode = (self.ui.tableWidget_14.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from supplier WHERE id_14=?", (currentcode,))
        database_connection.commit()
        orders_function.setButtons_suppliers(self)
        cusr.close()
        database_connection.close()

    def delete_client(self):
        row = self.ui.tableWidget_11.currentRow()
        currentcode = (self.ui.tableWidget_11.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE from clients WHERE id_10=?", (currentcode,))
        database_connection.commit()
        self.clientdata()
        cusr.close()
        database_connection.close()

    def coa_load(self):
        """loads all list of accounts to table chart_of_accounts_tb and setting details button 
        to the table
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT code, role, account, balance_type FROM chart_of_accounts"
        result = database_connection.execute(query).fetchall()
        self.ui.chart_of_accounts_tb.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.chart_of_accounts_tb.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.chart_of_accounts_tb.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
                details_btn = QPushButton("Details")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                details_btn.setFont(font)
                details_btn.setStyleSheet(u"QPushButton{\n"
                              "\n"
                              "border-radius : 20px;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(85, 170, 255);\n"
                              "}")
                
                edit_btn = QPushButton()
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                edit_btn.setFont(font)
                edit_btn.setStyleSheet(u"QPushButton{\n"
                              "\n"
                              "border-radius : 20px;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(85, 170, 255);\n"
                              "}")
                icon5 = QIcon()
                icon5.addFile(
                    u":/icons/images/icons/cil-pen-alt.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                edit_btn.setIcon(icon5)
                edit_btn.setIconSize(QSize(40, 40))
                self.ui.chart_of_accounts_tb.setCellWidget(row_number, 4, details_btn)
                self.ui.chart_of_accounts_tb.setCellWidget(row_number, 5, edit_btn)
                details_btn.clicked.connect(self.account_trans_list_report)
                edit_btn.clicked.connect(self.update_coa_page)


    def account_trans_list_report(self):
        """when the details button in is clicked this fuction is invoked returning all 
        transaction associated with that account
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_31)
        row = self.ui.chart_of_accounts_tb.currentRow()
        currentcode = (self.ui.chart_of_accounts_tb.item(row, 0).text()) # get the text or data of the first cell in the current row
        currentcode = (''.join(map(str, currentcode)))
        row = self.ui.chart_of_accounts_tb.currentRow()
        currentcode3 = (self.ui.chart_of_accounts_tb.item(row, 2).text()) # get the text or data of the first cell in the current row
        currentcode3 = (''.join(map(str, currentcode3)))

        currentcode2 = (self.ui.chart_of_accounts_tb.item(row, 1).text()) # get the text or data of the first cell in the current row
        currentcode2 = (''.join(map(str, currentcode2)))
        account_name = database_connection.execute("SELECT account from chart_of_accounts WHERE code=?", (currentcode,)).fetchone()
        account_name = (''.join(map(str, account_name)))
        self.ui.label_21.setText(str(currentcode + ":" + account_name))
        self.ui.label_21.setFont(QFont("Times", 23))
        self.ui.label_21.setAlignment(QtCore.Qt.AlignCenter)
        
        result = database_connection.execute("SELECT coa_id, tx_type, KSH, description FROM transactions WHERE coa_id=? AND name=?", (currentcode2, currentcode3,)).fetchall()
        self.ui.tableWidget_24.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_24.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_24.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))


    def update_orders_page(self):
        invoice_id.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_17)
        self.ui.lineEdit_3.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_19.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_31.setValidator(QtGui.QIntValidator())
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_6.currentRow()
        currentcode = (self.ui.tableWidget_6.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        invoice_id.append(currentcode)
        print('this is the order number code', currentcode)
        print("this is currentcode", currentcode)
        d = "discount"
        column_list = [
            d,
            "client_name",
            "grand_total",
            "total_amount",
            "sub_total",
            "order_date ",
            "due"]
        column_list2 = [
            "payment_type",
            "payment_status",
            "terms",
            "invoice_status"
        ]
        line_edits = [
            self.ui.lineEdit_4,
            self.ui.lineEdit_2,
            self.ui.lineEdit_3,
            self.ui.lineEdit_5,
            self.ui.lineEdit_19,
            self.ui.lineEdit_24,
            self.ui.lineEdit_25]
        combos = [
            self.ui.comboBox_49,
            self.ui.comboBox_51,
            self.ui.comboBox_20,
            self.ui.comboBox_21
            ]
        for col, edits in zip(column_list, line_edits):
            print(col)
            var_y = cusr.execute(
                "SELECT %s FROM orders WHERE code=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            print(var_y)
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
        for col, combo in zip(column_list2, combos):
            var_t = cusr.execute(
                "SELECT %s FROM orders WHERE code=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            combo.setCurrentText(var_t)

    def update_supplier_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_26)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_14.currentRow()
        currentcode = (self.ui.tableWidget_14.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        column_list = [
                "name",
                "tel1",
                "tel2",
                "email",
                "addr1",
                "addr2",
                "site",
                "country"]
        line_edits = [
            self.ui.lineEdit_46,
            self.ui.lineEdit_47,
            self.ui.lineEdit_48,
            self.ui.lineEdit_49,
            self.ui.lineEdit_50,
            self.ui.lineEdit_51,
            self.ui.lineEdit_90,
            self.ui.lineEdit_91
            ]
        for col, edits in zip(column_list, line_edits):
            var_y = cusr.execute(
                "SELECT %s FROM supplier WHERE id_14=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))

    def update_client_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_29)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_11.currentRow()
        currentcode = (self.ui.tableWidget_11.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        column_list = ["name", "telno", "address", "email", "date", "balance"]
        line_edits = [
            self.ui.lineEdit_56,
            self.ui.lineEdit_55,
            self.ui.lineEdit_54,
            self.ui.lineEdit_52,
            self.ui.lineEdit_53,
            self.ui.lineEdit_57]
        for col, edits in zip(column_list, line_edits):
            var_y = cusr.execute(
                "SELECT %s FROM clients WHERE id_10=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
    def update_tx_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_60)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_37.currentRow()
        currentcode = (self.ui.tableWidget_37.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        jr_id = cusr.execute("SELECT journal_entry_id FROM transactions WHERE id_4=?", (currentcode,)).fetchone()
        jr_id = (''.join(map(str, jr_id)))
        
        jr_id_lst.append(jr_id)
        jr_id_lst.append(currentcode)
        column_list = ["KSH", "description"]
        column_list2 = ["name", "tx_type"]
        line_edits = [
            self.ui.lineEdit_12,
            self.ui.lineEdit_15]
        combos = [
            self.ui.comboBox_46,
            self.ui.comboBox_47]
        for col, edits in zip(column_list, line_edits):
            var_y = cusr.execute(
                "SELECT %s FROM transactions WHERE id_4=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
        for col, combo in zip(column_list2, combos):
            var_t = cusr.execute(
                "SELECT %s FROM transactions WHERE id_4=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            combo.setCurrentText(var_t)
    def update_coa_page(self):
        self.ui.stackedwidget_3.setCurrentWidget(self.ui.debts_page_2)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.chart_of_accounts_tb.currentRow()
        currentcode = (self.ui.chart_of_accounts_tb.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        combo1 = cusr.execute("SELECT locked FROM chart_of_accounts WHERE code=?", (currentcode,)).fetchone()
        combo1 = (''.join(map(str, combo1)))
        combo2 = cusr.execute("SELECT active FROM chart_of_accounts WHERE code=?", (currentcode,)).fetchone()
        combo2 = (''.join(map(str, combo2)))
    
        if combo1 == "1":
            self.ui.checkBox_5.setChecked(True)
        else:
            self.ui.checkBox_2.setChecked(True)
        column_list = ["account", "code"]
        column_list2 = ["role", "balance_type"]
        line_edits = [
            self.ui.lineEdit_93,
            self.ui.lineEdit_92]
        combos = [
            self.ui.comboBox_48,
            self.ui.comboBox_50]
        for col, edits in zip(column_list, line_edits):
            var_y = cusr.execute(
                "SELECT %s FROM chart_of_accounts WHERE code=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
        for col, combo in zip(column_list2, combos):
            var_t = cusr.execute(
                "SELECT %s FROM chart_of_accounts WHERE code=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            combo.setCurrentText(var_t)
    

    def reloder_payment(self):
        row = self.ui.tableWidget_6.currentRow()
        currentcode = (self.ui.tableWidget_6.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        result = cusr.execute(
            "SELECT * FROM payment WHERE code=?", (currentcode,)).fetchall()
        self.ui.tableWidget_12.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_12.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def btn_triger(self):
        # orders_function.setButtons(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.reloder_payment()
        row = self.ui.tableWidget_6.currentRow()
        currentcode = (self.ui.tableWidget_6.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        result = cusr.execute(
            "SELECT * FROM payment WHERE code=?", (currentcode,)).fetchall()
        self.ui.tableWidget_12.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_12.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def supplier_payment_page(self):
        # orders_function.setButtons(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_27)
        row = self.ui.tableWidget_14.currentRow()
        currentcode = (self.ui.tableWidget_14.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        print("this is currentcode", currentcode)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        result = cusr.execute(
            "SELECT * FROM debt_payment WHERE code=?", (currentcode,)).fetchall()
        self.ui.tableWidget_23.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_23.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_23.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def load_suplier(self):
        orders_function.setButtons_suppliers(self)

    def clientbtn(self):
        self.ui.lib_btn4_5.clicked.connect(self.clientdata)

    def clientdata(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM clients"
        result = database_connection.execute(query)
        self.ui.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                push = QPushButton()
                push.setStyleSheet(u"QPushButton{\n"
                                   "\n"
                                   "border-radius : 20px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: rgb(85, 170, 255);\n"
                                   "}")
                icon5 = QIcon()
                icon5.addFile(
                    u":/icons/images/icons/cil-pen-alt.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                push.setIcon(icon5)
                push.setIconSize(QSize(40, 40))
                deletebtn = QPushButton()
                deletebtn.setStyleSheet(
                    u"QPushButton{\n"
                    "\n"
                    "border-radius : 20px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	background-color: rgb(85, 170, 255);\n"
                    "}")
                deletebtn = QPushButton()
                deletebtn.setStyleSheet(
                    u"QPushButton{\n"
                    "\n"
                    "border-radius : 20px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	background-color: rgb(85, 170, 255);\n"
                    "}")
                icon7 = QIcon()
                icon7.addFile(
                    u":/icons/images/icons/cil-remove.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                deletebtn.setIcon(icon7)
                deletebtn.setIconSize(QSize(40, 40))
                self.ui.tableWidget_11.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                self.ui.tableWidget_11.setCellWidget(row_number, 7, push)
                self.ui.tableWidget_11.setCellWidget(row_number, 8, deletebtn)
                push.clicked.connect(self.update_client_page)
                deletebtn.clicked.connect(self.delete_client)

    def balance_sheet(self):
        """calculates the balance sheet between certain date range
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        qdate = self.ui.dateEdit_13.date()
        order_date = qdate.toPython()
        qdate = self.ui.dateEdit_14.date()
        order_date2 = qdate.toPython()
        alltb = self.c.execute(
        "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2, "Sales Returns and Allowances")).fetchone()

        total_income = self.c.execute(
            "SELECT SUM(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
             order_date2, "revenue")).fetchone()
        total_income = float(''.join(map(str, total_income)))
        alltb = (''.join(map(str, alltb)))
        if alltb == str(None):
            alltb = 0
        else:
            alltb = float(''.join(map(str, alltb)))
        if total_income == str(None):
            total_income = 0
        else:
            paid = float(''.join(map(str, paid)))
        gross_profit = (total_income - alltb)
        total_revenue = (total_income)
        total_fix_expe = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2,
            "fixedexpenses"
            )).fetchone()
        total_fix_expe = float(''.join(map(str, total_fix_expe)))
        var_a = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2,
            "expenses"
            )).fetchone()
        var_a = float(''.join(map(str, var_a)))
        var_b = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2,
            "currentassets"
            )).fetchone()
        var_b = float(''.join(map(str, var_b)))
        var_l = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2,
            "fixedassets"
            )).fetchone()
        var_l = float(''.join(map(str, var_l)))
        var_d = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
            order_date2,
            "Longtermliabilities"
            )).fetchone()
        var_d = float(''.join(map(str, var_d)))
        var_e = cusr.execute(
            "SELECT sum(KSH) FROM transactions WHERE transactionsdate BETWEEN ? AND ? AND coa_id=?",
            (order_date,
             order_date2,
            "currentliabilities"
            )).fetchone()
        var_e = float(''.join(map(str, var_e)))
        total_assets = (var_b + var_l)
        total_lib = (var_d + var_e)
        total_expenses = (total_fix_expe + var_a)
        working_capital = (var_b - var_e)
        capital_employed = (var_l + working_capital)
        debt_ratio = (total_lib / total_assets)
        current_ratio = (var_b + var_e)
        net_profit = (total_revenue - total_expenses)
        var_sum1 = babel.numbers.format_currency(
            decimal.Decimal(total_fix_expe), cash_label, locale='en_US')
        self.ui.label_246.setText(str(var_sum1))
        self.ui.label_246.setFont(QFont("Times", 20))
        var_sum2 = babel.numbers.format_currency(
            decimal.Decimal(var_a), cash_label, locale='en_US')
        self.ui.label_247.setText(str(var_sum2))
        self.ui.label_247.setFont(QFont("Times", 20))
        var_sum3 = babel.numbers.format_currency(
            decimal.Decimal(total_assets), cash_label, locale='en_US')
        self.ui.label_213.setText(str(var_sum3))
        self.ui.label_213.setFont(QFont("Times", 20))
        var_sum4 = babel.numbers.format_currency(
            decimal.Decimal(total_lib), cash_label, locale='en_US')
        self.ui.label_244.setText(str(var_sum4))
        self.ui.label_244.setFont(QFont("Times", 20))
        var_sum5 = babel.numbers.format_currency(
            decimal.Decimal(total_expenses), cash_label, locale='en_US')
        self.ui.label_248.setText(str(var_sum5))
        self.ui.label_248.setFont(QFont("Times", 20))
        var_sum6 = babel.numbers.format_currency(
            decimal.Decimal(var_l), cash_label, locale='en_US')
        self.ui.label_214.setText(str(var_sum6))
        self.ui.label_214.setFont(QFont("Times", 20))
        var_sum7 = babel.numbers.format_currency(
            decimal.Decimal(var_e), cash_label, locale='en_US')
        self.ui.label_242.setText(str(var_sum7))
        self.ui.label_242.setFont(QFont("Times", 20))
        var_sum8 = babel.numbers.format_currency(
            decimal.Decimal(var_d), cash_label, locale='en_US')
        self.ui.label_243.setText(str(var_sum8))
        self.ui.label_243.setFont(QFont("Times", 20))
        var_sum9 = babel.numbers.format_currency(
            decimal.Decimal(gross_profit), cash_label, locale='en_US')
        self.ui.label_265.setText(str(var_sum9))
        self.ui.label_265.setFont(QFont("Times", 20))
        var_sum10 = babel.numbers.format_currency(
            decimal.Decimal(var_b), cash_label, locale='en_US')
        self.ui.label_217.setText(str(var_sum10))
        self.ui.label_217.setFont(QFont("Times", 20))
        var_sum11 = babel.numbers.format_currency(
            decimal.Decimal(working_capital), cash_label, locale='en_US')
        self.ui.label_264.setText(str(var_sum11))
        self.ui.label_264.setFont(QFont("Times", 20))
        var_sum12 = babel.numbers.format_currency(
            decimal.Decimal(capital_employed), cash_label, locale='en_US')
        self.ui.label_263.setText(str(var_sum12))
        self.ui.label_263.setFont(QFont("Times", 20))
        var_sum13 = babel.numbers.format_currency(
            decimal.Decimal(net_profit), cash_label, locale='en_US')
        self.ui.label_266.setText(str(var_sum13))
        self.ui.label_266.setFont(QFont("Times", 20))
        self.ui.label_270.setText(str(round(current_ratio)))
        self.ui.label_270.setFont(QFont("Times", 20))
        self.ui.label_271.setText(str(round(debt_ratio)))
        self.ui.label_271.setFont(QFont("Times", 20))
        print("this is", total_fix_expe)

    def kshposappend(self, b):
        self.kshpos.append(b)
        print(self.kshpos)

    def itemposappend(self, itemid):
        self.itempos.append(itemid)

    def posappend(self, itemid):
        """
        it appends the item UPC to the list so  it can be used to remove an itame from
        pos table
        """
        self.poslist.append(itemid)
        print(itemid)

    def __str__(self):
        return str(self.removefrompostable())

    def removefrompostable(self):
        """this fuction removes item from POS table when REMOVE button is clicked,
            when the remove button is clicked it shows its postion at the QTabelwidget
            by row which is an integer , this int will be used by th C variable to locate
            the item UPC from the POSLIST list where by the poslist contains items UPC (which are added using
            the pointofsale_addto_postable() fuction) so variable B is the index of the UPC in pos list
        """
        btn = self.sender()
        # index is the row of the btn where the signal is emited from pos table
        index = self.ui.tableWidget_16.indexAt(btn.pos())
        print(self.poslist)
        if index.isValid():
            b = int(index.row())
            print("this where the error is and this what", b)
            # c acts like the UPC for use in querying by using the poslist which contains
            # a list of item UPC
            c = self.poslist[b]
            print("this where the error is2", b)
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT Quantity FROM pos_table WHERE UPC=? ", (c,)).fetchone()
            var_y = float(''.join(map(str, var_y)))
            # main, it undo pointofsale_addto_postable() fuction i.e returns
            # back the item to stock bcoz its not sold
            cusr.execute(
                "UPDATE stock SET Quantity=(Quantity + ?) WHERE UPC=? ",
                (var_y,
                 c)).fetchone()
            cusr.execute("DELETE from pos_table WHERE UPC=?", (c,))
            database_connection.commit()
            # removes the UPC from poslist
            self.poslist.pop(b)
            self.load_postable_data()

    def tx_back_btn(self):
        self.ui.pushButton_163.clicked.connect(self.tx_back)
    def update_order_btn(self):
        self.ui.orders_update_btn.clicked.connect(self.update_orders)
    def update_ledger_btn(self):
        self.ui.pushButton_168.clicked.connect(self.update_ledger)

    def update_supplier_btn(self):
        self.ui.pushButton_79.clicked.connect(self.update_supplier)
    def update_uom_btn(self):
        self.ui.pushButton_159.clicked.connect(self.update_uom)

    def update_client_btn(self):
        self.ui.pushButton_81.clicked.connect(self.update_client)

    def update_bill_btn(self):
        self.ui.pushButton_110.clicked.connect(self.update_bill)
    def pay_bill_btn(self):
        self.ui.pushButton_78.clicked.connect(self.pay_bill)

    def add_bill_items_btn(self):
        self.ui.pushButton_109.clicked.connect(self.add_bill_items)

    def bill_ledger_btn(self):
        self.ui.pushButton_106.clicked.connect(self.post_bill_ledger)
    def invoice_ledger_btn(self):
        self.ui.pushButton_119.clicked.connect(self.post_invoice_ledger)
    def unlock_invoice_ledger_btn(self):
        self.ui.pushButton_118.clicked.connect(self.unlock_invoice_ledger)
    def lock_invoice_ledger_btn(self):
        self.ui.pushButton_120.clicked.connect(self.lock_invoice_ledger)

    def lock_bill_ledger_btn(self):
        self.ui.pushButton_107.clicked.connect(self.lock_bill_ledger)

    def unlock_bill_ledger_btn(self):
        self.ui.pushButton_108.clicked.connect(self.unlock_bill_ledger)

    def bill_journal_entriesr_btn(self):
        self.ui.pushButton_111.clicked.connect(self.bill_journal_entries)

    def bill_detail_update_btn(self):
        self.ui.pushButton_102.clicked.connect(self.bill_update_page)
    def uppdate_purchase_order_btn(self):
        self.ui.pushButton_114.clicked.connect(self.uppdate_purchase_order)
    def uppdate_purchase_order_page_btn(self):
        self.ui.pushButton_95.clicked.connect(self.uppdate_purchase_page_order)
    def insert_purchase_order_items_btn(self):
        self.ui.pushButton_116.clicked.connect(self.insert_purchase_order_items)
    def create_bill_from_purchase_order_btn(self):
        self.ui.pushButton_115.clicked.connect(self.create_bill_from_purchase_order)
    def update_employee_btn(self):
        self.ui.pushButton_134.clicked.connect(self.update_employee)
    def update_department_btn(self):
        self.ui.pushButton_136.clicked.connect(self.update_department)
    def update_transactions_btn(self):
        self.ui.pushButton_162.clicked.connect(self.update_transactions)
    def update_coa_btn(self):
        self.ui.pushButton_49.clicked.connect(self.update_coa)
    def update_position_btn(self):
        self.ui.pushButton_138.clicked.connect(self.update_position)

    def tx_back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_43)
        try:
            currentcode = jr_id_lst[0]
            database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            query = "SELECT id_4, name, tx_type, KSH, description FROM transactions WHERE journal_entry_id=?"
            result = cusr.execute(query, (currentcode,)).fetchall()
            jr_id_lst.clear()
            self.ui.tableWidget_37.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_37.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_37.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
                    btn = QPushButton("Edit")
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)
                    # font.setWeight(75)
                    btn.setFont(font)
                    btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: rgb(0, 255, 0);;\n"
                                    "border-radius : 25px;\n"
                                    "color : rgb(7, 7, 7); \n"
                                    "}")
                    icon5 = QIcon()
                    icon5.addFile(
                        u":/icons/images/icons/cil-pen-alt.png",
                        QSize(),
                        QIcon.Normal,
                        QIcon.Off)
                    btn.setIcon(icon5)
                    btn.setIconSize(QSize(40, 40))
                    self.ui.tableWidget_37.setCellWidget(row_number, 5, btn)
                    btn.clicked.connect(self.update_tx_page)
            
        except Exception:
            print("transactions loading")

    def employee_profile_page(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_49)
            row = self.ui.tableWidget_40.currentRow()
            currentcode = (self.ui.tableWidget_40.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            column_list = ["first_name", "last_name", "mobile", "email", "address", "emmp_postion", "department", "gender", "joined"]
            line_edits = [
                self.ui.label_328,
                self.ui.label_331,
                self.ui.label_332,
                self.ui.label_333,
                self.ui.label_334,
                self.ui.label_335,
                self.ui.label_336,
                self.ui.label_338,
                self.ui.label_339
                ]
            for col, labels in zip(column_list, line_edits):
                var_y = cusr.execute(
                    "SELECT %s FROM employee WHERE emp_code=? " %
                    (str(
                        col,)), (currentcode,)).fetchone()
                var_y = (''.join(map(str, var_y)))
                labels.setText((var_y))
                labels.setFont(QFont("Times", 13))
            emp_code = cusr.execute("SELECT emp_code FROM employee WHERE emp_code=?", (currentcode,)).fetchone()
            emp_code = (''.join(map(str, emp_code)))
            self.ui.label_355.setText((emp_code))
            self.ui.label_355.setFont(QFont("Times", 17))

    def position_update_page(self):
        UPDATE_PAGE_SetWidgetsData.update_page_set_data_widgets(
            stacked_Widget =self.ui.stackedWidget_4,
            page = self.ui.page_51,
            table_Widget = self.ui.tableWidget_38,
            row_num = 0,
            line_edits = [
                self.ui.lineEdit_75,
                self.ui.lineEdit_76,
                # self.ui.lineEdit_74,
            ],
            sqlquery = "SELECT %s FROM positions WHERE pos_code=? ",
            column_list = [
                "pos_code",
                "pos_name"
            ],
            plaintexteditsql = "SELECT pos_description FROM positions WHERE pos_code=?",
            plaintextedit = self.ui.plainTextEdit_7)
    def tx_update_page(self):
        UPDATE_PAGE_SetWidgetsData.update_page_set_data_widgets(
            stacked_Widget =self.ui.stackedWidget,
            page = self.ui.page_60,
            table_Widget = self.ui.tableWidget_37,
            row_num = 0,
            line_edits = [
                self.ui.lineEdit_12,
                self.ui.lineEdit_15
                # self.ui.lineEdit_74,
            ],
            sqlquery = "SELECT %s FROM transactions WHERE id_4=? ",
            column_list = [
                "KSH",
                "description"
            ],
            plaintexteditsql = None,
            plaintextedit = None
        )
    def department_update_page(self):
        UPDATE_PAGE_SetWidgetsData.update_page_set_data_widgets(
            stacked_Widget = self.ui.stackedWidget_4,
            page = self.ui.page_50,
            table_Widget = self.ui.tableWidget_39,
            row_num = 0,
            line_edits = [
                self.ui.lineEdit_72,
                self.ui.lineEdit_71,
            ],
            sqlquery = "SELECT %s FROM department WHERE dep_code=? ",
            column_list = [
                "dep_code",
                "dep_name"
            ],
            plaintexteditsql = "SELECT dep_description FROM department WHERE dep_code=?",
            plaintextedit = self.ui.plainTextEdit_6

        )
    def employee_update_page(self):
        UPDATE_PAGE_SetWidgetsData.update_page_set_data_widgets(
            stacked_Widget = self.ui.stackedWidget_4,
            page = self.ui.page_48,
            table_Widget = self.ui.tableWidget_40,
            row_num = 0,
            line_edits = [
                self.ui.lineEdit_68,
                self.ui.lineEdit_66,
                self.ui.lineEdit_67,
                self.ui.lineEdit_65,
                self.ui.lineEdit_69,
                self.ui.lineEdit_70],
            sqlquery = "SELECT %s FROM employee WHERE emp_code=? ",
            column_list = ["emp_code",
                        "first_name", 
                        "last_name", 
                        "mobile", 
                        "email", 
                        "address", 
                        "gender"],
            plaintexteditsql=None,
            plaintextedit=None
        )
    def uom_update_page(self):

        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_58)
        row = self.ui.tableWidget_42.currentRow()
        currentcode = (self.ui.tableWidget_42.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        var_uom = cusr.execute("SELECT is_active FROM uom").fetchall()
        uom = [item for t in var_uom for item in t]
        self.completer2 = QCompleter(uom)
        self.ui.lineEdit_89.setCompleter(self.completer2)
        column_list = [
                        "name", 
                        "unit_abbr",
                        "is_active"]
        line_edits = [
                self.ui.lineEdit_87,
                self.ui.lineEdit_88,
                self.ui.lineEdit_89
                ]
        for col, edits in zip(column_list, line_edits):
            var_y = cusr.execute(
                "SELECT %s FROM uom WHERE uom_id=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))

    def update_position(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_38.currentRow()
            currentcode = (self.ui.tableWidget_38.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            updated = dt.today()   
            position_code = str(self.ui.lineEdit_75.text())
            position_name = str(self.ui.lineEdit_76.text())
            position_level = str(self.ui.comboBox_33.currentText())
            position_status= str(self.ui.comboBox_34.currentText())
            position_description = self.ui.plainTextEdit_7.document().toPlainText()

            column_list = ["pos_code", "pos_name", "pos_level", "pos_description", "status"]
            edits = [ 
                updated,
                position_code,
                position_name,
                position_level,
                position_description,
                position_status]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE positions SET %s=? WHERE pos_code=?" %
                    (str(
                        col,)), (ed, currentcode))
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'client is updated.')
                
            # except Exception:
            #     QMessageBox.warning(
            #         QMessageBox(),
            #         'Error',
            #         'Could not update client.')

    def update_department(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_39.currentRow()
            currentcode = (self.ui.tableWidget_39.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            updated = dt.today()   
            department_code = str(self.ui.lineEdit_72.text())
            department_name = str(self.ui.lineEdit_71.text())

            department_level = str(self.ui.comboBox_32.currentText())
            department_status= str(self.ui.comboBox_31.currentText())
            department_description = self.ui.plainTextEdit_6.document().toPlainText()

            column_list = ["updated", "dep_code", "dep_name", "dep_level", "dep_description", "status"]
            edits = [ 
                updated,
                department_code,
                department_name,
                department_level,
                department_description,
                department_status]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE department SET %s=? WHERE dep_code=?" %
                    (str(
                        col,)), (ed, currentcode))
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'client is updated.')
                
            # except Exception:
            #     QMessageBox.warning(
            #         QMessageBox(),
            #         'Error',
            #         'Could not update client.')
    def update_transactions(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_37.currentRow()
            currentcode = (self.ui.tableWidget_37.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            updated = dt.today()   
            amount = str(self.ui.lineEdit_12.text())
            description = str(self.ui.lineEdit_15.text())

            acc = str(self.ui.comboBox_46.currentText())
            txtype= str(self.ui.comboBox_47.currentText())

            column_list = ["name", "tx_type", "KSH", "description", "updated"]
            edits = [ 
                acc,
                txtype,
                amount,
                description,
                updated]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE transactions SET %s=? WHERE id_4=?" %
                    (str(
                        col,)), (ed, currentcode))
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'transaction is updated.')
                
            # except Exception:
            #     QMessageBox.warning(
            #         QMessageBox(),
            #         'Error',
            #         'Could not update client.')
    def update_coa(self):
        # logging.basicConfig(level=logging.INFO)
        # with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.chart_of_accounts_tb.currentRow()
        currentcode = (self.ui.chart_of_accounts_tb.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        amount = str(self.ui.lineEdit_93.text())
        code = str(self.ui.lineEdit_92.text())

        acc = str(self.ui.comboBox_48.currentText())
        txtype= str(self.ui.comboBox_50.currentText())

        column_list = ["role", "account", "code", "balance_type"]
        edits = [ 
            acc,
            amount,
            code,
            txtype]
        for col, ed in zip(column_list, edits):
            cusr.execute(
                "UPDATE chart_of_accounts SET %s=? WHERE code=?" %
                (str(
                    col,)), (ed, currentcode))
            database_connection.commit()
        if self.ui.checkBox_5.isChecked() == True:
            cusr.execute("UPDATE chart_of_accounts SET locked=? WHERE code=?", ("1", currentcode))
            database_connection.commit()
            cusr.execute("UPDATE chart_of_accounts SET active=? WHERE code=?", ("0", currentcode))
            database_connection.commit()
        else:
            cusr.execute("UPDATE chart_of_accounts SET active=? WHERE code=?", ("1", currentcode))
            database_connection.commit()
            cusr.execute("UPDATE chart_of_accounts SET locked=? WHERE code=?", ("0", currentcode))
            database_connection.commit()
        QMessageBox.information(
            QMessageBox(),
            'Successful',
            'transaction is updated.')
            
        # except Exception:
        #     QMessageBox.warning(
        #         QMessageBox(),
        #         'Error',
        #         'Could not update client.')


    def update_employee(self):
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_40.currentRow()
            currentcode = (self.ui.tableWidget_40.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            updated = dt.today()   
            qdate = self.ui.dateEdit_21.date()
            employee_start_date = qdate.toPython()
            employee_code = str(self.ui.lineEdit_68.text())
            employee_first_name = str(self.ui.lineEdit_66.text())
            employee_last_name = str(self.ui.lineEdit_67.text())
            employee_mobile = str(self.ui.lineEdit_65.text())
            employee_email = str(self.ui.lineEdit_69.text())
            employee_addres = str(self.ui.lineEdit_70.text())
            gender = str(self.ui.comboBox_28.currentText())
            position = str(self.ui.comboBox_27.currentText())
            employee_depertment = str(self.ui.comboBox_26.currentText())
            column_list = ["updated", "emp_code", "first_name", "last_name", "mobile", "email", "address", "gender", "emmp_postion", "department", "joined"]
            edits = [ 
                updated,
                employee_code,
                employee_first_name,
                employee_last_name,
                employee_mobile,
                employee_email,
                employee_addres,
                gender,
                position,
                employee_depertment,
                employee_start_date]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE employee SET %s=? WHERE emp_code=?" %
                    (str(
                        col,)), (ed, currentcode))
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'client is updated.')
                
            # except Exception:
            #     QMessageBox.warning(
            #         QMessageBox(),
            #         'Error',
            #         'Could not update client.')


    def purchase_order_view_bill_details(self):
        """view the billed purchase order details
        """
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            row = self.ui.tableWidget_28.currentRow()
            # get the purchase_order_item_uuid from tableWidget_28 at row number 4
            currentcode = (self.ui.tableWidget_28.item(row, 4).text())
            currentcode = (''.join(map(str, currentcode)))
            print(currentcode, "$$$$$$$$$$$$$$$$$$$$$$$$$")
            # get the purchase_order_uuid using the purchase_order_item_uuid(current code)
            purchase_order_uuid = cusr.execute("SELECT purchase_order_uuid FROM purchase_order_items WHERE uuid=?", (currentcode,)).fetchone()
            purchase_order_uuid = (''.join(map(str, purchase_order_uuid)))
            # get the purchase ordder uuid using the purchase_order_uuid

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_37)
    
            result = cusr.execute("SELECT bill_number, date,  vendor_id, amount_due, amount_paid FROM bill WHERE purchase_order_uuid=?", (purchase_order_uuid,)).fetchall()

            self.ui.tableWidget_30.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_30.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_30.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
                    btn = QPushButton("Details")
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)
                    # font.setWeight(75)
                    btn.setFont(font)
                    btn.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    push = QPushButton("Update")
                    push.setStyleSheet(u"QPushButton{\n"
                                        "\n"
                                        "border-radius : 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
                    self.ui.tableWidget_30.setCellWidget(row_number, 5, btn)
                    self.ui.tableWidget_30.setCellWidget(row_number, 6, push)
                    btn.clicked.connect(self.bill_details_page)
                    push.clicked.connect(self.bill_update_page)

    def uppdate_purchase_page_order(self):
        self.ui.plainTextEdit_4.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_36)
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        po_title = cusr.execute("SELECT po_title FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
        po_title = (''.join(map(str, po_title)))
        po_notes = cusr.execute("SELECT notes FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
        po_notes = (''.join(map(str, po_notes)))
        po_status = cusr.execute("SELECT po_status FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
        po_status = (''.join(map(str, po_status)))
        fulfilled = cusr.execute("SELECT fulfilled FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
        fulfilled = (''.join(map(str, fulfilled)))
        self.ui.lineEdit_6.setText(po_title)
        self.ui.comboBox_13.setCurrentText(po_status)
        self.ui.plainTextEdit_4.insertPlainText(po_notes)
        if fulfilled == "1":
            self.ui.checkBox.setChecked(True)
        PurchaseOrder.purchase_order_items_load_table(self)

    def create_bill_from_purchase_order(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))

        purchase_order_bill_uuid.append(currentcode)
        
        po_status = str(self.ui.comboBox_17.currentText())
        status = str(self.ui.comboBox_17.currentText())
        if self.ui.comboBox_13.itemText(self.ui.comboBox_13.currentIndex()) == 'Approved' and self.ui.comboBox_16.itemText(self.ui.comboBox_16.currentIndex()) == 'ordered':
            self.add_bill()

    def insert_purchase_order_items(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        updated = dt.today()
        created = dt.today()
        uuid_po = uuid.uuid4().hex
        po_name = str(self.ui.comboBox_15.currentText())
        unit_cost = float(str(self.ui.lineEdit_61.text()))
        quantity =  int(str(self.ui.lineEdit_18.text()))
        amount = (unit_cost * quantity)   
        cusr.execute(
            "INSERT INTO purchase_order_items(created , updated , uuid , purchase_order_uuid, name , cogs, quantity, amount) VALUES (?,?,?,?,?,?,?,?)",
            ((updated,
              created,
              uuid_po,
              currentcode,
              po_name,
              unit_cost,
              quantity,
              amount)))
        database_connection.commit()
        PurchaseOrder.purchase_order_items_load_table(self)


    def uppdate_purchase_order(self):
        fulfilled = self.ui.checkBox
        if fulfilled.isChecked() == True and self.ui.comboBox_13.currentText() != "Approved":
            QMessageBox.warning(
            QMessageBox(),
            'Error',
            'Cant mark as Fullfield Make sure the purchase order is Approved')
        else:
            database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_27.currentRow()
            currentcode = (self.ui.tableWidget_27.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))    
            purchase_order_uuid = cusr.execute("SELECT uuid FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
            purchase_order_uuid = (''.join(map(str, purchase_order_uuid)))
            po_title = self.ui.lineEdit_6.text() 
            updated = dt.today()
            p_date = self.ui.dateEdit.date()
            po_date = p_date.toPython()
            notes = self.ui.plainTextEdit_4.document().toPlainText()
            po_amount_recived = cusr.execute("SELECT SUM(amount) FROM purchase_order_items WHERE purchase_order_uuid=?", (purchase_order_uuid,)).fetchone()
            po_amount_recived = (''.join(map(str, po_amount_recived)))
            print(po_amount_recived)
            if po_amount_recived == str(None):
                po_amount_recived = 0.0
                print(po_amount_recived, "@@@@@@@@@@@@@@@@@@@@@@@@@@")
            else:
                po_amount_recived = float(''.join(map(str, po_amount_recived)))
                print(po_amount_recived, "############################")

            fulfilled = self.ui.checkBox
            if fulfilled.isChecked() == True:
                fulfilled = "1"
            else:
                fulfilled="0"
            ft_date = self.ui.dateEdit_2.date()
            fulfillment_date = ft_date.toPython()
            
            po_status = str(self.ui.comboBox_13.currentText())
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("UPDATE purchaseorder SET updated=?, notes=?, po_date=?, po_title=?, po_amount_recived=?, fulfilled=?, fulfillment_date=?, po_status=? WHERE po_number=?",(
                updated,
                notes,
                po_date,
                po_title,
                po_amount_recived,
                fulfilled,
                fulfillment_date,
                po_status,
                currentcode
                ))
            database_connection.commit()

    def bill_journal_entries(self):
        database_connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_30.currentRow()
        currentcode2 = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode2 = (''.join(map(str, currentcode2)))
        ledger_posted = cusr.execute("SELECT active FROM ledgers WHERE name=?", (currentcode2,)).fetchone() # get all ledgers name
        ledger_posted = (''.join(map(str, ledger_posted))) # convert data into list
        # check if ledger_name is in the ledger table to avoid duplicates of bills in ledgers
        if ledger_posted == '0':
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Post the bill to the ledger by pressing the green button "Bill ledger".')
        else:
            b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode2,)).fetchone()
            b = (''.join(map(str, b)))
            print(f"journal uuid ------- > {b}")
            # self.ledger_id.append(b) #append ledger i wich will be used to add new journal entry
            ledger_id.append(b) #append ledger i wich will be used to add new journal entry
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_33)
            result = database_connection.execute("SELECT id, description, journal_entrydate, activity FROM journal_entries WHERE ledger_id=?", (b,)).fetchall()

            self.ui.tableWidget_26.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_26.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_26.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
                    btn = QPushButton("TXS")
                    font = QtGui.QFont()
                    font.setPointSize(9)
                    font.setBold(True)
                    # font.setWeight(75)
                    btn.setFont(font)
                    btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: rgb(0, 255, 0);;\n"
                                    "border-radius : 25px;\n"
                                    "color : rgb(7, 7, 7); \n"
                                    "}")
                    self.ui.tableWidget_26.setCellWidget(row_number, 4, btn)
                    btn.clicked.connect(self.jouranal_entry_transaction)

    def unlock_bill_ledger(self):
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        LEDGERBUTTONS.lock_bill_invoice_ledger(
            self.ui.tableWidget_30,
            "The Bill is unlocked.",
            "The Bill is successfully Unlocked..",
            "0"
        )
        
    def unlock_invoice_ledger(self):
         LEDGERBUTTONS.lock_bill_invoice_ledger(
            self.ui.tableWidget_6,
            "The invoice is successfully unlocked",
            "The invoice is Already unLocked.",
            "0"
        )
    def post_bill_ledger(self):
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        LEDGERBUTTONS.bill_ledger_journal_entries(
            self.ui.tableWidget_30,
            "The Bill is successfully Posted.",
            "The Bill is Alredy Posted.",
            "1"
        )
        
    def post_invoice_ledger(self):
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        LEDGERBUTTONS.lock_bill_invoice_ledger(
            self.ui.tableWidget_6,
            "The Invoice is successfully Posted.",
            "The Invoice is Alredy Posted..",
            "1"
        )

        
    def lock_bill_ledger(self):
        """function that bills a ledger at the bills update page
        checks if the bill is posted if true it raises an exception if false it post it to the ledger
        """
        LEDGERBUTTONS.lock_bill_invoice_ledger(
            self.ui.tableWidget_30,
            "The Bill is successfully Posted.",
            "The Bill is successfully locked.",
            "1"
        )

    def lock_invoice_ledger(self):
        LEDGERBUTTONS.lock_bill_invoice_ledger(
            self.ui.tableWidget_6,
            "The invoice is successfully locked",
            "The invoice is Already Locked.",
            "1"
        )

    def update_bill(self):
        """function that updates a bill
        """
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_30.currentRow()
        currentcode = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode))) # bill number
        ledger_locked = cusr.execute("SELECT locked FROM ledgers WHERE name=?", (currentcode,)).fetchone() # get all ledgers name
        ledger_locked = (''.join(map(str, ledger_locked))) # convert data into list
        # check if ledger_name is in the ledger table to avoid duplicates of bills in ledgers
        
        if ledger_locked == '1':
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'This Bill is Locked Unlock to make changes.')
        else:
            ad_uuidd = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            ad_uuidd = (''.join(map(str, ad_uuidd)))
            amount_d = cusr.execute("SELECT amount_due FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            amount_d = (''.join(map(str, amount_d)))
            a_d = cusr.execute("SELECT SUM(amount) FROM bill_item WHERE bill_uuid=?", (ad_uuidd,)).fetchone()
            print("%%%%%%%%%%%%%%%%%%", a_d)
            a_d = (''.join(map(str, a_d)))
            if a_d == str(None):
                QMessageBox.warning(
                    QMessageBox(),
                    'Error',
                    'Please Bill some Items in order to save.')

            total_am = float(self.ui.lineEdit_58.text())
            paid_bill = float(str(self.ui.lineEdit_45.text()))
            if paid_bill > total_am:
                QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Amount paid cant exceed Amount Billed/Amount due.')

            updated = dt.today()
            terms = str(self.ui.comboBox_17.currentText())


            d_r = 'Deferred Revenue'
            p_e = 'prepaid Expenses'
            deferred_revenue = cusr.execute("SELECT code FROM chart_of_accounts WHERE account=?", (d_r,)).fetchone()
            deferred_revenue = (''.join(map(str, deferred_revenue))) # gets Deferred Revenue ID from chart of accounts 

            prepaid_expenses = cusr.execute("SELECT code FROM chart_of_accounts WHERE account=?", (p_e,)).fetchone()
            prepaid_expenses = (''.join(map(str, prepaid_expenses)))  # gets prepaid Expenses ID from chart of accounts 

            amount_unerned = cusr.execute("SELECT KSH FROM transactions WHERE coa_id=?", (deferred_revenue,)).fetchone() # gets amount_unerned amount from transactions using deferred_revenue variable as Id for querying
            # amount_unerned = (''.join(map(str, amount_unerned)))
            
            if amount_unerned == str(None):
                amount_unerned = float(''.join(map(str, amount_unerned)))
            
            else:

                amount_unerned=0.0
                print('$$$$$$$$$$$$$$$$$$', amount_unerned)

            amount_recivable = cusr.execute("SELECT KSH FROM transactions WHERE coa_id=?", (prepaid_expenses,)).fetchone() # gets amount_recivable amount from transactions using prepaid_expenses variable as Id for querying
            # amount_recivable = (''.join(map(str, amount_recivable)))
            if amount_recivable == str(None):
                amount_recivable = float(''.join(map(str, amount_recivable)))
            else:
                amount_recivable=0.0
            amount_earned = self.ui.lineEdit_45.text()

            paid = self.ui.checkBox_3
            if paid.isChecked() == True and amount_d == "0":
                paid = "1"
            elif paid.isChecked() == True and amount_d != "0":
                QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Cannot marked as paid, make sure the bill is fully paid')
            else:
                paid="0"
            date_1 = date.today()
            days_reg = str(self.ui.comboBox_17.currentText())
            if days_reg == 'Due on receipt':
                due_date = date.today()
            else:
                day_reg = int(''.join(x for x in days_reg if x.isdigit())) # extracts digit from the terms string  e.g NET 30 gets 30 
                due_date = date.today() + timedelta(days=day_reg) # calculates the remaining days until the bill is due e.g NET 30 days timedelta(days=30)

            xref = self.ui.lineEdit_59.text()
            accrue = ' '


            bill_status = str(self.ui.comboBox_18.currentText())
            vendor = str(self.ui.comboBox_52.currentText())
            markdown_notes = self.ui.plainTextEdit_3.document().toPlainText()
            cusr.execute(
                    "UPDATE bill SET updated=?, terms=?,  amount_recivable=?, amount_unerned=?, amount_earned=?, date=?, due_date=?, xref=?, accrue=?, vendor_id=?, bill_status=?, markdown_notes=? WHERE bill_number=? ", (
                        updated,
                        terms,
                        amount_recivable,
                        amount_unerned,
                        amount_earned,
                        
                        date_1,
                        due_date,
                        xref,
                        accrue,
                        vendor,
                        bill_status,
                        markdown_notes,
                        currentcode
                        ))
            database_connection.commit()
    def pay_bill(self):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_30.currentRow()
        currentcode = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode))) # bill number
        ledger_locked = cusr.execute("SELECT locked FROM ledgers WHERE name=?", (currentcode,)).fetchone() # get all ledgers name
        ledger_locked = (''.join(map(str, ledger_locked))) # convert data into list
        # check if ledger_name is in the ledger table to avoid duplicates of bills in ledgers
        
        if ledger_locked == '1':
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'This Bill is Locked Unlock to make changes.')
        else:
            ad_uuidd = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            ad_uuidd = (''.join(map(str, ad_uuidd)))
            ledger = cusr.execute("SELECT id FROM ledgers WHERE name=?", (currentcode,)).fetchone()
            ledger = (''.join(map(str, ledger)))
            amount_d = cusr.execute("SELECT amount_due FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            amount_d = float(''.join(map(str, amount_d)))
            amount_p = cusr.execute("SELECT amount_paid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            amount_p = float(''.join(map(str, amount_p)))
            a_d = cusr.execute("SELECT SUM(amount) FROM bill_item WHERE bill_uuid=?", (ad_uuidd,)).fetchone()
            print("%%%%%%%%%%%%%%%%%%", a_d)
            a_d = (''.join(map(str, a_d)))
            if a_d == str(None):
                QMessageBox.warning(
                    QMessageBox(),
                    'Error',
                    'Please Bill some Items in order to save.')

            total_am = float(self.ui.lineEdit_58.text())
            created = dt.today()
            updated = dt.today()
            journal_uuid = uuid.uuid4().hex
            uuid1 = uuid.uuid4().hex
            uuid3 = uuid.uuid4().hex
            paid_bill = float(str(self.ui.lineEdit_45.text()))
            total_bill_amount = float(str(self.ui.lineEdit_58.text()))
            amount_paid = amount_p + paid_bill
            amount_due =  total_bill_amount - amount_paid
            
            paid = self.ui.checkBox_3
            if paid.isChecked() == True and amount_d == "0":
                paid = "1"
            elif paid.isChecked() == True and amount_d != "0":
                QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Cannot marked as paid, make sure the bill is fully paid')
            else:
                paid="0"
            p_paid_date = self.ui.dateEdit_8.date()
            paid_date = p_paid_date.toPython()
            if paid_bill > total_am:
                QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Amount paid cant exceed Amount Billed/Amount due.')
            cusr.execute(
                    "UPDATE bill SET amount_due=?, amount_paid=?,  paid=?, paid_date=? WHERE bill_number=? ", (
                        amount_due,
                        amount_paid,
                        paid,
                        paid_date,
                        currentcode
                        ))
            database_connection.commit()
            cusr.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger, "other", "bill payment", "1", "0", paid_date))
            database_connection.commit()
            cusr.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid1,
                    created,
                    updated,
                    "currentliabilities",
                    journal_uuid,
                    currentcode,
                    'accounts payable',
                    amount_paid,
                    "paid bill",
                    "credit",
                    paid_date))
            database_connection.commit()
            cusr.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (uuid3,
                created,
                updated,
                "currentassets",
                journal_uuid,
                currentcode,
                'cash and cash equivalents',
                amount_paid,
                "paid bill",
                "credit",
                paid_date))
            database_connection.commit()

    def add_bill_items(self):
        # try:
        """add items to be billed into the database
        """
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_30.currentRow()
        currentcode = (self.ui.tableWidget_30.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        
        uuid_1 = uuid.uuid4().hex        
        created = dt.today()
        updated = dt.today()
        amount = int(str(self.ui.lineEdit_60.text()))
        bill_uuid = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
        bill_uuid = (''.join(map(str, bill_uuid)))
        b = cusr.execute('SELECT id FROM ledgers WHERE name=?', (currentcode,)).fetchone()
        b = (''.join(map(str, b)))
        name = str(self.ui.comboBox_19.currentText())
        journal_uuid = uuid.uuid4().hex
        uuid1 = uuid.uuid4().hex
        uuid3 = uuid.uuid4().hex
        try:
            cusr.execute("INSERT INTO bill_item(created, updated, uuid, bill_uuid, name, amount) VALUES (?,?,?,?,?,?)", (created, updated, uuid_1, bill_uuid, name, amount))
            database_connection.commit()
            cusr.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, b, "other", "bill items", "1", "0", created))
            database_connection.commit()
            cusr.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid1,
                    created,
                    updated,
                    "currentliabilities",
                    journal_uuid,
                    currentcode,
                    'accounts payable',
                    amount,
                    "bill items",
                    "debit",
                    created))
            database_connection.commit()
            database_connection.commit()
            bills.Bill.billed_items_load_table(self)
            current = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode,)).fetchone()
            current = (''.join(map(str, current)))
            amount_due = cusr.execute("SELECT SUM(amount) FROM bill_item WHERE bill_uuid=?", (current,)).fetchone()
            amount_due = (''.join(map(str, amount_due)))
            self.ui.lineEdit_58.clear()
            self.ui.lineEdit_58.setText(amount_due)
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Item is billed successfully.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not bill item .')

    def setcombos_bill_update(self):
        """sets the combobox with values 
        """
        status = [
        'Draft',
        'Inreview',
        'Approved',
        'Canceled']
        terms = [
        'Due on receipt',
        'Net 30 Days',
        'Net 60 Days',
        'Net 90 Days',
        ]
        purchase_ordeer_status = [
            'ordered',
            'Not ordered',
            'In Transit',
            'Recived',
            'Canceled'
        ]
        self.ui.comboBox_18.addItems(status)
        self.ui.comboBox_13.addItems(status)
        self.ui.comboBox_16.addItems(purchase_ordeer_status)
        
        self.ui.comboBox_17.addItems(terms)
        self.ui.comboBox_14.addItems(status)
        self.ui.comboBox_24.addItems(terms)
        self.ui.comboBox_20.addItems(terms)
        self.ui.comboBox_21.addItems(status)
        expense = "expenses"
        e = self.c.execute(
            "SELECT account FROM chart_of_accounts WHERE role=?", (expense,)).fetchall()
        b = [item for t in e for item in t]
        stock = self.c.execute(
            "SELECT name FROM stock ").fetchall()
        stock2 = [item for t in stock for item in t]
        self.ui.comboBox_19.addItems(b)
        self.ui.comboBox_19.addItems(stock2)
    
    def bill_details_page(self):
        """displays in detail the statuts of a bill i.e if its paid, approved, due date etc
            and sets data to labes on this page
        """
        ledger_id.clear()
        bills.Bill.BILL_DETAILS_page(self)

    def bill_update_page(self):
        self.ui.plainTextEdit_3.clear()
        logging.basicConfig(level=logging.INFO)
        with SQLite_CONTEX_MANAGER(file_name=pathtodb + "\\yobi\\yobi_database.db") as cusr:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_39)
            bills.Bill.billed_items_load_table(self)
            row = self.ui.tableWidget_30.currentRow()
            currentcode = (self.ui.tableWidget_30.item(row, 2).text())
            currentcode = (''.join(map(str, currentcode)))

            currentcode2 = (self.ui.tableWidget_30.item(row, 0).text())
            currentcode2 = (''.join(map(str, currentcode2)))

            self.ui.label_275.setText(currentcode)
            self.ui.label_275.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label_275.setFont(QtGui.QFont("Times", 20))
            column_list = ["addr1", "tel1", "email"]
            labels = [
                self.ui.label_277,
                self.ui.label_276,
                self.ui.label_278
            ]
            for col, edits in zip(column_list, labels):
                var_y = cusr.execute(
                    "SELECT %s FROM supplier WHERE name=? " %
                    (str(
                        col,)), (currentcode,)).fetchone()
                var_y = (''.join(map(str, var_y)))
                edits.setText((var_y))
                edits.setFont(QtGui.QFont("Times", 17))
            expense = "expenses"
            amount_paid = cusr.execute("SELECT amount_paid FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            amount_paid = (''.join(map(str, amount_paid)))
            current = cusr.execute("SELECT uuid FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            print(currentcode2)
            current = (''.join(map(str, current)))
            amount_due = cusr.execute("SELECT SUM(amount) FROM bill_item WHERE bill_uuid=?", (current,)).fetchone()
            amount_due = (''.join(map(str, amount_due)))
            
            external_refrence = cusr.execute("SELECT xref FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            external_refrence = (''.join(map(str, external_refrence)))
            external_refrence = cusr.execute("SELECT xref FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            external_refrence = (''.join(map(str, external_refrence)))
            terms_bill = cusr.execute("SELECT terms FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            terms_bill = (''.join(map(str, terms_bill)))
            bill_status = cusr.execute("SELECT bill_status FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            bill_status = (''.join(map(str, bill_status)))
            notes = cusr.execute("SELECT markdown_notes FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            notes = (''.join(map(str, notes)))
            
            # paid_date = cusr.execute("SELECT paid_date FROM bill WHERE bill_number=?", (currentcode2,)).fetchone()
            # paid_date = (''.join(map(str, paid_date)))
            # paid_date_re = (re.sub("[-]", ",", paid_date))
            # print('@@@@@@@@@@@@@@@@@@@@@@@@', paid_date_re)
            if amount_paid == str(None):
                amount_paid = str(0.0)
            if amount_due == str(None):
                amount_due = str(0.0)
            if external_refrence == str(None):
                external_refrence = 0.0
            np = babel.numbers.format_currency(
            decimal.Decimal(amount_paid), cash_label, locale='en_US')

            self.ui.label_382.setText(np)
            self.ui.label_382.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label_382.setFont(QtGui.QFont("Times", 11))
            self.ui.lineEdit_58.setText(amount_due)
            self.ui.lineEdit_59.setText(external_refrence)
            self.ui.comboBox_17.setCurrentText(terms_bill)
            self.ui.comboBox_18.setCurrentText(bill_status)
            self.ui.plainTextEdit_3.insertPlainText(notes)
            # da = QDate(int(paid_date_re))
            # print("daaaaaaaaaaaaaa", da)
            # self.ui.dateEdit_8.setDate(da)

            #  bills.Bill.BILL_UPDATE_page(self)

    def details_page(self):
        self.ui.plainTextEdit_8.clear()
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_35)
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        column_list = ["po_number", "po_status", "fulfilled", "po_amount_recived", "po_title"]
        labels = [
            self.ui.label_57,
            self.ui.label_71,
            self.ui.label_65,
            self.ui.label_127,
            self.ui.label_135
        ]
        for col, edits in zip(column_list, labels):
            var_y = cusr.execute(
                "SELECT %s FROM purchaseorder WHERE po_number=? " %
                (str(
                    col,)), (currentcode,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            edits.setText((var_y))
            edits.setAlignment(QtCore.Qt.AlignCenter)
            edits.setFont(QFont("Times", 20))
        po_notes = cusr.execute("SELECT notes FROM purchaseorder WHERE po_number=?", (currentcode,)).fetchone()
        po_notes = (''.join(map(str, po_notes)))
        po_amount = cusr.execute("SELECT SUM(amount) FROM purchase_order_items WHERE purchase_order_uuid=?", (currentcode,)).fetchone()
        po_amount = float(''.join(map(str, po_amount)))
        tp_m = babel.numbers.format_currency(
            decimal.Decimal(po_amount), cash_label, locale='en_US')
        self.ui.label_101.setText(tp_m)
        self.ui.label_101.setFont(QFont("Times", 20))
        self.ui.plainTextEdit_8.insertPlainText(po_notes)
        self.load_purchase_order_tb()

    def set_ledger_update_page(self):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_62)
        row = self.ui.tableWidget_25.currentRow()
        currentcode = (self.ui.tableWidget_25.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        combo1 = cusr.execute("SELECT locked FROM ledgers WHERE lg_id=?", (currentcode,)).fetchone()
        combo1 = (''.join(map(str, combo1)))
        combo2 = cusr.execute("SELECT active FROM ledgers WHERE lg_id=?", (currentcode,)).fetchone()
        combo2 = (''.join(map(str, combo2)))
        name = cusr.execute("SELECT name FROM ledgers WHERE lg_id=?", (currentcode,)).fetchone()
        name = (''.join(map(str, name)))
        if combo1 == "1":
            self.ui.checkBox_8.setChecked(True)
        else:
            self.ui.checkBox_9.setChecked(True)
        self.ui.lineEdit_95.setText((name))

        

    def load_purchase_order_tb(self):
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        row = self.ui.tableWidget_27.currentRow()
        currentcode = (self.ui.tableWidget_27.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode)))
        
        result = self.connection.execute("SELECT name , cogs, quantity, amount, uuid FROM purchase_order_items WHERE purchase_order_uuid=?", (currentcode,)).fetchall()
    
        self.ui.tableWidget_28.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_28.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_28.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("view bill")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                "    background-color: rgb(208, 0, 0);;\n"
                                "border-radius : 25px;\n"
                                "color : rgb(7, 7, 7); \n"
                                "}")
                self.ui.tableWidget_28.setCellWidget(row_number, 5, btn)
                btn.clicked.connect(self.purchase_order_view_bill_details)

    def update_orders(self):
        try:
            discount = float(str(self.ui.lineEdit_4.text()))
            #code = str(self.ui.lineEdit.text())
            client_name = str(self.ui.lineEdit_2.text())
            grand_total = float(str(self.ui.lineEdit_3.text()))
            total_amount = float(str(self.ui.lineEdit_5.text()))
            sub_total = float(str(self.ui.lineEdit_19.text()))
            payment_type = str(self.ui.comboBox_49.currentText())
            payment_status = str(self.ui.comboBox_51.currentText())
            terms = str(self.ui.comboBox_20.currentText())
            status = str(self.ui.comboBox_21.currentText())
            order_date = str(self.ui.lineEdit_24.text())
            due = float(str(self.ui.lineEdit_25.text()))
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            # row = self.ui.tableWidget_6.currentRow()
            # currentcode = (self.ui.tableWidget_6.item(row, 0).text())
            # currentcode = (''.join(map(str, currentcode)))
            currentcode = invoice_id[0]
            column_list = [
                "discount",
                "client_name",
                "grand_total",
                "total_amount",
                "sub_total",
                "payment_type",
                "payment_status",
                "order_date ",
                "due",
                "terms",
                "invoice_status"
                ]
            edits = [discount, client_name, grand_total, total_amount,
                        sub_total, payment_type, payment_status, order_date, due, terms, status]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE orders SET %s=? WHERE code=?" %
                    (str(
                        col,)), (ed, currentcode))
                database_connection.commit()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'order is updated.')
            orders_function.setButtons2(self)
            orders_function.orders_label(self)
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not update current order.')

    def update_supplier(self):
        try:
            supplier_name = str(str(self.ui.lineEdit_46.text()))
            #code = str(self.ui.lineEdit.text())
            tel1 = str(self.ui.lineEdit_47.text())
            tel2 = str(str(self.ui.lineEdit_48.text()))
            email = str(str(self.ui.lineEdit_49.text()))
            addr1 = str(str(self.ui.lineEdit_50.text()))
            addr2 = str(str(self.ui.lineEdit_51.text()))
            site = str(str(self.ui.lineEdit_90.text()))
            country = str(str(self.ui.lineEdit_91.text()))

            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_14.currentRow()
            currentcode = (self.ui.tableWidget_14.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            column_list = [
                "name",
                "tel1",
                "tel2",
                "email",
                "addr1",
                "addr2",
                "site",
                "country"]
            edits = [supplier_name, tel1, tel2, email, addr1,
                     addr2, site, country]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE supplier SET %s=? WHERE id_14=?" %
                    (str(
                        col,)), (ed, currentcode))
                database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'supplier is updated.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not update Supplier.')
    def update_uom(self):
        try:
            supplier_name = str(str(self.ui.lineEdit_46.text()))
            #code = str(self.ui.lineEdit.text())
            name = str(self.ui.lineEdit_87.text())
            abbr = str(str(self.ui.lineEdit_88.text()))
            status = str(str(self.ui.lineEdit_89.text()))

            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_42.currentRow()
            currentcode = (self.ui.tableWidget_42.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            column_list = [
                        "name", 
                        "unit_abbr",
                        "is_active"]
            edits = [
                name,
                abbr,
                status
                ]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE uom SET %s=? WHERE uom_id=?" %
                    (str(
                        col,)), (ed, currentcode))
                database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Unit is updated Successfully.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not update Unit.')

    def update_client(self):
        try:
            client_name = str(self.ui.lineEdit_56.text())
            grand_total = str(str(self.ui.lineEdit_55.text()))
            total_amount = str(str(self.ui.lineEdit_54.text()))
            sub_total = (str(self.ui.lineEdit_52.text()))
            sub_total2 = str(str(self.ui.lineEdit_53.text()))
            datee = float(str(self.ui.lineEdit_57.text()))
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_11.currentRow()
            currentcode = (self.ui.tableWidget_11.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))
            column_list = [
                "name",
                "telno",
                "address",
                "email",
                "date",
                "balance"]
            edits = [client_name, grand_total, total_amount,
                     sub_total, sub_total2, datee]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE clients SET %s=? WHERE id_10=?" %
                    (str(
                        col,)), (ed, currentcode))
                database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'client is updated.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not update client.')
    def update_ledger(self):
        try:
            sub_total2 = str(str(self.ui.lineEdit_95.text()))
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            row = self.ui.tableWidget_25.currentRow()
            currentcode = (self.ui.tableWidget_25.item(row, 0).text())
            currentcode = (''.join(map(str, currentcode)))

            column_list = [
                "name"]
            edits = [sub_total2]
            for col, ed in zip(column_list, edits):
                cusr.execute(
                    "UPDATE ledgers SET %s=? WHERE lg_id=?" %
                    (str(col,)), (ed, currentcode))
                database_connection.commit()
            if self.ui.checkBox_8.isChecked() == True:
                cusr.execute("UPDATE ledgers SET locked=? WHERE lg_id=?", ("1", currentcode))
                database_connection.commit()
                cusr.execute("UPDATE ledgers SET active=? WHERE lg_id=?", ("0", currentcode))
                database_connection.commit()
            else:
                cusr.execute("UPDATE ledgers SET active=? WHERE lg_id=?", ("1", currentcode))
                database_connection.commit()
                cusr.execute("UPDATE ledgers SET locked=? WHERE lg_id=?", ("0", currentcode))
                database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'ledger is updated.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not update ledger.')

    def return_order_btn(self):
        self.ui.pushButton_32.clicked.connect(self.ord_return)

    def ord_return(self):
        orders_function.return_order(self)

    def addstock2(self):
        self.ui.pushButton_12.clicked.connect(self.stockadd)

    def save_payment_btn(self):
        self.ui.pushButton_7.clicked.connect(self.save_payment)

    def save_payment(self):
        payment.get_selected_row_details(self)
        self.btn_triger()
        orders_function.orders_label(self)

    def update1(self):
        self.ui.pushButton_16.clicked.connect(self.updatestock2)

    def sales(self):
        self.ui.pushButton_55.clicked.connect(self.salesedit)


    def prof_edit(self):
        self.ui.pushButton_44.clicked.connect(self.profileedit)


    def add_ledger_btn(self):
        self.ui.client_btn_4.clicked.connect(self.add_ledger)

    def add_journalentry_btn(self):
        self.ui.pushButton_23.clicked.connect(self.add_journalentry)

    def add_po_btn(self):
        self.ui.pushButton_53.clicked.connect(self.add_po)
    def add_bill_btn(self):
        self.ui.pushButton_100.clicked.connect(self.add_bill)
        
    def taxset(self):
        self.ui.pushButton_54.clicked.connect(self.taxsettings)

    def income(self):
        self.ui.pushButton_55.clicked.connect(self.editincome)

    def cvs(self):
        try:
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                sql = "SELECT * FROM stock"
                cur.execute(sql)
                data = cur.fetchall()
    # Create the csv file
            with open('STATSSTOCK.csv', 'w', newline='') as f_handle:
                writer = csv.writer(f_handle)
                # Add the header/column names
                header = [
                    'UPC',
                    'name',
                    'BP',
                    'SP',
                    'Quantity',
                    'Supplier',
                    'Category',
                    'reoder limit',
                    'Discount',
                    'VAT',
                    'date',
                    'sold']
                writer.writerow(header)
        # Iterate over `data`  and  write to the csv file
                for row in data:
                    writer.writerow(row)
                QMessageBox.information(
                    QMessageBox(),
                    'Successful',
                    'The data is successfully exported.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not export data.')

    def keystroke(self):
        self.shortcut_open = QShortcut(QKeySequence('Del'), self)
        self.shortcut_open.activated.connect(self.onEmployeeBtnClicked)

    def receiptload(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM recip_detail"
        result = database_connection.execute(query)
        self.ui.tableWidget_14.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_14.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_14.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def recip_detail(self):
        self.ui.pushButton_31.clicked.connect(self.insert_company_details)

    def addrow(self):
        self.ui.pushButton_71.clicked.connect(self.pointofsale_addto_postable)

    def delete_pos_tb(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("DELETE FROM pos_table")
        database_connection.commit()

    def receipt_table(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT name, Quantity, KSH FROM pos_table"
        result = database_connection.execute(query)
        self.ui.tableWidget_15.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_15.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_15.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def prev(self):
        pass
        # self.ui.pushButton_38.clicked.connect(self.inv)

    def export_inv(self):
        self.ui.pushButton_24.clicked.connect(self.invoice)

    def invoice(self):
        ban(self)

    def receipt(self):
        self.ui.pushButton_64.clicked.connect(self.Preview)

    def save_as_csv(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        qdate = self.ui.dateEdit_4.date()
        order_date = qdate.toPython()
        qdate = self.ui.dateEdit_5.date()
        order_date2 = qdate.toPython()
        alltb = cusr.execute(
            "SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_sales = cusr.execute(
            "SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        sale_return = cusr.execute(
            "SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()

    def Preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.PaintRequest)
        dialog.exec()

    def PaintRequest(self, printer):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        document = QtGui.QTextDocument()
        p = QtPrintSupport.QPrinter()
        p.setResolution(100)
        p.setFullPage(True)
        cursor = QtGui.QTextCursor(document)
        header_formart = QtGui.QTextCharFormat()
        sales_formart = QtGui.QTextCharFormat()
        rev_formart = QtGui.QTextCharFormat()
        adress_f = QtGui.QTextBlockFormat()
        adress_f.setLineHeight(150, QtGui.QTextBlockFormat.ProportionalHeight)
        adress_f.setAlignment(QtCore.Qt.AlignRight)
        # adress_f.setRightMargin(50)
        adress = QtGui.QTextBlockFormat()
        adress.setLineHeight(150, QtGui.QTextBlockFormat.ProportionalHeight)
        adress.setAlignment(QtCore.Qt.AlignLeft)
        # adress.setRightMargin(25)
        adres = QtGui.QTextBlockFormat()
        adres.setLineHeight(150, QtGui.QTextBlockFormat.ProportionalHeight)
        adres.setAlignment(QtCore.Qt.AlignCenter)
        rightal = QtGui.QTextBlockFormat()
        #rightal.setLineHeight(150, QtGui.QTextBlockFormat.ProportionalHeight)
        rightal.setAlignment(QtCore.Qt.AlignRight)
        lefal = QtGui.QTextBlockFormat()
        lefal.setLineHeight(150, QtGui.QTextBlockFormat.ProportionalHeight)
        lefal.setAlignment(QtCore.Qt.AlignLeft)
        # adres.setRightMargin(25)
        qdate = self.ui.dateEdit_4.date()
        order_date = qdate.toPython()
        qdate = self.ui.dateEdit_5.date()
        order_date2 = qdate.toPython()
        # alltb = cusr.execute("SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?", (order_date, order_date2)).fetchone()
        # total_sales = cusr.execute("SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?", (order_date, order_date2)).fetchone()
        # sale_return = cusr.execute("SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?", (order_date, order_date2)).fetchone()
        name = cusr.execute(
            "SELECT name FROM fix_expe WHERE fixdate BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchall()
        cash = cusr.execute(
            "SELECT KSH FROM fix_expe WHERE fixdate BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchall()
        # sale_return = float(''.join(map(str, sale_return)))
        # total_sales = float(''.join(map(str, total_sales)))
        # alltb = float(''.join(map(str, alltb)))
        # total_revenue = str(total_sales + alltb)
        # sales_return = str(float(total_revenue) - float(sale_return))
        header_formart.setFontWeight(QtGui.QFont.Bold)
        header_formart.setFontPointSize(20)
        sales_formart.setFontPointSize(13)
        sales_formart.setFontWeight(QtGui.QFont.Bold)
        sales_formart.AlignMiddle
        rev_formart.setFontPointSize(11)
        cursor.setCharFormat(header_formart)
        cursor.insertBlock(adres)
        cursor.insertText("Profit and loss Statment")
        cursor.setCharFormat(header_formart)
        cursor.insertBlock(adres)
        cursor.insertText(
            "From date" +
            " " +
            str(order_date) +
            " " +
            "to date" +
            " " +
            str(order_date2))
        cursor.insertBlock(lefal)
        cursor.setCharFormat(sales_formart)
        cursor.insertText(
            "__________________________________________________________________________________")
        cursor.insertBlock(lefal)
        cursor.insertText("Revenue")
        cursor.insertBlock(lefal)
        cursor.setCharFormat(rev_formart)
        ls_P = ['Sales revenue', 'Sales returns']
        #ls_P2 = [total_revenue, sales_return]
        for sl, tv in zip(name, cash):
            sl = (''.join(map(str, sl)))
            tv = (''.join(map(str, tv)))
            import textwrap
            v = textwrap.fill(sl, 10)
            cursor.insertText(v)
            cursor.insertText("                                    ")
            cursor.insertText(tv)
            cursor.insertBlock()
        cursor.insertBlock(lefal)
        cursor.insertBlock(adress)
        cursor.insertBlock()
        cursor.insertBlock(adress_f)
        cursor.insertText("Sub Total")
        cursor.insertBlock(adress_f)
        cursor.insertText("VAT")
        cursor.insertBlock(adress_f)
        cursor.insertText("Total")
        cursor.insertBlock(adress_f)
        cursor.insertText("Balance Due")
        document.print_(printer)

    def reoder_limit(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT name, Quantity, category FROM stock WHERE reoder > Quantity"
        result = database_connection.execute(query)
        self.ui.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_8.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def combo(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        curs = database_connection.cursor()
        department_level = [
        'First Level',
        'Second Level',
        'Third Level',
        'Fourth Level',
        'Fifth Level',
        ]
        status = [
        'active',
        'inactive',
        ]
        gender = [
        'Male',
        'Female',
        'other'
        ]
        d = curs.execute(
        "SELECT dep_name FROM department ").fetchall()
        b = [item for t in d for item in t]
        dee = curs.execute(
        "SELECT name FROM supplier ").fetchall()
        sup = [item for t in dee for item in t]

        position = curs.execute(
        "SELECT pos_name FROM positions ").fetchall()
        position_name = [item for t in position for item in t]

        self.ui.comboBox_29.addItems(status)
        self.ui.comboBox_52.addItems(sup)
        self.ui.comboBox_34.addItems(status)
        self.ui.comboBox_31.addItems(status)
        self.ui.comboBox_26.addItems(b)
        self.ui.comboBox_28.addItems(department_level)
        self.ui.comboBox_33.addItems(department_level)
        self.ui.comboBox_32.addItems(gender)
        self.ui.comboBox_27.addItems( position_name)
        self.ui.comboBox.addItems(
            ["category", "name", "UPC", "vat", "Quantity", "Supplier"])
        self.ui.comboBox_2.addItems(["All", "code", "client name"])
        self.ui.comboBox_9.addItems(
            ["supplier name", "adress", "email", "contacts"])
        self.ui.comboBox_3.addItems(
            ["client name", "adress", "email", "contacts"])
        self.ui.comboBox_39.addItems(
            ["All", "locked", "active", "name"])
        self.ui.comboBox_41.addItems(
            ["All", "name"])
        self.ui.comboBox_25.addItems(
            ["All", "name"])
        self.ui.comboBox_8.addItems(curencies(self))

    def idex(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        d = cusr.execute(
            " SELECT * FROM sqlite_master WHERE type = 'index'").fetchone()
        d = (''.join(map(str, d)))

    def reset_postable_button(self):
        self.ui.pushButton_23.clicked.connect(self.reset_solditems_postable)

    def reset_solditems_postable(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("DELETE FROM pos_table")
            self.poslist = []
            self.kshpos = []
            self.itempos = []
            self.ui.lineEdit_8.clear()
            # self.ui.label_126.clear()
            database_connection.commit()
            self.load_postable_data()
            cusr.close()
            database_connection.close()
        except Exception:
            print("reset sold items")

    def load_postable_data(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT UPC , name , category , Quantity , KSH  FROM pos_table"
        result = database_connection.execute(query)
        self.ui.tableWidget_16.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_16.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_16.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("REMOVE")
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(255, 5, 42);\n"
                                  "border-radius : 25px;\n"
                                  "color : rgb(7, 7, 7); \n"
                                  "}")
                add = QPushButton("+")
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                # font.setWeight(75)
                add.setFont(font)
                
                add.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(0, 207, 0);\n"
                                  "border-radius : 25px;\n"
                                  "color : rgb(7, 7, 7); \n"
                                  "}")
                minus = QPushButton("-")
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                # font.setWeight(75)
                minus.setFont(font)
                minus.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(0, 155, 232);\n"
                                  "border-radius : 25px;\n"
                                  "color : rgb(7, 7, 7); \n"
                                  "}")
                btn.clicked.connect(self.removefrompostable)
                add.clicked.connect(self.add_quantity)
                minus.clicked.connect(self.remove_quantity)
                self.ui.tableWidget_16.setCellWidget(row_number, 7, btn)
                self.ui.tableWidget_16.setCellWidget(row_number, 5, add)
                self.ui.tableWidget_16.setCellWidget(row_number, 6, minus)

    def add_quantity(self):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_16.currentRow()
        currentcode = (self.ui.tableWidget_16.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode))) # bill number
        cusr.execute(
            "UPDATE pos_table SET Quantity=(Quantity+?) WHERE name=?",
            ("1",
             currentcode))
        database_connection.commit()
        var_x = cusr.execute(
                "SELECT selling_price FROM stock WHERE UPC=? ", (currentcode,)).fetchone()
        var_x = float(''.join(map(str, var_x)))
        quantity = cusr.execute(
                "SELECT Quantity FROM pos_table WHERE UPC=? ", (currentcode,)).fetchone()
        quantity = float(''.join(map(str, quantity)))
        total_am = var_x * quantity
        cusr.execute(
            "UPDATE pos_table SET KSH=? WHERE name=?",
            (total_am,
             currentcode))
        database_connection.commit()
        self.load_postable_data()
    def remove_quantity(self):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        row = self.ui.tableWidget_16.currentRow()
        currentcode = (self.ui.tableWidget_16.item(row, 0).text())
        currentcode = (''.join(map(str, currentcode))) # bill number
        cusr.execute(
            "UPDATE pos_table SET Quantity=(Quantity-?) WHERE name=?",
            ("1",
             currentcode))
        database_connection.commit()
        var_x = cusr.execute(
                "SELECT selling_price FROM stock WHERE UPC=? ", (currentcode,)).fetchone()
        var_x = float(''.join(map(str, var_x)))
        quantity = cusr.execute(
                "SELECT Quantity FROM pos_table WHERE UPC=? ", (currentcode,)).fetchone()
        quantity = float(''.join(map(str, quantity)))
        total_am = var_x * quantity
        cusr.execute(
            "UPDATE pos_table SET KSH=? WHERE name=?",
            (total_am,
             currentcode))
        database_connection.commit()
        self.load_postable_data()
    def pos_line(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            b = cusr.execute("SELECT SUM(count) FROM sales_count").fetchone()
            b = (''.join(map(str, b)))
            self.ui.lineEdit_7.setText(("1"))
            if b == str(None):
                self.ui.lineEdit_33.setText(("1"))
                v = int(1)
                cusr.execute("INSERT INTO sales_count(count) VALUES (?)", (v,))
                database_connection.commit()
            else:
                self.ui.lineEdit_33.setText((b))
        except Exception:
            print("sqlite3.OperationalError: database is locked")


    def search_stock_category(self):
        self.ui.pushButton_18.clicked.connect(self.searchstock)

    def search_orders(self):
        self.ui.pushButton_21.clicked.connect(self.search_orders1)

    def search_sup_btn(self):
        self.ui.pushButton_39.clicked.connect(self.search_supplier)

    def search_client_btn(self):
        self.ui.pushButton_22.clicked.connect(self.search_client)

    def search_ledger_btn(self):
        self.ui.pushButton_151.clicked.connect(self.search_ledger)

    def search_bills_btn(self):
        self.ui.pushButton_153.clicked.connect(self.search_bills)

    def search_purchase_orders_btn(self):
        self.ui.pushButton_123.clicked.connect(self.search_purchase_orders)

    def search_ledger(self):
        category = self.ui.lineEdit_80.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox_39.itemText(
                self.ui.comboBox_39.currentIndex()) == "name":
            result = database_connection.execute(
                "SELECT lg_id, name, ledger_date FROM ledgers WHERE name=?", (category,))
        elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "All":
            result = database_connection.execute(
                "SELECT lg_id, name, ledger_date FROM ledgers")
        elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "locked":
            result = database_connection.execute(
                "SELECT lg_id, name, ledger_date FROM ledgers WHERE locked=?", ("1",))
        elif self.ui.comboBox_39.itemText(self.ui.comboBox_39.currentIndex()) == "active":
            result = database_connection.execute(
                "SELECT lg_id, name, ledger_date FROM ledgers WHERE active=?", ("1",))
        TableQt.load_search_table(
            tablename = self.ui.tableWidget_25,
            column_num = [3,4], 
            funccalled = [self.set_ledger_update_page, self.all_journal_entries],  
            sqlquery = result,
            btn_name = ["Edit","Details"])
            
    def search_bills(self):
        category = self.ui.lineEdit_82.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox_41.itemText(
                self.ui.comboBox_41.currentIndex()) == "name":
            result1 = database_connection.execute(
                "SELECT bill_number, date, vendor_id, amount_due, amount_paid FROM bill WHERE bill_number=?", (category,))
        elif self.ui.comboBox_41.itemText(self.ui.comboBox_41.currentIndex()) == "All":
            result1 = database_connection.execute(
                "SELECT bill_number, date, vendor_id, amount_due, amount_paid FROM bill")
        TableQt.load_search_table(
            tablename = self.ui.tableWidget_30,
            column_num = [5,6], 
            funccalled = [self.bill_details_page, self.bill_update_page],  
            sqlquery = result1,
            btn_name = ["Details", "Update"])

    def search_purchase_orders(self):
        category = self.ui.lineEdit_64.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox_25.itemText(
                self.ui.comboBox_25.currentIndex()) == "name":
            result1 = database_connection.execute(
                "SELECT po_number, po_title, po_date, po_status, fulfilled, po_amount_recived FROM purchaseorder WHERE po_number=?", (category,))
        elif self.ui.comboBox_25.itemText(self.ui.comboBox_25.currentIndex()) == "All":
            result1 = database_connection.execute(
                "SELECT po_number, po_title, po_date, po_status, fulfilled, po_amount_recived FROM purchaseorder")
        TableQt.load_search_table(
            tablename = self.ui.tableWidget_27,
            column_num = [6], 
            funccalled = [self.details_page],  
            sqlquery = result1,
            btn_name = ["Details"])

    def search_orders1(self):
        category = self.ui.lineEdit_9.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        if self.ui.comboBox_2.itemText(
                self.ui.comboBox_2.currentIndex()) == "code":
            result = cusr.execute(
                "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders WHERE code=?",
                (category,
                 ))
        elif self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "client name":
            result = cusr.execute(
                "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders WHERE client_name=?",
                (category,
                 ))
        elif self.ui.comboBox_2.itemText(self.ui.comboBox_2.currentIndex()) == "All":
            result = cusr.execute(
                "SELECT code, client_name, grand_total, total_amount, payment_status,  order_date, due FROM orders ORDER BY id_13 DESC LIMIT 100 ")
        self.ui.tableWidget_6.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_6.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("$$$")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(0, 255, 0);;\n"
                                  "border-radius : 25px;\n"
                                  "color : rgb(7, 7, 7); \n"
                                  "}")
                rtn = QPushButton("Details")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                rtn.setFont(font)
                rtn.setStyleSheet(u"QPushButton{\n"
                                  "\n"
                                  "border-radius : 20px;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(85, 170, 255);\n"
                                  "}")
                self.push = QPushButton()
                self.push.setStyleSheet(
                    u"QPushButton{\n"
                    "\n"
                    "border-radius : 20px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	background-color: rgb(85, 170, 255);\n"
                    "}")
                icon5 = QIcon()
                icon5.addFile(
                    u":/icons/images/icons/cil-pen-alt.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                self.push.setIcon(icon5)
                self.push.setIconSize(QSize(40, 40))
                deletebtn = QPushButton()
                deletebtn.setStyleSheet(
                    u"QPushButton{\n"
                    "\n"
                    "border-radius : 20px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	background-color: rgb(85, 170, 255);\n"
                    "}")
                icon7 = QIcon()
                icon7.addFile(
                    u":/icons/images/icons/cil-remove.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                deletebtn.setIcon(icon7)
                deletebtn.setIconSize(QSize(40, 40))
                btn.clicked.connect(self.btn_triger)
                self.ui.tableWidget_6.setCellWidget(row_number, 7, btn)
                self.ui.tableWidget_6.setCellWidget(row_number, 8, self.push)
                self.ui.tableWidget_6.setCellWidget(row_number, 9, deletebtn)
                self.ui.tableWidget_6.setCellWidget(row_number, 10, rtn)
                deletebtn.clicked.connect(self.deleteorders)
                self.push.clicked.connect(self.update_orders_page)
                rtn.clicked.connect(self.set_return_orders)

    def searchstock(self):
        category = self.ui.lineEdit_10.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox.itemText(
                self.ui.comboBox.currentIndex()) == "category":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE category=?", (category,))
        elif self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()) == "name":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE name=?", (category,))
        elif self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()) == "UPC":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE UPC=?", (category,))
        elif self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()) == "vat":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE vat=?", (category,))
        elif self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()) == "Quantity":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE Quantity=?", (category,))
        elif self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()) == "Supplier":
            result = database_connection.execute(
                "SELECT * FROM stock WHERE Supplier=?", (category,))
        self.ui.tableWidget_4.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_4.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def search_client(self):
        category = self.ui.lineEdit_11.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox_3.itemText(
                self.ui.comboBox_3.currentIndex()) == "client name":
            result = database_connection.execute(
                "SELECT * FROM clients WHERE name=?", (category,))
        elif self.ui.comboBox_3.itemText(self.ui.comboBox_3.currentIndex()) == "contacts":
            result = database_connection.execute(
                "SELECT * FROM clients WHERE telno=?", (category,))
        elif self.ui.comboBox_3.itemText(self.ui.comboBox_3.currentIndex()) == "email":
            result = database_connection.execute(
                "SELECT * FROM clients WHERE email=?", (category,))
        elif self.ui.comboBox_3.itemText(self.ui.comboBox_3.currentIndex()) == "adress":
            result = database_connection.execute(
                "SELECT * FROM clients WHERE address=?", (category,))
        self.ui.tableWidget_11.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_11.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def search_supplier(self):
        category = self.ui.lineEdit_39.text()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        if self.ui.comboBox_9.itemText(
                self.ui.comboBox_9.currentIndex()) == "supplier name":
            result = database_connection.execute(
                "SELECT * FROM supplier WHERE name=?", (category,))
        elif self.ui.comboBox_9.itemText(self.ui.comboBox_9.currentIndex()) == "adress":
            result = database_connection.execute(
                "SELECT * FROM supplier WHERE addr1=?", (category,))
        elif self.ui.comboBox_9.itemText(self.ui.comboBox_9.currentIndex()) == "email":
            result = database_connection.execute(
                "SELECT * FROM supplier WHERE email=?", (category,))
        elif self.ui.comboBox_9.itemText(self.ui.comboBox_9.currentIndex()) == "contacts":
            result = database_connection.execute(
                "SELECT * FROM supplier WHERE tel1=?", (category,))
        self.ui.tableWidget_14.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_14.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_14.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
                btn = QPushButton("$$$")
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                # font.setWeight(75)
                btn.setFont(font)
                btn.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(0, 255, 0);;\n"
                                  "border-radius : 25px;\n"
                                  "color : rgb(7, 7, 7); \n"
                                  "}")
                self.push = QPushButton()
                self.push.setStyleSheet(
                    u"QPushButton{\n"
                    "\n"
                    "border-radius : 20px;\n"
                    "}\n"
                    "QPushButton:hover {\n"
                    "	background-color: rgb(85, 170, 255);\n"
                    "}")
                icon9 = QIcon()
                icon9.addFile(
                    u":/icons/images/icons/cil-pen-alt.png",
                    QSize(),
                    QIcon.Normal,
                    QIcon.Off)
                self.push.setIcon(icon9)
                self.push.setIconSize(QSize(40, 40))
                edit = QPushButton()
                edit.setStyleSheet(u"QPushButton{\n"
                                   "\n"
                                   "border-radius : 20px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: rgb(85, 170, 255);\n"
                                   "}")
                self.ui.tableWidget_14.setCellWidget(row_number, 7, btn)
                self.ui.tableWidget_14.setCellWidget(row_number, 8, self.push)
                btn.clicked.connect(self.supplier_payment_page)
                self.push.clicked.connect(self.update_supplier_page)

    def vendor_bills(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_37)
        row = self.ui.tableWidget_14.currentRow()
        currentcode = (self.ui.tableWidget_14.item(row, 1).text())
        currentcode = (''.join(map(str, currentcode)))
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        result1 = database_connection.execute(
            "SELECT bill_number, date, vendor_id, amount_due, amount_paid FROM bill WHERE vendor_id=?", (currentcode,))
        TableQt.load_search_table(
            tablename = self.ui.tableWidget_30,
            column_num = [5,6], 
            funccalled = [self.bill_details_page, self.bill_update_page],  
            sqlquery = result1,
            btn_name = ["Details", "Update"])

    def auto2(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        v = cusr.execute("SELECT name FROM stock").fetchall()
        p = [item for t in v for item in t]
        var_x = cusr.execute("SELECT name FROM supplier").fetchall()
        y = [item for t in var_x for item in t]
        
        self.completer2 = QCompleter(y)
        self.completer = QCompleter(p)
        self.ui.lineEdit_37.setCompleter(self.completer2)
        self.ui.lineEdit_38.setCompleter(self.completer)

    def updatestock_search(self):
        """function calls the updatestock function when pushButton_3 is clicked
        """
        self.ui.pushButton_3.clicked.connect(self.updatestock)

    def updatestock(self):
        """queries for data from stock table using itemname as the ID for serching,
         gets the data and sets them to the Linedits
        """
        try:
            itemname = self.ui.lineEdit_9.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            stock_name = cusr.execute(
                "SELECT name FROM stock WHERE name=? ", (itemname,)).fetchone()
            stock_name = (''.join(map(str, stock_name)))
            self.ui.lineEdit_11.setText((stock_name))
            buying_price = cusr.execute(
                "SELECT Buying_price FROM stock WHERE name=? ", (itemname,)).fetchone()
            buying_price = (''.join(map(str, buying_price)))
            self.ui.lineEdit_12.setText((buying_price))
            selling_price = cusr.execute(
                "SELECT selling_price FROM stock WHERE name=? ", (itemname,)).fetchone()
            selling_price = (''.join(map(str, selling_price)))
            self.ui.lineEdit_13.setText((selling_price))
            quantity = cusr.execute(
                "SELECT Quantity FROM stock WHERE name=? ", (itemname,)).fetchone()
            quantity = (''.join(map(str, quantity)))
            self.ui.lineEdit_14.setText((quantity))
            self.ui.lineEdit_14.setValidator(QtGui.QIntValidator())
            discount = cusr.execute(
                "SELECT Discount FROM stock WHERE name=? ", (itemname,)).fetchone()
            discount = (''.join(map(str, discount)))
            self.ui.lineEdit_15.setText((discount))
            self.ui.lineEdit_15.setValidator(QtGui.QIntValidator())
            supplier = cusr.execute(
                "SELECT Supplier FROM stock WHERE name=? ", (itemname,)).fetchone()
            supplier = (''.join(map(str, supplier)))
            self.ui.lineEdit_16.setText((supplier))
            reoder = cusr.execute(
                "SELECT reoder FROM stock WHERE name=? ", (itemname,)).fetchone()
            reoder = (''.join(map(str, reoder)))
            self.ui.lineEdit_18.setText((reoder))
            self.ui.lineEdit_18.setValidator(QtGui.QIntValidator())
            upc = cusr.execute(
                "SELECT UPC FROM stock WHERE name=? ", (itemname,)).fetchone()
            upc = (''.join(map(str, upc)))
            self.ui.lineEdit_19.setText((upc))
            category = cusr.execute(
                "SELECT category FROM stock WHERE name=? ", (itemname,)).fetchone()
            category = (''.join(map(str, category)))
            self.ui.lineEdit_17.setText((category))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'invalid operation.')

    def autocompleter(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            stock_upc = cusr.execute("SELECT UPC FROM stock").fetchall() #gets all UPC from table stock
            stock_upc_list = [item for t in stock_upc for item in t] # converts fetched stock upc from tuple to list
            self.ui.comboBox_12.addItems(stock_upc_list)
            self.ui.comboBox_15.addItems(stock_upc_list)
        except Exception:
            print("Auto completer error")

    def most_sold_table(self):
        """queries stock table for sold to display them on tableWidget_7(most sold at the dashboard)
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT UPC, name, sold FROM stock ORDER BY sold DESC "
        result = database_connection.execute(query)
        self.ui.tableWidget_7.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_7.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
     # point of sale management function
    

    def pointofsalebutton_addto_postable(self):
        pass
        # self.ui.pushButton_20.clicked.connect(self.pointofsale_addto_postable)

    def pointofsale_addto_postable(self):
        itemid = str(self.ui.comboBox_12.currentText())
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        upc_pos = cusr.execute("SELECT UPC FROM pos_table").fetchall()
        sale_no = int(str(self.ui.lineEdit_33.text()))
        upc_list = [item for t in upc_pos for item in t]
        out_of_stock = cusr.execute(
                "SELECT Quantity FROM stock WHERE UPC=? ", (itemid,)).fetchone()
        out_of_stock = int(''.join(map(str, out_of_stock)))
        if out_of_stock < 0:
            QMessageBox.warning(QMessageBox(), 'Error', 'The item is out of stock.')
        else:
            if itemid in upc_list:
                QMessageBox.warning(QMessageBox(), 'Error', 'item already exists.')
            else:
                # try:
                # item id from stock
                # items quantity in stock table at quantity column
                quantity = float(str(self.ui.lineEdit_7.text()))
                quantity2 = int(str(self.ui.lineEdit_7.text()))
                self.posappend(itemid)
                var_y = cusr.execute(
                    "SELECT (Quantity - ?) FROM stock WHERE UPC=? ", (quantity, itemid)).fetchone()
                var_j = cusr.execute(
                    "SELECT category FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                buying_price = cusr.execute(
                    "SELECT Buying_price FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                disc = cusr.execute(
                    "SELECT Discount FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                var_x = cusr.execute(
                    "SELECT name FROM stock WHERE UPC=? ",
                    (itemid,
                        )).fetchone()  # querys the name of item being sold
                b = cusr.execute(
                    "SELECT (selling_price *?) FROM stock WHERE UPC=? ",
                    (quantity,
                        itemid)).fetchone()
                b2 = cusr.execute(
                    "SELECT selling_price FROM stock WHERE UPC=? ", (itemid,)).fetchone()
                var_f = cusr.execute(
                    "SELECT vat FROM stock WHERE UPC=?", (itemid,)).fetchone()
                var_f = (''.join(map(str, var_f)))
                var_q = cusr.execute(
                    "SELECT tax_percentage FROM tax_table WHERE tax_name=?", (var_f,)).fetchone()
                var_q = float(''.join(map(str, var_q)))
                var_y = float(''.join(map(str, var_y)))
                # removes the brackets from the name queryed
                var_x = (''.join(map(str, var_x)))
                var_j = (''.join(map(str, var_j)))
                buying_price = float(''.join(map(str, buying_price)))
                disc = (''.join(map(str, disc)))
                b = float(''.join(map(str, b)))
                b2 = (''.join(map(str, b2)))
                tp = babel.numbers.format_currency(
                    decimal.Decimal(float(b)), cash_label, locale='en_US')
                # totalvat = cusr.execute(
                #     "SELECT (? / (?+100)*100)*(?/100)FROM stock WHERE UPC=?",
                #     (b,
                #      var_q,
                #      var_q,
                #      itemid)).fetchone()
                # totalvat = float(''.join(map(str, totalvat)))
                totalvat = ((var_q / 100 * b))
                sale_date = date.today()
                self.pos = cusr.execute(
                    "INSERT INTO pos_table(sale_no, UPC, name, discount, category, Quantity, KSH, KSH2, VAT, totalvat, taxcode, buying_price, sale_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (sale_no,
                        itemid,
                        var_x,
                        disc,
                        var_j,
                        quantity,
                        b,
                        b2,
                        var_q,
                        totalvat,
                        var_f,
                        buying_price,
                        sale_date))
                cusr.execute(
                    "INSERT INTO most_sold(UPC, name, KSH) VALUES (?,?,?)", (itemid, var_x, tp))
                self.point_OS[itemid] = quantity2
                # var_t = cusr.execute(
                #     "UPDATE stock SET Quantity=? WHERE UPC=? ", (var_y, itemid)).fetchone()
                self.kshposappend(b)
                self.itemposappend(itemid)
                database_connection.commit()
                self.load_postable_data()
            
                discount = cusr.execute("SELECT SUM(discount) FROM pos_table").fetchone()
                discount = float(''.join(map(str, discount)))
                
                self.total = cusr.execute(
                    "SELECT SUM(totalvat) FROM pos_table").fetchone()
                self.total = float(''.join(map(str, self.total)))
                self.totalksh = cusr.execute(
                    "SELECT SUM(KSH) FROM pos_table").fetchone()
                self.totalksh = float(''.join(map(str, self.totalksh))) 
                grand = (self.total + self.totalksh)
                discount2 = (discount / 100 * grand)
                grand_total = (grand - discount2)
                np = babel.numbers.format_currency(decimal.Decimal(
                    grand_total), cash_label, locale='en_US')
                self.ui.label_123.setText(str(np))
                self.ui.label_123.setFont(QFont("Times", 21))
                self.ui.label_123.setStyleSheet("QLabel { color : white; }")
                cusr.close()
                database_connection.close()
                # except Exception:
                #     QMessageBox.warning(
                #         QMessageBox(),
                #         'Error',
                #         'enter valid details make sure TAX are set in tax setting ')

    def pos_details(self):
        self.ui.pushButton_20.clicked.connect(self.point_of_sale_function)


    def point_of_sale_function(self):
        # try:
        selliing_price = float(str(self.ui.lineEdit_8.text()))
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.totalksh = cusr.execute(
            "SELECT SUM(KSH) FROM pos_table").fetchone()
        self.totalqua = cusr.execute(
            "SELECT SUM(Quantity) FROM pos_table").fetchone()
        self.totalksh = float(''.join(map(str, self.totalksh)))
        self.totalqua = float(''.join(map(str, self.totalqua)))
        for item in self.poslist:
            posupc = cusr.execute(
                "SELECT KSH FROM pos_table WHERE UPC=?", (item,)).fetchone()
            posupc = float(''.join(map(str, posupc)))
            print("this is the item UPC", item)
            self.g = cusr.execute(
                "UPDATE stock SET sold=(sold + ?) WHERE UPC=? ", (posupc, item)).fetchone()
        database_connection.commit()
        self.most_sold_table()
        self.add_invoice()
        # except Exception:
        # QMessageBox.warning(QMessageBox(), 'Error', 'please enter valid details')

    def add_invoice(self):
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.posksh = self.c.execute("SELECT SUM(KSH) FROM pos_table").fetchone()
        self.posksh = float(''.join(map(str, self.posksh)))
        self.totalksh = float(str(self.ui.lineEdit_8.text()))
        
        discount = self.c.execute("SELECT SUM(discount) FROM pos_table").fetchone()
        discount = float(''.join(map(str, discount)))
        buying_price = self.c.execute("SELECT SUM(buying_price) FROM pos_table").fetchone()
        buying_price = float(''.join(map(str, buying_price)))

        client_name = str(self.ui.lineEdit_14.text())
        self.total = self.c.execute("SELECT SUM(totalvat) FROM pos_table").fetchone()
        self.total = float(''.join(map(str, self.total)))
        print(f"........./...POS............../")
        print(f"TOTAL DISCOUNT ---> {discount}")
        # pos.pos(self)
        print(f"dict{self.point_OS}")
        for key, value in self.point_OS.items():
            print(f"value ->{value}")
            print(f"key ->{key}")
            key2 = str(key)
            value2 = int(value)
            self.c.execute("UPDATE stock SET Quantity=(Quantity-?) WHERE UPC=? ", (value2, key2))
            self.connection.commit()
        

        total_amount = (self.total + self.posksh)

        discount2 = (discount / 100 * total_amount)
        discount3 = (discount / 100 * self.posksh)
        grand_total = (total_amount - discount2)
        print(f"DISCOUNT ON product ---> {discount2}")
        print(f"Grand TOTAL AFTER DEDUCTION OF DISCOUNT ---> {grand_total}")
        total_no_tax = (self.posksh - discount3)
        amount_paid = float(str(self.ui.lineEdit_8.text()))
        due = (grand_total - amount_paid)
        print(f"DUE AMOUNT ---> {due}")
        due2 = (total_no_tax - amount_paid)
        if due < 0:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Due error, Due amount cant be less than 0')
        else:
            item_code = str(self.ui.lineEdit_33.text())
            payment_type = str(self.ui.comboBox_4.currentText())
            payment_status = str(self.ui.comboBox_5.currentText())

            code = str(self.ui.lineEdit_16.text())
            order_date = date.today()
            credit = "credit"
            debit = "debit"
            description = ("sold goods on credit to" + " " + client_name)
            description2 = ("sold goods on credit to" + " " + client_name)
            name = ("Debitor" + "," + " " + client_name + item_code)
            terms = str(self.ui.comboBox_20.currentText())
            invoice_status = str(self.ui.comboBox_21.currentText())
            ledger_uuid = uuid.uuid4().hex
            invoice_uuid = uuid.uuid4().hex
            combo1,combo2 = '0', '1'
            invoice_number = ('INVOICE-' + (''.join(random.choices(string.ascii_uppercase, k=12))))
            date_1 = date.today()
            created = dt.today()
            updated = dt.today()
            journal_uuid = uuid.uuid4().hex
            uuid1 = uuid.uuid4().hex
            uuid2 = uuid.uuid4().hex
            uuid3 = uuid.uuid4().hex
            uuid6 = uuid.uuid4().hex
            uuid8 = uuid.uuid4().hex
            markdown_notes = self.ui.plainTextEdit_5.document().toPlainText()

            # try:
            self.c.execute(
                "INSERT INTO orders(uuid, created, sale_no, updated, terms, item_code, discount,  paid_amount, code, client_name, grand_total, total_amount, sub_total, payment_type, payment_status,  order_date, due, invoice_status, markdown_notes, ledger_uuid) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    invoice_uuid,
                    created,
                    item_code,
                    updated,
                    terms,
                    invoice_number,
                    discount,
                    amount_paid,
                    invoice_number,
                    client_name,
                    grand_total,
                    total_amount,
                    self.posksh,
                    payment_type,
                    payment_status,
                    order_date,
                    due,
                    invoice_status,
                    markdown_notes,
                    ledger_uuid
                    ))
            self.connection.commit()
            
            self.c.execute("INSERT INTO ledgers(id, name, locked, active, ledger_date) VALUES (?,?,?,?,?)",(ledger_uuid, invoice_number,combo1,combo2,date_1))
            self.connection.commit()
            

            if due > 0:
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid1,
                    created,
                    updated,
                    "currentassets",
                    journal_uuid,
                    ledger_uuid,
                    'Accounts Receivable',
                    due,
                    description,
                    debit,
                    order_date))
                self.connection.commit()
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid2,
                    created,
                    updated,
                    "revenue",
                    journal_uuid,
                    ledger_uuid,
                    'Product Sales',
                    due2,
                    description,
                    credit,
                    order_date))
                self.connection.commit()
                self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "operating", description, "1", "0", order_date))
                self.connection.commit()
            else:
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid2,
                    created,
                    updated,
                    "revenue",
                    journal_uuid,
                    ledger_uuid,
                    'Product Sales',
                    total_no_tax,
                    description2,
                    credit,
                    order_date))
                self.connection.commit()
                self.c.execute(
                        "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (uuid3,
                        created,
                        updated,
                        "currentassets",
                        journal_uuid,
                        ledger_uuid,
                        'cash and cash equivalents',
                        amount_paid,
                        description2,
                        debit,
                        order_date))
                self.connection.commit()
                self.c.execute(
                "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid8,
                    created,
                    updated,
                    "currentassets",
                    journal_uuid,
                    ledger_uuid,
                    "inventory",
                    buying_price,
                    description,
                    "credit",
                    order_date))
                self.connection.commit()
                self.c.execute(
                    "INSERT INTO transactions(uuid, updated, created, coa_id, journal_entry_id, ledger_id, name, KSH, description, tx_type, transactionsdate) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (uuid6,
                    created,
                    updated,
                    "expenses",
                    journal_uuid,
                    ledger_uuid,
                    "cost of goods sold",
                    buying_price,
                    description,
                    "debit",
                    order_date))
                self.connection.commit()
                self.c.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, "other", description, "1", "0", order_date))
                self.connection.commit()

            self.c.execute(
                "INSERT INTO sales SELECT sale_no, UPC, name, category, Quantity, KSH, VAT, totalvat, taxcode, sale_date FROM pos_table")
            bn = self.c.execute("SELECT * FROM sales").fetchall()

            current_num = int(str(self.ui.lineEdit_33.text()))
            new_num = int(current_num + 1)
            new = str(current_num + 1)
            self.c.execute("UPDATE sales_count SET count=?", (new_num,))
            self.connection.commit()
            self.ui.lineEdit_33.setText((new))
            self.c.execute("DELETE FROM pos_table")
            self.poslist = []
            self.kshpos = []
            self.itempos = []
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_16.clear()
            # self.ui.label_126.clear()
            self.connection.commit()
            self.load_postable_data()
            orders_function.setButtons(self)
            
            
            self.c.close()
            self.connection.close()

            QMessageBox.information(
                QMessageBox(),
                'Successful',
                    'Item is added successfully to the database.')
            # except Exception:
            #     QMessageBox.warning(
            #         QMessageBox(),
            #         'Error',
            #         'Could not add Item to the database, Make sure the VAT is set in the tax setting.')
            np = babel.numbers.format_currency(
                decimal.Decimal(grand_total), cash_label, locale='en_US')
            self.ui.label_114.setText(str(np))


    def s_t(self):
        self.ui.pushButton_2.clicked.connect(self.stock_turn)

    def stock_turn(self):
        try:
            cost = str(self.ui.lineEdit_3.text())
            o_s = str(self.ui.lineEdit_4.text())
            c_s = str(self.ui.lineEdit_5.text())
            avg = float(o_s) + float(c_s)
            ass = float(avg / 2.0)
            stockturnover = (float(cost) / float(ass))
            self.ui.label_122.setText(str(stockturnover))
            self.ui.label_122.setFont(QFont("Times", 22))
            self.ui.label_122.setStyleSheet("QLabel { color : white; }")
            self.ui.label_83.setText(str(stockturnover))
            self.ui.label_83.setFont(QFont("Times", 20))
            self.ui.label_83.setStyleSheet("QLabel { color : white; }")
            return stockturnover
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'please enter value')

    def act(self):
        app.exit()

    def net_profit(self):
        """_calculates the net profit_

        Returns:
            _float_: _net profit_
        """
        try:
            if self.total_sales() > self.total_expenses():
                n_p = self.total_sales() - self.total_expenses()
                net_profit = babel.numbers.format_currency(
                    decimal.Decimal(n_p), cash_label, locale='en_US')
                self.ui.label_35.setText(str(net_profit))
                self.ui.label_35.setFont(QFont("Times", 15))
                self.ui.label_35.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                return n_p
            else:
                n_p = self.total_sales() - self.total_expenses()
                net_profit = babel.numbers.format_currency(
                    decimal.Decimal(n_p), cash_label, locale='en_US')
                self.ui.label_35.setText(str(net_profit))
                self.ui.label_35.setFont(QFont("Times", 15))
                self.ui.label_35.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                self.ui.label_34.setText("LOSS")
                self.ui.label_34.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                return n_p
        except Exception:
            print("print net profit error")

    def gross_pr(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        qdate = self.ui.dateEdit_4.date()
        order_date = qdate.toPython()
        qdate = self.ui.dateEdit_5.date()
        order_date2 = qdate.toPython()
        alltb = cusr.execute(
            "SELECT SUM(total_amount) FROM sales_returns WHERE return_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        paid = cusr.execute(
            "SELECT SUM(paid) FROM payment WHERE payment_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_income = cusr.execute(
            "SELECT SUM(amount) FROM income WHERE income_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_income = float(''.join(map(str, total_income)))
        total_sales = cusr.execute(
            "SELECT SUM(paid_amount) FROM orders WHERE order_date BETWEEN ? AND ?",
            (order_date,
             order_date2)).fetchone()
        total_sales = float(''.join(map(str, total_sales)))
        paid = (''.join(map(str, paid)))
        alltb = (''.join(map(str, alltb)))
        if alltb == str(None):
            alltb = 0
        else:
            alltb = float(''.join(map(str, alltb)))
        if paid == str(None):
            paid = 0
        else:
            paid = float(''.join(map(str, paid)))
        gross_profit = ((total_income + total_sales + paid) - alltb)
        return gross_profit

    def gross_profit(self):
        try:
            if self.total_sales() > self.sum_var_exp():
                g_p = round(self.total_sales() - self.sum_var_exp())
                tp = babel.numbers.format_currency(
                    decimal.Decimal(g_p), cash_label, locale='en_US')
                self.ui.label_23.setText(str(tp))
                self.ui.label_23.setFont(QFont("Times", 20))
                self.ui.label_23.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                return g_p
            else:
                g_p = self.total_sales() - self.sum_var_exp()
                tp = babel.numbers.format_currency(
                    decimal.Decimal(g_p), cash_label, locale='en_US')
                self.ui.label_23.setText(str(tp))
                self.ui.label_23.setFont(QFont("Times", 20))
                self.ui.label_23.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                self.ui.label_32.setText("LOSS")
                self.ui.label_32.setStyleSheet(
                    "QLabel { background-color : rgb(29, 29, 29 ); color : rgb(0, 255, 255); }")
                return g_p
        except BaseException:
            print("gross profit error")

    def total_sales(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            total_paid = cusr.execute(
            "SELECT SUM(KSH) FROM transactions WHERE name=?",
            ("Product Sales",)).fetchone()
            total_paid = (''.join(map(str, total_paid)))
            if total_paid == str(None):
                total_paid = 0.00
            else:
                total_paid = float(''.join(map(str, total_paid)))
            return total_paid
        except BaseException:
            print("total sales error")

    def total_expenses(self):
        try:
            self.z = self.sum_fix_exp() + self.sum_var_exp()
            b = babel.numbers.format_currency(
                decimal.Decimal(self.z), cash_label, locale='en_US')
            self.ui.label_192.setText(str(b))
            self.ui.label_192.setFont(QFont("Times", 20))
            return self.z
        except Exception:
            # self.ui.label_113.setText("fixed expense or variable expense is empty ")
            print('total expense.')

    def total_liability(self):
        """calculates total liabilities
        Returns:
            _float_: _short term liabilities + long term liabilities_
        """
        try:
            self.z = self.sum_short_term() + self.sum_long_term()
            b = babel.numbers.format_currency(
                decimal.Decimal(self.z), cash_label, locale='en_US')
            self.ui.label_196.setText(b)
            self.ui.label_196.setFont(QFont("Times", 20))
            self.ui.label_26.setText(b)
            self.ui.label_26.setFont(QFont("Times", 20))
            return self.z
        except Exception:
            print("total liabilities error")

    def total_asset(self):
        """calculates total assets

        Returns:
            _float_: _sum of fixed and current asset_
        """
        try:
            self.z = self.sumCurrent_asset() + self.sumfixed_asset()
            b = babel.numbers.format_currency(
                decimal.Decimal(self.z), cash_label, locale='en_US')
            self.ui.label_198.setText(b)
            self.ui.label_198.setFont(QFont("Times", 20))
            self.ui.label_25.setText(b)
            self.ui.label_25.setFont(QFont("Times", 20))
            return self.z
        except Exception:
            print("total assets error")

    def sum_var_exp(self):
        """calculates total variable expenses

        Returns:
            _float_: _sum variable expense_
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        coa_account = "expenses"
        var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
        var_x = (''.join(map(str, var_x)))
        if var_x == str(None):
            var_x = 0.00
        else:
            var_x = float(''.join(map(str, var_x)))
            b = babel.numbers.format_currency(
                decimal.Decimal(var_x), cash_label, locale='en_US')
        return var_x

    def sum_fix_exp(self):
        """calculates sum of fixed expense

        Returns:
            _float_: _total fixed expenses_
        """
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            coa_account = "fixedexpenses"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.00
            else:
                var_x = float(''.join(map(str, var_x)))
            return var_x
        except Exception:
            print("sum fix expe error")

    def sum_long_term(self):
        """calculates sum of long term liabilities

        Returns:
            _float_: _total longterm liabilities_
        """
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            coa_account = "Longtermliabilities"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.0
            else:
                var_x = float(''.join(map(str, var_x)))
            return var_x
        except Exception:
            print("sum long term  error")

    def sum_short_term(self):
        """calculates sum shortterm liabilitiy

        Returns:
            _float_: _total shortterm liabilitiy_
        """
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            coa_account = "currentliabilities"
            var_x = cusr.execute(
                "SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.0
            else:
                var_x = float(''.join(map(str, var_x)))
            return var_x
        except Exception:
            print("sum short lib error")

    def sumCurrent_asset(self):
        """calculates sum current asset

        Returns:
            _float_: _total current asset_
        """
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            coa_account = "currentassets"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.0
            else:
                var_x = float(''.join(map(str, var_x)))
            return var_x
        except Exception:
            print("sum current asset error")

    def sumfixed_asset(self):
        """calculates sum fixed asset

        Returns:
            _float_: _total fixed asset_
        """
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            coa_account = "fixedassets"
            var_x = cusr.execute("SELECT SUM(KSH) FROM transactions WHERE coa_id=?", (coa_account,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            if var_x == str(None):
                var_x = 0.0
            else:
                var_x = float(''.join(map(str, var_x)))
            return var_x
        except Exception:
            print("sum fixed asset")

    def Margin(self):
        try:
            d_r = (self.gross_profit() / self.total_sales()) * 100
            progress = CircularProgress()
            progress.width = 100
            progress.height = 100
            progress.value = 0
            progress.setFixedSize(progress.width, progress.height)
            progress.font_size = 20
            progress.add_shadow(True)
            progress.progress_width = 4
            progress.progress_color = QColor("#bdff00")
            progress.text_color = QColor("#E6E6E6")
            progress.bg_color = QColor("#222222")
            progress.setParent(self.ui.frame_10)
            progress.show()
            progress.set_value((round(d_r, 2)))
        except Exception:
            print('Error', 'gross profit or total sales is empty.')
    # MARGIN FUNCTION

    def debt_percentage(self):
        try:
            d_r = (self.total_liability() / self.total_asset()) * 100
            progress = CircularProgress()
            progress.width = 100
            progress.height = 100
            progress.value = 0
            progress.setFixedSize(progress.width, progress.height)
            progress.font_size = 20
            progress.add_shadow(False)
            progress.progress_width = 4
            progress.progress_color = QColor("#bdff00")
            progress.text_color = QColor("#E6E6E6")
            progress.bg_color = QColor("#222222")
            progress.setParent(self.ui.preloader)
            progress.show()
            progress.set_value((round(d_r, 2)))
        except Exception:
            print("debt percentage error")

    def Netprofit_Margin(self):
        try:
            d_r = (self.net_profit() / self.total_sales()) * 100
            d_r = round(d_r, 2)
            progress = CircularProgress()
            progress.width = 100
            progress.height = 100
            progress.value = 0
            progress.setFixedSize(progress.width, progress.height)
            progress.font_size = 20
            progress.add_shadow(True)
            progress.progress_width = 4
            progress.progress_color = QColor("#bdff00")
            progress.text_color = QColor("#E6E6E6")
            progress.bg_color = QColor("#222222")
            progress.setParent(self.ui.frame_18)
            progress.show()
            progress.set_value((d_r))
        except Exception:
            print('Error', 'Could not add expense to the database.')

    def working_capital(self):
        try:
            w_r = round(self.sumCurrent_asset() - self.sum_short_term())
            tp = babel.numbers.format_currency(
                decimal.Decimal(w_r), cash_label, locale='en_US')
            self.ui.label_108.setText(str(tp))
            self.ui.label_108.setFont(QFont("Times", 15))
            #self.ui.label_108.setStyleSheet("QLabel { background-color : rgb(34, 34, 34 ); color : rgb(0, 255, 255); }")
            return w_r
        except Exception:
            print("working capital error")

    def capital_employed(self):
        try:
            c_e = round(self.sumfixed_asset() + self.working_capital())
            tp = babel.numbers.format_currency(
                decimal.Decimal(c_e), cash_label, locale='en_US')
            self.ui.label_109.setText(str(tp))
            self.ui.label_109.setFont(QFont("Times", 15))
            #self.ui.label_109.setStyleSheet("QLabel { background-color : rgb(34, 34, 34 ); color : rgb(0, 255, 255); }")
            return c_e
        except Exception:
            print("capital employed error")

    def debt_ratio(self):
        try:
            d_r = self.total_liability() / self.total_asset()
            self.ui.label_12.setText(str(round(d_r, 2)))
            self.ui.label_12.setFont(QFont("Times", 20))
            return d_r
        except Exception:
            print('Error', 'liability table or assets is empty.')

    def current_ratio(self):
        try:
            c_r = self.sumCurrent_asset() / self.sum_short_term()
            self.ui.label_18.setText(str(round(c_r, 2)))
            self.ui.label_18.setFont(QFont("Times", 20))
            return c_r
        except Exception:
            print("error, sumCurrent_asset and sum_short_term")



    def delete(self):
        dlg = DeleteDialog()
        dlg.exec()
        # SHOW ==> MAIN WINDOW         ########################################
        self.show()
        # ==> END

    def delete10(self):
        dlg = clientDeleteDialog()
        dlg.exec()
        self.show()


    def loaddata9(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            query = "SELECT UPC, name, Buying_price, selling_price, Quantity, Supplier, category, reoder, Discount, vat, stockdate FROM stock"
            result = database_connection.execute(query)
            self.ui.tableWidget_4.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget_4.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget_4.setItem(
                        row_number,
                        column_number,
                        QTableWidgetItem(
                            str(data)))
            database_connection.close()
            self.autocompleter()
            orders_function.items_worth(self)
            orders_function.total_orders(self)
            orders_function.total_cogs(self)
        except Exception:
            print("stock error")

    def loaddata13(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM income"
        result = database_connection.execute(query)
        self.ui.tableWidget_13.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget_13.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget_13.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))
        database_connection.close()

    def onEmployeeBtnClicked(self):
        """Launch the employee dialog."""
        dlg = EmployeeDlg(self)
        dlg.exec()

    def add_ledger(self):
        """calls the AddLedger dialouge
        """
        dlg = AddLedger(self)
        dlg.exec()
        self.load_ledgers()

    def add_journalentry(self):
        """calls the AddJournalEntry dialouge
        """
        dlg = AddJournalEntry(self)
        dlg.exec()

    def add_po(self):
        """calls the AddJournalEntry dialouge
        """
        dlg = AddPurchaseOrder(self)
        dlg.exec()
        PurchaseOrder.purchase_order_load_table(self)
    def add_bill(self):
        """calls the AddJournalEntry dialouge
        """
        dlg = AddBill(self)
        dlg.exec()
        bills.Bill.bill_load_table(self)

    def profileedit(self):
        dlg = profileEdit(self)
        dlg.exec()


    def salesedit(self):
        dlg = salesEedit(self)
        dlg.exec()

    def stockadd(self):
        dlg = stockAdd(self)
        dlg.exec()

    def updatestock2(self):
        dlg = Update(self)
        dlg.exec()

    def bizdet(self):
        dlg = Bizdetails(self)
        dlg.exec()

    def taxsettings(self):
        dlg = Taxsettings(self)
        dlg.exec()

    def editincome(self):
        dlg = incomeEdit(self)
        dlg.exec()
    def logout_dialog(self):
        dlg = LogoutUser(self)
        dlg.exec()

    def chart_of_acc(self):
        dlg = coa(self)
        dlg.exec()
        self.coa_load()
    def add_department(self):
        dlg = AddDepartment(self)
        dlg.exec()
        hrms.load_department_hrms(self)
    def user_managment(self):
        dlg = UserManagment(self)
        dlg.exec()
        admin.load_user_managment(self)

    def add_position(self):
        dlg = AddPosition(self)
        dlg.exec()
        hrms.load_positions_hrms(self)
    def add_uom(self):
        dlg = AddUOM(self)
        dlg.exec()
        uom.load_uom(self)
        # hrms.load_positions_hrms(self)

    def add_employee(self):
        dlg = AddEmployee(self)
        dlg.exec()
        hrms.load_employee_hrms(self)



class EmployeeDlg(QDialog):
    """Employee dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.update_postable)

    def update_postable(self):
        number = self.ui.lineEdit_2.text()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("DELETE from pos_table WHERE UPC=?", (number,))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'expense is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete.')




class AddLedger(QDialog):
    """a dialogue that adds new ledger to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_Add_Ledger()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_ledger)

    def add_ledger(self):
        try:

            """_ gets data from the database and sets them to the Line 
            edits using itemname as the ID for serching _
            """
            
            ledger_name = self.ui.lineEdit_22.text()
            # combo1 = self.ui.checkBox
            # combo2 = self.ui.checkBox_2
            ledger_date = date.today()
            ledger_uuid = uuid.uuid4().hex
            if self.ui.checkBox.isChecked() == True:
                combo2 = "0"
                combo1="1"
            elif self.ui.checkBox_2.isChecked() == False and self.ui.checkBox.isChecked() == False:
                combo2 = "1"
                combo1="0"
            elif self.ui.checkBox_2.isChecked() == True and self.ui.checkBox.isChecked() == True:
                combo2 = "1"
                combo1="0"

            elif self.ui.checkBox_2.isChecked() == True:
                combo2 = "1"
                combo1="0"
            else:
                combo2 = "1"
            

            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("INSERT INTO ledgers(id, name, locked, active, ledger_date) VALUES (?,?,?,?,?)",(ledger_uuid, ledger_name,combo1,combo2,ledger_date))
            database_connection.commit()
            QMessageBox.information(QMessageBox(),'Successfull', "Ledger added Successfully")
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add ledger.')



class AddJournalEntry(QDialog):
    """a dialogue that adds new journal entry to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_journal_entry()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_journal_entey)
        activity = [
        'Operating',
        'Financing',
        'Investing',
        'other']
        self.ui.comboBox.addItems(activity)

    def add_journal_entey(self):
        """_ gets data from the database and sets them to the Line 
        edits using itemname as the ID for serching _
        """
        
        description = self.ui.lineEdit_22.text()
        activities = str(self.ui.comboBox.currentText())
        combo1 = self.ui.checkBox
        combo2 = self.ui.checkBox_2
        qdate = self.ui.dateEdit.date()
        journal_date = qdate.toPython()
        journal_uuid = uuid.uuid4().hex
        ledger_uuid = str(ledger_id[0])
        if combo1.isChecked() == True:
            combo1 = "1"
        else:
            combo1="0"
        if combo2.isChecked() == True:
            combo2 = "1"
        else:
            combo2 = "0"

        print(combo1)
        print(combo2)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("INSERT INTO journal_entries(id, ledger_id, activity, description, posted, locked, journal_entrydate) VALUES (?,?,?,?,?,?,?)",(journal_uuid, ledger_uuid, activities, description, combo1, combo2, journal_date))
        database_connection.commit()



class AddPurchaseOrder(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_DialogPurchaseOrder()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_purchase_order)

    def add_purchase_order(self):
        try:    
            po_title = self.ui.lineEdit_22.text() 
            created = dt.today()
            updated = dt.today()
            p_date = self.ui.dateEdit.date()
            po_date = p_date.toPython()
            po_uuid = uuid.uuid4().hex
            notes = ' '
            po_number = (''.join(random.choices(string.ascii_uppercase, k=9)))
            po_amount_recived = 0
            fulfilled = ' '
            fulfillment_date = ' '
            po_status = 'Draft'
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("INSERT INTO purchaseorder(uuid, created, updated, notes, po_number, po_date, po_title, po_amount_recived, fulfilled, fulfillment_date, po_status) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(
                po_uuid,
                created,
                updated,
                notes,
                po_number,
                po_date,
                po_title,
                po_amount_recived,
                fulfilled,
                fulfillment_date,
                po_status))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Purchase Order is added successfully to the database.')
        except Exception:
            print(Exception)


class AddEmployee(QDialog):
    """a dialogue that adds new Employee to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Employee()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_employee)
        status = [
        'active',
        'inactive',
        ]
        gender = [
        'Male',
        'Female',
        'other'
        ]
        d = self.c.execute(
        "SELECT dep_name FROM department ").fetchall()
        b = [item for t in d for item in t]

        position = self.c.execute(
        "SELECT pos_name FROM positions ").fetchall()
        position_name = [item for t in position for item in t]

        self.ui.comboBox_4.addItems(status)
        self.ui.comboBox_3.addItems(b)
        self.ui.comboBox.addItems(gender)
        self.ui.comboBox_2.addItems( position_name)

    def add_employee(self):   
        created = dt.today()
        updated = dt.today()
        emp_uuid = uuid.uuid4().hex    
        qdate = self.ui.dateEdit.date()
        employee_start_date = qdate.toPython()
        employee_code = str(self.ui.lineEdit.text())
        employee_first_name = str(self.ui.lineEdit_2.text())
        employee_last_name = str(self.ui.lineEdit_3.text())
        employee_mobile = str(self.ui.lineEdit_4.text())
        employee_email = str(self.ui.lineEdit_5.text())
        employee_addres = str(self.ui.lineEdit_6.text())
        gender = str(self.ui.comboBox.currentText())
        position = str(self.ui.comboBox_2.currentText())
        employee_depertment = str(self.ui.comboBox_3.currentText())
        status = str(self.ui.comboBox_2.currentText())
        bank, salary = " ", " "
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("INSERT INTO employee(created, updated, uuid, emp_code, first_name, last_name, mobile, email, address, gender, emmp_postion, department, joined, bank, salary) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
            created,
            updated,
            emp_uuid,
            employee_code,
            employee_first_name,
            employee_last_name,
            employee_mobile,
            employee_email,
            employee_addres,
            gender,
            position,
            employee_depertment,
            employee_start_date,
            bank,
            salary))
        database_connection.commit()


class AddPosition(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Position()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_position)
        status = [
        'active',
        'inactive',
        ]
        d = self.c.execute(
        "SELECT dep_name FROM department ").fetchall()
        b = [item for t in d for item in t]
        self.ui.comboBox_2.addItems(status)
        self.ui.comboBox.addItems(b)

    def add_position(self):   
        created = dt.today()
        updated = dt.today()
        status = str(self.ui.comboBox_2.currentText())
        position_level =" "
        position_name = str(self.ui.lineEdit_4.text())
        position_code = str(self.ui.lineEdit.text())
        position_depertment = str(self.ui.comboBox.currentText())
        position_description = self.ui.plainTextEdit.document().toPlainText()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("INSERT INTO positions(created, updated, pos_name, pos_code, pos_level, pos_description, pos_depertment, status) VALUES (?,?,?,?,?,?,?,?)",(
            created,
            updated,
            position_name,
            position_code,
            position_level,
            position_description,
            position_depertment,
            status))
        database_connection.commit()

class AddUOM(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_UOM()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_uom)
        status = [
        'active',
        'inactive',
        ]

        self.ui.comboBox.addItems(status)

    def add_uom(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            user_uuid = str(who_is_logged[1])
            created = dt.today()
            updated = dt.today()
            status = str(self.ui.comboBox.currentText())
            name = str(self.ui.lineEdit.text())
            abbr = str(self.ui.lineEdit_2.text())
            
            cusr.execute("INSERT INTO uom(created, updated, unit_abbr, name, is_active, user_uuid) VALUES (?,?,?,?,?,?)",(
                created,
                updated,
                abbr,
                name,
                status,
                user_uuid))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'unit of measure is added successfully to the database.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add uint of measure to the database.')




class AddDepartment(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Departments()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_department)
        status = [
        'active',
        'inactive',
        ]
        department_level = [
        'First Level',
        'Second Level',
        'Third Level',
        'Fourth Level',
        'Fifth Level',
        ]
        self.ui.comboBox_3.addItems(status)
        self.ui.comboBox.addItems(department_level)

    def add_department(self):   
        created = dt.today()
        updated = dt.today()
        status = str(self.ui.comboBox_3.currentText())
        department_level = str(self.ui.comboBox.currentText())
        department_name = str(self.ui.lineEdit_2.text())
        department_code = str(self.ui.lineEdit.text())
        department_supirior = str(self.ui.comboBox_2.currentText())
        department_description = self.ui.plainTextEdit.document().toPlainText()
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        cusr.execute("INSERT INTO department(created, updated, dep_name, dep_code, dep_level, dep_description, dep_supirior, status) VALUES (?,?,?,?,?,?,?,?)",(
            created,
            updated,
            department_name,
            department_code,
            department_level,
            department_description,
            department_supirior,
            status))
        database_connection.commit()
class UserManagment(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_User_managment()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_asignee)
        status = [
        'active',
        'inactive',
        ]
        assign = [
        'Accounts',
        'POS',
        'HR',
        'Inventory',
        'CRM',
        ]
        employees = self.c.execute("SELECT first_name FROM employee").fetchall()
        employees_names = [item for t in employees for item in t]
        self.ui.comboBox_2.addItems(status)
        self.ui.comboBox_4.addItems(assign)
        self.ui.comboBox_3.addItems(employees_names)

    def add_asignee(self):
        password = str(self.ui.lineEdit_2.text())
        password2 = str(self.ui.lineEdit_4.text())
        username = str(self.ui.lineEdit_3.text())
        if len(password) < 8:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Password too short.')
        elif username == "":
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Username is required.')
        elif password != password2:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Password dosent match.')
        else:
            salt = uuid.uuid4().hex
            hashed_password =  str(hashlib.sha512(password.encode('utf-8')+salt.encode('utf-8')).hexdigest())
            created = dt.today()
            updated = dt.today()
            employee_name = str(self.ui.comboBox_3.currentText())
            role = str(self.ui.comboBox_5.currentText())
            username = str(self.ui.lineEdit_3.text())
            
            assign = str(self.ui.comboBox_4.currentText())
            status = str(self.ui.comboBox_2.currentText())
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("INSERT INTO user_managment(created, updated, employee_name, username, password, role,  assign, status) VALUES (?,?,?,?,?,?,?,?)",(
                created,
                updated,
                employee_name,
                username,
                hashed_password,
                role,
                assign,
                status))
            
            try:
                reqUrl = "http://localhost:8080/add_user/"

                headersList = {
                "Accept": "*/*",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "user": "e5477848-3fae-43b-967d-7fb094fd280b",
                "Content-Type": "application/json" 
                }

                payload = json.dumps({
                    "employee_name": employee_name,
                    "username": username,
                    "password": password,
                    "role": "Accounts",
                    "assign": assign,
                    "status": status
                })

                requests.request("POST", reqUrl, data=payload,  headers=headersList)
                database_connection.commit()
                QMessageBox.information(
                    QMessageBox(),
                    'Successful',
                    'User is added successfully to the database.')
            except Exception:
                QMessageBox.warning(
                    QMessageBox(),
                    'Error',
                    'Connection problem')


class AddBill(QDialog):
    """a dialogue that adds new purchase order to the database
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_Bills()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.connection = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        self.c = self.connection.cursor()
        self.ui.pushButton.clicked.connect(self.add_bill)
        terms = [
        'Due on receipt',
        'Net 30 Days',
        'Net 60 Days',
        'Net 90 Days',
        ]
        self.ui.comboBox_5.addItems(terms)
        d = self.c.execute(
        "SELECT name FROM supplier ").fetchall()
        b = [item for t in d for item in t]
        code = '1010'
        code2 = '1400'
        code3 = '2490'
        tx = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE code=? ", (code,)).fetchall()
        pr_e = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE code=? ", (code2,)).fetchall()
        unnerned = self.c.execute(
        "SELECT account FROM chart_of_accounts WHERE code=? ", (code3,)).fetchall()
        vb = [item for t in tx for item in t]
        prepaid = [item for t in pr_e for item in t]
        unnerned_acc = [item for t in unnerned for item in t]
        self.ui.comboBox.addItems(b)
        self.ui.comboBox_3.addItems(vb)
        self.ui.comboBox_4.addItems(prepaid)
        self.ui.comboBox_2.addItems(unnerned_acc)

    def add_bill(self):
        try:
            bill_uuid = uuid.uuid4().hex    
            ledger_uuid = uuid.uuid4().hex    
            created = dt.today()
            updated = dt.today()
            terms = str(self.ui.comboBox_5.currentText())
            amount_due = 0.0
            amount_paid = 0.0
            amount_recivable = 0.0
            amount_unerned = 0.0
            amount_earned = 0.0
            paid = 0.0
            paid_date = ' '
            date_1 = date.today()
            d_date = self.ui.dateEdit.date()
            due_date = d_date.toPython()
            xref = self.ui.lineEdit.text()
            accrue = ' '
            bill_number = ('BILL-' + (''.join(random.choices(string.ascii_uppercase, k=15))))
            if purchase_order_bill_uuid == []:
                ispurchase_order = '0'
                purchase_order_bill_uuid_list = ' '
            else:
                purchase_order_bill_uuid_list = purchase_order_bill_uuid[0]
                ispurchase_order = '1'

            cash_account_id_combo = str(self.ui.comboBox_3.currentText())
            cash_account_id = self.c.execute(
            "SELECT code FROM chart_of_accounts WHERE account=? ", (cash_account_id_combo,)).fetchone()
            cash_account_id = (''.join(map(str, cash_account_id)))

            prepaid_account_id_combo = str(self.ui.comboBox_4.currentText())
            prepaid_account_id = self.c.execute(
            "SELECT code FROM chart_of_accounts WHERE account=? ", (prepaid_account_id_combo,)).fetchone()
            prepaid_account_id = (''.join(map(str, prepaid_account_id)))

            unearned_account_id_combo = str(self.ui.comboBox_2.currentText())
            unearned_account_id = self.c.execute(
            "SELECT code FROM chart_of_accounts WHERE account=? ", (unearned_account_id_combo,)).fetchone()
            unearned_account_id = (''.join(map(str, unearned_account_id)))
            ledger_id = ' '
            vendor_id = str(self.ui.comboBox.currentText())
            combo1,combo2 = '0', '0'
            bill_status = 'Draft'
            markdown_notes = ' '
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("INSERT INTO bill(created, updated, terms, amount_due, amount_paid, amount_recivable, amount_unerned, amount_earned, paid, paid_date, date, due_date, xref, accrue, uuid, bill_number, cash_account_id, ledger_id, prepaid_account_id, unearned_account_id, ispurchase_order, purchase_order_uuid, vendor_id, bill_status, markdown_notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                created,
                updated,
                terms,
                amount_due,
                amount_paid,
                amount_recivable,
                amount_unerned,
                amount_earned,
                paid,
                paid_date,
                date_1,
                due_date,
                xref,
                accrue,
                bill_uuid,
                bill_number,
                cash_account_id,
                ledger_id,
                prepaid_account_id,
                unearned_account_id,
                ispurchase_order,
                purchase_order_bill_uuid_list,
                vendor_id,
                bill_status,
                markdown_notes))
            database_connection.commit()
            cusr.execute("INSERT INTO ledgers(id, name, locked, active, ledger_date) VALUES (?,?,?,?,?)",(ledger_uuid, bill_number,combo1,combo2,date_1))
            database_connection.commit()
            purchase_order_bill_uuid.clear()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Bill is added successfully to the database.')
        except Exception:
            print(Exception)



class incomeEdit(QDialog):
    """creates income editing dialog, upates current asset table
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog13()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.set_income_data)
        self.ui.pushButton.clicked.connect(self.update_income)
        self.ui.pushButton_2.clicked.connect(self.close_income_dialog)
        self.ui.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_5.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_6.setValidator(QtGui.QIntValidator())

    def set_income_data(self):
        """_ gets data from the database and sets them to the Line 
        edits using itemname as the ID for serching _
        """
        try:
            itemname = self.ui.lineEdit_4.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT name FROM income WHERE name=? ", (itemname,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit.setText((var_y))
            var_t = cusr.execute(
                "SELECT amount FROM income WHERE name=? ", (itemname,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            self.ui.lineEdit_2.setText((var_t))
            var_r = cusr.execute(
                "SELECT description FROM income WHERE name=? ", (itemname,)).fetchone()
            var_r = (''.join(map(str, var_r)))
            self.ui.lineEdit_3.setText((var_r))
            var_b = cusr.execute(
                "SELECT debit FROM income WHERE name=? ", (itemname,)).fetchone()
            var_b = (''.join(map(str, var_b)))
            self.ui.lineEdit_5.setText((var_b))
            var_p = cusr.execute(
                "SELECT credit FROM income WHERE name=? ", (itemname,)).fetchone()
            var_p = (''.join(map(str, var_p)))
            self.ui.lineEdit_6.setText((var_p))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find item.')

    def update_income(self):
        """updates current assets table with the new data from the line edits
        """
        try:
            item = self.ui.lineEdit_4.text()
            name = self.ui.lineEdit.text()
            ksh = self.ui.lineEdit_2.text()
            decr = self.ui.lineEdit_3.text()
            dr = self.ui.lineEdit_5.text()
            cr = self.ui.lineEdit_6.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE income SET name=? WHERE name=?", (name, item))
            cusr.execute(
                "UPDATE income SET amount=? WHERE name=?", (ksh, item))
            cusr.execute(
                "UPDATE income SET description=? WHERE name=?", (decr, item))
            cusr.execute(
                "UPDATE income SET debit=? WHERE name=?", (dr, item))
            cusr.execute(
                "UPDATE income SET credit=? WHERE name=?", (cr, item))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Income is edited successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not edit.')

    def close_income_dialog(self):
        """closes Dialog when enter is pressed or Qpushbutton clicked
        """
        self.close()


class coa(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_coa()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update_postable)
        accounts = [
            'fixedassets',
            'currentassets',
            'currentliabilities',
            'Longtermliabilities',
            'fixedexpenses']
        balance_type = [
            'credit',
            'debit'
        ]
        self.ui.comboBox.addItems(accounts)
        self.ui.comboBox_2.addItems(balance_type)

    def update_postable(self):
        try:
            code = str(self.ui.comboBox.currentText())
            balance_ty = str(self.ui.comboBox_2.currentText())
            name = str(self.ui.lineEdit_22.text())
            role = str(self.ui.lineEdit.text())
            coa_uuid = uuid.uuid4().hex
            if self.ui.checkBox.isChecked() == True:
                combo2 = "0"
                combo1="1"
            elif self.ui.checkBox_2.isChecked() == False and self.ui.checkBox.isChecked() == False:
                combo2 = "1"
                combo1="0"
            elif self.ui.checkBox_2.isChecked() == True and self.ui.checkBox.isChecked() == True:
                combo2 = "1"
                combo1="0"

            elif self.ui.checkBox_2.isChecked() == True:
                combo2 = "1"
                combo1="0"
            else:
                combo2 = "1"
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO chart_of_accounts(id, code, role, account, balance_type, locked, active) VALUES (?,?,?,?,?,?,?)", (coa_uuid, code, role, name, balance_ty, combo1,combo2))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'account added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find item.')


class profileEdit(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_profile()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.update_table()
        self.ui.pushButton_31.clicked.connect(self.update_ltl)
        self.ui.comboBox_8.addItems(curencies(self))

    def update_table(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT business_name FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_40.setText((var_y))
            var_t = cusr.execute(
                "SELECT pobox FROM recip_detail ").fetchone()
            var_t = (''.join(map(str, var_t)))
            self.ui.lineEdit_41.setText((var_t))
            var_y = cusr.execute(
                "SELECT contact FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_42.setText((var_y))
            var_y = cusr.execute(
                "SELECT email FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_43.setText((var_y))
            var_y = cusr.execute(
                "SELECT street_address FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_27.setText((var_y))
            notes = cusr.execute("SELECT notes FROM recip_detail").fetchone()
            notes = (''.join(map(str, notes)))
            self.ui.plainTextEdit.insertPlainText(notes)
            foot = cusr.execute("SELECT footer FROM recip_detail").fetchone()
            foot = (''.join(map(str, foot)))
            self.ui.plainTextEdit_2.insertPlainText(foot)
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find item.')

    def update_ltl(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            pobox = (str(self.ui.lineEdit_41.text()))
            contact = (str(self.ui.lineEdit_42.text()))
            business_name = (str(self.ui.lineEdit_40.text()))
            email = (str(self.ui.lineEdit_43.text()))
            street_address = (str(self.ui.lineEdit_27.text()))
            notes = self.ui.plainTextEdit.document().toPlainText()
            footer = self.ui.plainTextEdit_2.document().toPlainText()
            cash_label = str(self.ui.comboBox_8.currentText())
            cusr.execute(
                "UPDATE recip_detail SET business_name=? WHERE id_17=1", (business_name,))
            cusr.execute(
                "UPDATE recip_detail SET pobox=? WHERE id_17=1", (pobox,))
            cusr.execute(
                "UPDATE recip_detail SET contact=? WHERE id_17=1", (contact,))
            cusr.execute(
                "UPDATE recip_detail SET email=? WHERE id_17=1", (email,))
            cusr.execute(
                "UPDATE recip_detail SET street_address=? WHERE id_17=1", (street_address,))
            cusr.execute(
                "UPDATE recip_detail SET notes=? WHERE id_17=1", (notes,))
            cusr.execute(
                "UPDATE recip_detail SET footer=? WHERE id_17=1", (footer,))
            cusr.execute(
                "UPDATE recip_detail SET currency=? WHERE id_17=1", (cash_label,))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'profile is successfully updated.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not updated.')

    def close_ltl(self):
        self.close()



class salesEedit(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog7()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.update_table)
        self.ui.pushButton.clicked.connect(self.update_sales)
        self.ui.pushButton_2.clicked.connect(self.close_sales)
        self.ui.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_5.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_6.setValidator(QtGui.QIntValidator())

    def update_table(self):
        try:
            itemname = self.ui.lineEdit_4.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT name FROM sales WHERE name=? ", (itemname,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit.setText((var_y))
            var_t = cusr.execute(
                "SELECT KSH FROM sales WHERE name=? ", (itemname,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            self.ui.lineEdit_2.setText((var_t))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find item.')

    def update_sales(self):
        try:
            item = self.ui.lineEdit_4.text()
            name = self.ui.lineEdit.text()
            ksh = self.ui.lineEdit_2.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE sales SET name=? WHERE name=?", (name, item))
            cusr.execute("UPDATE sales SET KSH=? WHERE name=?", (ksh, item))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'current liability is edited successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not edit.')

    def close_sales(self):
        self.close()


class stockAdd(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog1()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.pushButton_21.clicked.connect(self.add_stock)
        self.ui.pushButton_22.clicked.connect(self.close_addstock)
        self.ui.pushButton.clicked.connect(self.close_addstock)
        self.ui.lineEdit_23.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_24.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_21.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_22.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_27.setValidator(QtGui.QIntValidator())
        self.auto()

    def auto(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        var_x = cusr.execute("SELECT tax_name FROM tax_table").fetchall()
        var_y = [item for t in var_x for item in t]
        var_uom = cusr.execute("SELECT name FROM uom").fetchall()
        var_m = [item for z in var_uom for item in z]
        self.completer = QCompleter(var_y)
        self.ui.lineEdit_29.setCompleter(self.completer)
        self.ui.comboBox.addItems(var_m)

    def add_stock(self):
        UPC = self.ui.lineEdit_28.text()
        name = self.ui.lineEdit_20.text()
        selling_price = self.ui.lineEdit_22.text()
        Buying_price = self.ui.lineEdit_21.text()
        Quantity = self.ui.lineEdit_23.text()
        category = self.ui.lineEdit_26.text()
        Discount = self.ui.lineEdit_24.text()
        Supplier = self.ui.lineEdit_25.text()
        reoder = self.ui.lineEdit_27.text()
        vat = self.ui.lineEdit_29.text()
        uom = str(self.ui.comboBox.currentText())
        stockdate = date.today()
        sold = 0.0
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        var_x = cusr.execute("SELECT UPC FROM stock").fetchall()
        var_y = [item for t in var_x for item in t]
        if UPC in var_y:
            QMessageBox.warning(QMessageBox(), 'Error', 'item already exists.')
        else:
            try:
                cusr.execute(
                    "INSERT INTO stock(UPC, name, Buying_price, selling_price, Quantity, category, Supplier, reoder, uom, Discount, vat, stockdate, sold ) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (UPC,
                     name,
                     Buying_price,
                     selling_price,
                     Quantity,
                     category,
                     Supplier,
                     reoder,
                     uom,
                     Discount,
                     vat,
                     stockdate,
                     sold))
                database_connection.commit()
                cusr.close()
                database_connection.close()
                QMessageBox.information(
                    QMessageBox(),
                    'Successful',
                    'Item is added successfully to the database.')
            except Exception:
                QMessageBox.warning(
                    QMessageBox(),
                    'Error',
                    'Could not add Item to the database.')

    def close_addstock(self):
        self.close()


class Update(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog8()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.pushButton_3.clicked.connect(self.updatestock)
        self.ui.pushButton_7.clicked.connect(self.stockupdate)
        self.ui.pushButton_19.clicked.connect(self.close_stockupdate)
        self.ui.pushButton.clicked.connect(self.close_stockupdate)
        self.auto()
        self.auto1()

    def auto1(self):
        """stock auto-completer for lineEdit_9
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        var_x = cusr.execute("SELECT name FROM stock").fetchall() # gets all stock name from table
        y = [item for t in var_x for item in t] # converts the names queried into a list 
        completer = QCompleter(y)# passes the list of tax name to the Qcompleter
        self.ui.lineEdit_9.setCompleter(completer)

    def auto(self):
        """tax auto completer for lineEdit_20
        """
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        var_x = cusr.execute("SELECT tax_name FROM tax_table").fetchall() #gets all tax name from table
        y = [item for t in var_x for item in t] # converts the names queried into a list 
        completer = QCompleter(y) # passes the list of tax name to the Qcompleter
        self.ui.lineEdit_20.setCompleter(completer)
        uom = cusr.execute("SELECT name FROM uom").fetchall() #gets all tax name from table
        uo = [item for t in uom for item in t]
        self.ui.comboBox.addItems(uo)

    def updatestock(self):
        try:
            itemname = self.ui.lineEdit_9.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT name FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_11.setText((var_y))
            self.z = cusr.execute(
                "SELECT Buying_price FROM stock WHERE name=? ", (itemname,)).fetchone()
            self.z = (''.join(map(str, self.z)))
            self.ui.lineEdit_13.setText((self.z))
            var_x = cusr.execute(
                "SELECT selling_price FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_x = (''.join(map(str, var_x)))
            self.ui.lineEdit_12.setText((var_x))
            var_e = cusr.execute(
                "SELECT Quantity FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_e = (''.join(map(str, var_e)))
            self.ui.lineEdit_14.setText((var_e))
            self.ui.lineEdit_14.setValidator(QtGui.QIntValidator())
            var_f = cusr.execute(
                "SELECT Discount FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_f = (''.join(map(str, var_f)))
            self.ui.lineEdit_15.setText((var_f))
            var_a = cusr.execute(
                "SELECT Supplier FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_a = (''.join(map(str, var_a)))
            self.ui.lineEdit_16.setText((var_a))
            var_b = cusr.execute(
                "SELECT reoder FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_b = (''.join(map(str, var_b)))
            self.ui.lineEdit_18.setText((var_b))
            self.ui.lineEdit_18.setValidator(QtGui.QIntValidator())
            var_r = cusr.execute(
                "SELECT UPC FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_r = (''.join(map(str, var_r)))
            self.ui.lineEdit_19.setText((var_r))
            var_d = cusr.execute(
                "SELECT category FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_d = (''.join(map(str, var_d)))
            self.ui.lineEdit_17.setText((var_d))
            var_l = cusr.execute(
                "SELECT vat FROM stock WHERE name=? ", (itemname,)).fetchone()
            var_l = (''.join(map(str, var_l)))
            self.ui.lineEdit_20.setText((var_l))
            uom = cusr.execute(
                "SELECT uom FROM stock WHERE name=? ", (itemname,)).fetchone()
            uom = (''.join(map(str, uom)))
            self.ui.comboBox.setCurrentText((uom))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'invalid operation.')

    def stockupdate(self):
        try:
            item = self.ui.lineEdit_9.text()
            itemname = self.ui.lineEdit_11.text()
            bp = self.ui.lineEdit_12.text()
            selling_price = self.ui.lineEdit_13.text()
            qu = self.ui.lineEdit_14.text()
            dis = self.ui.lineEdit_15.text()
            sup = self.ui.lineEdit_16.text()
            upc = self.ui.lineEdit_19.text()
            category = self.ui.lineEdit_18.text()
            vat = self.ui.lineEdit_20.text()
            uom = self.ui.comboBox.currentText()
            reoder = self.ui.lineEdit_17.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE stock SET Buying_price=? WHERE name=?", (selling_price, item))
            cusr.execute(
                "UPDATE stock SET selling_price=? WHERE name=?", (bp, item))
            cusr.execute(
                "UPDATE stock SET Quantity=? WHERE name=?", (qu, item))
            cusr.execute(
                "UPDATE stock SET Discount=? WHERE name=?", (dis, item))
            cusr.execute(
                "UPDATE stock SET Supplier=? WHERE name=?", (sup, item))
            cusr.execute("UPDATE stock SET UPC=? WHERE name=?", (upc, item))
            cusr.execute(
                "UPDATE stock SET category=? WHERE name=?", (reoder, item))
            cusr.execute(
                "UPDATE stock SET uom=? WHERE name=?", (uom, item))
            cusr.execute(
                "UPDATE stock SET reoder=? WHERE name=?", (category, item))
            cusr.execute("UPDATE stock SET vat=? WHERE name=?", (vat, item))
            cusr.execute(
                "UPDATE stock SET name=? WHERE name=?", (itemname, item))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'successfully updated stock.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not updated the stock.')

    def close_stockupdate(self):
        self.close()


class Bizdetails(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog10()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.update_table()
        self.ui.pushButton.clicked.connect(self.update_vee)
        self.ui.pushButton_2.clicked.connect(self.close_vee)

    def update_table(self):
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT business_name FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_4.setText((var_y))
            var_t = cusr.execute(
                "SELECT pobox FROM recip_detail ").fetchone()
            var_t = (''.join(map(str, var_t)))
            self.ui.lineEdit.setText((var_t))
            var_y = cusr.execute(
                "SELECT contact FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_2.setText((var_y))
            var_y = cusr.execute(
                "SELECT other FROM recip_detail").fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit_3.setText((var_y))
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'an error has occured.')

    def update_vee(self):
        try:
            bizname = self.ui.lineEdit_4.text()
            pobox = self.ui.lineEdit.text()
            num = self.ui.lineEdit_2.text()
            other = self.ui.lineEdit_3.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE recip_detail SET business_name=?", (bizname,))
            cusr.execute("UPDATE recip_detail SET pobox=?", (pobox,))
            cusr.execute("UPDATE recip_detail SET contact=?", (num,))
            cusr.execute("UPDATE recip_detail SET other=?", (other,))
            database_connection.commit()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'current liability is edited successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not edit.')

    def close_vee(self):
        self.close()


class Taxsettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.update_vee)
        self.ui.pushButton_3.clicked.connect(self.update_table)
        self.ui.pushButton.clicked.connect(self.add_settings)
        self.ui.lineEdit_20.setValidator(QtGui.QIntValidator())
        self.ui.pushButton_4.clicked.connect(self.close_vee)
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 280)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.showdata()

    def showdata(self):
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        query = "SELECT * FROM tax_table"
        result = database_connection.execute(query)
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(
                    row_number,
                    column_number,
                    QTableWidgetItem(
                        str(data)))

    def add_settings(self):
        tax_name = self.ui.lineEdit_19.text()
        tax_percentage = self.ui.lineEdit_20.text()
        tax_agent = self.ui.lineEdit_21.text()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO tax_table(tax_name, tax_percentage, tax_agent) VALUES (?,?,?)",
                (tax_name,
                 tax_percentage,
                 tax_agent))
            database_connection.commit()
            self.showdata()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'added to database.')
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add TAX to the database.')

    def update_table(self):
        try:
            itemname = self.ui.lineEdit_4.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            var_y = cusr.execute(
                "SELECT tax_name FROM tax_table WHERE tax_name=? ", (itemname,)).fetchone()
            var_y = (''.join(map(str, var_y)))
            self.ui.lineEdit.setText((var_y))
            var_t = cusr.execute(
                "SELECT tax_percentage FROM tax_table WHERE tax_name=? ", (itemname,)).fetchone()
            var_t = (''.join(map(str, var_t)))
            self.ui.lineEdit_2.setText((var_t))
            self.v = cusr.execute(
                "SELECT tax_agent FROM tax_table WHERE tax_name=? ", (itemname,)).fetchone()
            self.v = (''.join(map(str, self.v)))
            self.ui.lineEdit_3.setText((self.v))
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find item.')

    def update_vee(self):
        try:
            item = self.ui.lineEdit_4.text()
            tax_name = self.ui.lineEdit.text()
            tax_percentage = self.ui.lineEdit_2.text()
            tax_agent = self.ui.lineEdit_3.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "UPDATE tax_table SET tax_name=? WHERE tax_name=?", (tax_name, item))
            cusr.execute(
                "UPDATE tax_table SET tax_percentage=? WHERE tax_name=?",
                (tax_percentage,
                 item))
            cusr.execute(
                "UPDATE tax_table SET tax_agent=? WHERE tax_name=?", (tax_agent, item))
            database_connection.commit()
            QMessageBox.information(QMessageBox(), 'Successful', 'updated.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update.')

    def close_vee(self):
        self.close()


class supplieradd(QDialog):
    def __init__(self, *args, **kwargs):
        super(supplieradd, self).__init__(*args, **kwargs)
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setText("ADD")
        self.delete_pushbutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.setWindowTitle("sales")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.setStyleSheet(
            (u"background-color: rgb(0, 0, 12);\n"
             "QLineEdit {\n"
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
             ""))
        self.delete_pushbutton.clicked.connect(self.add_supplier)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("supplier name")
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.nameinput)
        self.telno = QLineEdit()
        self.telno.setPlaceholderText("telNo*")
        self.telno.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.telno)
        self.telno2 = QLineEdit()
        self.telno2.setPlaceholderText("telNo")
        self.telno2.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.telno2)
        self.address = QLineEdit()
        self.address.setPlaceholderText("address")
        self.address.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.address)
        self.address2 = QLineEdit()
        self.address2.setPlaceholderText("address2")
        self.address2.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.address2)
        self.email = QLineEdit()
        self.email.setPlaceholderText("email*")
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.email)

        self.website = QLineEdit()
        self.website.setPlaceholderText("website")
        self.website.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.website)

        self.country = QLineEdit()
        self.country.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.country)
        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def add_supplier(self):
        updated = dt.today()
        created = dt.today()
        user_uuid = str(who_is_logged[1])
        name = self.nameinput.text()
        tel1 = self.telno.text()
        tel2 = self.telno2.text()
        email = self.email.text()
        addr = self.address.text()
        addr2 = self.address2.text()
        site = self.website.text()
        country = self.country.text()
        client_date = date.today()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO supplier(created, updated, name, tel1, tel2, email, addr1, addr2, site, country, date, user_uuid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (created,
                 updated,
                 name,
                 tel1,
                 tel2,
                 email,
                 addr,
                 addr2,
                 site,
                 country,
                 client_date,
                 user_uuid
                 ))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'supplier is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add supplier to the database.')


class clientadd(QDialog):
    def __init__(self, *args, **kwargs):
        super(clientadd, self).__init__(*args, **kwargs)
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setText("ADD")
        self.delete_pushbutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.setWindowTitle("sales")
        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.setStyleSheet(
            (u"background-color: rgb(0, 0, 12);\n"
             "QLineEdit {\n"
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
             ""))
        self.delete_pushbutton.clicked.connect(self.add_client)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("client name")
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.nameinput)
        self.telno = QLineEdit()
        self.telno.setPlaceholderText("telno")
        self.telno.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.telno)
        self.address = QLineEdit()
        self.address.setPlaceholderText("address")
        self.address.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.address)
        self.email = QLineEdit()
        self.email.setPlaceholderText("email")
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.email)

        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def add_client(self):
        name = self.nameinput.text()
        telno = self.telno.text()
        address = self.address.text()
        email = self.email.text()
        balance = 0
        client_date = date.today()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO clients(name, telno, address, email, date, balance) VALUES (?,?,?,?,?,?)",
                (name,
                 telno,
                 address,
                 email,
                 client_date,
                 balance))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'client is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add client to the database.')


class InsertDialog7(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog7, self).__init__(*args, **kwargs)
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.delete_pushbutton.setText("ADD")
        self.setWindowTitle("sales")
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.delete_pushbutton.clicked.connect(self.add_sales)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("sales")
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.nameinput)
        self.KSH = QLineEdit()
        self.KSH.setPlaceholderText("KSH.")
        self.KSH.setValidator(QtGui.QIntValidator())
        self.KSH.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.KSH)
        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def add_sales(self):
        name = self.nameinput.text()
        saledate = date.today()
        KSH = self.KSH.text()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO sales(name, KSH, saledate) VALUES (?,?,?)", (name, KSH, saledate))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'expense is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add expense to the database.')




class InsertIncome(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertIncome, self).__init__(*args, **kwargs)
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setText("ADD")
        self.delete_pushbutton.setStyleSheet("color: rgb(255, 255, 255);")
        self.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.setWindowTitle("income/revenue")
        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.delete_pushbutton.clicked.connect(self.add_var_exp)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("income")
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.nameinput)
        self.KSH = QLineEdit()
        self.KSH.setPlaceholderText("KSH.")
        self.KSH.setValidator(QtGui.QIntValidator())
        self.KSH.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.KSH)
        self.des = QLineEdit()
        self.des.setPlaceholderText("description.")
        self.des.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.des)
        self.dr = QLineEdit()
        self.dr.setPlaceholderText("Dr.")
        self.dr.setValidator(QtGui.QIntValidator())
        self.dr.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.dr)
        self.cr = QLineEdit()
        self.cr.setPlaceholderText("Cr.")
        self.cr.setValidator(QtGui.QIntValidator())
        self.cr.setStyleSheet("background-color: rgb(255, 255, 255);")
        layout.addWidget(self.cr)
        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def add_var_exp(self):
        name = self.nameinput.text()
        description = self.des.text()
        debit = self.dr.text()
        credit = self.cr.text()
        KSH = self.KSH.text()
        vardate = date.today()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute(
                "INSERT INTO income(name,  amount, debit, credit, description, income_date) VALUES (?,?,?,?,?,?)",
                (name,
                 KSH,
                 debit,
                 credit,
                 description,
                 vardate))
            database_connection.commit()
            cusr.execute(
                "INSERT INTO transactions(name, KSH, description, debit, credit, transactionsdate) VALUES (?,?,?,?,?,?)",
                (name,
                 KSH,
                 debit,
                 credit,
                 description,
                 vardate))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'income is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not add income to the database.')




class clientDeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(clientDeleteDialog, self).__init__(*args, **kwargs)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setText("Delete")
        self.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.setWindowTitle("Delete client")
        self.setFixedWidth(250)
        self.setFixedHeight(100)
        self.delete_pushbutton.clicked.connect(self.delete_student)
        layout = QVBoxLayout()
        self.delete_input = QLineEdit()
        self.onlyinteger = QIntValidator()
        self.delete_input.setValidator(self.onlyinteger)
        self.delete_input.setPlaceholderText("client No.")
        layout.addWidget(self.delete_input)
        self.delete_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def delete_student(self):
        del_rol = ""
        del_rol = self.delete_input.text()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("DELETE from clients WHERE id_10=" + str(del_rol))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not Delete client from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        database_connection = sqlite3.connect(
            pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        self.delete_pushbutton = QPushButton()
        self.delete_pushbutton.setText("Delete")
        self.delete_pushbutton.setStyleSheet("QPushButton{\n"
                                "    background-color: rgb(255, 5, 42);\n"
                                "border-radius : 25px;\n"
                                "color : rgb(7, 7, 7); \n"
                                "}")
        self.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.setWindowTitle("Delete stock")
        self.setFixedWidth(250)
        self.setFixedHeight(100)
        self.delete_pushbutton.clicked.connect(self.delete_student)
        layout = QVBoxLayout()
        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("item UPC.")
        layout.addWidget(self.delete_input)
        self.delete_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        layout.addWidget(self.delete_pushbutton)
        self.setLayout(layout)

    def delete_student(self):
        del_rol = self.delete_input.text()
        try:
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            cusr.execute("DELETE from stock WHERE UPC=?", (del_rol,))
            database_connection.commit()
            cusr.close()
            database_connection.close()
            QMessageBox.information(
                QMessageBox(),
                'Successful',
                'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(
                QMessageBox(),
                'Error',
                'Could not Delete stock from the database.')



class LogoutUser(QDialog):
    """creates income editing dialog, upates current asset table
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui =  Ui_logout()
        # Run the .setupUi() method to show the GUI
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.logout_user)
        # self.ui.pushButton_3.clicked.connect(self.accounts_login)
        # self.ui.pushButton_8.clicked.connect(self.close_entrance)
    def logout_user(self):
        credentials = {
                    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDY2OTE4MSwiaWF0IjoxNjU0NTgyNzgxLCJqdGkiOiIyMzlkMjJiMjk5YzM0MWIyODk4MWNhMThlOWM0ODY3NiIsInVzZXJfaWQiOiIwNmFlZGI4NC0zZTY1LTQzNDctYWQ5ZC05NDg0OTVjMmE5NWMifQ.jp-g6CGro0RBph25wFlkwM2d-OB1bc9Jz6Uwq5n1SR8"
                }
        headers = {
                    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0NTg5MjY4LCJpYXQiOjE2NTQ1ODI3ODEsImp0aSI6ImIzODkwZTI5NDU1YzQzNzdhOTBhM2VlN2IwMDE1NGYxIiwidXNlcl9pZCI6IjA2YWVkYjg0LTNlNjUtNDM0Ny1hZDlkLTk0ODQ5NWMyYTk1YyJ9.X4pz7fxAe2nemkL5cu4YjcfJUB_pzBe6NZp1SUAZ1lY",
                }
        response = requests.post("http://127.0.0.1:8000/apiv1/logout/", json=credentials, headers=headers)
        print("&&&Status code", response.status_code)

class Accounts_login(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # Create an instance of the GUI
        self.ui = Ui_Accounts_Login()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login

    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            user = cusr.execute("SELECT user_uuid FROM admin").fetchone()
            user = (''.join(map(str, user)))
            pass_hash = cusr.execute("SELECT password FROM user_managment WHERE username=?", (username,)).fetchone()
            pass_hash = (''.join(map(str, pass_hash)))
            assign = cusr.execute("SELECT assign FROM user_managment WHERE username=?", (username,)).fetchone()
            assign = (''.join(map(str, assign)))
            pass_salt = cusr.execute("SELECT salt FROM user_managment WHERE username=?", (username,)).fetchone()
            pass_salt = (''.join(map(str, pass_salt)))

            check_password = str(hashlib.sha512(password.encode('utf-8')+pass_salt.encode('utf-8')).hexdigest())
            if check_password ==  pass_hash and assign == "Accounts":
                # database_connection.close()
                self.close()
                Entrance().close()
                
                who_is_logged.insert(0, assign)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])

                MainWindow()
            elif check_password ==  password and assign == "POS":
                self.close()
                Entrance().close()
                
                who_is_logged.insert(0, assign)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])
                MainWindow()
            elif check_password ==  password and assign == "Inventory":
                self.close()
                Entrance().close()
                who_is_logged.insert(0, assign)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])
                MainWindow()
            elif check_password ==  password and assign == "CRM":
                self.close()
                Entrance().close()
                who_is_logged.insert(0, assign)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])
                MainWindow()
            elif check_password ==  password and assign == "admin":
                self.close()
                Entrance().close()
                who_is_logged.insert(0, assign)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])
                MainWindow()
                
            else:
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()

class Admin_Login(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # Create an instance of the GUI
        self.ui = Ui_Login_Admin_In()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login

    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
            cusr = database_connection.cursor()
            user = cusr.execute("SELECT user_uuid FROM admin").fetchone()
            user = (''.join(map(str, user)))
            check_username = cusr.execute("SELECT email FROM admin").fetchone()
            check_username = (''.join(map(str, check_username)))
            pass_salt = cusr.execute("SELECT salt FROM admin").fetchone()
            pass_salt = (''.join(map(str, pass_salt)))
            pass_hash = cusr.execute("SELECT hash FROM admin").fetchone()
            pass_hash = (''.join(map(str, pass_hash)))
            check_password = str(hashlib.sha512(password.encode('utf-8')+pass_salt.encode('utf-8')).hexdigest())

            if check_username == username and check_password == pass_hash:
                database_connection.close()
                self.close()
                Entrance().close()
                b = 'admin'
                who_is_logged.insert(0, b)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])

                MainWindow()
                
                
            else:
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
class SignUp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # Create an instance of the GUI
        self.ui = Ui_Singnup()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login

    def check_login(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            reqUrl = "http://localhost:8080/authe/"

            headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json" 
            }

            payload = json.dumps({
                "username": "zam",
                "email":"zam@gmail.com",
                "password" : "123456"
            })

            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

            print(response.text)

            if check_username == username and check_password == pass_hash:
                database_connection.close()
                self.close()
                Entrance().close()
                b = 'admin'
                who_is_logged.insert(0, b)
                who_is_logged.insert(1, user)
                print(";:::::::::::::", who_is_logged[0])

                MainWindow()
                
                
            else:
                # SET STYLESHEET
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(255, 0, 127); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(255, 0, 127); }")
                self.shacke_window()
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))
                

        # self.ui.pushButton.clicked.connect(self.check_if_password_is_set)
        

    def check_if_password_is_set(self):
        """closes Dialog when enter is pressed or Qpushbutton clicked
        """
        print("###")


class Entrance(QDialog):
    """creates income editing dialog, upates current asset table
    Args:
        QDialog (_class_): _A dialog window is a top-level window mostly used for
         short-term tasks and brief communications with the user_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Entrance()
        # Run the .setupUi() method to show the GUI
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.check_if_password_is_set)
        self.ui.pushButton_3.clicked.connect(self.accounts_login)
        self.ui.pushButton_5.clicked.connect(self.accounts_login)
        self.ui.pushButton_4.clicked.connect(self.accounts_login)
        self.ui.pushButton_6.clicked.connect(self.accounts_login)
        self.ui.pushButton_8.clicked.connect(self.close_entrance)
        

    def check_if_password_is_set(self):
        """check if the admin has set his password if true it executes Admin_Login() so the admin can login
            if false it just open the main application
        """
        conn = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
        c = conn.cursor()
        pass_is_set = c.execute("SELECT password_set FROM admin").fetchone()
        pass_is_set = (''.join(map(str, pass_is_set)))
        if pass_is_set == "True":
            
            print("###################################################################################")
            self.admin_set = Admin_Login()
            # conn.close()
            # self.main.top_user.label_user.setText(username.capitalize())
            self.admin_set.show()
            
        else:
            conn.close()
            self.close()
            MainWindow()

    def accounts_login(self):
        Accounts_login().show()

    def close_entrance(self):
        self.close()


class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # GET WIDGETS FROM "ui_login.py"
        # Load widgets inside LoginWindow
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        # ///////////////////////////////////////////////////////////////

        # ADD DROP SHADOW

        # KEY PRESS EVENT
        # ///////////////////////////////////////////////////////////////
        self.ui.username.keyReleaseEvent = self.check_login
        self.ui.password.keyReleaseEvent = self.check_login
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        check_if_first_time_login = cusr.execute("SELECT logged_in FROM admin").fetchone()
        print("first login", check_if_first_time_login)
        #check_if_first_time_login = (''.join(map(str, check_if_first_time_login)))
        if check_if_first_time_login == None:
            self.show()
        else:
            self.main = Entrance()
                # self.main.top_user.label_user.setText(username.capitalize())
            self.main.show()  

    # CHECK LOGIN
    # ///////////////////////////////////////////////////////////////
    def check_login(self, event):
        database_connection = sqlite3.connect(
                pathtodb + "\\yobi\\yobi_database.db")
        cusr = database_connection.cursor()
        check_if_first_time_login = cusr.execute("SELECT logged_in FROM admin").fetchone()
        print("first login", check_if_first_time_login)
        #check_if_first_time_login = (''.join(map(str, check_if_first_time_login)))
        # if check_if_first_time_login == None:

        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            username = self.ui.username.text()
            password = self.ui.password.text()
            def open_main():
                # SHOW MAIN WINDOW
                self.main = Entrance()
                # self.main.top_user.label_user.setText(username.capitalize())
                self.main.show()                
                self.close()
            
            reqUrl = "http://localhost:8080/login/"

            headersList = {
            "Accept": "*/*",
           
            "Content-Type": "application/json" 
            }

            payload = json.dumps({
                "username": username,
                "email":username,
                "password" : password
            })
            response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

            resp = response.json()
            print(type(resp))
            print(resp)

            if response.status_code == 200:
                email = str(resp["user"]["email"])
                self.ui.user_description.setText(f"Welcome {email}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #00ff00 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid #0000ff; }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid #00ff00; }")
                
                
                
                id =str(resp["user"]["id"])
                # id = str(user[0])
                
                salt = uuid.uuid4().hex
                password1 =  str(hashlib.sha512(password.encode('utf-8')+salt.encode('utf-8')).hexdigest())
                print("@@@@@@@@@@@@@@@", password1)
                # tok = resp["token"]
                token = str(resp["token"])
                logged_in = "True"
                password_set = "True"
                cusr.execute(
                "INSERT INTO  admin(email, salt, hash, token, logged_in, password_set, user_uuid) VALUES (?,?,?,?,?,?,?)",
                (email,
                salt,
                password1,
                token,
                logged_in,
                password_set,
                id))
                database_connection.commit()
                database_connection.close()
                QTimer.singleShot(1200, lambda: open_main())
            else:
                # SET STYLESHEET
                error = "Invalid credentials, try again"
                self.ui.user_description.setText(f"{error}!")
                self.ui.user_description.setStyleSheet("#user_description { color: #ff0000 }")
                self.ui.username.setStyleSheet("#username:focus { border: 3px solid rgb(212, 0, 0); }")
                self.ui.password.setStyleSheet("#password:focus { border: 3px solid rgb(212, 0, 0); }")
                self.shacke_window()
        # else:
        #     self.close()
        #     self.main = Entrance()
        #         # self.main.top_user.label_user.setText(username.capitalize())
        #     self.main.show()  
            

    def shacke_window(self):
        # SHACKE WINDOW
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))

    # UPDATE PROGRESS BAR
    # ///////////////////////////////////////////////////////////////
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()
            self.animation_login()

        # INCREASE COUNTER
        counter += 1

    # START ANIMATION TO LOGIN
    # ///////////////////////////////////////////////////////////////
    def animation_login(self):
        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.frame_widgets, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(0, 70, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEndValue(QRect(0, -325, self.ui.frame_widgets.width(), self.ui.frame_widgets.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("capture.ico"))
    window = LoginWindow()
    sys.exit(app.exec())
