import pygame
from sprites import generate_level, all_sprites, tiles_group
from level_loader import load_level
from camera import Camera
from constants import WIDTH, HEIGHT, FPS, TILE_SIZE

def run_game(screen, level_filename):
    level = load_level(level_filename)
    player, level_width, level_height = generate_level(level)
    camera = Camera(WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                # Управление клавишами WASD
                if event.key == pygame.K_w:
                    dy = -1
                elif event.key == pygame.K_s:
                    dy = 1
                elif event.key == pygame.K_a:
                    dx = -1
                elif event.key == pygame.K_d:
                    dx = 1

                if dx or dy:
                    new_x = player.x + dx
                    new_y = player.y + dy

                    # Проверка границ уровня
                    if new_x < 0 or new_x >= level_width or new_y < 0 or new_y >= level_height:
                        continue

                    # Проверка на столкновение со стеной:
                    can_move = True
                    for tile in tiles_group:
                        # Если в целевой клетке находится стена, движение невозможно
                        if tile.tile_type == 'wall' and tile.rect.topleft == (new_x * TILE_SIZE, new_y * TILE_SIZE):
                            can_move = False
                            break

                    if can_move:
                        player.x = new_x
                        player.y = new_y
                        player.rect.topleft = (player.x * TILE_SIZE, player.y * TILE_SIZE)

        # Обновление камеры
        camera.update(player)
        # Применение смещения камеры ко всем спрайтам
        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
