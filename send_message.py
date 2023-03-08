from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

class EmailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def send_message(self, emails, availability):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.email, self.password)

        body = "<pre style=\"font-family: Arial, sans-serif, 'Open Sans'\">\n"
        for date in availability:
            body += f"Availability on {date}:"
            for slot in availability[date]:
                body += f"{slot} | "
            body += "\n\n"
        body += "</pre>"

        earliest_date = list(availability.keys())[0]
        msg = MIMEMultipart()
        msg['Subject'] = f"Alert: Availability Found on {earliest_date}"
        msg.attach(MIMEText(body,'html'))

        to = emails
        smtp.sendmail(from_addr=self.email,
                    to_addrs=to, msg=msg.as_string())
        print("Email successfuly sent to",*emails)
        smtp.quit()
