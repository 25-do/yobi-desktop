from main import *
from PySide6.QtGui import  QPixmap
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
def convertToBinaryData(self, filename):
    # Convert digital data to binary format
    print(filename)
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(self):
    try:
        self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
        self.c = self.connection.cursor()
        
        profile_photo = ""#convertToBinaryData(self, imagepath)
        pobox = (str(self.ui.lineEdit_41.text()))
        contact = (str(self.ui.lineEdit_42.text()))
        business_name = (str(self.ui.lineEdit_40.text()))
        email = (str(self.ui.lineEdit_43.text()))
        street_address = (str(self.ui.lineEdit_27.text()))
        notes = self.ui.plainTextEdit.document().toPlainText()
        footer = self.ui.plainTextEdit_2.document().toPlainText()
        cash_label = str(self.ui.comboBox_8.currentText())
        print(cash_label)
        self.c.execute("INSERT INTO recip_detail(business_name , pobox , contact , email , street_address, notes , footer , currency, profile_photo ) "
                    "VALUES (?,?,?,?,?,?,?,?,?)", (business_name , pobox , contact , email , street_address, notes , footer , cash_label, profile_photo))
        self.connection.commit()
        self.c.close()
        self.connection.close()
        QMessageBox.information(QMessageBox(), 'Successful', 'added company profile.')

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
        
def insertBLOB2(self):
    
    self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
    self.c = self.connection.cursor()
    
    
    pobox = (str(self.ui.lineEdit_41.text()))
    contact = (str(self.ui.lineEdit_42.text()))
    business_name = (str(self.ui.lineEdit_40.text()))
    email = (str(self.ui.lineEdit_43.text()))
    street_address = (str(self.ui.lineEdit_27.text()))
    notes = self.ui.plainTextEdit.document().toPlainText()
    footer = self.ui.plainTextEdit_2.document().toPlainText()
    cash_label = str(self.ui.comboBox_8.currentText())

    self.c.execute("UPDATE recip_detail SET business_name=? WHERE id_17=1", (business_name,))
    self.c.execute("UPDATE recip_detail SET pobox=? WHERE id_17=1", (pobox,))
    self.c.execute("UPDATE recip_detail SET contact=? WHERE id_17=1", (contact,))
    self.c.execute("UPDATE recip_detail SET email=? WHERE id_17=1", (email,))
    self.c.execute("UPDATE recip_detail SET street_address=? WHERE id_17=1", (street_address,))
    self.c.execute("UPDATE recip_detail SET notes=? WHERE id_17=1", (notes,))
    self.c.execute("UPDATE recip_detail SET footer=? WHERE id_17=1", (footer,))
    self.c.execute("UPDATE recip_detail SET currency=? WHERE id_17=1", (cash_label,))
    self.connection.commit()

    

def select_image(self):
    try:

        self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
        self.c = self.connection.cursor()
        b = self.c.execute("SELECT * FROM recip_detail").fetchall()
        
        for x in b:
            rec = x[6]
        with open('summary picture.jpg', 'wb') as f:
            f.write(rec)
        self.ui.label_174.setPixmap(QPixmap('summary picture.jpg'))
        self.ui.label_174.setScaledContents(True)

        self.connection.commit()
        self.c.close()
        self.connection.close()
    except UnboundLocalError:
        print('unnbound local error at SELECT_IMAGE')
