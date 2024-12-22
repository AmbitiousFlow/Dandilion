class URLEmptyException(Exception):
    def __init__(self):
        self.message = "URL is empty , please enter an URL"
        super().__init__(self.message)