import schedule
import time
import smtplib

sender_email = "sridummypro@gmail.com"
receiver_email = "srinadhianandan0905@gmail.com"
password = "qcqlggmmdlnqynxw"
message = "Hello, this is a test email!"

def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully")



schedule.every().day.at("16:16:00").do(send_email)
schedule.every().day.at("16:17:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
print('ok')
