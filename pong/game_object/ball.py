import pygame
import math
from . import GameObject
from ..util.velocity import to_ppt
import random

def theta_init():
    degree = 120 * random.random() - 60 

    is_left = random.random() > 0.5
    if is_left:
        degree = 180 - degree

    return degree

class Ball(GameObject):
    def __init__(self, root, platforms):
        super().__init__(root)
        self.r = 20
        self.x = self.root.displayw/2
        self.y = self.root.displayh/2

        self.pps = 50
        self.theta = theta_init()

        self.platforms = platforms

    def update(self):
        ppt = to_ppt(self.pps, self.root.fps)
        v_x = ppt * math.cos(math.radians(self.theta))
        v_y = ppt * math.sin(math.radians(self.theta))

        self.x += v_x
        self.y += v_y

    def draw(self):
        pygame.draw.circle(self.window, (255,255,255), (self.x, self.y), self.r)
    
    def interact(self):
        for platform in self.platforms:
            is_collide, direction = self.is_collide(platform)
            if is_collide:
                # update theta
                if direction == 'top' or direction == 'bot':
                    self.theta *= -1
                elif direction == 'left' or direction == 'right':
                    self.theta = -1 * (180 + self.theta)
    
    def is_collide(self, platform):
        result = False

        x_p = platform.x + platform.w/2
        y_p = platform.y + platform.h/2
        d_v = abs(self.y - y_p)
        d_h = abs(self.x - x_p)
    
        if d_v <= self.r + platform.h/2 and d_h <= self.r + platform.w/2:
            result = True

        direction = None
        if result:
            # tell if top, left, right, bottom
            # if top: direction = 'top'
            if self.f1(self.x, x_p, y_p, platform.w, platform.h) > self.y and self.f2(self.x, x_p, y_p, platform.w, platform.h) > self.y:
                direction = 'top'
            elif self.f1(self.x, x_p, y_p, platform.w, platform.h) <= self.y and self.f2(self.x, x_p, y_p, platform.w, platform.h) <= self.y:
                direction = 'bot'
            elif self.f1(self.x, x_p, y_p, platform.w, platform.h) <= self.y and self.f2(self.x, x_p, y_p, platform.w, platform.h) > self.y:
                direction = 'right'
            elif self.f1(self.x, x_p, y_p, platform.w, platform.h) > self.y and self.f2(self.x, x_p, y_p, platform.w, platform.h) <= self.y:
                direction = 'right'
        
        return result, direction

    def f1(self, x, x_p, y_p, w, h):
        return ((-1*h)*w/x) + (y_p+(h*x_p/w))

    def f2(self, x, x_p, y_p, w, h):
        return ((h/w)*x) + (y_p-h/w*x_p)