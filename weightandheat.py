#15V=PIN12  70V=PIN13 75V=PIN15 Buzzer=PIN16
#"python 0929.py" to run this code
#
import serial
import RPi.GPIO as GPIO
import time
from mlx90614 import MLX90614
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23
VT15=18
VT70=27
VT75=22
tall=0.0
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(VT15,GPIO.OUT)
GPIO.setup(VT70,GPIO.OUT)
GPIO.setup(VT75,GPIO.OUT)
ser= serial.Serial('/dev/ttyUSB0',9600,timeout=0.2);
thermometer_address = 0x5a
thermometer = MLX90614(thermometer_address)
heavy=int(input('input weight:'))
print("target weight=")
print(heavy)

while 1:
  start=time.time()
  response=ser.readall();
  #print(response);
  a=response;
  print(a);
  b=a.decode('UTF-8');
  b.strip();
  print(b);
  #print(len(b));
  if(len(b)>0):
      #print("hi")
      #print(type(b))
      c=int(b)
      #print(type(c))
      print("weight:",c)
      amb=((thermometer.get_amb_temp()))
      obj=((thermometer.get_obj_temp()))
      print("surrounding:",amb)
      print("face:",obj)
      if(c<heavy):
        #if(c<500)
        GPIO.output(buzzer,GPIO.HIGH)
        #print("a")
        GPIO.output(buzzer,GPIO.LOW)
        break
      if(c>heavy):
        if(amb>=25):
          if(obj<37):
            GPIO.output(VT75,GPIO.LOW)
            GPIO.output(VT15,GPIO.LOW) 
            GPIO.output(VT70,GPIO.HIGH)
            print("volt=70")
          if(obj>=37):
            GPIO.output(VT75,GPIO.LOW)
            GPIO.output(VT70,GPIO.LOW) 
            GPIO.output(VT15,GPIO.HIGH)
            print("volt=15")
        if(amb<25):
          if(obj<37):
            GPIO.output(VT70,GPIO.LOW)
            GPIO.output(VT15,GPIO.LOW) 
            GPIO.output(VT75,GPIO.HIGH)
            print("volt=75")
          if(obj>=37):
            GPIO.output(VT75,GPIO.LOW)
            GPIO.output(VT70,GPIO.LOW) 
            GPIO.output(VT15,GPIO.HIGH)
            print("15")
        if(obj>38):
          GPIO.output(VT75,GPIO.LOW)
          GPIO.output(VT70,GPIO.LOW)
          GPIO.output(VT15,GPIO.LOW)
          print("no") 
        end=time.time()
        tall=(end-start)+tall
        t=int(tall)
        #print(t)
        if(t>=180):
          GPIO.output(VT70,GPIO.LOW)
          print("stop")
          break
        #if(c>500):
          #print("b")
          #GPIO.output(buzzer,GPIO.HIGH)
          #sleep(0.5)
          #GPIO.output(buzzer,GPIO.LOW)

    #print(int(a));
    #int(response)
    #print(type(response));
    #g=response;
    #k=1;
    #g=g+k;
    #print g;
    #print k;

