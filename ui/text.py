from ui.uiElement import UiElement


class Text(UiElement):
    def __init__(self, game, pos, text, size, color):
        super().__init__(game, pos, (0, 0), True)
        self.color = color
        self.f_size = size
        self.surf = self.game.assets.draw_text(text, color, size)

    def update_text(self, text):
        self.surf = self.game.assets.draw_text(text, self.color, self.f_size)
