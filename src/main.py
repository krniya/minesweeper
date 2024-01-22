# pylint: disable=no-member
import pygame
from components.dashboard import Dashboard


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Main Menu")

    main_menu = Dashboard(screen)
    main_menu.run()


if __name__ == "__main__":
    main()
