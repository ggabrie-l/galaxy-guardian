import pygame

class StructureClass:
    def __init__(self):
        self.hp = 15
        self.state = "Active"
        self.color = (0, 128, 0)
        self.Rect = None
        self.damageable = True
        self.y = 0
        self.x = 0

    def destroy(self):
        # play animation 
        self.state = "Destroyed"

    def draw(self, display):
        self.y += 1
        self.Rect = pygame.Rect((self.x, self.y), (180, 100))
        pygame.draw.rect(display, color=self.color, rect=self.Rect)

    def takeDmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.destroy()