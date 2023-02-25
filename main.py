import pygame
import random 
pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE

)

class Player():
    def __init__(self, posx, posy):
        self.posx = posx 
        self.posy = posy
    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.posy -= 5
        if pressed_keys[K_DOWN]:
            self.posy += 5
        if pressed_keys[K_LEFT]:
            self.posx -= 5
        if pressed_keys[K_RIGHT]:
            self.posx += 5

        if self.posx <= 0:
            self.posx = 3
        if self.posx >= 420:
            self.posx = 418

class Bullet():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def shoot(self):

        self.posy -= 2

    def reset(self):

        self.posx = player.posx + 40 
        self.posy = 440
    
    def update(self):
        
        if shoot == False:

            self.posx = player.posx + 40
        
  
    

screen = pygame.display.set_mode([500, 500])
player = Player(20, 20)
bullet = Bullet(player.posx + 40, 440)
running = True 

counter = 0
shoot = False 

bubble_x = 10
bubble_y = 10




vel = [random.randint(0, 2), random.randint(-2, 1)]
while running: 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    bullet.update()

    if pressed_keys[K_SPACE]:
        shoot = True
        
    if shoot == True:
        bullet.shoot()
        counter += 1 
    if counter >= 350:
        bullet.reset()
        counter = 0
        shoot = False 
    

    screen.fill((0, 0, 0))

    bubble_x += vel[0]
    bubble_y += vel[1]

    if bubble_x <= 0:
        vel[0] = -vel[0]
    if bubble_x >=500:
        vel[0] = -vel[0]
    if bubble_y <=0:
        vel[1] = -vel[1]
    if bubble_y >= 250:
        vel[1] = -vel[1]

    if (bubble_y == bullet.posy or bubble_y in range(bullet.posy + 10) or bubble_y in range(bullet.posy -10)) and (bubble_x == bullet.posx or bubble_x in range(bullet.posx + 10) or bubble_x in range(bullet.posx + 10)):
        pygame.quit()

  
    #Halfway line 
    pygame.draw.rect(screen , (255, 255, 255), pygame.Rect(0, 250, 500, 10))

    #Bubble 
    pygame.draw.circle(screen, (200, 0, 255), (bubble_x, bubble_y), 5)

    #Paddle 
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(player.posx, 450, 80, 10))

    #Bullet 
    pygame.draw.circle(screen, (200, 0, 255), (bullet.posx, bullet.posy), 5)
    
    
pygame.display.flip()

pygame.quit()