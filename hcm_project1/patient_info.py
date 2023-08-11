#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi,pymysql
db=pymysql.Connect(host="localhost",user="root",password="Pugazh@22",database="healthcare")
cur=db.cursor()
#cur.execute("use healthcare")
#cur.execute("create table patient2(Patient_Name varchar(20),Gender varchar(10),DOB date,Height int(3),Weight int(3),Health_issue varchar(20),Medicine varchar(20),Age int(3),Marital_status varchar(10),Mobile_Number varchar(10), Email varchar(25),Address varchar(50))")

form=cgi.FieldStorage()

name=form.getvalue("name")
gen=form.getvalue("gender")
Dob=form.getvalue("dob")
height=form.getvalue("h")
weight=form.getvalue("w")
health=form.getvalue("health")
medicine=form.getvalue("med")
age=form.getvalue("age")
marital=form.getvalue("marital")
mobile=form.getvalue("mob")
mail=form.getvalue("mail")
add=form.getvalue("add")




print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>

<body>
<div class="container">
<nav class="navbar  navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">HEALTH CARE</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
      
    </ul>
    </div>
</nav>
</div> 
''')
query= "insert into patient2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
value=[name,gen,Dob,height,weight,health,medicine,age,marital,mobile,mail,add]
print(value)
cur.execute(query,value)
print(name)
db.commit()

