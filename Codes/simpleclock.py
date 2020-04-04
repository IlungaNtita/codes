import time
from datetime import datetime
import sys
import os
#import calender

days = 0

from turtle import *

setup()
tl=Turtle()
now = datetime.now()

#days_week=date.today()
#calendar.day_name[day_week.weekday()]  #'Wednesday'

day=datetime.today().strftime('%A')

while True:
	times=time.strftime('%H:%M:%S')
	tl.color("green")
	tl.screen.bgcolor('black')
	tl.clear() #to clear replace the written data
	
	tl.write(times.zfill(2), font=('arial',40,'normal'),align=("center") )
	tl.write(str(now.day)+" " + day +", "+ str(now.month) +", "+ str(now.year), align=("center"), font=("cambria", 8,"normal"))
	time.sleep(1)
	