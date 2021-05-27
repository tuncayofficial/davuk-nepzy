import pygame
import os

pygame.init()

height = 900
width = 400

fps = 60

WHITE = (255, 255, 255)


windows = pygame.display.set_mode((height, width))
pygame.display.set_caption("Davuk Nepzy : Diriliş")

davuk = pygame.image.load(os.path.join("Assets","davuk.png"))
background = pygame.image.load(os.path.join("Assets","indir.jpg"))
#border = pygame.Rect(height/2 - 5, 0, 10, width)


def draw(player):
     windows.fill(WHITE)
     windows.blit(davuk, (player.x, player.y))
     pygame.display.update()

def main():
    player = pygame.Rect(300, 100, 1, 1)
    clock = pygame.time.Clock() 
    run = True
    while run:
     clock.tick(fps)
     draw(player)
     keys_pressed = pygame.key.get_pressed()

     if keys_pressed[pygame.K_w] and player.y - -5 > 0:
         player.y += -5

     if keys_pressed[pygame.K_a] and player.x - -5 > 0:
         player.x += -5

     if keys_pressed[pygame.K_s] and player.y + -5 < height:
         player.y += 5

     if keys_pressed[pygame.K_d]:
         player.x += 5

     if keys_pressed[pygame.K_SPACE]:
        bullet = pygame.Rect(player.x + player.height, player.y + player.width/2, 10, 5)

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
           run = False
    
    pygame.quit()

main()