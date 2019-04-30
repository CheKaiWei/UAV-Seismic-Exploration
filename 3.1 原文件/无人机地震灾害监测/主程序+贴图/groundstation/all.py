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

class All_Dialog(QDialog, Ui_check.Ui_Dialog, Ui_twopage.Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
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
            global cap
            cap = cv2.VideoCapture(0)
            global cap1
            cap1 = cv2.VideoCapture(1)

            #QtCore.QObject.connect(self.secondUi.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenCarCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenCarCamera)
            QtCore.QObject.connect(self.secondUi.pushButton_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseCarCamera)
            QtCore.QObject.connect(self.secondUi.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenIp)
            QtCore.QObject.connect(self.secondUi.pushButton_16, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenUAVCamera)
            
            dlg.exec_()
            
            
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        
    @pyqtSignature("")
    def OpenCarCamera(self): # lian jie
        self.secondUi.timer = QtCore.QTimer()
        self.secondUi.timer.start(24)
        QtCore.QObject.connect(self.secondUi.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCamera_label_14)
       
        
    @pyqtSignature("")
    def CloseCarCamera(self):  #duan kai
        img = 'D:\\procedure\\groundstation\\duankai.jpg'
        QtCore.QObject.disconnect(self.secondUi.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCamera_label_14)
        self.secondUi.label_14.setPixmap(QtGui.QPixmap(img))
        
        
    @pyqtSignature("")
    def OpenUAVCamera(self): # lian jie
        self.secondUi.timer1 = QtCore.QTimer()
        self.secondUi.timer1.start(24)
        QtCore.QObject.connect(self.secondUi.timer1, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateUAV_Camera_label_12)
        
        
    @pyqtSignature("")
    def UpdateCamera_label_14(self):
        ret, frame = cap.read()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB , frame)
        qimg = QtGui.QImage(frame.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_14.setPixmap(QtGui.QPixmap.fromImage(qimg))
        
        
    @pyqtSignature("")
    def UpdateCamera_label_3(self):
        ret, frame = cap.read()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB , frame)
        qimg = QtGui.QImage(frame.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_3.setPixmap(QtGui.QPixmap.fromImage(qimg))
        
    @pyqtSignature("")
    def reconnect(self):
        HOST = self.secondUi.lineEdit.text()
        PORT = 23000
        self.timer_t.cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timer_t.cli_socket.connect((HOST,PORT)) 
        self.timer_t.cli_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,921600)
        return self.timer_t.cli_socket
        
    @pyqtSignature("")
    def OpenIp(self):
        self.timer_t = TimeThread()
        self.timer_t.start_timer()
        
    #@pyqtSignature("")
    def ShowPhoto(self, data1):

        new_data = Image.frombytes('RGB',(640,480),data1)
        im = np.asarray(new_data)
        im = cv2.resize(im, (1291,791 ), interpolation = cv2.INTER_CUBIC)
        height1, width1, bytesPerComponent1 = im.shape
        bytesPerLine1 = bytesPerComponent1 * width1
        cv2.cvtColor(im, cv2.COLOR_BGR2RGB , im)
        qimg1 = QtGui.QImage(im.data, width1, height1, bytesPerLine1,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_2.setPixmap(QtGui.QPixmap.fromImage(qimg1))


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
            self.timer_t.signal_time.emit(data1)
        self.timer_t.cli_socket.sendall('start')
        
    @pyqtSignature("")
    def UpdateUAV_Camera_label_12(self):
        ret1, frame1 = cap1.read()
        height1, width1, bytesPerComponent1 = frame1.shape
        bytesPerLine1 = bytesPerComponent1 * width1
        cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB , frame1)
        qimg1 = QtGui.QImage(frame1.data, width1, height1, bytesPerLine1,  QtGui.QImage.Format_RGB888)
        self.secondUi.label_12.setPixmap(QtGui.QPixmap.fromImage(qimg1))
        
    def tst(self, data2):
        line =data2
        print len(line)
    
class TimeThread(QtCore.QThread):
    signal_time = QtCore.pyqtSignal("QByteArray")
    def __init__(self, parent = None):
        super(TimeThread, self).__init__(parent)
        self.signal_time.connect(dialog.ShowPhoto)
        
    def start_timer(self):
        self.start()
    def run(self):
        self.cli_socket = dialog.reconnect()
        self.cli_socket.sendall('start')
        while(1):
            dialog.ConnectIP()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = All_Dialog()
    dialog.show()
    app.exec_()
