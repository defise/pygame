import pygame
from settings import get_language, toggle_volume


def show_main_menu(screen, clock):
    font = pygame.font.Font(None, 40)
    menu_text = "Найди выход - Главное меню"
    text_surface = font.render(menu_text, True, pygame.Color('white'))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # Переход к выбору уровня или настройкам
                return

        screen.fill((0, 0, 0))
        screen.blit(text_surface, (100, 100))
        pygame.display.flip()
        clock.tick(50)
