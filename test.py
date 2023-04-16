import pygame

def show_dialog_box(text):
    # Initialize Pygame
    pygame.init()

    # Set the size and position of the dialog box
    dialog_size = (1280, 720)
    dialog_pos = ((pygame.display.Info().current_w - dialog_size[0]) // 2,
                  (pygame.display.Info().current_h - dialog_size[1]) // 2)

    # Create a new Pygame window for the dialog box
    dialog_window = pygame.display.set_mode(dialog_size, pygame.NOFRAME)
    pygame.display.set_caption('Dialog Box')

    # Draw the dialog box on the Pygame window
    dialog_font = pygame.font.SysFont(None, 30)
    dialog_text = dialog_font.render(text, True, (0, 0, 0))
    dialog_rect = dialog_text.get_rect(center=(dialog_size[0] // 2, dialog_size[1] // 2))
    pygame.draw.rect(dialog_window, (255, 255, 255), (0, 0, dialog_size[0], dialog_size[1]))
    pygame.draw.rect(dialog_window, (0, 0, 0), (0, 0, dialog_size[0], dialog_size[1]), 20)
    dialog_window.blit(dialog_text, dialog_rect)

    # Set the Pygame window to be always on top
    pygame.display.set_caption('Dialog Box', 'Dialog Box')

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.quit()
                return

        pygame.display.update()

# Test the dialog box
show_dialog_box('This is a test dialog box. Press Enter to close it.')

# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
#
# popup_surface = pygame.Surface((300, 200))
# popup_surface.fill((255, 255, 255))
# my_font = pygame.font.SysFont(None, 24)
# text_surface = my_font.render('Hello, world!', True, (0, 0, 0))
# popup_surface.blit(text_surface, (10, 10))
#
# screen.blit(popup_surface, (170, 140))
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
#             pygame.quit()
#             sys.exit()