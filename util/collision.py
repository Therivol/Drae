import pygame as p


class Collision:
    def __init__(self, scene):
        self.scene = scene

    def get_collision(self, ent_rect, *args):
        hit_list = []
        for layer in args:
            if layer == "Terrain":
                for rect in self.scene.rects_from_rect(ent_rect):
                    if ent_rect.colliderect(rect):
                        hit_list.append(rect)
            if layer == "Entity":
                entities_rect = [r.rect for r in self.scene.loaded_entities]
                for rect in entities_rect:
                    if ent_rect.colliderect(rect):
                        hit_list.append(rect)

    @classmethod
    def collision(cls, ent, hit_list):
        cls.collision_x(ent, hit_list)
        cls.collision_y(ent, hit_list)

    @classmethod
    def collision_x(cls, ent, rect_list):
        ent.pos.x += ent.vel.x
        ent.rect.left = ent.pos.x
        hit_list = cls.test(ent.rect, rect_list)
        for tile in hit_list:
            if ent.vel.x > 0:
                ent.rect.right = tile.left
            elif ent.vel.x < 0:
                ent.rect.left = tile.right
            ent.pos.x = ent.rect.left

    @classmethod
    def collision_y(cls, ent, rect_list):
        ent.pos.y += ent.vel.y
        ent.rect.top = ent.pos.y
        hit_list = cls.test(ent.rect, rect_list)
        for tile in hit_list:
            if ent.vel.y > 0:
                ent.rect.bottom = tile.top
            elif ent.vel.y < 0:
                ent.rect.top = tile.bottom
            ent.pos.y = ent.rect.top



