# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 12-09-2016
# Ngon ngu lap trinh: Python 2
# Noi dung: Su dung Raspberry Pi doc gia tri nhiet do tu cam bien so DHT11
# Tham khao: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview

import Adafruit_DHT 	# Thu vien cua DHT11
import time

pinDHT = 17 		# Chan so 11 tren Board

def DHT11(): 		# Do nhiet do khong khi tu cam bien DHT11   
    h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,pinDHT) 	# Do am h, nhiet do t
    nhietdo = t
    return nhietdo

while True:
    print DHT11()
    time.sleep(10)
