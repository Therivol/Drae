import sys
import pygame as p
from util.controller import Controller
from util.assetManager import AssetManager
from state.stateHandler import StateHandler
from state.menu import MenuState
from util.settings import Settings


class Game:
    def __init__(self):
        self.settings = Settings(self)
        self.controller = Controller(self)
        self.assets = AssetManager(self)
        self.clock = p.time.Clock()

        self.w_size = (960, 540)
        self.window = p.display.set_mode(self.w_size, p.RESIZABLE)
        p.display.set_caption("Draeire")
        p.display.set_icon(self.assets.get_texture("icon"))

        self.RES = (1920, 1080)
        self.canvas = p.Surface(self.RES)

        self.running = True
        self.dt = 0
        self.prev_time = 0

        self.state = StateHandler(MenuState(self))

    def quit(self):
        self.running = False
        self.save()
        p.quit()
        sys.exit()

    def save(self):
        self.state.exit_all()

    def game_loop(self):
        while self.running:
            self.controller.handle_events()
            self.update()
            self.render()
            # self.clock.tick(144)

    def update(self):
        self.get_dt()
        self.state.current.update(self.dt)

    def render(self):
        self.state.current.render(self.canvas)
        self.window.blit(p.transform.scale(self.canvas, self.w_size), (0, 0))
        p.display.update()

    def get_dt(self):
        now = p.time.get_ticks() / 1000
        self.dt = now - self.prev_time
        self.prev_time = now


if __name__ == '__main__':
    g = Game()
    g.game_loop()
