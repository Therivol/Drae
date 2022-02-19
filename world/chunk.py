class Chunk:
    def __init__(self, tile_list, loc, game):
        self.loc = loc
        self.tile_list = tile_list
        self.game = game
        self.entity_list = []

    def rect_list(self, tile_size, chunk_size):
        rect_list = []
        for tile in self.tile_list:
            if tile.type != 0:
                rect_list.append(tile.rect(tile_size, self.loc, chunk_size))
        return rect_list

    def add_entity(self, entity):
        self.entity_list.append(entity)
