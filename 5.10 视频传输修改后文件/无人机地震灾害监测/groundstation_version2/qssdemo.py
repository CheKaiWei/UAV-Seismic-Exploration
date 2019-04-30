#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
class MainWindow(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.m_DragPosition=self.pos()
		self.resize(460,520)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setMouseTracking(True)
		self.setStyleSheet("background-color:#2C3E50;")
		qbtn_one=QtGui.QPushButton(u"开始测试",self)
		qbtn_one.setGeometry(0,0,120,80)
		qbtn_one.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}""QPushButton:hover{background-color:#333333;}")
		qbtn_close=QtGui.QPushButton(u"关闭此窗口",self)
		qbtn_close.setGeometry(120,0,120,80)
		qbtn_close.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:20px;}""QPushButton:hover{background-color:#333333;}")
		self.connect(qbtn_close,QtCore.SIGNAL("clicked()"),QtGui.qApp,QtCore.SLOT("quit()"))
	def mousePressEvent(self, event):
		if event.button()==Qt.LeftButton:
			self.m_drag=True
			self.m_DragPosition=event.globalPos()-self.pos()
			event.accept()
	def mouseMoveEvent(self, QMouseEvent):
		if QMouseEvent.buttons() and Qt.LeftButton:
			self.move(QMouseEvent.globalPos()-self.m_DragPosition)
			QMouseEvent.accept()
	def mouseReleaseEvent(self, QMouseEvent):
		self.m_drag=False
if __name__=="__main__":
	mapp=QtGui.QApplication(sys.argv)
	mw=MainWindow()
	mw.show()
	sys.exit(mapp.exec_())