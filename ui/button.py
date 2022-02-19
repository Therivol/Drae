from ui.uiElement import UiElement


class Button(UiElement):
    def __init__(self, game, pos, size, color, h_color, center):
        super().__init__(game, pos, size, center)
        self.color = color
        self.h_color = h_color
        self.collided = False
        self.clicked = False

    def on_update(self, dt):
        if self.rect.collidepoint(self.game.controller.get_mouse_pos()):
            if self.game.controller.get_button_down('1'):
                self.clicked = True
            self.collided = True
        else:
            self.collided = False

    def on_render(self, display):
        if self.collided:
            self.surf.fill(self.h_color)
        else:
            self.surf.fill(self.color)

    def get_click(self):
        if self.clicked:
            self.clicked = False
            return True
        return False

