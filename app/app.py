from app.controllers.DownloadController import DownloadController
from app.services.DownloadService import DownloadService
from app.views.MainWindow  import MainWindow
from PySide6.QtWidgets import QMainWindow

class App(QMainWindow):

    def __init__(self):
        """
        Initializes the application with the main window.
        :param main_window: An instance of MainWindow to be used as the main interface.
        """

        self.download_service = DownloadService()

        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)

        self.controller = DownloadController(self.download_service)

        self.set_actions()

    
    def set_actions(self):
        self.ui.PathButton.clicked.connect(self.controller.set_path)
        print(self.controller.get_path())
        
       