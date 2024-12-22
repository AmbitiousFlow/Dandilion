from PySide6.QtWidgets import QApplication , QMainWindow
from .ui.app           import Ui_Dandilion
import sys
import os

__title__   = "Dandilion"
__version__ = "1.0.0"
__author__  = "Kyle Myre"
__license__ = "GNU PUBLIC LICENSE 3.0V"
__icon__    = os.path.join(os.path.dirname(__file__) , "assets" , "icon.ico")
__themes__  = os.path.join(os.path.dirname(__file__) , "themes")
__font__    = "Ariel"

class Application():
    def __init__(self):

        self.app         = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.ui          = Ui_Dandilion()
        self.app.setStyle('Fusion')
        self.ui.setupUi(self.main_window)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())