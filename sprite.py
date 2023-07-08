import uuid
import pmath
from plus import pygame

group = pygame.sprite.Group()


class Object(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__(group)
        self.image = image
        self.pos = (pos[0], pos[1])
        self.rect = self.image.get_rect(center=pos)
        self.rotation = 0

    def update(self):
        self.rect.center = self.pos


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, pos, hitbox):
        super().__init__(group)
        self.image = image
        self.pos = (pos[0], pos[1])
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.hitbox = hitbox
        self.uuid = uuid.uuid4()

    def teleport(self, pos):
        self.rect.center = pos

    def update(self):
        self.rect.center = self.pos


class UI(pygame.sprite.Sprite):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture
        self.rect = self.texture.get_rect()


class Camera:
    def __init__(self, size, flags=0, depth=0, display=0, vsync=0, pos=(0, 0)):
        self.pos = pos
        self.size = size
        self.surface = pygame.display.set_mode(size, flags, depth, display, vsync)
        self.zoom_scale = 1

    def update(self):
        group.update()
        self.surface.fill('#000000')
        for sprite in group.sprites():
            offset_pos = ((self.pos[0] - sprite.pos[0]) * self.zoom_scale, (self.pos[1] - sprite.pos[1]) * self.zoom_scale)
            self.surface.blit(pygame.transform.scale(sprite.image, pmath.multiple_pair(sprite.rect.size, self.zoom_scale)), offset_pos)
        pygame.display.update()
