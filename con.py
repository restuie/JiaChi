import serial
#from time import sleep
import time
ser= serial.Serial('/dev/ttyUSB0',9600,timeout=0.2)
try: 
  while 1:
    response=ser.readall()
    a=response

    b=a.decode('UTF-8')
    b.strip()

    if(len(b)>0):
        c=int(b)
        print("weight:",c)
except:
  ser.close
