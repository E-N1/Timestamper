#Author Enver E.
#Date 07.02.24

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.width = 500
        self.height = 200

        # Title, Size
        self.setWindowTitle("Timestamper")
        self.setFixedSize(self.width,self.height)

        self.setWindowBottomRightCorner()
        self.setLabelsInWindowPosition("To begin, press 'Start' to record a working loop.",12,100,50)
        self.setButtonInWindowPosition("Start",self.startEachRecordingLoop,100,150)
        self.setButtonInWindowPosition("Beenden",self.closeWindow,300,150)



    # label: create a text, x,y(begins from top left corner): Position in window
    def setLabelsInWindowPosition(self,label,labelsize,x,y):
        
        self.label = QLabel(str(label),self)
        self.label.move(x,y)

        # Font and Size
        self.font = QFont("Arial", int(labelsize))
        self.label.setFont(self.font)

        # fills the widget, with the full text
        self.label.adjustSize()


    # buttonlabel: create the buttontext, x,y(begins from top left corner): Position in window
    def setButtonInWindowPosition(self,buttonLabel,function,x,y):
        self.button = QPushButton(str(buttonLabel),self)
        self.button.adjustSize()
        self.button.move(x,y)
        self.button.clicked.connect(function)


    def setWindowBottomRightCorner(self):
        screen = QDesktopWidget().screenGeometry()
        taskbar_height = QApplication.desktop().availableGeometry().height() - screen.height()

        window = self.frameGeometry()

        # get X and Y, and put's the window in bottom right corner (y from Windows 11)
        x = screen.width() - window.width()
        y = screen.height() - window.height() + taskbar_height - 30 
        self.move(x, y)


    def closeWindow(self):
        return self.close()


    def startEachRecordingLoop(self):
        self.setFixedSize(self.width,self.height+250)
        self.setWindowBottomRightCorner()


    def start(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()
        self.app.exec()