#Author Enver E.
#Date 07.02.24

import sys
from PyQt5.QtWidgets import QApplication
from Window import MainWindow

class Execute:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.execute = self.window.start()


execute = Execute()
