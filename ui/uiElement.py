import pygame as p


class UiElement:
    def __init__(self, game, pos, size, center=False):
        self.game = game
        self.pos = pos
        self.size = size
        self.centered = center
        new_size = (round(size[0] * self.game.RES[0]), round(size[1] * self.game.RES[1]))
        self.surf = p.Surface(new_size)
        self.rect = p.Rect((0, 0), self.get_real(size))
        self.update_pos(pos)

    def update(self, dt):
        self.on_update(dt)

    def on_update(self, dt):
        pass

    def render(self, display):
        self.on_render(display)
        if self.centered:
            blit_pos = (self.pos[0] * display.get_width() - self.surf.get_width() / 2,
                        self.pos[1] * display.get_height() - self.surf.get_height() / 2)
        else:
            blit_pos = self.get_real(self.pos)
        display.blit(self.surf, blit_pos)

    def on_render(self, display):
        pass

    def get_real(self, tup):
        return tup[0] * self.game.RES[0], tup[1] * self.game.RES[1]

    def update_pos(self, pos):
        self.pos = pos
        self.rect.center = self.get_real(pos)
