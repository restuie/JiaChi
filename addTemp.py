import time
import Jetson.GPIO as GPIO
from PyQt5 import QtCore

class addTemp(QtCore.QThread):
    #rawdata = QtCore.pyqtSignal(float)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.runing = False
        self.led_pin = 40

        self.buzzer=23
        self.VT15=18
        self.VT70=27
        self.VT75=22

        self.GPIO = GPIO
        self.GPIO.setwarnings(False)
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(self.led_pin,GPIO.OUT)
        self.GPIO.setup(self.buzzer,GPIO.OUT)
        self.GPIO.setup(self.VT15,GPIO.OUT)
        self.GPIO.setup(self.VT70,GPIO.OUT)
        self.GPIO.setup(self.VT75,GPIO.OUT)


    def run(self):
        while self.runing:
            try:
                self.GPIO.output(self.led_pin,self.GPIO.HIGH)
            except IOError:
                print("GPIO not output")

    def open(self):
        self.runing = True

    def close(self):
        self.runing = False
        self.GPIO.cleanup(self.led_pin)
        print("GPIO 40 close output")
    def stop(self):
        self.runing= False
        print("GPIO 40 stop output")

