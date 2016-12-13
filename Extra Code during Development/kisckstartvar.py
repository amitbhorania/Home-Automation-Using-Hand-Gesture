import time
import math
import numpy

from adxl345 import ADXL345
from array import*

from datetime import datetime

adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" %(adxl345.address)
file = open("updown2.csv",'w')

my_arrayX = [0] * 25;
my_arrayY = [0] * 25;
my_arrayZ = [0] * 25;

xMean = 0
yMean = 0
zMean = 0

xVar = 0
yVar = 0
zVar = 0

counter = 0

Threshold = 0.5

def operations():
	print ("i am in operations")
	#time.sleep(2)
	return
	
while True:
	ymean=0
	ysum =0
        
	#for loop runs for 25 times and
	#collects 25 individual readings of X, Y and Z
	for i in range (24):
		axes = adxl345.getAxes(True)
		my_arrayX[i] = axes['x']
		my_arrayY[i] = axes['y']
		my_arrayZ[i] = axes['z']
		time.sleep(.01)

	#xMean = statistics.variance(my_arrayX[0:24]);
	#yMean = statistics.variance(my_arrayY[0:24]);
	#zMean = statistics.variance(my_arrayZ[0:24]);
	
	xMean = numpy.mean(my_arrayX[0:24]);
	yMean = numpy.mean(my_arrayY[0:24]);
	zMean = numpy.mean(my_arrayZ[0:24]);
	
	
	
	xVar = numpy.var(my_arrayX[0:24]);
	yVar = numpy.var(my_arrayY[0:24]);
	zVar = numpy.var(my_arrayZ[0:24]);
	
	#xVar = statistics.variance(my_arrayX[0:24]);
	#yVar = statistics.variance(my_arrayY[0:24]);
	#zVar = statistics.variance(my_arrayZ[0:24]);
	
	#print ("         xMean = {}    yMean = {}    zMean = {}    xVar = {}    yVar = {}    zVar = {}" .format ( xMean, yMean, zMean, xVar, yVar, zVar ))
	print "         xMean = %.3f    yMean = %.3f    zMean = %.3f    xVar = %.3f    yVar = %.3f    zVar = %.3f" % ( xMean, yMean, zMean, xVar, yVar, zVar )
 
	if yVar >= Threshold or xVar >= Threshold or zVar >= Threshold :
		counter=counter+1
		print " counter = %.3f" %( counter )
		if counter >= 2:
			print ("############initiated operations################# ")
			operations()
			print("operation() completed ")
		else:
			continue
	else:
		counter=0
