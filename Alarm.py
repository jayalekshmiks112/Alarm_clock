from datetime import datetime
from playsound import playsound
import time

def check(t) :
    if len(t) != 11:
        return "Invalid format"
    else:
        if int(t[0:2]) > 12:
            time.sleep(1)
            return("Hour format is invalid")
        if int(t[3:5]) > 59:
            time.sleep(1)
            return("Minute format is invalid")
        if int(t[6:8]) > 59:
            time.sleep(1)
            return("Seconds format is invalid")
        else:
            time.sleep(1)
            return("Setting..")

while True:
    t = input("Enter time in format HH:MM:SS AM/PM: ")
    result = check(t)
    if result != "Setting..":
        print(result)
    else:
        print("Alarm set for time", t)
        break

hour = t[0:2]
min = t[3:5]
sec = t[6:8]
period = t[9:].upper()

while True:
    now = datetime.now()

    c_hour = now.strftime("%I")
    c_min = now.strftime("%M")
    c_sec = now.strftime("%S")
    c_period = now.strftime("%p")

    if period == c_period:
        if hour == c_hour:
            if min == c_min:
                if sec == c_sec:
                    print("Wake up!!!!")
                    break



