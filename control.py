import pygame
import sys


def events(char, pop_up):
    """обработка событий"""
    for event in pygame.event.get():  # событие на нажатие крестика окна
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # событие при нажатии левой кнопки мыши
            if event.button == 1:
                if char.collidepoint(event.pos):  # нажатие мыши на область выбора персонажа
                    pop_up.fill((255, 255, 255))


def update_screen(planche, characters, clock):
    # screen.fill((255, 255, 255))  # задний фон (больше не нужен из-за отрисовки планшетки)
    planche.output()  # отрисовка планшетки
    characters.draw_char()  # отрисовка области персонажа
    pygame.display.update()  # обновление экрана
    clock.tick(60)  # частота обновления экрана
    pygame.display.flip()  # загрузка последнего экрана


# def pop_up():


