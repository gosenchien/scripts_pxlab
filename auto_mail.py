import smtplib
import datetime
date_object = datetime.date.today()

smtpssl=smtplib.SMTP("smtp.gmail.com",587)
smtpssl.ehlo()
smtp.starttls()
smtp.login("GTWPX01@gmail.com","fbhpxgsjvkxjcdau")
from_addr="GTWPX01@gmail.com"
to_addr=["chiensheng@google.com","peggykao@google.com","maylalee@google.com","jamc@google.com"]
msg="Subject:Gmail sent by Python script_testing\nHello World!"
status=smtp.sendmail(from_addr,to_addr,msg)
if status=={}:
    print("mail send out success")
else:
    print("mail sent fail!")
    smtp.quit()
 attachments = ['/home/hvst01/signalData/(str(date_object)+ '_signal.txt')']

