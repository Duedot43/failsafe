import os
import subprocess
#os.system("mkdir /home/elliott/Documents/remotestart/server/linux/failsafe")
subprocess.call(["git", "clone", "https://github.com/Duedot43/failsafe.git"])
os.system("rm startup.py ; cd failsafe ; mv startup.py ..")

cmd1 = "rm /home/elliott/Documents/remotestart/server/linux/ngrok.log"

subprocess.Popen(["rm", "/home/elliott/Documents/remotestart/server/linux/ngrok.log"])
cmd2 = "xterm -e ./ngrok tcp 25565"
subprocess.Popen(["xterm", "-e", "./ngrok", "tcp", "25565"])
os.system("sleep 2")
update = open('/home/elliott/Documents/remotestart/server/linux/ngrok.log','r')
for line in update:
    ngrok = line.strip()
print(ngrok)

subprocess.Popen(["xterm", "-e", "./start.sh"])
#ngrok = "test"
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "Ello! there's a new ip!!"

#The mail addresses and password
sender_address = 'hehe.exe.py@gmail.com'
sender_pass = 'M5FS8rWDQatRq9'
receiver_address = 'Jackgendill@icloud.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'New IP!!'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
message.attach(MIMEText(ngrok, 'plain'))

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
mail_content = 'Ello! there tis a new ip!!'

#The mail addresses and password

receiver_address = 'jgonzalez67@cherrycreekschools.org'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'New IP!!'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
message.attach(MIMEText(ngrok, 'plain'))

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
mail_content = 'Ello! there tis a new ip!!'

#The mail addresses and password

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'New IP!!'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
