import smtplib
from email.message import EmailMessage
import ssl
import smtplib

# Enter your email Address here
EMAIL_ADDR = ""

#Enter you password given by Google
EMAIL_PASS = ""

#Enter the receiver
EMAIL_REC = ""

subject = "Test Email"
body = "This is a test email"

em = EmailMessage()
em['From'] = EMAIL_ADDR
em['To'] = EMAIL_REC
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(EMAIL_ADDR, EMAIL_PASS)
    smtp.sendmail(EMAIL_ADDR, EMAIL_REC, em.as_string())
    print("Email Sent")