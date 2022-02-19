import pygame as p


class Entity:
    def __init__(self, pos):
        self.pos = p.math.Vector2(pos)
        self.image = None
        self.components = []

    def update(self, dt):
        for component in self.components:
            component.update(dt)

    def add_comp(self, component):
        self.components.append(component)

    def remove_comp(self, component):
        self.components.remove(component)

    def render(self):
        pass
