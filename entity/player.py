from entity.entity import Entity
import pygame as p


class Player(Entity):
    def __init__(self, game, pos, scene):
        super().__init__(game, pos, "player", 100, 10, False)
        self.scene = scene

    def on_update(self, dt):
        self.vel.update(self.game.controller.get_action("right") - self.game.controller.get_action("left"),
                        self.game.controller.get_action("down") - self.game.controller.get_action("up"))
