import pygame

from .game_object.platform import PlatformLeft, PlatformRight, PlatformUp, PlatformDown
from .game_object.ball import Ball

class PongGame:
    def __init__(self):
        self.displayw = 1000
        self.displayh = 700
        self.window = pygame.display.set_mode((self.displayw, self.displayh))

        self.windowclock = pygame.time.Clock()
        self.fps = 60

        self.platforms = [PlatformLeft(self), PlatformRight(self),
                          PlatformUp(self), PlatformDown(self)]
        self.ball = Ball(self, self.platforms)
        self.objs = [self.ball]
        self.objs.extend(self.platforms)
    
    def run(self):
        while True:
            self.window.fill((0, 0, 0))

            # update
            for obj in self.objs:
                obj.update()

            # interact
            for obj in self.objs:
                obj.interact()
            
            # draw
            for obj in self.objs:
                obj.draw()
        
            pygame.display.update()
            self.windowclock.tick(self.fps)
    
     
hit = PongGame()
hit.run()
