# Thuc hien: Thi Minh Nhut - Email: thiminhnhut@gmail.com
# Thoi gian: 12-09-2016
# Ngon ngu lap trinh: Python 2
# Noi dung: Su dung Raspberry Pi doc gia tri nhiet do tu cam bien analog LM35 thong qua Arduino

import pyfirmata 				# Dung dieu khien Arduino
import time

def LM35(): 					# Cam bien LM35 do nhiet do be mat dat
    t1=time.time() 				# Thoi gian bat dau xu ly
    sleep = 3 					# Don vi: phut. Thoi gian doi lay so lieu (trong truong hop tin hieu truyen khong tot)
    
    port = '/dev/ttyACM0'					# Cong giao tiep giua Arduino va RPi
    board = pyfirmata.Arduino(port) 		# Nhan board Arduino
    analog_pin = board.get_pin('a:1:i')		# Chan analog A1
    it = pyfirmata.util.Iterator(board)
    it.start()
    analog_pin.enable_reporting()
    
    i = 0
    while i == 0:
        time.sleep(5)
        reading = analog_pin.read()				# Da chia cho 1024 roi, khac voi Arduino
        if reading != None:
            nhietdo = (reading*5.0*1000)/10
            i = 1
        else:
            i = 0

        if i == 0:								# Chua lay duoc nhiet do
            if (time.time()-t1) > (sleep*60): 	# Qua thoi gian cho phep do so lieu
                break 							
            
    return nhietdo

while True:
    print LM35()
    time.sleep(10)
