import time
from smbus2 import SMBus
from mlx90614 import MLX90614
from PyQt5 import QtCore
import numpy as np

class readTemp(QtCore.QThread):
    rawdata = QtCore.pyqtSignal(float)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.runing = False
        self.thermometer_address=0x5a
        self.bus = SMBus(1)
        self.sensor = MLX90614(self.bus,address=self.thermometer_address)

    def run(self):
        while self.runing:
            try:
                object_temp = self.sensor.get_obj_temp()
                #print("{0:>5.2f}C ".format(object_temp), end='\r')
                self.rawdata.emit(object_temp)
                time.sleep(1)
            except IOError:
                print('Mlx90614 not connect')
            # finally:
            #     print('Mlx90614 not connect')
            #     self.bus.close()
            #     self.runing = False
    def open(self):
        self.runing = True

    def close(self):
        self.runing = False
        self.bus.close()
        print("Mlx90614 close")
    def stop(self):
        self.runing=False
        print("Mlx90614 stop")

