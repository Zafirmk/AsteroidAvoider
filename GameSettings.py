import pygame
import os
import random
import numpy as np
import neat

pygame.init()

#  Display settings
window_width = 900
playable_height = 200
window_height = 320
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Astroid Avoider")
bg_img = pygame.image.load('./Images/Background.png')
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#  Game variables
font = pygame.font.SysFont(None, 25)

#  NEAT variables
max_distance = np.sqrt(((1100-20) **2) + ((playable_height-31) **2))

class Player:
    def __init__(self):
        self.x = 20
        self.y = 70
        self.change = 0
        self.width = 59
        self.height = 31
        self.image = pygame.image.load("./Images/Spaceship.png")
        self.score = 0

    def reset(self):
        self.x = 20
        self.y = 70

    def moveUP(self):
        self.change -= 5

    def moveDOWN(self):
        self.change += 5

    def draw(self):
        window.blit(self.image, (self.x, self.y))

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class asteroid():
    def __init__(self, num, y_max, speed, width, height, threshold_score):
        self.x = 1100
        self.y = random.randrange(0, y_max)
        self.image = pygame.image.load("./Images/Asteroid" + str(num) + ".png")
        self.speed = -speed
        self.width = width
        self.height = height
        self.threshold_score = threshold_score

    def collision(self, x):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        player_rect = x.getRect()
        if player_rect.colliderect(rect):
            x.score = 0
            x.reset()
            return True

    def move(self, x):
        if self.x < 0:
            self.x = 1100
            self.y = random.randrange(0, playable_height-self.height)

        if x.score >= self.threshold_score:
            self.x += self.speed
            self.draw()

    def draw(self):
        window.blit(self.image, (self.x, self.y))

    def reset(self, lst):
        for x in range(1, 5):
            lst[x].x = 1100
            lst[x].y = random.randrange(0, self.height)

def GetDistance(num, player, lst):
    l1 = abs(player.y - lst[num].y)
    l2 = abs(lst[num].x - player.x)
    distance = ((l1 **2) + (l2 ** 2)) ** 0.5 / max_distance
    return distance

def Text_display(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, (x, y))
