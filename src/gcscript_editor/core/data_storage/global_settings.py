from dataclasses import dataclass,asdict
from typing import Any
import pytoml as toml
from pathlib import Path
from textual import notifications

SETTINGS_LOCATION: Path = Path(Path.home(),".gcscript-config.toml")

@dataclass
class GlobalSettings:
    theme: str = "textual-dark"
    
    @classmethod
    def load(cls):
        if not SETTINGS_LOCATION.exists():
            print("No global settings found, creating default...")
            default = cls()
            default.save()
            return default

        try:
            with open(SETTINGS_LOCATION) as file:
                settings = toml.load(file)
            return GlobalSettings(**settings["general"])
        except Exception as e:
            print("error",e)
            return cls()

    def _serialize(self) -> dict:
        return {
            "general": asdict(self)
        }

    def save(self):
        print("Saving Settings")
        with SETTINGS_LOCATION.open("w") as file:
            file.write(toml.dumps(self._serialize()))
        print("Settings Saved")