import customtkinter as ctk
from . import __title__,__icon__,__themes__,__font__
from app.services.services import DownloadService
from threading import Thread

ctk.set_appearance_mode("System")
ctk.set_default_color_theme(__themes__ + "\\" + "marsh.json")


class Application(ctk.CTk):
    _download_serivce: DownloadService

    def __init__(self):
        """
        Initialize the Application window with a specific geometry and title.

        This constructor sets up various widgets including labels, an entry field,
        option menu, text box, progress bar, and a button. It also configures the
        window's icon and ensures the window is not resizable.

        Widgets:
            - CTkLabel: Displays the main title 'Dandilion' and other labels for URI and Type.
            - CTkEntry: Allows user input for URI.
            - CTkOptionMenu: Dropdown menu for selecting type (MP3 or MP4).
            - CTkTextbox: Displays output messages, initially disabled.
            - CTkProgressBar: Shows progress of an action, initially set to 0.
            - CTkButton: 'Download' button to perform an action.
        """
        super().__init__()

        self.geometry("695x295")
        self.iconbitmap(__icon__)
        self.title(__title__)

        self.bigTitle = ctk.CTkLabel(self, text="Dandilion", font=(__font__, 25))
        self.bigTitle.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.uriTitle = ctk.CTkLabel(self, text="URI :", font=(__font__, 15))
        self.uriTitle.grid(row=2, column=0, padx=10, pady=10)

        self.uriEntry = ctk.CTkEntry(self, width=610)
        self.uriEntry.grid(row=2, column=1, padx=10, pady=10)

        self.outputArea = ctk.CTkTextbox(
            self, width=670, height=100, font=(__font__, 15)
        )
        # self.outputArea.configure(state="disabled")
        self.outputArea.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        self.progressBar = ctk.CTkProgressBar(self, width=670)
        self.progressBar.set(0)
        self.progressBar.grid(row=5, column=0, padx=0, pady=10, columnspan=2)

        self.actionButton = ctk.CTkButton(
            self, text="Download", width=670, font=(__font__, 15)
        )
        self.actionButton.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        self._download_serivce = DownloadService(
            progress_bar=self.progressBar, output_area=self.outputArea
        )

        self.thread = Thread(target=self._download_serivce.download , args=(self.uriEntry.get() , "./output"))

        self.actionButton.configure(
            command=self.start_action
        )
        self.resizable(False, False)

    def start_action(self):
        self.thread = Thread(target=self._download_serivce.download , args=(self.uriEntry.get() , "./output"))
        self.thread.start()

    def run(self):
        """
        Start the main event loop of the application.
        This function will block until the application is closed.
        """
        self.mainloop()
