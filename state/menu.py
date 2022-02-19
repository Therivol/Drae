from state.state import State
from state.load import LoadScreen
from state.settingsMain import SettingsMain
import ui.text
import ui.background
import ui.button


class MenuState(State):
    def __init__(self, game):
        super().__init__(game, "Menu")

        self.add_ui(ui.background.Background(game, (0.5, 0.5), (1, 1), (165, 170, 188)))

        self.load_button = ui.button.Button(game, (0.5, 0.4), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.load_button, ui.text.Text(game, (0.5, 0.4), "Load", 64, (0, 0, 0)))

        self.settings_button = ui.button.Button(game, (0.5, 0.6), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.settings_button, ui.text.Text(game, (0.5, 0.6), "Settings", 64, (0, 0, 0)))

    def on_update(self, dt):
        if self.load_button.get_click():
            self.game.state.enter_state(LoadScreen(self.game))
        if self.settings_button.get_click():
            self.game.state.enter_state(SettingsMain(self.game))

    def on_render(self, display):
        pass
