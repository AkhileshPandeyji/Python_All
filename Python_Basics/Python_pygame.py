import pygame


game_display = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello")
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(60)
pygame.draw.circle(game_display,(255,0,0),[200,200],50)
pygame.display.update()
help(pygame)
game_display.fill((255,255,255))
