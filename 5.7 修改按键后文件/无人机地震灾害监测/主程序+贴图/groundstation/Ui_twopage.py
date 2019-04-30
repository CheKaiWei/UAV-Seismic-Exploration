# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\project\���˻������ֺ����\������+��ͼ\groundstation\twopage.ui'
#
# Created: Thu Apr 19 15:09:06 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1350, 951)
        Dialog.setStyleSheet(_fromUtf8("QDialog{border-image:url(D:/procedure/groundstation/checkin/denglu2/bj-1.png)}"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1331, 721))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8("#tab_2{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/tab.png);\n"
"}\n"
"#tab{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/tab.png);\n"
"}\n"
"#tab_3{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/tab.png);\n"
"}\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1311, 681))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(60, 640, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"\n"
"\n"
"}"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 650, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_SO = QtGui.QPushButton(self.groupBox)
        self.pushButton_SO.setGeometry(QtCore.QRect(260, 630, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_SO.setFont(font)
        self.pushButton_SO.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalianjie.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalianjie.png) } "))
        self.pushButton_SO.setText(_fromUtf8(""))
        self.pushButton_SO.setObjectName(_fromUtf8("pushButton_SO"))
        self.pushButton_SC = QtGui.QPushButton(self.groupBox)
        self.pushButton_SC.setGeometry(QtCore.QRect(380, 630, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_SC.setFont(font)
        self.pushButton_SC.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankai.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankai.png) } "))
        self.pushButton_SC.setText(_fromUtf8(""))
        self.pushButton_SC.setObjectName(_fromUtf8("pushButton_SC"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 630, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufakaishiluxiang.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufakaishiluxiang.png) } "))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 630, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankailuxiang.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankailuxiang.png) } "))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 861, 581))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(920, 20, 381, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(1210, 630, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufatuichuchengxu.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufatuichuchengxu.png) } "))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_CO = QtGui.QPushButton(self.groupBox)
        self.pushButton_CO.setGeometry(QtCore.QRect(920, 340, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_CO.setFont(font)
        self.pushButton_CO.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalianjie.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalianjie.png) } "))
        self.pushButton_CO.setText(_fromUtf8(""))
        self.pushButton_CO.setObjectName(_fromUtf8("pushButton_CO"))
        self.pushButton_CC = QtGui.QPushButton(self.groupBox)
        self.pushButton_CC.setGeometry(QtCore.QRect(1040, 340, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_CC.setFont(font)
        self.pushButton_CC.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankai.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankai.png) } "))
        self.pushButton_CC.setText(_fromUtf8(""))
        self.pushButton_CC.setObjectName(_fromUtf8("pushButton_CC"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 661, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox{color:white}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 641, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("color:white"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(200, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankai.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankai.png) } "))
        self.pushButton_15.setText(_fromUtf8(""))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_16.setGeometry(QtCore.QRect(70, 290, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalianjie.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalianjie.png) } "))
        self.pushButton_16.setText(_fromUtf8(""))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(680, 0, 641, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(20, 30, 281, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(330, 30, 291, 181))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.pushButton_32 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_32.setGeometry(QtCore.QRect(500, 210, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufafasongduanxin.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufafasongduanxin.png) } "))
        self.pushButton_32.setText(_fromUtf8(""))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(1000, 440, 321, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufakaiqipaowu.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufakaiqipaowu.png) } "))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaguanbipaowu.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaguanbipaowu.png) } "))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.lineEdit_33 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_33.setGeometry(QtCore.QRect(10, 90, 301, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(11)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,54,61);\n"
"    selection-background-color: white;\n"
"color:rgb(124,125,128);\n"
"\n"
"\n"
"}"))
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 350, 661, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 301, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("color:white"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(340, 30, 301, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("color:white"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton_11 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 260, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalianjie.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalianjie.png) } "))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 260, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankai.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankai.png) } "))
        self.pushButton_12.setText(_fromUtf8(""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_13 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_13.setGeometry(QtCore.QRect(390, 260, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalianjie.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalianjie.png) } "))
        self.pushButton_13.setText(_fromUtf8(""))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_14 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_14.setGeometry(QtCore.QRect(520, 260, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaduankai.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaduankai.png) } "))
        self.pushButton_14.setText(_fromUtf8(""))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(680, 250, 641, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pushButton_17 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_17.setGeometry(QtCore.QRect(120, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufashang.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufashang.png) } "))
        self.pushButton_17.setText(_fromUtf8(""))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_18.setGeometry(QtCore.QRect(120, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaxia.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaxia.png) } "))
        self.pushButton_18.setText(_fromUtf8(""))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_20 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_20.setGeometry(QtCore.QRect(180, 48, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufayouxuan.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufayouxuan.png) } "))
        self.pushButton_20.setText(_fromUtf8(""))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.pushButton_21 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_21.setGeometry(QtCore.QRect(480, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufayou.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufayou.png) } "))
        self.pushButton_21.setText(_fromUtf8(""))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_22 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_22.setGeometry(QtCore.QRect(420, 90, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufahou.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufahou.png) } "))
        self.pushButton_22.setText(_fromUtf8(""))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.pushButton_23 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_23.setGeometry(QtCore.QRect(420, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setAutoFillBackground(False)
        self.pushButton_23.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufaqian.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufaqian.png) } "))
        self.pushButton_23.setText(_fromUtf8(""))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.pushButton_24 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_24.setGeometry(QtCore.QRect(360, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufazuo.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufazuo.png) } "))
        self.pushButton_24.setText(_fromUtf8(""))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.pushButton_25 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_25.setGeometry(QtCore.QRect(250, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufajiesuo.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufajiesuo.png) } "))
        self.pushButton_25.setText(_fromUtf8(""))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.pushButton_26 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_26.setGeometry(QtCore.QRect(340, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufayijianqifei.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufayijianqifei.png) } "))
        self.pushButton_26.setText(_fromUtf8(""))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.pushButton_27 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_27.setGeometry(QtCore.QRect(440, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufayijianjiangluo.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufayijianjiangluo.png) } "))
        self.pushButton_27.setText(_fromUtf8(""))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.pushButton_28 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_28.setGeometry(QtCore.QRect(530, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufasuoji.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufasuoji.png) } "))
        self.pushButton_28.setText(_fromUtf8(""))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.pushButton_29 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_29.setGeometry(QtCore.QRect(60, 48, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufazuoxuan.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufazuoxuan.png) } "))
        self.pushButton_29.setText(_fromUtf8(""))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(680, 440, 311, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.pushButton_30 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_30.setGeometry(QtCore.QRect(24, 12, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufafasong.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufafasong.png) } "))
        self.pushButton_30.setText(_fromUtf8(""))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.pushButton_31 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_31.setGeometry(QtCore.QRect(20, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(12)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufajieshou.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufajieshou.png) } "))
        self.pushButton_31.setText(_fromUtf8(""))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.label_15 = QtGui.QLabel(self.groupBox_10)
        self.label_15.setGeometry(QtCore.QRect(140, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("color:white"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalSlider_2 = QtGui.QSlider(self.groupBox_10)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(230, 30, 61, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.lineEdit_32 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_32.setGeometry(QtCore.QRect(10, 90, 291, 111))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_32.sizePolicy().hasHeightForWidth())
        self.lineEdit_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(11)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(52,54,61);\n"
"    selection-background-color: white;\n"
"color:rgb(124,125,128);\n"
"\n"
"\n"
"\n"
"}"))
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 20, 1301, 331))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet(_fromUtf8("QGroupBox{color:white}"))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_21 = QtGui.QLabel(self.groupBox_8)
        self.label_21.setGeometry(QtCore.QRect(10, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(_fromUtf8("color:white"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_17.setGeometry(QtCore.QRect(120, 115, 41, 20))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_22 = QtGui.QLabel(self.groupBox_8)
        self.label_22.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(_fromUtf8("color:white"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_18.setGeometry(QtCore.QRect(120, 195, 41, 20))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.label_23 = QtGui.QLabel(self.groupBox_8)
        self.label_23.setGeometry(QtCore.QRect(630, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(_fromUtf8("color:white"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_19 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_19.setGeometry(QtCore.QRect(740, 35, 41, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_24 = QtGui.QLabel(self.groupBox_8)
        self.label_24.setGeometry(QtCore.QRect(10, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8("color:white"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lineEdit_20 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 275, 41, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.label_25 = QtGui.QLabel(self.groupBox_8)
        self.label_25.setGeometry(QtCore.QRect(290, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("color:white"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_21 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_21.setGeometry(QtCore.QRect(490, 275, 41, 20))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.label_26 = QtGui.QLabel(self.groupBox_8)
        self.label_26.setGeometry(QtCore.QRect(630, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(_fromUtf8("color:white"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.lineEdit_22 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_22.setGeometry(QtCore.QRect(740, 195, 41, 20))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.label_27 = QtGui.QLabel(self.groupBox_8)
        self.label_27.setGeometry(QtCore.QRect(290, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(_fromUtf8("color:white"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_23 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_23.setGeometry(QtCore.QRect(490, 35, 41, 20))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.label_28 = QtGui.QLabel(self.groupBox_8)
        self.label_28.setGeometry(QtCore.QRect(910, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(_fromUtf8("color:white"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.lineEdit_24 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_24.setGeometry(QtCore.QRect(1110, 115, 61, 20))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.label_29 = QtGui.QLabel(self.groupBox_8)
        self.label_29.setGeometry(QtCore.QRect(290, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(_fromUtf8("color:white"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.lineEdit_25 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_25.setGeometry(QtCore.QRect(490, 195, 41, 20))
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.label_30 = QtGui.QLabel(self.groupBox_8)
        self.label_30.setGeometry(QtCore.QRect(290, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(_fromUtf8("color:white"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.lineEdit_26 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_26.setGeometry(QtCore.QRect(490, 115, 41, 20))
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.label_31 = QtGui.QLabel(self.groupBox_8)
        self.label_31.setGeometry(QtCore.QRect(910, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(_fromUtf8("color:white"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit_27 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_27.setGeometry(QtCore.QRect(1110, 35, 41, 20))
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.label_32 = QtGui.QLabel(self.groupBox_8)
        self.label_32.setGeometry(QtCore.QRect(630, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(_fromUtf8("color:white"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.lineEdit_28 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_28.setGeometry(QtCore.QRect(740, 115, 41, 20))
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.label_33 = QtGui.QLabel(self.groupBox_8)
        self.label_33.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(_fromUtf8("color:white"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.lineEdit_29 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_29.setGeometry(QtCore.QRect(120, 35, 41, 20))
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.label_34 = QtGui.QLabel(self.groupBox_8)
        self.label_34.setGeometry(QtCore.QRect(910, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(_fromUtf8("color:white"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_30 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_30.setGeometry(QtCore.QRect(1110, 195, 41, 20))
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 360, 1301, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_35 = QtGui.QLabel(self.groupBox_9)
        self.label_35.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(_fromUtf8("color:white"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.groupBox_9)
        self.label_36.setGeometry(QtCore.QRect(10, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(_fromUtf8("color:white"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_14.setGeometry(QtCore.QRect(100, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_31 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_31.setGeometry(QtCore.QRect(100, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.label_40 = QtGui.QLabel(self.groupBox_9)
        self.label_40.setGeometry(QtCore.QRect(290, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(_fromUtf8("color:white"))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_42 = QtGui.QLabel(self.groupBox_9)
        self.label_42.setGeometry(QtCore.QRect(290, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(_fromUtf8("color:white"))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.groupBox_9)
        self.label_43.setGeometry(QtCore.QRect(630, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(_fromUtf8("color:white"))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_44 = QtGui.QLabel(self.groupBox_9)
        self.label_44.setGeometry(QtCore.QRect(630, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(_fromUtf8("color:white"))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_45 = QtGui.QLabel(self.groupBox_9)
        self.label_45.setGeometry(QtCore.QRect(920, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(_fromUtf8("color:white"))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.lineEdit_35 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_35.setGeometry(QtCore.QRect(350, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.lineEdit_37 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_37.setGeometry(QtCore.QRect(350, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.lineEdit_38 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_38.setGeometry(QtCore.QRect(720, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.lineEdit_39 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_39.setGeometry(QtCore.QRect(720, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.lineEdit_40 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_40.setGeometry(QtCore.QRect(1020, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.pushButton_19 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_19.setGeometry(QtCore.QRect(1200, 190, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(14)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"border-image:url(D:/procedure/groundstation/checkin/denglu2/weichufalishijilu.png);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton:hover { border-image:url(D:/procedure/groundstation/checkin/denglu2/chufalishijilu.png) } "))
        self.pushButton_19.setText(_fromUtf8(""))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.label_46 = QtGui.QLabel(self.groupBox_9)
        self.label_46.setGeometry(QtCore.QRect(920, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(_fromUtf8("color:white"))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.lineEdit_41 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_41.setGeometry(QtCore.QRect(1030, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setText(_fromUtf8(""))
        self.lineEdit_41.setObjectName(_fromUtf8("lineEdit_41"))
        self.label_47 = QtGui.QLabel(self.groupBox_9)
        self.label_47.setGeometry(QtCore.QRect(10, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(_fromUtf8("color:white"))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.lineEdit_42 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_42.setGeometry(QtCore.QRect(100, 110, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setText(_fromUtf8(""))
        self.lineEdit_42.setObjectName(_fromUtf8("lineEdit_42"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(460, 530, 451, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.label_48 = QtGui.QLabel(self.groupBox_11)
        self.label_48.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(_fromUtf8("color:white"))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.lineEdit_43 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_43.setGeometry(QtCore.QRect(120, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_43.setObjectName(_fromUtf8("lineEdit_43"))
        self.label_49 = QtGui.QLabel(self.groupBox_11)
        self.label_49.setGeometry(QtCore.QRect(10, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(_fromUtf8("color:white"))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_50 = QtGui.QLabel(self.groupBox_11)
        self.label_50.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(_fromUtf8("color:white"))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.lineEdit_44 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_44.setGeometry(QtCore.QRect(120, 60, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.lineEdit_45 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_45.setGeometry(QtCore.QRect(120, 90, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_45.setObjectName(_fromUtf8("lineEdit_45"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(940, 530, 371, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.lineEdit_36 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_36.setGeometry(QtCore.QRect(120, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.label_41 = QtGui.QLabel(self.groupBox_12)
        self.label_41.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(_fromUtf8("color:white"))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.groupBox_13 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 530, 421, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(14)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setStyleSheet(_fromUtf8("QGroupBox{color:white;}"))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.label_51 = QtGui.QLabel(self.groupBox_13)
        self.label_51.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(_fromUtf8("color:white"))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.lineEdit_46 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_46.setGeometry(QtCore.QRect(80, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setStyleSheet(_fromUtf8("color:white"))
        self.lineEdit_46.setObjectName(_fromUtf8("lineEdit_46"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "山体地质灾害智能勘测系统主控界面", None))
        self.groupBox.setTitle(_translate("Dialog", "会议内容", None))
        self.lineEdit.setText(_translate("Dialog", "192.168.1.116", None))
        self.label.setText(_translate("Dialog", "IP:", None))
        self.label_2.setText(_translate("Dialog", "server", None))
        self.label_3.setText(_translate("Dialog", "client", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1", None))
        self.groupBox_2.setTitle(_translate("Dialog", "现场灾情显示", None))
        self.label_12.setText(_translate("Dialog", "无人机信息", None))
        self.groupBox_5.setTitle(_translate("Dialog", "救援指挥辅助决策与建议", None))
        self.lineEdit_13.setText(_translate("Dialog", "识别情况", None))
        self.lineEdit_15.setText(_translate("Dialog", "决策与建议", None))
        self.groupBox_6.setTitle(_translate("Dialog", "救援机构控制", None))
        self.lineEdit_33.setText(_translate("Dialog", "开启抛物成功...", None))
        self.groupBox_3.setTitle(_translate("Dialog", "车顶及单兵摄像头", None))
        self.label_14.setText(_translate("Dialog", "车顶360度环视信息", None))
        self.label_18.setText(_translate("Dialog", "单兵检测信息", None))
        self.groupBox_7.setTitle(_translate("Dialog", "无人机控制", None))
        self.groupBox_10.setTitle(_translate("Dialog", "空地对话控制", None))
        self.label_15.setText(_translate("Dialog", "音量大小db：", None))
        self.lineEdit_32.setText(_translate("Dialog", "发送成功...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))
        self.groupBox_8.setTitle(_translate("Dialog", "土壤参数设置", None))
        self.label_21.setText(_translate("Dialog", "土壤摩擦角::", None))
        self.lineEdit_17.setText(_translate("Dialog", "22", None))
        self.label_22.setText(_translate("Dialog", "土壤单位容重:", None))
        self.lineEdit_18.setText(_translate("Dialog", "12.5", None))
        self.label_23.setText(_translate("Dialog", "土壤类型参数:", None))
        self.lineEdit_19.setText(_translate("Dialog", "100", None))
        self.label_24.setText(_translate("Dialog", "土壤饱和度:", None))
        self.lineEdit_20.setText(_translate("Dialog", "0.39", None))
        self.label_25.setText(_translate("Dialog", "土壤黏聚力最大值参数∂:", None))
        self.lineEdit_21.setText(_translate("Dialog", "3.4", None))
        self.label_26.setText(_translate("Dialog", "降雨量:", None))
        self.lineEdit_22.setText(_translate("Dialog", "283", None))
        self.label_27.setText(_translate("Dialog", "土壤孔隙度:", None))
        self.lineEdit_23.setText(_translate("Dialog", "0.4", None))
        self.label_28.setText(_translate("Dialog", "土壤饱和层水力传导度:", None))
        self.lineEdit_24.setText(_translate("Dialog", "0.000018", None))
        self.label_29.setText(_translate("Dialog", "土壤毛管力:", None))
        self.lineEdit_25.setText(_translate("Dialog", "500", None))
        self.label_30.setText(_translate("Dialog", "土壤初始水含量:", None))
        self.lineEdit_26.setText(_translate("Dialog", "0.4", None))
        self.label_31.setText(_translate("Dialog", "土壤饱和水含量:", None))
        self.lineEdit_27.setText(_translate("Dialog", "0.9", None))
        self.label_32.setText(_translate("Dialog", "坡角:", None))
        self.lineEdit_28.setText(_translate("Dialog", "26", None))
        self.label_33.setText(_translate("Dialog", "土壤黏聚力:", None))
        self.lineEdit_29.setText(_translate("Dialog", "10", None))
        self.label_34.setText(_translate("Dialog", "土壤黏聚力最大值参数λ:", None))
        self.lineEdit_30.setText(_translate("Dialog", "0.4", None))
        self.groupBox_9.setTitle(_translate("Dialog", "山体土壤检测状态", None))
        self.label_35.setText(_translate("Dialog", "识别情况：", None))
        self.label_36.setText(_translate("Dialog", "水分含量：", None))
        self.lineEdit_14.setText(_translate("Dialog", "是", None))
        self.lineEdit_31.setText(_translate("Dialog", "60%", None))
        self.label_40.setText(_translate("Dialog", "高度：", None))
        self.label_42.setText(_translate("Dialog", "电量：", None))
        self.label_43.setText(_translate("Dialog", "竖直速度：", None))
        self.label_44.setText(_translate("Dialog", "锁定状态：", None))
        self.label_45.setText(_translate("Dialog", "水平速度：", None))
        self.lineEdit_35.setText(_translate("Dialog", "500", None))
        self.lineEdit_37.setText(_translate("Dialog", "50%", None))
        self.lineEdit_38.setText(_translate("Dialog", "1", None))
        self.lineEdit_39.setText(_translate("Dialog", "否", None))
        self.lineEdit_40.setText(_translate("Dialog", "2", None))
        self.label_46.setText(_translate("Dialog", "现土壤黏聚力：", None))
        self.label_47.setText(_translate("Dialog", "现入渗深度：", None))
        self.groupBox_11.setTitle(_translate("Dialog", "卫星参数显示", None))
        self.label_48.setText(_translate("Dialog", "GPS卫星数目：", None))
        self.lineEdit_43.setText(_translate("Dialog", "7", None))
        self.label_49.setText(_translate("Dialog", "纬度：", None))
        self.label_50.setText(_translate("Dialog", "经度：", None))
        self.lineEdit_44.setText(_translate("Dialog", "119", None))
        self.lineEdit_45.setText(_translate("Dialog", "25", None))
        self.groupBox_12.setTitle(_translate("Dialog", "单兵参数显示", None))
        self.lineEdit_36.setText(_translate("Dialog", "2000", None))
        self.label_41.setText(_translate("Dialog", "距离：", None))
        self.groupBox_13.setTitle(_translate("Dialog", "车辆参数显示", None))
        self.label_51.setText(_translate("Dialog", "车速：", None))
        self.lineEdit_46.setText(_translate("Dialog", "7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Tab 3", None))

