from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    sender="bettywang1994@gmail.com"
    sender_pwd="19941018betty"
    to_email=email
    subject='Height Data'


    message="Hey there, your height is %s.Average height of all is %s based on %s samples" % (height,average_height,count)
    msg=MIMEText(message)
    print(type(msg))
    msg['Subject']=subject
    msg['From']=sender
    msg['to']=to_email
    try:
        gmail=smtplib.SMTP("smtp.gmail.com",587)
        gmail.ehlo()#identifies you to the SMTP server
        gmail.starttls()#use tls
        gmail.login(sender,sender_pwd)
        gmail.sendmail(sender,to_email,msg.as_string())#msg must be changed to string 
    except:
        print("something went wrong")
