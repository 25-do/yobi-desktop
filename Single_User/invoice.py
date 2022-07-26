import getopt
from main import *

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

import time
import sys
from pycss import generate_stylesheet

basepath = os.path.expanduser('~/Documents')
pathtodb = str(basepath)
newpath = (pathtodb + "\\yobi")
if not os.path.exists(newpath):
    os.makedirs(newpath)

try:
    conn = sqlite3.connect(pathtodb + "\\yobi\\yobi_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recip_detail(id_17 INTEGER PRIMARY KEY, business_name TEXT, pobox TEXT, contact TEXT, email TEXT, street_address TEXT, notes TEXT, footer TEXT, currency TEXT, profile_photo BLOB)")
    cash_label = c.execute("SELECT currency FROM recip_detail WHERE id_17=1").fetchone()
    cash_label = (''.join(map(str, cash_label)))
    print("*********************************", cash_label)
    c.close()
except Exception:
    cash_label = "$"

# Global definitions for the Company sending the invoice.
doc_title              = "Customer Invoice"


# Global definitions for the current order being processed.
order_date             = "June 1, 2017"
order_method           = "Electronic Deposit"

# Global list of goods or services being purchased; defined as follows:
#
# 1) Description
# 2) Hours
# 3) Hourly rate in dollars
#



# Current Taxable Rate, as a percent.


# Global definition for the invoice-specific notes.
 

# Global defintion of the final thank you


#
# Function to generate the specific order number.
#
def generate_order_number(self):

    # Attempt to grab the current epoch time.
    tmp_num = str(time.time())
    if (len(tmp_num) < 1):
        return ""

    # Since the time call returns possible milliseconds, then split the result.
    parts = tmp_num.split(".")

    # If the second element is blank, add two zeros.
    if (len(parts[1]) == 0):
        return parts[0] + "00"

    # If the second element is only one digit, add an extra zero.
    if (len(parts[1]) == 1):
        return parts[0] + "" + parts[1] + "0"
    
    # If the second element is two digits, append the two parts together.
    if (len(parts[1]) == 2):
        return parts[0] + parts[1]

    # In the event something really odd occurred, which it shouldn't, force
    # the program to ignore the second part.
    return parts[0] + "00"

#
# Function to assemble the <head> section of the document.
#
def assemble_head_section(self, document_title):

    head_html = ""

    head_html += "    <!-- Head -->\n" 
    head_html += "    <head>\n" 
    head_html += "        <meta charset=\"utf-8\" />\n" 
    head_html += "        <meta name=\"description\" content=\"Customer Invoice\" />\n" 
    head_html += "        <meta name=\"keywords\" content=\"invoice template\" />\n"
    head_html += "        <meta name=\"robots\" content=\"index,follow\" />\n" 
    head_html += "        <meta name=\"author\" content=\"John Smith\" />\n" 
    head_html += generate_stylesheet(self)
    head_html += "        <title>" + document_title + "</title>\n" 
    head_html += "    </head>\n"

    return head_html

#
# Function to assemble the header section of the invoice.
#
def assemble_invoice_header_section(self, name, street_address, email, state_country, phone):

    header_section_html  = ""

    header_section_html += "             <!-- Document Header -->\n" 
    header_section_html += "             <div id=\"invoice_header\">\n"
    header_section_html += "                 <div id=\"invoice_text_area\">\n"
    header_section_html += "                     <div id=\"company_name\">\n" 
    header_section_html += "                     " + name + "\n"
    header_section_html += "                     </div>\n" 
    header_section_html += "                     <table id=\"company_details\">\n"
    header_section_html += "                         <tr>\n"
    header_section_html += "                             <td>\n"
    header_section_html += "                               " + street_address + "\n"
    header_section_html += "                             </td>\n"
    header_section_html += "                             <td>\n"
    header_section_html += "                               " + email + "\n"
    header_section_html += "                             </td>\n" 
    header_section_html += "                         </tr>\n" 
    header_section_html += "                         <tr>\n" 
    header_section_html += "                             <td>\n" 
    header_section_html += "                               " + state_country + "\n" 
    header_section_html += "                             </td>\n" 
    header_section_html += "                             <td>\n" 
    header_section_html += "                               " + phone + "\n"
    header_section_html += "                             </td>\n"
    header_section_html += "                         </tr>\n"
    header_section_html += "                     </table>\n"
    header_section_html += "                 </div>\n"
    header_section_html += "             </div>\n"

    return header_section_html

#
# Function to assemble the client information section of the invoice.
#
def assemble_invoice_client_information_section(self, name, street_address, state_country, postal, account):

    client_section_html  = ""

    client_section_html += "                 <!-- Customer Information -->\n"
    client_section_html += "                 <div id=\"customer_info\">\n"
    client_section_html += "                     <table>\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <th>\n"
    client_section_html += "                               Customer Information\n" 
    client_section_html += "                             </th>\n" 
    client_section_html += "                             <th>\n"
    client_section_html += "                             </th>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Buffer -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                         </tr>\n"
   
    client_section_html += "                         <!-- Client Name -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Name:</td>\n"
    client_section_html += "                             <td>" + name + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Street Address -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Address:</td>\n"
    client_section_html += "                             <td>" + street_address + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- City, Province/State, Country -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                             <td>" + state_country + "</td>\n"
    client_section_html += "                         </tr>\n"
   
    client_section_html += "                         <!-- Postal Code -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>&nbsp;</td>\n"
    client_section_html += "                             <td>" + postal + "</td>\n"
    client_section_html += "                         </tr>\n"
    
    client_section_html += "                         <!-- Account Number is just a number -->\n"
    client_section_html += "                         <tr>\n"
    client_section_html += "                             <td>Account Number:</td>\n"
    client_section_html += "                             <td>" + account + "</td>\n"
    client_section_html += "                         </tr>\n"
    client_section_html += "                     </table>\n"
    client_section_html += "                 </div>\n"

    return client_section_html

#
# Function to assemble the order information section of the invoice.
#
def assemble_invoice_order_information_section(self, number, date, method):

    order_info_section_html = ""
 
    order_info_section_html += "                 <!-- Order Information -->\n"
    order_info_section_html += "                 <div id=\"order_info\">\n"
    order_info_section_html += "                     <table>\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <th>\n"
    order_info_section_html += "                               Order Information\n"
    order_info_section_html += "                             </th>\n"
    order_info_section_html += "                             <th>&nbsp;</th>\n"
    order_info_section_html += "                         </tr>\n" 
    
    order_info_section_html += "                         <!-- Buffer -->\n"
    order_info_section_html += "                         <tr>\n" 
    order_info_section_html += "                             <td>&nbsp;</td>\n"
    order_info_section_html += "                             <td>&nbsp;</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Number is timestamp -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Number:</td>\n"
    order_info_section_html += "                             <td>" + str(number) + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Date -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Date:</td>\n"
    order_info_section_html += "                             <td>" + date + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    
    order_info_section_html += "                         <!-- Order Payment Method -->\n"
    order_info_section_html += "                         <tr>\n"
    order_info_section_html += "                             <td>Method:</td>\n"
    order_info_section_html += "                             <td>" + method + "</td>\n"
    order_info_section_html += "                         </tr>\n"
    order_info_section_html += "                     </table>\n"
    order_info_section_html += "                 </div>\n"

    return order_info_section_html

#
# Function to assemble the order details section of the invoice.
#
def assemble_invoice_order_details_section(self, details_array, taxable_rate):

    num_of_orders              = len(details_array)
    current_num                = 0
    current_type               = "odd"
    order_details_section_html = ""
    invoice_cost_summary       = 0

    order_details_section_html += "                 <!-- Main Table of Supplied Goods and Services -->\n"
    order_details_section_html += "                 <table id=\"order_details_table\">\n"
    order_details_section_html += "                     <tr>\n"
    order_details_section_html += "                         <th class=\"requested_service_column\">\n"
    order_details_section_html += "                             ITEM DESCRIPTION\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"hours_column\">\n"
    order_details_section_html += "                             QUA\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"hour_rate_column\">\n"
    order_details_section_html += "                             TOTAL\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"cost_column\">\n"
    order_details_section_html += "                             Amount\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                     </tr>\n" 
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                         <td>&nbsp;</td>\n" 
    order_details_section_html += "                     </tr>\n" 
   
    # Generate the HTML table tags for each of the orders.
    for current_num in range (0, num_of_orders):
 
        # Sanity check, ensure this is an actual entry, otherwise skip
        if (details_array[current_num] is None):
            continue

        # Sanity check, make sure we got a proper entry, else skip to the next
        if (len(details_array[current_num]) != 3):
            continue

        # Stagger the <tr> css styles to produce a line-by-line effect
        if (current_type == "odd"):
            current_type = "even"
        else:
            current_type = "odd"
        
        # Calculate the cost of a given service.
        cost = details_array[current_num][1] * details_array[current_num][2]
        invoice_cost_summary += cost

        # Format the hourly rate / entry cost.
        hourly_rate = "{:.2f}".format(details_array[current_num][2])
        cost = "{:.2f}".format(cost)

        # Generate the <tr> and <td> elements based on the current entry.
        order_details_section_html += "                     <tr class=\"" + current_type + "\">\n"
        order_details_section_html += "                         <td>" + details_array[current_num][0] + "</td>\n"
        order_details_section_html += "                         <td>" + str(details_array[current_num][1]) + "</td>\n"
        order_details_section_html += "                         <td>" + hourly_rate + "</td>\n"
        order_details_section_html += "                         <td class=\"align_dollars\">" + cash_label + cost + "</td>\n"
        order_details_section_html += "                     </tr>\n"
    
    # Generate the HTML <tr> buffers to make the page standard height.
    if (num_of_orders < 7):

        # Go ahead and cycle based on how much more space we need. 
        for x in range (0, 7 - num_of_orders):

            # Stagger the <tr> css styles to produce a line-by-line effect
            if (current_type == "odd"):
                current_type = "even"
            else:
                current_type = "odd"

            # Append the necessary buffer rows to the table.
            order_details_section_html += "                     <!-- Buffer Rows -->\n"
            order_details_section_html += "                     <tr class=\"" + current_type + "\">\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                         <td>&nbsp;</td>\n"
            order_details_section_html += "                     </tr>\n" 
    
    # If the previous entry was "even" make sure we have an "odd" separator
    # to improve page appearance.
    if (current_type == "even"):
        order_details_section_html += "                     <!-- Buffer Separator -->\n"
        order_details_section_html += "                     <tr class=\"odd\">\n"
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                         <td>&nbsp;</td>\n" 
        order_details_section_html += "                     </tr>\n"

    order_details_section_html += "                     <!-- Cost Summary Before Tax -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n" 
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th>\n" 
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                            Summary\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th class=\"align_dollars\">\n" 
    order_details_section_html += (                            cash_label)
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary)) + "\n" 
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                     </tr>\n"
 
    order_details_section_html += "                     <!-- Taxes -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                            Tax\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"align_dollars\">\n"
    order_details_section_html += (                            cash_label)
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary + taxable_rate )) + "\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                     </tr>\n"
   
    order_details_section_html += "                     <!-- Total -->\n"
    order_details_section_html += "                     <tr class=\"odd\">\n" 
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th>\n"
    order_details_section_html += "                             &nbsp;\n"
    order_details_section_html += "                         </th>\n" 
    order_details_section_html += "                         <th>\n" 
    order_details_section_html += "                            Total\n"
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                         <th class=\"align_dollars\">\n"
    order_details_section_html += (                           cash_label)
    order_details_section_html += ("{:.2f}".format(invoice_cost_summary + (invoice_cost_summary * (taxable_rate / 100)))) + "\n" 
    order_details_section_html += "                         </th>\n"
    order_details_section_html += "                     </tr>\n"
    order_details_section_html += "                 </table>\n"

    return order_details_section_html

#
# PROGRAM MAIN
#
def ban(self):
    self.connection = sqlite3.connect(pathtodb + "\yobi\yobi_database.db")
    self.c = self.connection.cursor()
    order_details_array = []
    alltb = self.c.execute("SELECT name, Quantity, KSH2 FROM pos_table")
    for index, tuple in enumerate(alltb):
        b= order_details_array.append(tuple)
        print('doing ban invoice', b)

    notes = self.c.execute("SELECT notes FROM recip_detail").fetchone()
    notes = (''.join(map(str, notes)))

    thank_you = self.c.execute("SELECT footer FROM recip_detail").fetchone()
    thank_you = (''.join(map(str, thank_you)))

    company_name = self.c.execute("SELECT business_name FROM recip_detail").fetchone()
    company_name = (''.join(map(str, company_name)))

    company_street_address = self.c.execute("SELECT pobox FROM recip_detail").fetchone()
    company_street_address= (''.join(map(str, company_street_address)))
    
    company_state_country  = self.c.execute("SELECT street_address FROM recip_detail").fetchone()
    company_state_country = (''.join(map(str, company_state_country)))
    company_email = self.c.execute("SELECT email FROM recip_detail").fetchone()
    company_email= (''.join(map(str, company_email)))

    company_phone = self.c.execute("SELECT contact FROM recip_detail").fetchone()
    company_phone = (''.join(map(str, company_phone)))

    # vat1 = (str(self.ui.lineEdit_15.text()))
    vat = self.c.execute("SELECT SUM(totalvat) FROM pos_table").fetchone()
    vat = float(''.join(map(str, vat)))
    taxable_rate = vat 


    # Global definitions for the Client receiving the invoice.
    itemid = self.ui.lineEdit_14.text()
    client_name = self.c.execute("SELECT name FROM clients WHERE name=?", (itemid,)).fetchone()
    client_name = (''.join(map(str, client_name)))
    client_street_address = self.c.execute("SELECT address FROM clients WHERE name=?", (itemid,)).fetchone()
    client_street_address = (''.join(map(str, client_street_address)))
    client_state_country = self.c.execute("SELECT telno FROM clients WHERE name=?", (itemid,)).fetchone()
    client_state_country = (''.join(map(str, client_state_country)))
    client_postal = self.c.execute("SELECT email FROM clients WHERE name=?", (itemid,)).fetchone()
    client_postal = (''.join(map(str, client_postal)))
    client_account = " "

    argv = sys.argv[1:]

    usage = 'generate_invoice.py -d <date> -o <file>\nWhere date is like... "June 15, 2019"\n'

    order_date = str(date.today())
    output = '/tmp/biz_invoice.html'

    try:
        opts, args = getopt.getopt(argv,"hd:o:",["date=","output="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-d", "--date"):
            order_date = arg
        elif opt in ("-o", "--output"):
            output = arg

    if (order_date == ''):
        print("Please enter a valid datetime.\n")
        print(usage)
        sys.exit(1)

    if (output == ''):
        print("Please enter a valid output file name.\n")
        print(usage)
        sys.exit(1)

    html = ""

    html += "<!DOCTYPE html>\n"
    html += "<html lang=\"en\">\n"
     
    html += assemble_head_section(self, doc_title)
 
    html += "    <body>\n"
    html += "        <div id=\"central_element\">\n"
    
    # Assemble the header of the invoice, with company logo and information.
    html += assemble_invoice_header_section(self,
                                            company_name,
                                            company_street_address,
                                            company_email,
                                            company_state_country,
                                            company_phone)

    html += "             <hr />\n"
    
    # Assemble the customer information section.
    html += "             <!-- Customer & Order Information Section -->\n"
    html += "             <div id=\"customer_and_order_information\">\n"
   
    # Assemble the client information section of the invoice. 
    html += assemble_invoice_client_information_section(self, client_name,
                                                        client_street_address,
                                                        client_state_country,
                                                        client_postal,
                                                        client_account)

    # Attempt to generate an order number.
    order_number = self.ui.lineEdit_16.text()
    # Assemble the order information section of the invoice.
    html += assemble_invoice_order_information_section(self, order_number,
                                                       order_date,
                                                       order_method)

    # Close the client / order info section.
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Order Details Section -->\n"
    html += "             <div id=\"order_details\">\n"
    html += assemble_invoice_order_details_section(self, order_details_array,
                                                   taxable_rate)
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Additional message content -->\n"
    html += "             <div id=\"message_content\">\n"
    html += "                 <table>\n"
    html += "                     <tr>\n"
    html += "                         <th>Notes</th>\n"
    html += "                     </tr>\n"
    html += "                     <tr>\n"
    html += "                         <td>\n"
    html += "                           " + notes + "\n"
    html += "                         <td>\n"
    html += "                     </tr>\n"
    html += "                 </table>\n"
    html += "             </div>\n"
    
    html += "             <hr />\n"
    
    html += "             <!-- Thank you message -->\n"
    html += "             <div id=\"thank_you\">\n"
    html += "                 <strong>\n"
    html += "                   " + thank_you + "\n"
    html += "                 </strong>\n" 
    html += "             </div>\n"
    
    html += "        </div>\n"
    html += "    </body>\n"
     
    html += "</html>\n"
    
    doc_name = str(self.ui.lineEdit_33.text())
    doc_name1 = str("Invoice_" + doc_name + ".html")
    doc_name2 = str("Invoice_" + doc_name + ".pdf")
    print("this the document file", doc_name1)
    f = open(doc_name1,"w")
    f.write(html)
    f.close()

    os.startfile(doc_name1)
    
    
    
    print("Writting output file to: " + output)
    

    return html

