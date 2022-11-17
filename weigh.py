from urllib import response
import serial
import PyQt5
import time
from PyQt5 import QtCore

class weigh(QtCore.QThread):
    rawdata = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.runing = False
        self.ser= serial.Serial('/dev/ttyUSB0',9600,timeout=0.2)


    def run(self):
        while self.runing:
            try:
                response = self.ser.readall()
                a=response
                b=a.decode('UTF-8')
                b.strip()
                
                if(len(b)>0):
                    c=int(b)
                    #print("{0:>5d} ".format(c))
                    self.rawdata.emit(c)
            except IOError:
                print('weigh not connect')
                self.ser.close

    def open(self):
        self.runing = True

    def stop(self):
        self.runing = False

    def close(self):
        self.runing = False
        self.ser.close