from PySide6.QtWidgets import QMainWindow
from app.views.MainWindow  import MainWindow


class App(QMainWindow):

    def __init__(self):
        """
        Initializes the application with the main window.
        :param main_window: An instance of MainWindow to be used as the main interface.
        """
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)


