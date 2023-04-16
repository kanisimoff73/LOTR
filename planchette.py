import images


class Planche:

    def __init__(self, screen):
        """инициализация планшетки"""
        self.screen = screen  # создание экрана
        self.image = images.planchette  # подгрузка объекта планшетки
        self.screen_rect = screen.get_rect()  # создание поверхности экрана
        self.img_rect = self.image.get_rect()  # создание поверхности планшетки
        self.img_rect.centerx = self.screen_rect.centerx  # центрирование планшетки по левой стороне
        self.img_rect.bottom = self.screen_rect.bottom  # центрирование планшетки по низу

    def output(self):
        """рисуем планшетку на экране"""
        self.screen.blit(self.image, self.img_rect)  # вывод планшетки на экран
