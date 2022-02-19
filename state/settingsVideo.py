import pygame as p
from state.state import State
import ui


class SettingsVideo(State):
    def __init__(self, game):
        super().__init__(game, "Video")

        self.add_ui(ui.background.Background(game, (0.5, 0.5), (1, 1), (165, 170, 188)))

        self.enter_button = ui.button.Button(game, (0.5, 0.4), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.enter_button, ui.text.Text(game, (0.5, 0.4), "Video", 64, (0, 0, 0)))

    def on_update(self, dt):
        if self.game.controller.get_key_down("escape"):
            self.game.state.exit_state()

    def on_render(self, display):
        pass
