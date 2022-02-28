from plistlib import UID
import sys
import random
import time
from PyQt5.QtWidgets import QDialog, QApplication
from uSingle import *
from PyQt5 import QtCore

class Single(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.labelAnswer.setVisible(False)
        self.ui.buttonNo .clicked.connect(self.buttonNo)
        self.ui.buttonYes.clicked.connect(self.buttonYes)
        self.show()
    
    def buttonNo(self):
        x = random.randrange(200, 340, 1)
        y = random.randrange(170, 250, 1)
        self.ui.buttonNo.setGeometry(QtCore.QRect(x, y,75,31))
    
    def buttonYes(self):
        self.ui.labelQuestion.setVisible(False)
        self.ui.labelAnswer.setVisible(True)
       
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Single()
    w.show()
    sys.exit(app.exec_())