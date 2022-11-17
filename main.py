from asyncore import read
from PyQt5 import QtCore,QtGui,QtWidgets
from UI import Ui_MainWindow
import readTemp
from readTemp import readTemp
from addTemp import addTemp
from weigh import weigh
import Jetson.GPIO as GPIO


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #開始加溫按鈕
        self.StartAddTemp.clicked.connect(self.startAddTemp)
        
        self.StopAddTemp.clicked.connect(self.stopAddTemp)
        # self.StartAddTemp.setEnabled(False)
        # self.StopAddTemp.setEnabled(False)
        self.weigh = weigh()#建立重量偵測物件
        self.readTemp = readTemp()#建立讀取溫度物件
        #self.addTemp = addTemp()#建立加溫物件
        self.temp = 0.0
        self.weight = 0.0
        self.tempflag = False
        self.RealTimeTemp.setText("請掛上透析液袋.......")
        

        if self.readTemp.runing == False:
            self.readTemp.rawdata.connect(self.getRaw)
           
        if self.weigh.runing ==False:
            self.weigh.rawdata.connect(self.getWeight)

        self.buzzer = 23
        self.VT15 = 18
        self.VT70 = 27
        self.VT75 = 22
        self.GPIO = GPIO

        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.buzzer,GPIO.OUT)
        self.GPIO.setup(self.VT15,GPIO.OUT)
        self.GPIO.setup(self.VT70,GPIO.OUT)
        self.GPIO.setup(self.VT75,GPIO.OUT)

        self.GPIO.output(self.buzzer,GPIO.LOW)
        self.GPIO.output(self.VT75,GPIO.LOW)
        self.GPIO.output(self.VT70,GPIO.LOW)
        self.GPIO.output(self.VT15,GPIO.LOW)
        self.weigh.start()
        self.weigh.open()



    #開啟加溫功能函式
    def startAddTemp(self):
        if self.readTemp.runing ==False:
            self.readTemp.start()
            self.readTemp.open()

    #開啟重量測重功能 
    def startweigh(self):
        if self.weigh.runing == False:
            pass

    #暫停加溫功能函式
    def stopAddTemp(self):
        if self.readTemp.runing == True:
            self.readTemp.stop()
        self.GPIO.output(self.VT75,GPIO.LOW)
        self.GPIO.output(self.VT70,GPIO.LOW)
        self.GPIO.output(self.VT15,GPIO.LOW)

    #暫停重量測重功能
    def stopweigh(self):
        if self.weigh.runing == True:
            self.weigh.stop()

    #取得溫度資料
    def getRaw(self,data):
        #發送溫度資料
        self.sendData(data)
    #取得重量資料
    def getWeight(self,data):
        #發送重量資料
        self.sendWeightData(data)

    #發送溫度資料
    def sendData(self,temp):
        #print("{0:>5.2f}C ".format(temp), end='\r')
        print("{0:>5.2f}C ".format(temp))
        self.RealTimeTemp.setText("即時溫度：{0:>5.2f}C ".format(temp))
        self.temp = temp
        if(temp < 25.0):
            self.GPIO.output(self.VT70,GPIO.LOW)
            self.GPIO.output(self.VT15,GPIO.LOW) 
            self.GPIO.output(self.VT75,GPIO.HIGH)
            print("volt=75")
        elif(temp >= 25.0 and temp < 37):
            self.GPIO.output(self.VT75,GPIO.LOW)
            self.GPIO.output(self.VT15,GPIO.LOW) 
            self.GPIO.output(self.VT70,GPIO.HIGH)
            print("volt=70")
        else:
            self.GPIO.output(self.VT75,GPIO.LOW)
            self.GPIO.output(self.VT70,GPIO.LOW) 
            self.GPIO.output(self.VT15,GPIO.HIGH)
            print("volt=15")

        if(temp>37.0 and self.tempflag == False):
            self.tempflag = True
            QtWidgets.QMessageBox.information(None,' 提示','加熱到指定溫度')
            #self.readTemp.stop()
            #QtWidgets.QMessageBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            
    #發送重量資料
    def sendWeightData(self,weight):
        print("{0:>5d} ".format(weight))
        self.weigh = weight
        # if weight > 300 and self.readTemp.runing == False:
        #     self.StartAddTemp.setEnabled(True)
        #     self.StopAddTemp.setEnabled(True)
        #     self.RealTimeTemp.setText("即時溫度：")
        # elif weight < 300:
        #     self.StartAddTemp.setEnabled(False)
        #     self.StopAddTemp.setEnabled(False)
        #     self.RealTimeTemp.setText("請掛上透析液袋.......")
        #     if(self.readTemp.runing == True):
        #         self.readTemp.stop()
        self.RealtimeWeight.setText("即時重量：{0:>5d}".format(weight))

    def closeEvent(self, event):
        if self.readTemp.runing ==False:
            self.readTemp.close()
            self.readTemp.terminate()
        self.GPIO.output(self.VT75,GPIO.LOW)
        self.GPIO.output(self.VT70,GPIO.LOW)
        self.GPIO.output(self.VT15,GPIO.LOW)
        QtWidgets.QApplication.closeAllWindows()

if __name__ =='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())