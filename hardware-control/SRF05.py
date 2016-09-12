# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 12-09-2016
# Ngon ngu lap trinh: Python 2
# Noi dung: Su dung Raspberry Pi do khoang cach voi cam bien sieu am SRF05
# Tham khao 1: http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/
# Tham khao 2: http://www.raspberrypi-spy.co.uk/2013/01/ultrasonic-distance-measurement-using-python-part-2/


import RPi.GPIO as GPIO 	# Can thiep den chan GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 22 		# Chan so 15 tren Board
GPIO_ECHO    = 27 		# Chan so 13 treb Board

def SRF05():    
    GPIO.setwarnings(False) 
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)		# Chan phat tin hieu
    GPIO.setup(GPIO_ECHO,GPIO.IN)      		# Chan thu tin hieu

    # Dat chan phat muc thap truoc khi phat tin hieu
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5) 				# Thoi gian nhan Module SRF05

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True) 		# Bat dau phat
    time.sleep(0.00001)	   	 		# Chan phat tin hieu trong 10us = 0.00001s
    GPIO.output(GPIO_TRIGGER, False)		# Dung phat tin hieu

    # Thoi gian bat dau nhan tin hieu
    # Chan echo chuyen tu muc thap len muc cao
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
          start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
          stop = time.time()

    # Calculate pulse length    
    elapsed = stop-start 			# Thoi gian nhan tin hieu, don vi la us

    # Distance pulse travelled in that time is time
    # Quang duong s = vt
    distance = (elapsed * 34400)/2 		# Don vi cm
    return distance

while True:
    print SRF05()
    time.sleep(10)
