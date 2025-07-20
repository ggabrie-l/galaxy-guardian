import pygame

class Player():
    def __init__(self):
        self.hp = 3
        self.color = (63, 72, 204)
        self.speed = 2
        self.x = 10.0
        self.y = 10
        self.Rect = None
        self.state = "Active"

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.attack = False
        self.cooldown = pygame.USEREVENT + 0
        pygame.time.set_timer(self.cooldown, 150)

    def draw(self, display):
        surface = pygame.surface.Surface((60, 60))
        pygame.draw.rect(surface, self.color, pygame.Rect(30, 30, 60, 60)) 

        if self.up == True:
            self.y -= self.speed
        elif self.down == True:
            self.y += self.speed
        elif self.left == True:
            self.x -= self.speed
        elif self.right == True:
            self.x += self.speed

        display.blit(surface, (self.x, self.y))