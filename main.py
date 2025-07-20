import pygame
import sys

import player
import enemy
import Bullet
import Structure

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Galaxy Guardian')

Player = player.Player()
StructureObj = Structure.StructureClass()

alive_objects = []
alive_objects.append(Player)
alive_objects.append(StructureObj)

alive_bullets = []

clock = pygame.time.Clock()

if __name__ == "__main__":
    running = True  

    while running:    
        DISPLAYSURF.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Player.up = True
                if event.key == pygame.K_DOWN:
                    Player.down = True
                if event.key == pygame.K_LEFT:
                    Player.left = True
                if event.key == pygame.K_RIGHT:
                    Player.right = True
                if event.key == pygame.K_SPACE:
                    Player.attack = True
            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_UP: 
                    Player.up = False
                if event.key == pygame.K_DOWN:
                    Player.down = False
                if event.key == pygame.K_LEFT:
                    Player.left = False
                if event.key == pygame.K_RIGHT:
                    Player.right = False
                if event.key == pygame.K_SPACE:
                    Player.attack = False

            if event.type == pygame.USEREVENT + 0 and Player.attack == True:
                new_shoot = Bullet.Bullet(True, Player.x + 37, Player.y + 10)
                alive_bullets.append(new_shoot)
        print(alive_objects)
        if len(alive_objects) == 1:
            new_structure = Structure.StructureClass()
            alive_objects.append(new_structure)
        for object in alive_objects: 
            if object.state == "Destroyed":
                del(object)
                continue
            object.draw(DISPLAYSURF)
            if len(alive_bullets) > 1:    
                for bullet in alive_bullets:
                    if object == Player:
                        continue
                    if bullet.state == "Destroyed":
                        del(bullet)
                        continue
                    else:
                        bullet.draw(DISPLAYSURF)

                    if bullet.Rect != None and bullet.Rect.bottom < object.Rect.bottom and bullet.Rect.left > object.Rect.left and bullet.Rect.right < object.Rect.right:
                            object.takeDmg(1)
                            bullet.state = "Destroyed"

        pygame.display.update() 
        clock.tick(60)