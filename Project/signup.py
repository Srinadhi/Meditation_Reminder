#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()

name=form.getvalue("u")
number=form.getvalue("n")
mail=form.getvalue("e")
password=form.getvalue("p")
dob=form.getvalue("d") 
age=form.getvalue("a")
aad=form.getvalue("r")

print('''
<!DOCTYPE html>
<html>
<head>
<style>
body {
  font-size: 28px;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
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

li a:hover {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}

</style>
</head>
<body>

<div class="header">
  <h2 style="color:green;"><center>Welcome to Self Care</center></h2>
  <h3 style="color:green;"><center>Self Care for Your Care...</center</h3>
</div>
<style>
	body{
		background-image:url('pro.jpg');
		background-repeat:no-repeat;
		background-size:cover;
}
</style>
<ul>
  <li><a href="home.html">Home</a></li>
  <li><a class="active" href="#signup">Signup</a></li>
  <li><a href="login.py">Login</a></li>
  <li><a href="#contact">News</a></li>
  <li style="float:right"><a href="#about">Contact:+91 9632541220</a></li>

</ul>

<h1 style="color:green;"><center>Welcome to <strong>Signup</strong>.</center></h1>
<form method="post">
<center>
<h5>User Name: <input type ="text" name="u"></h5>
<h5>Number: <input type="number" name='n'></h5>
<h5>Mail-Id: <input type="email"  name="e"></h5>
<h5 >Password: <input type="password" name="p"></h5>
<h5>Date of Birth: <input type="text" name='d'></h5>
<h5>Age: <input type="number" name='a'></h5>
<h5>Aadhar -No: <input type="text" name="r"></h5>

<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">SignUp</button>
<h2 >If you have already sigup,you can directly go to LogIn Page.</h2>
</center>
</form>
</body>
</html>
''')

cur.execute("SELECT * FROM admin_details WHERE aad=%s",(aad))
result = cur.fetchone()
if result:
    print('<h1 style="color:green;"><center>You are already Signup  </center></h1>')
else:
    query="insert into admin_details values(%s,%s,%s,%s,%s,%s,%s)"  
    val=[name,number,mail,password,dob,age,aad]
    cur.execute(query,val)
    db.commit()
    print('<h1 style="color:green;"><center>SignUp successfully</center></h1>')
