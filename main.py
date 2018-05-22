import pygame
import ctypes

user32 = ctypes.windll.user32
background_colour = (0,0,0)#red, Green, Blue

screen = pygame.display.set_mode((user32.GetSystemMetrics(0)-100, user32.GetSystemMetrics(1)-100))

pygame.display.set_caption('Space-Game')

screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
