import smtplib

sender = 'efeekpomebe@gmail.com'
receivers = 'efeekpomebe@gmail.com'

message = """From: Efe <efeekpomebe@gmail.com>
To: efeekpomebe <efeekpomebe@gmail.com>
Subject: SMTP e-mail test

This is a test email message.

"""

try:
    smtpobj = smtplib.SMTP('smtp.gmail.com', 465)
    smtpobj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
