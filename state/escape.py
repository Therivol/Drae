import pygame as p
import os
from state.state import State
from state.settingsMain import SettingsMain
import ui


class EscapeMenu(State):
    def __init__(self, game):
        super().__init__(game, "Escape")
        self.game.state.prev_state = self.game.state.stack[-1]
        print(self.game.state.prev_state)

        mist = ui.background.Background(game, (0.5, 0.5), (1, 1), (0, 0, 0))
        mist.surf.set_alpha(80)
        self.add_ui(mist, ui.background.Background(game, (0.5, 0.5), (0.8, 0.8), (165, 170, 188)))

        self.return_button = ui.button.Button(game, (0.5, 0.3), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.return_button, ui.text.Text(game, (0.5, 0.3), "Return", 64, (0, 0, 0)))

        self.settings_button = ui.button.Button(game, (0.5, 0.5), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.settings_button, ui.text.Text(game, (0.5, 0.5), "Settings", 64, (0, 0, 0)))

        self.exit_button = ui.button.Button(game, (0.5, 0.7), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.exit_button, ui.text.Text(game, (0.5, 0.7), "Exit", 64, (0, 0, 0)))

    def on_update(self, dt):
        if self.game.controller.get_key_down("escape"):
            self.game.state.exit_state()
        if self.return_button.get_click():
            self.game.state.exit_state()
        if self.settings_button.get_click():
            self.game.state.enter_state(SettingsMain(self.game))
        if self.exit_button.get_click():
            self.game.save()
            while len(self.game.state.stack) > 1:
                self.game.state.exit_state()

    def on_render(self, display):
        self.game.state.prev_state.render(display)
