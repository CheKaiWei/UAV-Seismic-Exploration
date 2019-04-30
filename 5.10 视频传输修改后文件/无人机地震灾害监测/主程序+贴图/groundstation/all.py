# -*- coding: utf-8 -*-

"""
Module implementing All_Dialog.
"""
import Ui_check, Ui_twopage, PyQt4.QtGui, sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from PyQt4 import QtCore, QtGui
import cv2, time
import socket
import numpy as np
from PIL import Image


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
#继承：导入的QDialog，Ui_check里的Ui_Dialog类和Ui_twopage里的Ui_Dialog类
class All_Dialog(QDialog, Ui_check.Ui_Dialog, Ui_twopage.Ui_Dialog):
    """
    Class documentation goes here.
    """


    def __init__(self, parent=None):#带参数的构造函数，初始化
        QDialog.__init__(self, parent)#调用未关联的超类构造函数
        self.setupUi(self)
        self.connect(self.pushButton, PyQt4.QtCore.SIGNAL("clicked()"), self.on_pushButton_clicked)
        
        #global secondUi, firstUi
        self.secondUi =Ui_twopage.Ui_Dialog()
        self.firstUi = Ui_check.Ui_Dialog()
        
       # self.timer_t.signal_time.connect(self.ConnectIP)

    @pyqtSignature("")
    def on_pushButton_clicked(self): #denglu jiemian
        admin = self.lineEdit.text()
        key = self.lineEdit_2.text()
        if admin == '1'and key == '1':
            self.close()
            dlg = QDialog()
            self.secondUi.setupUi(dlg)
            global cap  #电脑自带摄像头
            cap = cv2.VideoCapture(0)
            global cap1 #外接摄像头
            cap1 = cv2.VideoCapture(1)
            global cap2 #外接摄像头
            cap2 = cv2.VideoCapture(2)

            QtCore.QObject.connect(self.secondUi.pushButton_16, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenUAVCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_15, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseUAVCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenCarCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseCarCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_13, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenSingleCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_14, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseSingleCamera)
            #QtCore.QObject.connect(self.secondUi.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenServerCamera)
            #QtCore.QObject.connect(self.secondUi.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseServerCamera)
            #QtCore.QObject.connect(self.secondUi.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenClientCamera)
            #QtCore.QObject.connect(self.secondUi.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseClientCamera)

            QtCore.QObject.connect(self.secondUi.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenIp)

            dlg.exec_()
            
            
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):#注册
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError

    @pyqtSignature("")
    def OpenUAVCamera(self):
        self.secondUi.timer_UAV = QtCore.QTimer()
        self.secondUi.timer_UAV.start(24)
        QtCore.QObject.connect(self.secondUi.timer_UAV, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateUAVCamera_label_12)
    @pyqtSignature("")
    def CloseUAVCamera(self):  #duan kai
        img = 'D:\\procedure\\groundstation\\duankai.jpg'
        QtCore.QObject.disconnect(self.secondUi.timer_UAV, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateUAVCamera_label_12)
        self.secondUi.label_12.setPixmap(QtGui.QPixmap(img))

    @pyqtSignature("")
    def UpdateUAVCamera_label_12(self):
        ret_UAV, frame_UAV = cap2.read()
        height_UAV, width_UAV, bytesPerComponent_UAV = frame_UAV.shape
        bytesPerLine_UAV = bytesPerComponent_UAV * width_UAV
        cv2.cvtColor(frame_UAV, cv2.COLOR_BGR2RGB , frame_UAV)
        qimg_UAV = QtGui.QImage(frame_UAV.data, width_UAV, height_UAV, bytesPerLine_UAV,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_12.setPixmap(QtGui.QPixmap.fromImage(qimg_UAV))

    @pyqtSignature("")
    def OpenCarCamera(self):
        self.secondUi.timer_car = QtCore.QTimer()
        self.secondUi.timer_car.start(24)
        QtCore.QObject.connect(self.secondUi.timer_car, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCarCamera_label_14)
    @pyqtSignature("")
    def CloseCarCamera(self):
        img = 'D:\\procedure\\groundstation\\duankai.jpg'
        QtCore.QObject.disconnect(self.secondUi.timer_car, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCarCamera_label_14)
        self.secondUi.label_14.setPixmap(QtGui.QPixmap(img))
    @pyqtSignature("")
    def UpdateCarCamera_label_14(self):#CarCamera一帧的更新
        ret_car, frame_car = cap.read()
        height_car, width_car, bytesPerComponent_car = frame_car.shape
        bytesPerLine_car = bytesPerComponent_car * width_car
        cv2.cvtColor(frame_car, cv2.COLOR_BGR2RGB , frame_car)
        qimg_car = QtGui.QImage(frame_car.data, width_car, height_car, bytesPerLine_car,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_14.setPixmap(QtGui.QPixmap.fromImage(qimg_car))

    @pyqtSignature("")
    def OpenSingleCamera(self):
        self.secondUi.timer_single = QtCore.QTimer()
        self.secondUi.timer_single.start(24)
        QtCore.QObject.connect(self.secondUi.timer_single, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateSingleCamera_label_18)
    @pyqtSignature("")
    def CloseSingleCamera(self):  #duan kai
        img = 'D:\\procedure\\groundstation\\duankai.jpg'
        QtCore.QObject.disconnect(self.secondUi.timer_single, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateSingleCamera_label_18)
        self.secondUi.label_18.setPixmap(QtGui.QPixmap(img))
    @pyqtSignature("")
    def UpdateSingleCamera_label_18(self):
        ret_single, frame_single = cap1.read()
        height_single, width_single, bytesPerComponent_single = frame_single.shape
        bytesPerLine_single = bytesPerComponent_single * width_single
        cv2.cvtColor(frame_single, cv2.COLOR_BGR2RGB , frame_single)
        qimg_single = QtGui.QImage(frame_single.data, width_single, height_single, bytesPerLine_single,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_18.setPixmap(QtGui.QPixmap.fromImage(qimg_single))

    @pyqtSignature("")
    def OpenServerCamera(self):
         self.secondUi.timer_server = QtCore.QTimer()
         self.secondUi.timer_server.start(24)
         QtCore.QObject.connect(self.secondUi.timer_server, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateServerCamera_label_2)

    @pyqtSignature("")
    def CloseServerCamera(self):  #duan kai
         img = 'D:\\procedure\\groundstation\\duankai.jpg'
         QtCore.QObject.disconnect(self.secondUi.timer_server, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateServerCamera_label_2)
         self.secondUi.label_2.setPixmap(QtGui.QPixmap(img))
    @pyqtSignature("")
    def UpdateServerCamera_label_2(self):
         ret_server, frame_server = cap.read()
         height_server, width_server, bytesPerComponent_server = frame_server.shape
         bytesPerLine_server = bytesPerComponent_server * width_server
         cv2.cvtColor(frame_server, cv2.COLOR_BGR2RGB , frame_server)
         qimg_server = QtGui.QImage(frame_server.data, width_server, height_server, bytesPerLine_server,  QtGui.QImage.Format_RGB888)
         self.secondUi.label_2.setPixmap(QtGui.QPixmap.fromImage(qimg_server))

    # @pyqtSignature("")
    # def OpenClientCamera(self):
    #     self.secondUi.timer_client = QtCore.QTimer()
    #     self.secondUi.timer_client.start(24)
    #     QtCore.QObject.connect(self.secondUi.timer_client, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateClientCamera_label_3)
    # @pyqtSignature("")
    # def CloseClientCamera(self):  #duan kai
    #     img = 'D:\\procedure\\groundstation\\duankai.jpg'
    #     QtCore.QObject.disconnect(self.secondUi.timer_client, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateClientCamera_label_3)
    #     self.secondUi.label_3.setPixmap(QtGui.QPixmap(img))
    # @pyqtSignature("")
    # def UpdateClientCamera_label_3(self):#第1页client视频
    #     ret_client, frame_client = cap.read()
    #     height_client, width_client, bytesPerComponent_client = frame_client.shape
    #     bytesPerLine_client = bytesPerComponent_client * width_client
    #     cv2.cvtColor(frame_client, cv2.COLOR_BGR2RGB , frame_client)
    #     qimg_client = QtGui.QImage(frame_client.data, width_client, height_client, bytesPerLine_client,  QtGui.QImage.Format_RGB888)
    #     self.secondUi.label_3.setPixmap(QtGui.QPixmap.fromImage(qimg_client))


    @pyqtSignature("")
    def OpenIp(self):
        self.timer_t = TimeThread()
        self.timer_t.start_timer()

    @pyqtSignature("")
    def ConnectIP(self):
        try:
            data1 = self.timer_t.cli_socket.recv(921600)
        except:
            print 'test'
        if len(data1) != 921600:
            self.timer_t. cli_socket.sendall('notok')
            self.timer_t.cli_socket.close()
            time.sleep(0.25)
            self.timer_t.cli_socket = self.reconnect()
            print 'reconnecting'
            #time.sleep(0.04)
        else:
            ########################
            self.timer_t.signal_time.emit(data1)
        self.timer_t.cli_socket.sendall('start')

    @pyqtSignature("")
    def reconnect(self):
        #HOST = self.secondUi.lineEdit.text()
        HOST='172.31.105.159'
        PORT = 33000
        self.timer_t.cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timer_t.cli_socket.connect((HOST,PORT))
        self.timer_t.cli_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,921600)
        return self.timer_t.cli_socket

    @pyqtSignature("")
    def ShowPhoto(self, data1):
        new_data = Image.frombytes('RGB',(640,480),data1)
        im = np.asarray(new_data)
        im = cv2.resize(im, (1291,791 ), interpolation = cv2.INTER_CUBIC)
        height1, width1, bytesPerComponent1 = im.shape
        bytesPerLine1 = bytesPerComponent1 * width1
        cv2.cvtColor(im, cv2.COLOR_BGR2RGB , im)
        qimg1 = QtGui.QImage(im.data, width1, height1, bytesPerLine1,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_2.setPixmap(QtGui.QPixmap.fromImage(qimg1))

class TimeThread(QtCore.QThread):
    signal_time = QtCore.pyqtSignal("QByteArray")
    def __init__(self, parent = None):
        super(TimeThread, self).__init__(parent)
        ##########################
        self.signal_time.connect(dialog.ShowPhoto)
    def start_timer(self):
        self.start()
    def run(self):
        self.cli_socket = dialog.reconnect()
        self.cli_socket.sendall('start')
        while(1):
            dialog.ConnectIP()

    # def tst(self, data2):
    #     line =data2
    #     print len(line)
if __name__ == "__main__": #
    app = QtGui.QApplication(sys.argv)
    dialog = All_Dialog()
    dialog.show()
    app.exec_()
