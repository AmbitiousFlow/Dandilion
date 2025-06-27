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

        self.ui.PathButton.clicked.connect(self.set_path)

        self.ui.ConvertButton.clicked.connect(self.download)

    
    def set_path(self):
        """
        Sets the download path for the media files.
        Opens a file dialog to select the directory.
        """
        self.controller.set_path()
        self.ui.PathLineEdit.setText(self.controller.get_path())

    def download(self):
        """
        Initiates the download of media files based on user input.
        Retrieves the URL and format from the UI and calls the controller to perform the download.
        """
        url = self.ui.UrlTextInput.text()
        media_format = self.ui.MediaTypeComboBox.currentText()
        destination = self.controller.get_path()

        if not url:
            self.ui.StatusLabel.setText("Please enter a valid URL.")
            return

        try:

            self.controller.download(url, media_format, destination)
            self.ui.LogsTextEdit.append(f"Downloading {media_format} from {url} to {destination}")

        except Exception as e:
            ...