from .errors.URLEmptyException import URLEmptyException
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from .widgets.app import Ui_Dandilion
from .widgets.about import Ui_About
from .services.DownloadService import DownloadService
from pathlib import Path
from threading import Thread
from rich.traceback import install
import sys
import os

install()

__title__ = "Dandilion"
__version__ = "1.0.0"
__author__ = "Kyle Myre"
__license__ = "GNU PUBLIC LICENSE 3.0V"
__icon__ = os.path.join(os.path.dirname(__file__), "assets", "icon.ico")
__themes__ = os.path.join(os.path.dirname(__file__), "themes")
__font__ = "Ariel"


class Application:
    # Injection :
    _main_widget = Ui_Dandilion()
    _about = Ui_About()

    def __init__(self):

        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.app.setStyle("Fusion")
        self._main_widget.setupUi(self.main_window)

        self._download_service = DownloadService(
            self._main_widget.DownloadProgressBar, self._main_widget.OutputAreaBox
        )

        self.inject()

    def show_about(self):
        self.about = QWidget()
        self._about.setupUi(self.about)
        self.about.show()

    def download(self):
        try:
            if self._main_widget.UrlEntry.text() == "":
                raise URLEmptyException()

            self._download_service.download(
                self._main_widget.UrlEntry.text(),
                str(Path.home() / "Downloads"),
                self._main_widget.TypeComboBox.currentText(),
            )

        except URLEmptyException as error:
            self.message = QMessageBox()
            self.message.critical(self.main_window, "Error", str(error))

    def inject(self):
        self._main_widget.actionAbout.triggered.connect(self.show_about)
        self._main_widget.DownloadButton.clicked.connect(lambda : Thread(target=self.download).start())

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())
