# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 16-09-2016
# Ngon ngu lap trinh: Python 2
# Noi dung: Su dung Raspberry Pi phat hien chuyen dong voi cam bien PIR

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR = 23               		# GPIO17
delay = 1 			# Thoi gian giua cac lan kiem tra, don vi la giay
GPIO.setup(PIR_PIN,GPIO.IN)

try:
    print 'PIR Module phat hien chuyen dong (nhan CTRL + C de ket thuc)' 
    time.sleep(2)
    print 'San sang hoat dong'

    while True:
        if GPIO.input(PIR):
            print 'Co chuyen dong'

        time.sleep(delay)

except KeyboardInterrupt:	# Nhan Ctrl + C de thoat
    print 'Dung chuong trinh'
    GPIO.cleanup()
