#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()


name1=form.getvalue("u1")
mail1=form.getvalue("e1")
password1=form.getvalue("p1")

sql = "SELECT * FROM admin_details WHERE name=%s  AND  mail=%s AND password=%s"
val = [name1,mail1,password1]
cur.execute(sql, val)
result = cur.fetchone()
print('''
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<style>
	body{
		background-image:url('pro1.jpg');
		background-repeat:no-repeat;
		background-size:cover;
}
</style>
<body>

<ul>
  <li><a  class="active" href="home.html">Home</a></li>
  <li><a href="add.py">People</a></li>
  <li><a href="admin.py">Send-Mail</a></li>
  <li><a href="">Contact</a></li>

  <li style="float:right"><a class="active" href="home.html">Signout</a></li>
</ul>

</body>
</html>


''')
if result:
    print("<h1 style='color:green;'><center>Welcome",name1, "if you want to add new patient please fill the details</center></h1><br><br><br>")
    print('''
<html>
<head>
<title> Add new Patient Details</title>
</head>
<body>
<form action="user.py" method="post">
<center>
<h2>Patient- Name: <input type ="text" name="p"></h2>
<h2>Phone-Number: <input type="number" name='n'></h2>
<h2>Mail-Id: <input type="email"  name="e"></h2>
<h2>Password: <input type="password" name="pa"></h2>
<h2>Date of Birth: <input type="text" name='d'></h2>
<h2>Age: <input type="number" name='a'></h2>
<h2>Aadhar -No: <input type="text" name="r"></h2>
<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Login</button>
</center>
</form>
</body>
</html>
''')
    


else:
    print( "<h1 style='color:green;'><center>Invalid username or password</center></h1>")


