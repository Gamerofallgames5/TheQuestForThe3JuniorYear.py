import pygame
from config import *
import math
import random

import pygame as pg
from config import *
class Player(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def collider_box(self, direction):
        return

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Enemy(pg.sprite.Sprite):

    def __init__(self, game, x, y, tier):
        self.groups = game.all_sprites, game.enemys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.movementdirection = 0
        self.x = x
        self.y = y
        self.tier = tier
        self.damage = 3 * tier
        self.doordistances = []
        for i in range(len(game.doorlist)):
            self.pythagx = abs(game.doorlist[i].x - self.x)
            self.pythgay = abs(game.doorlist[i].y - self.y)
            self.pythagans = math.sqrt((self.pythagx**2) + (self.pythgay**2))
            self.doordistances.append(self.pythagans)
        self.closestdoor = game.doorlist[self.doordistances.index(min(self.doordistances))]
        self.active = False





    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def collider_box(self, direction):
        return

    def update(self):
        if self.closestdoor.opened:
            self.active = True
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

#Wall Class
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.walls,game.obsticles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Door(pg.sprite.Sprite):
    def __init__(self, game, x, y, opened = False):
        self.groups = game.doors , game.obsticles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
        self.opened = opened
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        if not self.opened:
            self.image.fill(WHITE)
        else:
            self.image.fill((0,0,0,0))


