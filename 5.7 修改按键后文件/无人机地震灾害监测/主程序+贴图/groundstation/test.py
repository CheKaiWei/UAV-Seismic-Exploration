
from PyQt4 import QtCore, QtGui
class AThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(int)

    def run(self):
        print('n[0]')
        self.trigger.emit(0)
        time.sleep(10)
        print('n[1]')
        self.trigger.emit(1)
