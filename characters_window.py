import images
import pygame


class Choice:
    def __init__(self, screen):
        """создание области для выбора персонажа"""
        self.screen = screen
        self.aragorn = images.aragorn
        self.aragorn = pygame.transform.smoothscale(self.aragorn, (354, 207))
        self.aragorn_rect = self.aragorn.get_rect()  # создание поверхности
        self.aragorn_rect.center = (210, 170)  # координаты расположения поверхности
        self.beravor = images.beravor
        self.beravor_rect = self.beravor.get_rect()  # создание поверхности
        self.beravor_rect.center = (200, 50)  # координаты расположения поверхности
        self.bilbo = images.bilbo
        self.bilbo_rect = self.bilbo.get_rect()  # создание поверхности
        self.gimli = images.gimli
        self.gimli_rect = self.gimli.get_rect()  # создание поверхности
        self.elena = images.elena
        self.elena_rect = self.elena.get_rect()  # создание поверхности
        self.legolas = images.legolas
        self.legolas_rect = self.legolas.get_rect()  # создание поверхности

    def draw_char(self):
        """рисуем область"""
        self.screen.blit(self.aragorn, self.aragorn_rect)  # вывод картинки на эран
        # self.screen.blit(self.beravor, self.beravor_rect)
