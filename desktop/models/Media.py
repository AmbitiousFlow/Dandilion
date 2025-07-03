
class Media:

    def __init__(self, url: str, format: str):
        self.url = url
        self.format = format

    def __repr__(self):
        return f"Media <type={self.format}, url={self.url}>"

 