from app.controllers.DownloadController import DownloadController
from app.services.DownloadService import DownloadService
from app.ui.MainWindow import MainWindow
from PySide6.QtWidgets import QMainWindow , QFileDialog , QProgressBar
from PySide6.QtCore import QThread
from datetime import datetime


class App(QMainWindow):
    """Main application window for the download application."""

    def __init__(self):
        """Initialize the main application window and its components."""
        super().__init__()
        self._setup_ui()
        self._setup_services()
        self._connect_signals()

    def _setup_ui(self):
        """Set up the main window UI."""
        self.ui = MainWindow()
        self.ui.setupUi(self)
        # Validate that DownloadProgress is a QProgressBar
        if not hasattr(self.ui, 'DownloadProgress') or not isinstance(self.ui.DownloadProgress, QProgressBar):
            self._log_error("DownloadProgress is not a valid QProgressBar")

    def _setup_services(self):
        """Initialize the download service and controller."""
        self.download_service = DownloadService()
        self.controller = DownloadController(self.download_service)

    def _connect_signals(self):
        """Connect UI signals to their respective slots."""
        self.ui.ConvertButton.clicked.connect(self._handle_convert)
        self.ui.PathButton.clicked.connect(self._handle_file_dialog)

    def _handle_convert(self):
        """Handle the conversion/download process triggered by the Convert button."""
        try:
            url = self.ui.UrlTextInput.text().strip()
            if not url:
                raise ValueError("URL cannot be empty")
            output = self.ui.PathLineEdit.text().strip()
            if not output:
                raise ValueError("Output directory cannot be empty")
            media_type = self.ui.MediaTypeComboBox.currentText()
            widget = self.ui.DownloadProgress
            # Reset progress bar before starting
            widget.setValue(0)
            self.controller.download(url=url, widget=widget, format=media_type, output=output)
            self._log_error("Download initiated")  # Debug log to confirm start
        except Exception as e:
            self._log_error(f"Download failed: {str(e)}")

    def _handle_file_dialog(self):
        """Open a file dialog to select the download destination."""
        dialog = QFileDialog.getExistingDirectory(self, "Select Download Directory", ".")
        if dialog:
            self.ui.PathLineEdit.setText(dialog)
        else:
            self._log_error("No directory selected for download.")

    def _log_error(self, message: str):
        """Log an error message to the UI's LogsTextEdit with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.LogsTextEdit.append(f"[{timestamp}] [Error] {message}")