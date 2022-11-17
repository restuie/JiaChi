# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.container = QtWidgets.QWidget(MainWindow)
        self.container.setEnabled(True)
        self.container.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.container.setObjectName("container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartAddTemp = QtWidgets.QPushButton(self.container)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.StartAddTemp.setFont(font)
        self.StartAddTemp.setObjectName("StartAddTemp")
        self.horizontalLayout_2.addWidget(self.StartAddTemp)
        self.StopAddTemp = QtWidgets.QPushButton(self.container)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.StopAddTemp.setFont(font)
        self.StopAddTemp.setObjectName("StopAddTemp")
        self.horizontalLayout_2.addWidget(self.StopAddTemp)
        self.RealTimeTemp = QtWidgets.QLabel(self.container)
        self.RealTimeTemp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RealTimeTemp.sizePolicy().hasHeightForWidth())
        self.RealTimeTemp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.RealTimeTemp.setFont(font)
        self.RealTimeTemp.setObjectName("RealTimeTemp")
        self.horizontalLayout_2.addWidget(self.RealTimeTemp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RealtimeWeight = QtWidgets.QLabel(self.container)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.RealtimeWeight.setFont(font)
        self.RealtimeWeight.setObjectName("RealtimeWeight")
        self.horizontalLayout_5.addWidget(self.RealtimeWeight)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.container)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartAddTemp.setText(_translate("MainWindow", "開始加溫"))
        self.StopAddTemp.setText(_translate("MainWindow", "停止加溫"))
        self.RealTimeTemp.setText(_translate("MainWindow", "即時溫度："))
        self.RealtimeWeight.setText(_translate("MainWindow", "即時重量："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

