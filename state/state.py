import pygame as p


class State:
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.ui = []

    def render(self, display):
        self.on_render(display)
        for element in self.ui:
            element.render(display)

    def on_render(self, display):
        pass

    def update(self, dt):
        self.on_update(dt)
        for element in self.ui:
            element.update(dt)

    def on_update(self, dt):
        pass

    def add_ui(self, *args):
        for element in args:
            self.ui.append(element)

    def save(self):
        pass
