import pygame
import event
from event import eventbus
from sprite import Camera

pygame = pygame
isEnable = True
fps = 30
clock = pygame.time.Clock()

__e_enable = list()
__e_update = list()


def enable(func):
    def inner():
        __e_enable.append(func)

    inner()
    return inner


def update(func):
    def inner():
        __e_update.append(func)

    inner()
    return inner


def run():
    for e in __e_enable:
        e()
    while isEnable:
        clock.tick(fps)
        for e in __e_update:
            e()
        for e in pygame.event.get():
            if e.type in event.events:
                for func in event.events[e.type]:
                    func(e)


pygame.init()
camera = None


def set_camera(size, flags=0, depth=0, display=0, vsync=0, pos=(0, 0)):
    global camera
    if camera is not None:
        return camera
    camera = Camera(size, flags, depth, display, vsync, pos)
    __e_update.append(lambda: camera.update())
    return camera


@eventbus(pygame.QUIT)
def on_quit(e):
    global isEnable
    isEnable = False
