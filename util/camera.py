import pygame as p


class Camera:
    def __init__(self, game, entity):
        self.entity = entity
        self.game = game
        self.scroll = [entity.pos.x, entity.pos.y]

    def update(self):
        self.scroll[0] = self.entity.pos.x - self.game.RES[0] / 2 + self.entity.image.get_width() / 2
        self.scroll[1] = self.entity.pos.y - self.game.RES[1] / 2 + self.entity.image.get_height() / 2
