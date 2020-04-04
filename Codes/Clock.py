#creating an alarm
#first lets create it so it displays the seconds, minute and hours.
import time
from datetime import datetime

days = 0

#next lets import time for the time.sleep(x) funtion

from turtle import *

setup()
tl = Turtle()
#now we have a turtle tl that will build our time
#now we build a loop
while True:
	now = datetime.now()
	seconds = now.second
	minutes = now.minute
	hours = now.hour
	tl.clear() #to clear replace the written data
	tl.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2)+":" + str(seconds).zfill(2), font=("arial", 25, "normal"))
	#zfill(2) forces python to display the str in 2 digits
	seconds += 1
	time.sleep(1)
	#now we want to restart the seconds to restart its countdown from 59 secons to 0 seconds.
	if seconds == 60: #now i want the clock to add 1min for every 60 seconds 
		minutes += 1
		seconds = 0
		#seconds start back from 0 to 60 again
		time.sleep(1)
	if minutes == 60:
		hours += 1
		minutes = 0
		#same here
		time.sleep(1)
	if hours == 24:
		days += 1
		hours = 0
		time.sleep(1)
	