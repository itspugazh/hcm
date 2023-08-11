#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi,pymysql
con=pymysql.Connect(host="localhost",user="root",password="Pugazh@22",database="healthcare")
cursor=con.cursor()
#cur.execute("use healthcare")
#cur.execute("create table patient(Patient_Name varchar(20),Gender varchar(10),DOB date,Age int(3),Marital_status varchar(10),Health_issue varchar(20),Medicine varchar(20),Mobile_Number varchar(10), Email varchar(25),Address varchar(50))")

form=cgi.FieldStorage()

name=form.getvalue("name")
gen=form.getvalue("gender")
Dob=form.getvalue("dob")
age=form.getvalue("age")
marital=form.getvalue("marital")
health=form.getvalue("health")
medicine=form.getvalue("med")
mobile=form.getvalue("mob")
mail=form.getvalue("mail")
add=form.getvalue("add")

query= "INSERT INTO patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
value=[name,gen,Dob,age,marital,health,medicine,mobile,mail,add]
cursor.execute(query,value)


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
<style type="text/css">
    #st2
    {
            position: absolute;
            height: 480px;
            width: 350px;
            background-color: rgba(223, 255, 255,0.6);
            margin-left: 400px;
            margin-top: 40px;
            padding-right: 50px;
            padding-left: 50px;

    }
    body
        {
            background-image:Url("doctor3.jpg");
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: 1140px 700px;
        }
</style>

<body>
<div class="container">
<nav class="navbar  navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">SK HEALTH CARE</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
      <li><a href="patient_details.html">Add Patient</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="home.html" class="btn btn-info btn-lg" style= "background-color:black;"><span class="glyphicon glyphicon-log-out"></span>Logout</a></li>
    </ul>
    </div>
</nav>
<h2 align="center">Patient Details</h2>
</div>

''')

select_patient = """SELECT * FROM patient"""
cursor.execute(select_patient)
result = cursor.fetchall()

print("<div class='container'>")
print("<table class='table table-striped table-hover'>")
print("<thead>")
print("<tr>")
print("<th>Patient Name</th><th>Gender</th><th>DOB</th><th>Age</th><th>Marital Status</th><th>Health Issue</th><th>Medicine Name</th><th>Mobile Number</th><th>Email</th><th>Address</th>")
print("</tr>")
print("</thead>")
for row in result:
    print("<tr>")
    print("<td>{}</td>".format(row[0]))
    print("<td>{}</td>".format(row[1]))
    print("<td>{}</td>".format(row[2]))
    print("<td>{}</td>".format(row[3]))
    print("<td>{}</td>".format(row[4]))
    print("<td>{}</td>".format(row[5]))
    print("<td>{}</td>".format(row[6]))
    print("<td>{}</td>".format(row[7]))
    print("<td>{}</td>".format(row[8]))
    print("<td>{}</td>".format(row[9]))
    print("</tr>")
print("</table>")
print("</div>")
print("</body>")
print("</html>")
con.commit()
print('''
<div class="container">
<div class="row">
<form class="form-horizontal" id="log-in" method="post" action="mail.py">
<div id="st2" align="center">
    <div class="form-group">
    <label class="l1"><h3> Medicine Reminder </h3></label><br>
    
    <label class="l1">Patient Name: </label>	
    <input type="text" name="pname" class="form-control"><br>		

    <label class="l1">Patient Email Id: </label>	
    <input type="Email" name="pmail" class="form-control"><br>
    
    <label class="l1" for="sel1">Medicine's: </label>
    <select multiple class="form-control" id="sel1" name="med" required>
            <option>metformin</option>
            <option>amlodipine,felodipine</option>
            <option>Omeprazole,pantoprazole and lansoprazole</option>
            <option>acetaminophen</option>
            <option>Levothyroxine</option>
    </select><br>					

    <label class="l1">time: </label>	
    <input type="time" name="time" class="form-control"><br>	

    <button type="submit" class=" btn btn-success btn-lg">Send Mail</button>
''')

