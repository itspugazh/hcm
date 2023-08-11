"""#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
db=pymysql.Connect(host="localhost",user="root",password="Pugazh@22",database="healthCare")
cur=db.cursor()

import cgi
form=cgi.FieldStorage()

from email.message import EmailMessage
import ssl
import smtplib


pat_name=form.getvalue("pname")
pat_mail=form.getvalue("pmail")
#pat_category=form.getvalue("health")
med_name=form.getvalue("med")
med_time=(form.getvalue("time"))

email_sen='pugazhenthis123@gmail.com'
email_pass='rgzwxibrvepletsp'
email_rece=pat_mail
subject="Don't forget to take medicine"
body=("hello, "+pat_name+" now time is: "+str(med_time)+", you need to take "+med_name+" tablet")

em=EmailMessage()
em["From"]=email_sen
em["To"]=email_rece
em["Subject"]=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_sen,email_pass)
    smtp.sendmail(email_sen,email_rece,em.as_string())
  
print('''
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
<title>Mail sended page</title>

</head>
<body>

<div class="container">
<div class="row">
<div align="center" id="st1">
<h1>Mail sent successfully!.</h1>
</div>	
</div>
</div> 	
</div>

</body>
</html>
''')



""""""
from email.message import EmailMessage
import ssl
import smtplib
email_s='pugazhenthis123@gmail.com'
email_p='rgzwxibrvepletsp'
email_r='spugazh2000@gmail.com'
subject="Don't forget to take medicine"
body=("hello, you need to take medicine")

em=EmailMessage()
em["From"]=email_s
em["To"]=email_r
em["Subject"]=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_s,email_p)
    smtp.sendmail(email_s,email_r,em.as_string())
"""


"""
try:
    query="insert into mail values(%s,%s,%s)"
    val=[pat_name,pat_mail,med_time]
    cur.execute(query,val)
    db.commit()
except Exception as e:
    print("Error executing SQL query:", e)
    db.rollback()
finally:
    cur.close()
    db.close()

"""


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        self.stock += quantity
    
class StockManager:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product.name] = product
    
    def remove_product(self, name):
        del self.products[name]
    
    def update_stock(self, name, quantity):
        self.products[name].update_stock(quantity)
    
    def generate_report(self):
        print("Current Stock Levels:")
        for product_name, product in self.products.items():
            print(f"{product_name}: {product.stock}")
    
    def make_sale(self, name, quantity):
        if name not in self.products:
            print("Error: Product not found.")
            return False
        elif self.products[name].stock < quantity:
            print("Error: Not enough stock.")
            return False
        else:
            self.products[name].update_stock(-quantity)
            print(f"Sale made: {quantity} x {name} for {quantity * self.products[name].price} dollars.")
            return True

name=['a','b']
price=['20','40']
quantity=['10','10']
p=Product(name,price,quantity)











