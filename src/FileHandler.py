import json
import os
from dataclasses import dataclass, asdict

@dataclass
class FileHandler:
    text: str
    rot_type: str
    status: str

    @property
    def get_text(self):
        return self.text

    @get_text.setter
    def get_text(self, value):
        self.text = value

    @property
    def get_rot_type(self):
        return self.rot_type

    @get_rot_type.setter
    def get_rot_type(self, value):
        self.rot_type = value

    @property
    def get_status(self):
        return self.status

    @get_status.setter
    def get_status(self, value):
        self.status = value

    def save(self, file_name: str, did_override: (str, None)):
        with open(file_name, 'w') as writer:
            json.dump(asdict(self), writer)

    def open(self, file_name):
        with open(file_name, 'r') as reader:
            json.load(reader)

