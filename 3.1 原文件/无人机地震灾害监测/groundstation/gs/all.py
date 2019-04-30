# -*- coding: utf-8 -*-

"""
Module implementing All_Dialog.
"""
import Ui_check, Ui_groundstation, PyQt4.QtGui, sys
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from PyQt4 import QtCore, QtGui
import cv2
import socket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class All_Dialog(QDialog, Ui_check.Ui_Dialog, Ui_groundstation.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.pushButton, PyQt4.QtCore.SIGNAL("clicked()"), self.on_pushButton_clicked)
        
        global secondUi, firstUi
        secondUi =Ui_groundstation.Ui_Dialog()
        firstUi = Ui_check.Ui_Dialog()

    
    @pyqtSignature("")
    def on_pushButton_clicked(self): #denglu jiemian
        admin = self.lineEdit.text()
        key = self.lineEdit_2.text()
        if admin == 'zhucheng'and key == '15':
            self.close()
            dlg = QDialog()
            secondUi.setupUi(dlg)
            global cap
            cap = cv2.VideoCapture(0)
            global cap1
            cap1 = cv2.VideoCapture(1)

            QtCore.QObject.connect(secondUi.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenCarCamera)
            QtCore.QObject.connect(secondUi.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CloseCarCamera)
            QtCore.QObject.connect(secondUi.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ConnectIP)
            QtCore.QObject.connect(secondUi.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OpenUAVCamera)
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
        #global cap
        #cap = cv2.VideoCapture(0)
        secondUi.timer = QtCore.QTimer()
        secondUi.timer.start(24)
        QtCore.QObject.connect(secondUi.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCamera_label_6)
       
        
    @pyqtSignature("")
    def CloseCarCamera(self):  #duan kai
    
        #cap.release()
        img = 'D:\\procedure\\groundstation\\duankai.jpg'
        QtCore.QObject.disconnect(secondUi.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCamera_label_6)
        secondUi.label_6.setPixmap(QtGui.QPixmap(img))
        
    @pyqtSignature("")
    def OpenUAVCamera(self): # lian jie

        secondUi.timer1 = QtCore.QTimer()
        secondUi.timer1.start(24)
        QtCore.QObject.connect(secondUi.timer1, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateUAV_Camera_label_5)
        
    @pyqtSignature("")
    def UpdateCamera_label_6(self):
       
        ret, frame = cap.read()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB , frame)
        qimg = QtGui.QImage(frame.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        secondUi.label_6.setPixmap(QtGui.QPixmap.fromImage(qimg))
        
        
    @pyqtSignature("")
    def UpdateCamera_label_3(self):
        ret, frame = cap.read()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = bytesPerComponent * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB , frame)
        qimg = QtGui.QImage(frame.data, width, height, bytesPerLine,  QtGui.QImage.Format_RGB888)
        secondUi.label_3.setPixmap(QtGui.QPixmap.fromImage(qimg))
        
        
        
    @pyqtSignature("")
    def ConnectIP(self):
        global HOST, PORT
        HOST = secondUi.lineEdit_29.text()
        #HOST = '192.168.1.108'
        print HOST
        PORT = 23000
        global cli_socket
        cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_socket.connect((HOST,PORT))
        #QtCore.QObject.connect(secondUi.timer, QtCore.SIGNAL(_fromUtf8("timeout()")), self.UpdateCamera)
        #secondUi.label_3.setPixmap(QtGui.QPixmap(img))
        
    @pyqtSignature("")
    def UpdateUAV_Camera_label_5(self):
       
        ret1, frame1 = cap1.read()
        height1, width1, bytesPerComponent1 = frame1.shape
        bytesPerLine1 = bytesPerComponent1 * width1
        cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB , frame1)
        qimg1 = QtGui.QImage(frame1.data, width1, height1, bytesPerLine1,  QtGui.QImage.Format_RGB888)
        secondUi.label_5.setPixmap(QtGui.QPixmap.fromImage(qimg1))
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dialog = All_Dialog()
    dialog.show()
    app.exec_()
