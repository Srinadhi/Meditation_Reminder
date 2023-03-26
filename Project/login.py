#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()




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
<style>
	body{
		background-image:url('doc.jpg');
		background-repeat:no-repeat;
		background-size:cover;
}
</style>
<body>

<div class="header">
  <h2 style="color:green;"><center>Welcome to Self Care</center></h2>
  <h3 style="color:green;"><center>Self Care for Your Care...</center</h3>
</div>

<ul>
  <li><a href="home.html">Home</a></li>
  <li><a href="signup.py">Signup</a></li>
  <li><a class="active" href="#login.py">Login</a></li>
  <li><a href="#contact">News</a></li>
  <li style="float:right"><a href="#about">Contact:+91 9632541220</a></li>

</ul>

<h1 style="color:green;"><center>Welcome to <strong>LogIn</strong>.</center></h1>
<form  action="confirm.py" method="post">
<center>
<h5  >User Name:<input type ="mail" name="u1"></h5><br>
<h5 >Mail-Id:<input type ="mail" name="e1"></h5><br>                        
<h5 >Password:<input type="password" name="p1"></h5><br>
<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Login</button>
</center>
</form>
</body>
</html>
''')

