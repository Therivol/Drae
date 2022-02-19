import pygame as p
import os
import json
from state.scene import Scene


class AssetManager:
    def __init__(self, game):
        self.game = game
        p.font.init()
        self.assets_dir = os.path.join("assets")
        self.load_dir = os.path.join("load")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font_path = os.path.join(self.font_dir, "PressStart2P-vaV7.ttf")
        self.base_textures = {}
        self.loaded_textures = {}

        self.load_base_textures()

    def load_base_textures(self):
        self.base_textures["icon"] = p.image.load(os.path.join("assets", "sprites", "player", "player_front1.png"))

    def clear_textures(self):
        self.loaded_textures = {}

    def get_texture(self, tag):
        if tag in self.base_textures:
            return self.base_textures[tag]
        elif tag in self.loaded_textures:
            return self.loaded_textures[tag]
        else:
            print("No Texture Found")

    def draw_text(self, text, color, size):
        font = p.font.Font(self.font_path, size)
        text_surface = font.render(text, False, color)
        return text_surface

    ########
    @staticmethod
    def load_file(path):
        with open(path) as read_file:
            file = json.load(read_file)
            read_file.close()
        return file
