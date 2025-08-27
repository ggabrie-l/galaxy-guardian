import pygame

class Bullet():
    def __init__(self, player, x , y):
        self.player = player
        self.state = "Active"
        self.Rect = None
        self.x = x
        self.y = y
    
    def draw(self, display):
        self.Rect = pygame.Rect((self.x, self.y), (15, 15))
        self.y -= 3
        if self.y < 0:
            self.destroy()
        pygame.draw.rect(display, (255,255,128), rect=self.Rect)

    def destroy(self):
        # Play Animation
        self.state = "Destroyed"