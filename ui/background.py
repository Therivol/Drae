from ui.uiElement import UiElement


class Background(UiElement):
    def __init__(self, game, pos, size, color):
        super().__init__(game, pos, size, True)
        self.surf.fill(color)

    def change_color(self, color):
        self.surf.fill(color)
