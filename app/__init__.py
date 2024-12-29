from app.errors.URLEmptyException import URLEmptyException
from app.services.DownloadService import DownloadService
from app.settings.settings        import Settings
from app.widgets.about            import Ui_About
from app.widgets.app              import Ui_Dandilion
from PyQt6.QtGui                  import QDesktopServices
from PySide6.QtCore               import QThread
from PySide6.QtCore               import QObject
from PySide6.QtCore               import Signal
from PySide6.QtWidgets            import QApplication
from PySide6.QtWidgets            import QMessageBox
from PySide6.QtWidgets            import QMainWindow
from PySide6.QtWidgets            import QWidget
from PyQt6.QtCore                 import QUrl
from pathlib                      import Path
import sys

class DownloadWorker(QObject):
    finished = Signal()
    error_occurred = Signal(str)

    def __init__(self, url, path, file_type, download_service):
        super().__init__()
        self.url = url
        self.path = path
        self.file_type = file_type
        self.download_service = download_service

    def run(self):
        try:
            self.download_service.download(self.url, self.path, self.file_type)
        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            self.finished.emit()

class Application:
    """
    The Application class initializes and sets up the main application, including
    the main window, about window, and settings window. It also manages the download
    service and its associated thread.
    """
    main_widget = Ui_Dandilion()
    about_widget = Ui_About()
    settings_config = Settings()
    def __init__(self):
        """
        Initializes the Application class by setting up the QApplication, main window,
        about window, and settings window. It also configures the application style
        and sets up the UI components and services.
        """
        # Injecting
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.about_window = QWidget()
        self.settings_window = QWidget()
        self.app.setStyle(self.settings_config.config['theme'])
        # Setting Up
        self.main_widget.setupUi(self.main_window)
        self.about_widget.setupUi(self.about_window)
        # Services
        self.download_service = DownloadService(
            self.main_widget.DownloadProgressBar, self.main_widget.OutputAreaBox
        )
        self.download_thread = None  # Initialize as None
        self.set_actions()

    def start_download(self):
        if self.main_widget.UrlEntry.text() == "":
            self.show_error_message("Empty URL Warning", "Please provide a URL.")
            return

        url = self.main_widget.UrlEntry.text()
        path = self.settings_config.config['path']
        file_type = self.main_widget.TypeComboBox.currentText()

        # Create and set up worker thread
        self.download_thread = QThread()
        self.download_worker = DownloadWorker(url, path, file_type, self.download_service)
        self.download_worker.moveToThread(self.download_thread)

        # Connect signals
        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.finished.connect(self.download_thread.quit)
        self.download_worker.finished.connect(self.download_worker.deleteLater)
        self.download_thread.finished.connect(self.download_thread.deleteLater)
        self.download_worker.error_occurred.connect(self.show_error_message)

        # Start the thread
        self.download_thread.start()

    def show_error_message(self, title, message):
        msg = QMessageBox()
        msg.critical(self.main_window, title, message)

    def set_actions(self):
        url = QUrl('https://github.com/Kyle-Myre')
        self.main_widget.DownloadButton.clicked.connect(self.start_download)
        self.main_widget.WikiButton.clicked.connect(self.about_window.show)
        self.main_widget.GithubButton.clicked.connect(lambda: QDesktopServices.openUrl(url))

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())
