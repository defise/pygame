import os

import pygame



WIDTH, HEIGHT = 640, 480
FPS = 50
TILE_SIZE = 32


def load_image(name):
    # Определяем абсолютный путь до папки data/images относительно этого файла
    base_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'images')
    full_path = os.path.join(base_path, name)
    return pygame.image.load(full_path)


tile_images = {
    'wall': load_image('wall.png'),
    'empty': load_image('empty.png')
}
player_image = load_image('player.png')
