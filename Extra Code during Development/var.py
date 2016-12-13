import time
import math
from adxl345 import ADXL345

from datetime import datetime

adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" % (adxl345.address)
file = open("trial1.csv",'w')

def calVar(mean, arr):
        var = 0
	for i in range(24):
                var = var +( math.pow((arr[i]-mean),2))
	var=var/25
        return var


counter = 0
x=0
y=0
z=0
arra=[0]*25
Zth=.5
while True:
        Zmean=0
        sum =0
	var=0
        # for loop runs for 25 times and
        #collects 25 individual readings of X, Y and Z
        for i in range (24):
                axes = adxl345.getAxes(True)
                        #OBprint "   x = %.3fG" % ( axes['x'] )
                        #print "   y = %.3fG" % ( axes['y'] )
                        #print "   z = %.3fG" % ( axes['z'] )
               # print datetime.now().strftime('%H:%M:%S')
               # print "         x = %.3f    y = %.3f    z = %.3f" % ( axes['x'], axes['y'], axes['z'] )
                file.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
                arra[i]=axes['z']
                        #y=y+axes[y]
                        #z=z+axes[z]
                        #x1
                        #y2
                        #y3
                        #for j=1 to j=25
                        #x[j] = axes['x']
                sum = sum+axes['z']
                time.sleep(.02)
        #print sum

        #calculate Xmean ()
        #calculate Ymean ()
        Zmean = sum/25
        var=calVar(Zmean,arra)
	print "var = %.3f, Zmean = %.3f" %(var,Zmean)
        if var >= Zth:
                counter=counter+1
               #Zmean = 0
                if counter >= 2:
                        # initiate label value (1,2,3,4) and pass to PI
                        lable =1 #Only Z value changed, label as 1 and consider it as UP gesture
                        counter=0
                        print("UP Gesture")
                        #Zmean = 0
                else:
                        continue
        else:
                        counter=0
                        Zmean =0

