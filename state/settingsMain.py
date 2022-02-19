import pygame as p
from state.state import State
import ui
from state.settingsVideo import SettingsVideo
from state.settingsAudio import SettingsAudio
from state.settingsControl import SettingsControl


class SettingsMain(State):
    def __init__(self, game):
        super().__init__(game, "Settings")

        self.add_ui(ui.background.Background(game, (0.5, 0.5), (1, 1), (165, 170, 188)))

        self.video_button = ui.button.Button(game, (0.5, 0.3), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.video_button, ui.text.Text(game, (0.5, 0.3), "Video", 64, (0, 0, 0)))

        self.audio_button = ui.button.Button(game, (0.5, 0.5), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.audio_button, ui.text.Text(game, (0.5, 0.5), "Audio", 64, (0, 0, 0)))

        self.controls_button = ui.button.Button(game, (0.5, 0.7), (0.3, 0.09), (110, 110, 115), (140, 145, 153), True)
        self.add_ui(self.controls_button, ui.text.Text(game, (0.5, 0.7), "Controls", 64, (0, 0, 0)))

    def on_update(self, dt):
        if self.game.controller.get_key_down("escape"):
            self.game.state.exit_state()
        if self.video_button.get_click():
            self.game.state.enter_state(SettingsVideo(self.game))
        if self.audio_button.get_click():
            self.game.state.enter_state(SettingsAudio(self.game))
        if self.controls_button.get_click():
            self.game.state.enter_state(SettingsControl(self.game))

    def on_render(self, display):
        pass
