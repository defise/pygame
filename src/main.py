import pygame
import sys
from menu import show_main_menu
from game import run_game  # Импортируем run_game

FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Найди выход")
    clock = pygame.time.Clock()

    # Показ главного меню
    show_main_menu(screen, clock)

    # Запуск игрового цикла
    run_game(screen, 'level1.txt')

    terminate()


if __name__ == '__main__':
    main()
