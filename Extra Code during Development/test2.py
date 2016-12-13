#!/usr/bin/env python

import serial
import string

rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm" )

test=serial.Serial("/dev/ttyAMA0",115200)
test.open()

try:
    while True:
                test.write(string.translate(line, rot13))
                line = test.readline(eol='\r')

except KeyboardInterrupt:
    pass # do cleanup here

test.close()
