import requests
import json
from send_message import EmailSender

def build_url(event_type, timezone, range_start, range_end):
    return f"https://calendly.com/api/booking/event_types/{event_type}/calendar/range?timezone={timezone}&diagnostics=false&range_start={range_start}&range_end={range_end}"

class Scraper:
    def __init__(self):
        self.url = ""
        self.emails = []
        self.sender_setup = False
    
    def set_url(self, event_type, timezone, range_start, range_end):
        self.url = build_url(event_type, timezone, range_start, range_end)
    
    def set_sender(self, email, password):
        self.sender_setup = True
        self.email_sender = EmailSender(email, password)
    
    def add_recipient(self, email):
        self.emails.append(email)

    def get_payload(self):
        return requests.get(self.url).json()

    def check(self):
        if self.url == "":
            print("Error: please specify the calendly you want to scrape with set_url")
            exit(1)
        if len(self.emails) == 0:
            print("Warning: no email recipient specified")
        if not self.sender_setup:
            print("Warning: email alerts not set up, please log in with set_sender")

    def get_availability(self):
        self.check()

        payload = self.get_payload()
        available_dates = {}

        days = payload["days"]
        num_dates = 0
        for day in days:
            date = day["date"]
            spots = day["spots"]
            if len(spots) > 0:
                num_dates += 1
                times = []
                for spot in spots:
                    time = spot["start_time"]
                    time = time.replace(date+"T","")
                    time = time.split('+')[0]
                    times.append(time)
                
                available_dates[date] = times

        if num_dates > 0:
            self.send_availability(available_dates)

    def send_availability(self, available_dates):
        if self.sender_setup:
            self.email_sender.send_message(self.emails, available_dates)
        with open("result.json", 'w') as outfile:
            json.dump(available_dates, outfile, indent=2)
