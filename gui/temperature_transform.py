import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("tempconv.ui")[0]
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)
        self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btn_CtoF_clicked)
        self.actionF_to_C.triggered.connect(self.btn_FtoC_clicked)
        self.actionexit.triggered.connect(self.menuExit_selected)
        
    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9 / 5.0 + 32
        self.spinFahr.setValue(int(fahr + 0.5))
    
    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5 / 9.0
        cel_change = '%.2f' % cel
        self.editCel.setText(str(cel_change))
        
    def menuExit_selected(self):
        self.close()
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()