#!/usr/bin/env python
from datetime import datetime
import time

from config import alarm
from transition import Transition
from splash import splash

alarm_wait = 10
post_alarm_wait = 30
transition_step_time = 0.1

def check(hour, minute):
    x = datetime.today()
    y = datetime.today().replace(minute = minute, hour = hour)
    return (x.hour == y.hour and x.minute == y.minute)

def fire_alarm():
    t = Transition(transition_step_time)
    t.start()

    time.sleep(post_alarm_wait)

def schedule_alarm(hour, minute):
    while(check(hour, minute) == False):
        print(".")
        time.sleep(alarm_wait)
    fire_alarm()

if(__name__ == '__main__'):
    splash()
    while(True):
        schedule_alarm(alarm["start_hour"], alarm["start_minute"])
