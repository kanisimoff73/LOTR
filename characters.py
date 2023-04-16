import images


class Characters:
    def __init__(self, screen):
        """создание области для выбора персонажа"""
        self.screen = screen
        self.characters = images.choice_character  # подгрузка картинки с кнопкой "выбрать персонажа"
        self.characters_rect = self.characters.get_rect()  # создание поверхности
        self.characters_rect.center = (552, 448)  # координаты расположения поверхности

    def draw_char(self):
        """рисуем область"""
        self.screen.blit(self.characters, self.characters_rect)  # вывод картинки на эран
