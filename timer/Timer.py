import time
from math import floor
from playsound import playsound

class Timer:
    def __init__(self, duration) -> None:
        self.timeLeft = duration
    
    def timeStamp(self):
        hours = floor(self.timeLeft/3600)
        minutes = floor((self.timeLeft-hours)/60)
        seconds = self.timeLeft-hours*3600-minutes*60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def start(self):
        print("TIME LEFT:")
        print("hh:mm:ss")
        print(self.timeStamp(), end='\r')
        while self.timeLeft > 0:
            time.sleep(1)
            self.timeLeft -= 1
            print(self.timeStamp(), end='\r')
        print("00:00:00")
    
    def playAlarm(self): 
        while(True):
            print('Time up!!')
            playsound('/home/stefano/code/python/timer/alarm.wav')
