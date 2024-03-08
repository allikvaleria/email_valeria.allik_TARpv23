import smtplib, ssl
from email.message import EmailMessage

smpt_server="smtp.gmail.com"
port=587 #for starttls
sender_email="allik.valeria@gmail.com"
#to_email="marina.oleinik@tthk.ee"
password=input("Type ur password and press enter :")
context=ssl.create_default_context()
#Create a secure SSL context
#context= ssl.create_default_context()
#msg="Tere tulemast!"
msg=EmailMessage()
msg.set_content("Tere tulemast!")
msg['Subject']="Kirja teema"
msg['From']="allik.valeria@gmail.com"
msg['To']="marina.oleinik@tthk.ee"

#Try to log in to server and send email
try:
    server= smtplib.SMTP(smpt_server,port)
    server.ehlo() #Can be omitted
    server.starttls(context=context) #Secure the connection
    server.ehlo() #Can be omitted
    server.login(sender_email,password)
    #server.sendmail(sender_email,to_email,msg)
    server.send_message(msg)
except Exception as e :
    #Print any error massages to stdout
    print(e)
finally:
    server.quit()