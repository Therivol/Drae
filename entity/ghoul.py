from entity.entity import Entity
import pygame as p


class Ghoul(Entity):
    def __init__(self, game, pos):
        super().__init__(game, pos, "ghoul", 30, 1, True)
        self.target = None

    def on_update(self, dt):
        if self.target:
            self.vel.update(self.target.pos.x - self.pos.x, self.target.pos.y - self.pos.y)

    def update_target(self, entity):
        self.target = entity
