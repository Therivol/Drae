import os
import json


class Settings:
    def __init__(self, game):
        self.game = game
        self.path = os.path.join("load", "settings")
        self.key_binds = {}
        self.graphics = {}
        self.audio = {}
        self.load_all()

    def load_all(self):
        with open(os.path.join(self.path, "key_binds"), "r") as open_file:
            self.key_binds = json.load(open_file)
