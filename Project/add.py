#!C:\Python311\python.exe
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
  <li style="float:right"><a class="active" href="admin.py">Signout</a></li>
</ul>

</body>
</html>


''')
print('''
<html>
<head>
</head>
<body>
<form >
<center>
<h1 style="color:green;">Enter the patient name to Update tablet schelude</h1>
<h2>Patient- Name: <input type ="text" name="p"></h2>
<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Submit</button>
</center>
</form>
</body>
</html>
''')

cur.execute("SELECT * FROM  pat_details WHERE name=%s",(name))
result = cur.fetchone()
if result:
    print('''
<html>
<head>
<h1 style="color:green;"><center>Enter the medicine to be updated</center></h1>
</head>
<body>
<center>
<form action="tab.py" >
<h2  >Patient- Name: <input type ="text" name="p"></h2>
<h2  >Doctor_Name: <input type ="text" name="d"></h2>
<h2  >Medicine-Name: <input type ="text" name="n"></h2>
<h2  >Medicine-count: <input type ="text" name="c"></h2>
<h2  >Before or After Meal: <input type ="text" name="a"></h2>
<h2  >Time of day: <input type ="text" name="t"></h2>
<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Submit</button>
</center>
</form>
</body>
</html>
''')
    


else:
    print("<h1 style='color:green;'><center>This patient's details is not present in database</center></h1>")





