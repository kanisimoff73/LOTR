# # # import pygame
# # #
# # # # --- constants --- (UPPER_CASE names)
# # #
# # # SCREEN_WIDTH = 430
# # # SCREEN_HEIGHT = 410
# # #
# # # #BLACK = (  0,   0,   0)
# # # WHITE = (255, 255, 255)
# # # RED   = (255,   0,   0)
# # #
# # # FPS = 30
# # #
# # # # --- classses --- (CamelCase names)
# # #
# # # # empty
# # #
# # # # --- functions --- (lower_case names)
# # #
# # # # empty
# # #
# # # # --- main ---
# # #
# # # # - init -
# # #
# # # pygame.init()
# # #
# # # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# # # #screen_rect = screen.get_rect()
# # #
# # # pygame.display.set_caption("Tracking System")
# # #
# # # # - objects -
# # #
# # # rectangle = pygame.rect.Rect(176, 134, 17, 17)
# # # rectangle_draging = False
# # #
# # # # - mainloop -
# # #
# # # clock = pygame.time.Clock()
# # #
# # # running = True
# # #
# # # while running:
# # #
# # #     # - events -
# # #
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False
# # #
# # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # #             if event.button == 1:
# # #                 if rectangle.collidepoint(event.pos):
# # #                     rectangle_draging = True
# # #                     mouse_x, mouse_y = event.pos
# # #                     offset_x = rectangle.x - mouse_x
# # #                     offset_y = rectangle.y - mouse_y
# # #
# # #         elif event.type == pygame.MOUSEBUTTONUP:
# # #             if event.button == 1:
# # #                 rectangle_draging = False
# # #
# # #         elif event.type == pygame.MOUSEMOTION:
# # #             if rectangle_draging:
# # #                 mouse_x, mouse_y = event.pos
# # #                 rectangle.x = mouse_x + offset_x
# # #                 rectangle.y = mouse_y + offset_y
# # #
# # #     # - updates (without draws) -
# # #
# # #     # empty
# # #
# # #     # - draws (without updates) -
# # #
# # #     screen.fill(WHITE)
# # #
# # #     pygame.draw.rect(screen, RED, rectangle)
# # #
# # #     pygame.display.flip()
# # #
# # #     # - constant game speed / FPS -
# # #
# # #     clock.tick(FPS)
# # #
# # # # - end -
# # #
# # # pygame.quit()
# #
# # from tkinter import messagebox
# #
# # # show a simple message box with an "OK" button
# # messagebox.showinfo("Hello", "Welcome to my program!")
# #
# # # show a question message box with "Yes" and "No" buttons
# # result = messagebox.askquestion("Confirm", "Are you sure you want to quit?")
# #
# # # check the result of the question message box
# # if result == 'yes':
# #     # user clicked "Yes" button
# #     print("Quitting...")
# #     # do some cleanup and exit the program
# # else:
# #     # user clicked "No" button
# #     print("Cancelled.")
# #     # continue with the program
#
# import sys
# import pygame as pg
#
# pg.init()
# screen = pg.display.set_mode((640, 480))
#
# IMAGE = pg.Surface((100, 60))
# IMAGE.fill(pg.Color('sienna2'))
# pg.draw.circle(IMAGE, pg.Color('royalblue2'), (50, 30), 20)
# # New width and height will be (50, 30).
# IMAGE_SMALL = pg.transform.scale(IMAGE, (50, 30))
# # Rotate by 0 degrees, multiply size by 2.
# IMAGE_BIG = pg.transform.rotozoom(IMAGE, 0, 2)
#
#
# def main():
#     clock = pg.time.Clock()
#     done = False
#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True
#
#         screen.fill(pg.Color('gray15'))
#         screen.blit(IMAGE, (50, 50))
#         screen.blit(IMAGE_SMALL, (50, 155))
#         screen.blit(IMAGE_BIG, (50, 230))
#         pg.display.flip()
#         clock.tick(30)
#
#
# if __name__ == '__main__':
#     main()
#     pg.quit()
#     sys.exit()

import pygame

import win32api
import win32con
import win32gui

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

transparent = (74, 65, 42)
window_info = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(window_info, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(window_info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window_info, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)

running = True
while running:

      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RCTRL:
                        running = False

      screen.fill(transparent)

      pygame.draw.circle(screen, (255, 255, 255), (150, 150), 75)

      pygame.display.flip()

pygame.quit()