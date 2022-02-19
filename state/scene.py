import os
import math
import pygame as p
from world.chunk import Chunk
from world.tile import Tile
from util.collision import Collision


class Scene:
    def __init__(self, game, name, cam):
        self.game = game
        self.name = name
        self.cam = cam
        self.map = [[1]]
        self.textures = {}
        self.game_map = {}
        self.loaded_chunks = {}
        self.loaded_entities = []
        self.CHUNK_SIZE = 8
        self.TILE_SIZE = 64
        self.collision = Collision(self)
        self.load_map(f"load/scene/{name}/map.txt")
        self.load_chunks()
        self.load_entities()

    def render(self, display):
        display.fill((165, 170, 188))
        self.sort_entities()
        self.render_map(display)
        self.render_entities(display)

    def update(self, dt):
        self.load_chunks()
        self.load_entities()
        for entity in self.loaded_entities:
            entity.update(dt, self.rects_from_rect(entity.rect))

    def sort_entities(self):
        self.loaded_entities.sort(key=lambda entity: entity.rect.bottom)

    def render_map(self, display):
        for chunk in self.loaded_chunks:
            chunk_loc = chunk.split(';')
            chunk_loc = int(chunk_loc[0]), int(chunk_loc[1])
            chunk_rect = p.Rect(chunk_loc[0] * self.CHUNK_SIZE * self.TILE_SIZE - self.cam.scroll[0],
                                chunk_loc[1] * self.CHUNK_SIZE * self.TILE_SIZE - self.cam.scroll[1],
                                self.CHUNK_SIZE * self.TILE_SIZE, self.CHUNK_SIZE * self.TILE_SIZE)
            for tile in self.loaded_chunks[chunk].tile_list:
                tile.render(display, self.cam.scroll, self.TILE_SIZE, chunk_loc, self.CHUNK_SIZE)
            p.draw.rect(display, (145, 150, 168), chunk_rect, 2)

    def render_entities(self, display):
        for entity in self.loaded_entities:
            entity.render(display, self.cam.scroll)

    def load_all(self):
        load_path = os.path.join("../", "load", "scene", self.name)
        self.map = self.game.assets.load_file(os.path.join(load_path, "map"))
        self.entities = self.game.assets.load_file(os.path.join(load_path, "entities"))
        self.textures = self.game.assets.load_file(os.path.join(load_path, "textures"))

    def load_map(self, path):
        file = open(path, "r")
        data = file.read()
        file.close()
        data = data.split('\n')

        chunks_y = math.ceil(len(data) / self.CHUNK_SIZE)
        chunks_x = 0
        for row in data:
            if chunks_x < len(row):
                chunks_x = len(row)
        chunks_x = math.ceil(chunks_x / self.CHUNK_SIZE)

        for y in range(chunks_y):
            for x in range(chunks_x):
                new_chunk = []
                for y_pos in range(self.CHUNK_SIZE):
                    for x_pos in range(self.CHUNK_SIZE):
                        if len(data) <= (y * self.CHUNK_SIZE + y_pos):
                            tile_type = 0
                        elif len(data[y * self.CHUNK_SIZE + y_pos]) <= (x * self.CHUNK_SIZE + x_pos):
                            tile_type = 0
                        else:
                            tile_type = data[y * self.CHUNK_SIZE + y_pos][x * self.CHUNK_SIZE + x_pos]
                        new_chunk.append(Tile(tile_type, (x_pos, y_pos), self.game))
                self.game_map[str(x) + ';' + str(y)] = Chunk(new_chunk, (x, y), self.game)

    def load_chunks(self):
        self.loaded_chunks = {}
        for y in range(math.ceil(self.game.RES[1] / (self.CHUNK_SIZE * self.TILE_SIZE)) + 1):
            for x in range(math.ceil(self.game.RES[0] / (self.CHUNK_SIZE * self.TILE_SIZE)) + 1):
                target_x = x - 1 + math.ceil(self.cam.scroll[0] / (self.CHUNK_SIZE * self.TILE_SIZE))
                target_y = y - 1 + math.ceil(self.cam.scroll[1] / (self.CHUNK_SIZE * self.TILE_SIZE))
                target_chunk = str(target_x) + ';' + str(target_y)
                if target_chunk not in self.game_map:
                    self.generate_chunk(target_chunk)
                self.loaded_chunks[target_chunk] = self.game_map[target_chunk]

    def load_entities(self):
        self.loaded_entities = []
        for chunk in self.loaded_chunks:
            self.loaded_entities += self.loaded_chunks[chunk].entity_list
            self.loaded_chunks[chunk].entity_list = []
        self.loaded_entities = list(set(self.loaded_entities))

        for entity in self.loaded_entities:
            for chunk in self.chunk_of_rect(entity.rect):
                chunk.entity_list.append(entity)

    def add_entity(self, *args):
        for entity in args:
            for chunk in self.chunk_of_rect(entity.rect):
                chunk.entity_list.append(entity)
        self.sort_entities()

    def remove_entity(self, entity):
        if entity in self.loaded_entities:
            self.loaded_entities.remove(entity)
        for chunk in self.chunk_of_rect(entity.rect):
            chunk.entity_list.remove(entity)

    def generate_chunk(self, chunk_loc):
        new_tiles = []
        for y in range(self.CHUNK_SIZE):
            for x in range(self.CHUNK_SIZE):
                new_tiles.append(Tile(0, (x, y), self.game))
        self.game_map[chunk_loc] = Chunk(new_tiles, chunk_loc, self.game)

    def rects_from_rect(self, rect):
        rect_list = []
        for chunk in self.chunks_of_rect(rect):
            rect_list += chunk.rect_list(self.TILE_SIZE, self.CHUNK_SIZE)
        return rect_list

    def chunks_of_rect(self, rect):
        chunk_hit_list = []
        for chunk in self.loaded_chunks:
            chunk_loc = chunk.split(';')
            chunk_loc = int(chunk_loc[0]), int(chunk_loc[1])
            chunk_rect = p.Rect(chunk_loc[0] * self.CHUNK_SIZE * self.TILE_SIZE, chunk_loc[1] * self.CHUNK_SIZE *
                                self.TILE_SIZE, self.CHUNK_SIZE * self.TILE_SIZE, self.CHUNK_SIZE * self.TILE_SIZE)
            if rect.colliderect(chunk_rect):
                chunk_hit_list.append(self.game_map[chunk])
                if (str(chunk_loc[0] + 1) + ';' + str(chunk_loc[1])) in self.game_map:
                    chunk_hit_list.append(self.game_map[str(chunk_loc[0] + 1) + ';' + str(chunk_loc[1])])
                if (str(chunk_loc[0] - 1) + ';' + str(chunk_loc[1])) in self.game_map:
                    chunk_hit_list.append(self.game_map[str(chunk_loc[0] - 1) + ';' + str(chunk_loc[1])])
                if (str(chunk_loc[0]) + ';' + str(chunk_loc[1] + 1)) in self.game_map:
                    chunk_hit_list.append(self.game_map[str(chunk_loc[0]) + ';' + str(chunk_loc[1] + 1)])
                if (str(chunk_loc[0]) + ';' + str(chunk_loc[1] - 1)) in self.game_map:
                    chunk_hit_list.append(self.game_map[str(chunk_loc[0]) + ';' + str(chunk_loc[1] - 1)])

        return chunk_hit_list

    def chunk_of_rect(self, rect):
        chunk_hit_list = []
        for chunk in self.loaded_chunks:
            chunk_loc = chunk.split(';')
            chunk_loc = int(chunk_loc[0]), int(chunk_loc[1])
            chunk_rect = p.Rect(chunk_loc[0] * self.CHUNK_SIZE * self.TILE_SIZE, chunk_loc[1] * self.CHUNK_SIZE *
                                self.TILE_SIZE, self.CHUNK_SIZE * self.TILE_SIZE, self.CHUNK_SIZE * self.TILE_SIZE)
            if rect.colliderect(chunk_rect):
                chunk_hit_list.append(self.game_map[chunk])
        return chunk_hit_list
