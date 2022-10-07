from datetime import datetime
from playsound import playsound
import time

def check(t) :
    if len(t) != 11:
        return "Invalid format"
    else:
        if int(t[0:2])>12:
            time.sleep(1)
            return "Hour format is invalid"
        elif int(t[3:5])>59:
            time.sleep(1)
            return "Minute format is invalid"
        elif int(t[6:8])>59:
            time.sleep(1)
            return "Seconds format is invalid"
        else:
            time.sleep(1)
            return "Setting.."
while True:
    t = input("Enter time in format HH:MM:SS AM/PM: ")
    result = check(t)
    if result != "Setting..":
        print(result)
    else:
        print("Alarm set for time", t)
        break




