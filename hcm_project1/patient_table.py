#!C:\Python311\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi,pymysql,mysql.connector
db=pymysql.connect(host="localhost",user="root",password="Pugazh@22",database="healthCare")
cur=db.cursor()

select_patient = """SELECT * FROM patient"""
cur.execute(select_patient)
result = cur.fetchall()

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
      <a class="navbar-brand" href="#">SK HEALTH CARE</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
      <li><a href="patient_details.py">Add Patient</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="mail.html" class="btn btn-dark"><span class="next"></span>Sent Alert</a></li>
    </ul>
    </div>
</nav>
<h1 align="center">Patient Details</h1>
</div>
 
''')

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

db.commit()

        
