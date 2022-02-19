import pygame as p


class Collider:
    def __init__(self, scene, ent, layers):
        self.scene = scene
        self.ent = ent
        self.layers = layers
        self.rect = p.rect.Rect(0, 0, 64, 64)
        self.rect.center = ent.pos.pos

    def update(self, ent):
        if ent.vel.vel.length() != 0:
            hit_list = self.scene.collision.get_collision(self.rect, "Terrain")


