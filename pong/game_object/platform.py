import pygame
from . import GameObject
from ..util.velocity import to_ppt

class Platform(GameObject):
    def __init__(self, root):
        super().__init__(root)
        self.w = 30
        self.h = 150

        self.y_min = 0
        self.y_max = self.root.displayh - self.h
        self.x_bound = self.root.displayw * 0.1

        self.y = (self.root.displayh/2)-(self.h/2)

        self.color = (255, 255, 255)

        self.pps = 5000

    def update(self):
        for event in pygame.event.get():
            ppt = to_ppt(self.pps, self.root.fps)

            if event.type == pygame.KEYDOWN:
                if event.key == self.up_key:
                    print(event.key)
                    self.y -= ppt
                if event.key == self.down_key:
                    print(event.key)
                    self.y += ppt
                if event.key == self.left_key:
                    print(event.key)
                    self.x -= ppt
                if event.key == self.right_key:
                    print(event.key)
                    self.x += ppt
        
        # check if over the boundary
        if self.x < self.x_min:
            self.x = self.x_min
        if self.x > self.x_max:
            self.x = self.x_max

        if self.y < self.y_min:
            self.y = self.y_min
        if self.y > self.y_max:
            self.y = self.y_max
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h))

class PlatformUp(Platform):
    def __init__(self, root):
        super().__init__(root)
        self.x = 0
        self.y = 0
        self.w = self.root.displayw
        self.h = self.root.displayh * 0.05

        self.color = (255, 255, 0)
    
    def update(self):
        pass

class PlatformDown(Platform):
    def __init__(self, root):
        super().__init__(root)
        self.w = self.root.displayw
        self.h = self.root.displayh * 0.05
        self.x = 0
        self.y = self.root.displayh - self.h

        self.color = (255, 255, 0)

    def update(self):
        pass   

class PlatformLeft(Platform):
    def __init__(self, root):
        super().__init__(root)
        self.x = 0
    
        self.x_min = 0
        self.x_max = self.x_bound - self.w

        self.up_key = pygame.K_w
        self.down_key = pygame.K_s
        self.left_key = pygame.K_a
        self.right_key = pygame.K_d

class PlatformRight(Platform):
    def __init__(self, root):
        super().__init__(root)
        self.x = self.root.displayw - self.w

        self.x_min = self.root.displayw - self.x_bound
        self.x_max = self.root.displayw - self.w

        self.up_key = pygame.K_f
        self.down_key = pygame.K_v
        self.left_key = pygame.K_c
        self.right_key = pygame.K_b
       
