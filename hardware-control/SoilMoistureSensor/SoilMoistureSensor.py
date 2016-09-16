# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 16-09-2016
# Ngon ngu lap trinh: Python 2
# Noi dung: Su dung Raspberry Pi phat hien do am dat

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

D0 = 17 			# GPIO17
delay = 10 			# Thoi gian giua cac lan do, don vi la giay
GPIO.setup(D0,GPIO.IN)		# Dat chan D0 la chan nhan tin hieu vao (IN)

try:
    while True:
        if GPIO.input(D0) == 1: 
            print "Dat kho"
        else:
            print "Dat am"

        time.sleep(delay)
        
except KeyboardInterrupt:	# Nhan Ctrl + C de thoat
    GPIO.cleanup()
    print "Dung chuong trinh"
