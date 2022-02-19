from state.state import State
from state.gameWorld import GameWorld
import os
from os.path import exists
import ui.text
import ui.background
import ui.button


class LoadScreen(State):
    def __init__(self, game):
        super().__init__(game, "Load")

        self.saves = []
        self.save_buttons = []
        self.create_button = None
        self.load_saves()
        self.load_ui()
        print(self.saves)

    def on_update(self, dt):
        if self.game.controller.get_key_down("escape"):
            self.game.state.exit_state()
        for button in self.save_buttons:
            if button.get_click():
                self.game.state.enter_state(GameWorld(self.game, self.saves[self.save_buttons.index(button)]))
        if self.create_button.get_click():
            self.game.state.enter_state(GameWorld(self.game, os.path.join("load", "world", "save_" + str(len(self.saves) + 1)), True))

    def on_render(self, display):
        pass

    def load_saves(self):
        i = 1
        while True:
            path = (os.path.join("load", "world", "save_" + str(i)))
            if exists(path):
                self.saves.append(path)
                i += 1
            else:
                break

    def load_ui(self):
        self.add_ui(ui.background.Background(self.game, (0.5, 0.5), (1, 1), (165, 170, 188)))
        for i in range(len(self.saves)):
            i += 1
            button = ui.button.Button(self.game, (0.5, 0.1 * i), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
            text = ui.text.Text(self.game, (0.5, 0.1 * i), "Save " + str(i), 64, (0, 0, 0))
            self.save_buttons.append(button)
            self.add_ui(button, text)
        self.create_button = ui.button.Button(self.game, (0.5, 0.8), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.create_button, ui.text.Text(self.game, (0.5, 0.8), "New", 64, (0, 0, 0)))
