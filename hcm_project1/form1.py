#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
form=cgi.FieldStorage()
a=int(form.getvalue("n1"))
b=int(form.getvalue("n2"))
print("<h1>Addition is: ",a+b,"</h1>")
