import os
import pygame as p
from util.collision import Collision
from entity.component.health import Health


class Entity:
    def __init__(self, game, pos, tag, health, speed, hostile):
        self.hostile = hostile
        self.tag = tag
        self.game = game
        self.pos = p.math.Vector2(pos)
        self.speed = speed
        self.vel = p.math.Vector2(0, 0)
        self.rect = p.rect.Rect(0, 0, 32, 32)
        self.rect.center = pos
        self.image = p.transform.scale(p.image.load(os.path.join("assets", "sprites", tag, tag + "_front1.png")), (64, 64))

        self.health = Health(self, health, 0)

    def render(self, display, scroll):
        display.blit(self.image, (self.pos.x - scroll[0], self.pos.y - scroll[1]))

    def update(self, dt, rect_list):
        self.on_update(dt)
        if self.vel.length() != 0:
            self.vel.scale_to_length(dt * self.speed * 100)
        Collision.collision_x(self, rect_list)
        Collision.collision_y(self, rect_list)

    def on_update(self, dt):
        pass

    def load_texture(self):
        self.image = p.transform.scale(p.image.load(os.path.join("assets", "sprites", self.tag,
                                                                 self.tag + "_front1.png")), (64, 64))
