#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
import cgi
form=cgi.FieldStorage()

db=pymysql.connect(host="localhost", user="root", password="sri9500", database="patients_details")
cur=db.cursor()

name=form.getvalue("p")
number=form.getvalue("n")
mail=form.getvalue("e")
password=form.getvalue("pa")
dob=form.getvalue("d") 
age=form.getvalue("a")
aad=form.getvalue("r")

table_name=name.lower()


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
  <li style="float:right"><a class="active" href="home.html">Signout</a></li>
</ul>

</body>
</html>


''')


cur.execute("SELECT * FROM  pat_details WHERE name=%s",(name))
result = cur.fetchone()
if result:
    #time.sleep(2)
    print('<h1 style="color:green;"><center>This Patient data is already registered </h1>')


else:
    query="insert into pat_details values(%s,%s,%s,%s,%s,%s,%s)"  
    val=[name,number,mail,password,dob,age,aad]
    cur.execute(query,val)
    db.commit()
    print('<h1 style="color:green;"><center>Patient data registered sucessfully.</h1>')
    sql = "CREATE TABLE " + table_name + " (doctor_name VARCHAR(40),medicine_name  VARCHAR(40),medication_count VARCHAR(40),meal VARCHAR(40),time_of_day VARCHAR(40))"
    cur.execute(sql)









