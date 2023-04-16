import pygame
import control
import images
from planchette import Planche
from characters import Characters


def run():
    """инициализация игры и создание экранов и вспомогательных осей"""
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))  # создание графического окна
    pop_up = pygame.display.set_mode((1280, 720))  # создание всплывающего окна
    pygame.display.set_caption('Lord of the Ring')  # название игры
    icon = images.icon  # загрузка иконки игры
    pygame.display.set_icon(icon)  # создание иконки
    fps = pygame.time.Clock()  # частота обновления экрана
    planche = Planche(screen)  # планшетка
    characters = Characters(screen)  # рамка выбора персонажей (надо нарисовать рамку с кнопкой "выбор персонажа")

    while True:
        control.events(characters.characters_rect, pop_up)
        control.update_screen(planche, characters, fps)


run()
