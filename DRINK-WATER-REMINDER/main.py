import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(title = "Please sip some water ", message = "you need to drink some water!")
    time.sleep(60*60)