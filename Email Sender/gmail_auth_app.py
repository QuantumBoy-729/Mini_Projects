from email.message import EmailMessage
from pwdstore import password
import ssl,smtplib
emailSender = 'youremailaddress' 
emailPassWord = password

email_reciever = 'someone"s email addr'

subject = "Hello Macha!!"
body = """
    
    How are you, this is a trash message!
    Nahi
    Trash Nahi
    Tere maut ka farmaan hai
    Tere baare main sab jaanta hu main toh abhi mujhe 1000 rupay bhej
"""

Email = EmailMessage()
Email['From'] = emailSender
Email['To'] = email_reciever
Email['Subject'] = subject
Email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(emailSender,emailPassWord)
    smtp.sendmail(emailSender,email_reciever,Email.as_string())

