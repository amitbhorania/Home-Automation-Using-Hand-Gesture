import time
import math
from adxl345 import ADXL345

from datetime import datetime

adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" % (adxl345.address)
file = open("test1.csv",'w')

counter = 0
x=0
y=0
z=0
yth=.3

def operations():
	print ("i am in operations")
	time.sleep(2)
	return


while True:
	ymean=0
	ysum =0
        # for loop runs for 25 times and
        #collects 25 individual readings of X, Y and Z
        for i in range (24):
                axes = adxl345.getAxes(True)
                ysum = abs(ysum+axes['y'])
                time.sleep(.01)
		file.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	ymean = abs(ysum/25)
        print "         x = %.3f    y = %.3f    z = %.3f mean = %.3f " % ( axes['x'], axes['y'], axes['z'],ymean )
	file.write(" %s,%.3f,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z'],ymean))
	#print "ymean = %.3f " %(ymean)
        if ymean >= yth:
                counter=counter+1
		print("counter= %.3f"%( counter))
                if counter >= 2:
			print("initiated operations")
			operations()
			print("operation() completed ")
		
		else:
			continue
	else:
		counter=0




