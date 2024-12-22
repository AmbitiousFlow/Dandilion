from pathlib import Path
import json
import os


__DIRNAME__ = os.path.join(os.path.dirname(__file__), "settings.json")


class Settings:
    def __init__(self):
        with open(__DIRNAME__) as file:
            self.config = json.load(file)
            if self.config["path"] == None:
                self.config["path"] = str(Path.home() / "Downloads")
                with open(__DIRNAME__, "w") as file:
                    json.dump(self.config, file, indent=4)


