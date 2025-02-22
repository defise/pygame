import pygame
from constants import TILE_SIZE, tile_images, player_image

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_type = tile_type  # Сохраняем тип тайла
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.x = pos_x  # Координата в клетках по X
        self.y = pos_y  # Координата в клетках по Y
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)

def generate_level(level):
    new_player = None
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == '.':
                Tile('empty', x, y)
            elif cell == '#':
                Tile('wall', x, y)
            elif cell == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, len(level[0]), len(level)
