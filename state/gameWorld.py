import ui.background
from state.state import State
from state.scene import Scene
from state.escape import EscapeMenu
from entity.player import Player
from entity.ghoul import Ghoul
from util.camera import Camera
import ui.unitFrame
import ui.text
import pickle


class GameWorld(State):
    def __init__(self, game, path, new=False):
        super().__init__(game, "World")
        self.path = path
        print(new)

        if new:
            self.player = Player(game, (0, 0), "practice")
            self.cam = Camera(game, self.player)
            self.scene = Scene(game, "practice", self.cam)
            self.scene.add_entity(self.player)
        else:
            self.player = self.load_world()
            self.player.load_texture()
            self.player.game = game
            self.cam = Camera(game, self.player)
            self.scene = Scene(game, self.player.scene, self.cam)
            self.scene.add_entity(self.player)

        self.healthBar = None
        self.fps = None
        self.last_tick = 0
        self.load_ui()

    def on_update(self, dt):
        self.scene.update(dt)
        self.last_tick += dt
        if self.last_tick > 0.2:
            self.fps.update_text(str(round(1 / dt)))
            self.last_tick = 0
        if self.game.controller.get_key_down("escape"):
            self.game.state.enter_state(EscapeMenu(self.game))
        if self.game.controller.get_button_down('3'):
            self.scene.add_entity(Ghoul(self.game, self.game.controller.get_mouse_scroll(self.cam.scroll)))
        self.cam.update()

    def on_render(self, display):
        self.scene.render(display)

    def load_scene(self, name):
        self.scene = self.game.assets.load_scene(name)
        self.scene.add_entity(self.player)

    def load_world(self):
        with open(self.path, "rb") as file:
            return pickle.load(file)

    def load_ui(self):
        self.fps = ui.text.Text(self.game, (0.95, 0.05), "", 32, (255, 255, 255))
        self.add_ui(self.fps)
        self.healthBar = ui.unitFrame.UnitFrame(self.game, self.player)
        self.add_ui(self.healthBar)

    def save(self):
        with open(self.path, "wb") as file:
            self.player.game = None
            self.player.image = None
            pickle.dump(self.player, file)

