import os
import pygame as p

types_to_name = {0: 'dirt', 1: 'dirt'}


class Tile:
    def __init__(self, tile_type, location, game):
        self.game = game
        self.type = int(tile_type)
        self.x, self.y = location
        if self.type != 0:
            self.img_path = os.path.join(self.game.assets.assets_dir, "tiles", types_to_name[self.type] + ".png")
            self.img = p.image.load(self.img_path).convert()

    def render(self, display, scroll, tile_size, chunk_loc, chunk_size):
        if self.type == 0:
            return
        transformed = p.transform.scale(self.img, (tile_size, tile_size))
        display.blit(transformed, (chunk_loc[0] * (chunk_size * tile_size) + self.x * tile_size - scroll[0],
                                   chunk_loc[1] * (chunk_size * tile_size) + self.y * tile_size - scroll[1]))

    def rect(self, tile_size, chunk_loc, chunk_size):
        if self.type == 0:
            return
        tile_rect = p.Rect(chunk_loc[0] * (chunk_size * tile_size) + self.x * tile_size,
                           chunk_loc[1] * (chunk_size * tile_size) + self.y * tile_size, tile_size, tile_size)
        return tile_rect
