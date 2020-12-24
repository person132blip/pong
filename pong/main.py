import pygame


class PongGame:
    def __init__(self):
        self.displayw = 1000
        self.displayh = 500
        self.window = pygame.display.set_mode((self.displayw, self.displayh))

        self.windowclock = pygame.time.Clock()
        self.fps = 60
    
    def run(self):
        while True:
            self.window.fill((0, 0, 0))

            # game sequence

            pygame.display.update()
            self.windowclock.tick(self.fps)
     
hit = PongGame()
hit.run()
