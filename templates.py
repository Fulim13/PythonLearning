# email package - subpackage mime (multipurpose internet main extension - standard define the format of email)
# this class support html and plain text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from string import Template
from pathlib import Path


template = Template(Path("templates.html").read_text())


message = MIMEMultipart()
message["from"] = "Fu Lim"
message["to"] = "limtest13@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
# body = template.substitute(name="John") same as above
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("zoro.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # hey our client want to connect smtp
    smtp.starttls()  # put the smtp connection to tls (transport layer security- all the thing send to smtp server will be encryted)
    # for password -https://www.letscodemore.com/blog/smtplib-smtpauthenticationerror-username-and-password-not-accepted/
    smtp.login("fulim1130@gmail.com", "fvbofzktsothiqbz")
    smtp.send_message(message)
    print("Sent ...")
