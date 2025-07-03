if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    sys.dont_write_bytecode = True
    from desktop.app import App

    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())
