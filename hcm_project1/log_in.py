#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi,pymysql
db=pymysql.connect(host="localhost",user="root",password="Pugazh@22",database="healthcare")
cur=db.cursor()

#cur.execute("create database healthCare")
#cur.execute("use healthCare")
#cur.execute("create table admin(Name varchar(20),Email varchar(20),Password varchar(8))")

form=cgi.FieldStorage()
Name=form.getvalue("name")
email=form.getvalue("mail")
password=form.getvalue("pwd1")
rpassword=form.getvalue("pwd2")

query="insert into admin values(%s,%s,%s)"
value=[Name,email,password]
cur.execute(query,value)
db.commit()

if password==rpassword:
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <style type="text/css">
        #st1
        {
            position: absolute;
            height: 400px;
            width: 350px;
            background-color: rgba(223, 255, 255,0.6);
            margin-left: 500px;
            margin-top: 50px;
            padding-right: 50px;
            padding-left: 50px;
        }
        body
        {
            background-image:Url("login.jpg");
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: 1140px 700px;
        }
    </style>
    <title>Log-in Window</title>
    </head>
    
    <body>
    <div class="container"
    <div class="row">
    <nav class="navbar  navbar-inverse">
    <div class="container-fluid">
    <div class="navbar-header">
    <a class="navbar-brand" href="#">SK HEALTH CARE</a>
    </div>
    <ul class="nav navbar-nav">
    <li><a href="home.html">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
    <li><a href="sign_up.html" class="active"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
    </ul>
    </div>
    </nav>
    </div>

    <div class="row">
    <form class="form-horizontal"  action="patient_details.py">
            <div id="st1"align="center">
                    <div class="form-group">            
            <h2 style="font-weight: bold;">LOGIN</h2><br><br>
            <input type="email" name="m" placeholder="Email adress" class="form-control" required><br><br>
            <input type="password" name="pwd4" placeholder="Password" class="form-control" required><br>
            <h5><a href="#"> Forgot Password?</a></h5><br>
            <button type="submit" class=" btn btn-success"> SUBMIT</button><br><br>
            Not a Member?<a href="sign_up.html"> Register</a>	
		
	</div>		
	</div> 
    </div>
    </body>
    </html>''')

