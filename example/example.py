import plus
from plus import pygame, eventbus
from sprite import Entity

camera = plus.set_camera((1280, 720))
image = pygame.image.load("image/Elaina.jpg")
elaina = Entity(image, (0, 0), (1, 1))


@eventbus(pygame.MOUSEWHEEL)
def on_mouse(e):
    camera.zoom_scale += e.y * 0.03


mouse_click = False


@eventbus(pygame.MOUSEBUTTONUP)
def mouse_up(e):
    global mouse_click
    mouse_click = False


@eventbus(pygame.MOUSEBUTTONDOWN)
def mouse_up(e):
    global mouse_click
    mouse_click = True


@eventbus(pygame.MOUSEMOTION)
def mouse_motion(e):
    if mouse_click:
        camera.pos = (camera.pos[0] + e.rel[0] / camera.zoom_scale, camera.pos[1] + e.rel[1] / camera.zoom_scale)


plus.run()
