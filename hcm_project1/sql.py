
import cgi,pymysql
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pugazh@22",
    database="healthcare"
)

cursor = db.cursor()
query = "SELECT * FROM admin"
cursor.execute(query)

data = cursor.fetchall()

# Print HTML table
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>MySQL Data</title>")
print("</head>")
print("<body>")
print("<table>")
print("<tr><th>NAme</th><th>Email</th><th>password</th></tr>")
for row in data:
    print("<tr>") 
    print("<td>{}</td>".format(row[0]))
    print("<td>{}</td>".format(row[1]))
    print("<td>{}</td>".format(row[2]))
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")

db.close()
    
