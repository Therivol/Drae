import pygame.math


class Velocity:
    def __init__(self, ent, speed):
        self.ent = ent
        self.vel = pygame.math.Vector2(0, 0)
        self.speed = speed

    def update(self, dt):
        if self.vel.length() != 0:
            self.vel.scale_to_length(dt * self.speed * 100)

