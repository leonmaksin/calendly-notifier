import time
from scraper import Scraper

class Engine:
    def __init__(self, event_type, timezone, range_start, range_end,
                 sender_email, sender_password, recipient_email):
        pass
        if range_end < range_start:
            print("Error: Invalid date range")
            exit(1)

        self.scraper = Scraper()
        self.scraper.set_url(event_type, timezone, range_start, range_end)
        self.scraper.set_sender(sender_email, sender_password)
        self.scraper.add_recipient(recipient_email)

    def run(self):
        self.is_running = True
        while self.is_running:
            print("Running cycle")
            self.scraper.get_availability()
            time.sleep(30)