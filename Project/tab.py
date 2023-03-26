#!C:\Program Files\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()

name=form.getvalue("p")


doc=form.getvalue("d")
med_name=form.getvalue("n")
med_cou=form.getvalue("c")
boa=form.getvalue("a")
tod=form.getvalue("t")


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
  <li><a href="home.html">Home</a></li>
  <li><a class="active" href="add.py">People</a></li>
  <li><a href="admin.py">Send-Mail</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="admin.py">Send-Mail</a></li>
</ul>

</body>
</html>
''')
x=name.lower()
query="insert into "+x+" values(%s,%s,%s,%s,%s)"
value=[doc,med_name,med_cou,boa,tod]
db.commit()
print("<h1 style='color:green;'><center>",name,'tabltes updated sucessfully</center></h1>')


