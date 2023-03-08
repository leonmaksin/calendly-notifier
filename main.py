from datetime import date
import os
from dotenv import load_dotenv
from engine import Engine

load_dotenv()

# Modify these values
event_type = os.getenv("EVENT_TYPE") # specific calendly event ID, I'll release a tutorial soon on how to find this
timezone = "Europe%2FBerlin" # your timezone
range_start = str(date.today()) # search range start
range_end = "2023-03-20" # search range end
sender_email = os.getenv("SENDER_EMAIL") # email used to send email alerts
sender_password = os.getenv("SENDER_PASSWORD") # password for email used to send email alerts
recipient_email = os.getenv("RECIPIENT_EMAIL") # email alert recipient email

engine = Engine(event_type, timezone, range_start, range_end,
                sender_email, sender_password, recipient_email)
engine.run()
