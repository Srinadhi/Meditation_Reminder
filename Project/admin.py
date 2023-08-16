#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")


import pymysql
import smtplib
from email.mime.text import MIMEText
import cgi


form=cgi.FieldStorage()


name=form.getvalue('p')
mail=form.getvalue('m')


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
  <li><a href="add.py">People</a></li>
  <li><a class="active" href="admin.py">Send-Mail</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="home.html">Signout</a></li>
</ul>

</body>
</html>


''')
print('''
<html>
<head>
<h1 style="color:green;"> <center>Enter the patient name to Update tablet schelude</center></h1>
</head>
<body>
<form >
<center>
<h2  >Patient- Name: <input type ="text" name="p"></h2>
<h2  >Mail_ID: <input type ="mail" name="m"></h2>
<button type="submit" style="background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer;">Submit</button>
</center>
</form>
</body>
</html>
''')


x=name.lower()



r=mail
p="qcqlggmmdlnqynxw"

# Connect to the MySQL database
db = pymysql.connect(
  host="localhost",
  user="root",
  password="sri9500",
  database="patients_details"
)


 
mycursor = db.cursor()
query=("SELECT doctor_name, medicine_name,medication_count,meal,time_of_day FROM {}".format(x))
mycursor.execute(query)
medication_data = mycursor.fetchall()




time_groups = {}
for data in medication_data:
    time_of_day = data[4]
    if time_of_day not in time_groups:
        time_groups[time_of_day] = []
    time_groups[time_of_day].append(data)




sender_email = "sridummypro@gmail.com"
sender_password = p
subject = "Medication Schedule"



for time_of_day, time_group in time_groups.items():
    message = f"Dear {name},\n\nYour medication schedule for {time_of_day} is as follows:\n\n"
    for data in time_group:
        medicine_name = data[1]
        medication_count = data[2]
        meal=data[3]
        message += f"{meal}:{medication_count}:{medicine_name}\n"
    message += "\nRegards,\nYour Healthcare Provider"
    recipient_email = mail
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    

        
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(sender_email, sender_password)
    smtp_connection.sendmail(sender_email, recipient_email, msg.as_string())
    smtp_connection.quit()

print("<h1 style='color:green;'><center>&#128512;Mail sent to patient</center></h1>") 


