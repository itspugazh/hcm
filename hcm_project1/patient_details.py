#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi,pymysql
db=pymysql.connect(host="localhost",user="root",password="Pugazh@22",database="healthCare")
cur=db.cursor()

form=cgi.FieldStorage()
log_mail=form.getvalue("m")
log_pass1=form.getvalue("pwd4")

cur.execute("select * from admin")

for i in cur:
    if i[1]==log_mail:
        if i[2]==log_pass1:
            print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<style type="text/css">
        #st1
        {
                position: absolute;
                height: 1100px;
                width: 480px;
                margin-left: 500px;
                padding-right: 50px;
                padding-left: 50px;
                background-color: rgba(223, 255, 255, 0.6);
                border-radius: 20px;
        }
        .l1
        {
                font-family: cambria;
                font-size: 20px;
        }
        body
        {
                background-image:Url("doctor2.jpg");
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: 1170px 800px;
        }
</style>
<title></title>
</head>
<body>
<div class="container">
<div class="row">
        <nav class="navbar  navbar-inverse">
        <div class="container-fluid">
        <div class="navbar-header">
        <a class="navbar-brand" href="#">SK HEALTH CARE</a>
        </div>
        <ul class="nav navbar-nav">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
        </ul>
        </div>
</nav>
</div>
</div>
<div class="container mt-3">
<div class="row">
    <form name="f1" class="form-horizontal" id="st1" method="POST" action="patient.py">
    <div class="form-group">
    <h2 align="center" style="font-weight: bold;">PATIENT DETAILS</h2><br>

    <label class="l1">Patient Name: </label>
    <input type="text" name="name" class="form-control" required><br>

    <label class="l1" for="sel1">Gender: </label>
    <select class="form-control" id="sel1" name="gender" required>
            <option>Male</option>
            <option>Female</option>
            <option>Others</option>
    </select><br>

    <label class="l1">DOB: </label>
    <input type="date" name="dob" class="form-control" required><br>

    <label class="l1">Age: </label>	
    <input type="text" name="age" class="form-control" required><br>

    <label class="l1" for="sel1" class="form-label">Marital Status:</label>
    <select class="form-control" id="sel1" name="marital" required>
      <option>Single</option>
      <option>Married</option>
      <option>Divorced</option>
      <option>Widowed</option>
    </select><br>		

    <label class="l1" for="sel1">Health Issue: </label>
    <select class="form-control" id="sel1" name="health" required>
            
            <option>Diabetes</option>
            <option>High Blood Pressure</option>
            <option>Ulcer</option>
            <option>Fever</option>
            <option>Thyroid Problems</option>
    </select><br>

    <label class="l1" for="sel1">Medicine's: </label>
    <select multiple class="form-control" id="sel1" name="med" required>
            <option>metformin</option>
            <option>amlodipine,felodipine</option>
            <option>Omeprazole,pantoprazole and lansoprazole</option>
            <option>acetaminophen</option>
            <option>Levothyroxine</option>
    </select><br>					

    
    <label class="l1">Mobile Number: </label>	
    <input type="tel" name="mob" maxlength="10" class="form-control" required><br>		

    <label class="l1">Email Id: </label>	
    <input type="Email" name="mail" class="form-control" required><br>	

    <label class="l1">Address: </label>	
    <input type="text" name="add" class="form-control" required><br><br>
    
    <button type="submit" class=" btn btn-success btn-block btn-lg" style="back">UPLOAD</button>
</div>
</form>

</div>
</div>

</body>
</html>
''')
