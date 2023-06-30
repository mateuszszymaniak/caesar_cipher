from dataclasses import dataclass


@dataclass
class Text:
    txt: str
    rot_type: str
    status: str

    def __str__(self):
        return f"txt = {self.txt}, rot_type = {self.rot_type}, status = {self.status}"
