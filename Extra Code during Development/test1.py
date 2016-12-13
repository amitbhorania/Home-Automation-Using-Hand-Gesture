import time
from adxl345 import ADXL345
x=0.888
from datetime import datetime  

adxl345 = ADXL345()

print "ADXL345 on address 0x%x:" % (adxl345.address)
file = open("up2dec.csv",'w')


while True:
	axes = adxl345.getAxes(True)
#	print "   x = %.3fG" % ( axes['x'] )
#	print "   y = %.3fG" % ( axes['y'] )
#	print "   z = %.3fG" % ( axes['z'] )
	print datetime.now().strftime('%H:%M:%S')
	print " 	x = %.3f    y = %.3f    z = %.3f" % ( axes['x'], axes['y'], axes['z'] )
#	if (axes['x'] or  axes['y'] or axes['x'])  >= x:
	file.write(" %s,%.3f,%.3f,%.3f\n" % (datetime.now().strftime('%H:%M:%S'),axes['x'],axes['y'],axes['z']))
	time.sleep(.2)
