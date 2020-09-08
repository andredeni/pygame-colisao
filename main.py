import pygame
import random
import sys

pygame.init()
window = pygame.display.set_mode([800, 580])
spaceship = pygame.image.load('spaceship.png')

imgX = 350
imgY = 400
speedX = 0
quadX = random.randrange(0, 700)
quadY = 0
speedQuad = 1

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speedX = -10
      if event.key == pygame.K_RIGHT:
        speedX = 10
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT
        or event.key == pygame.K_RIGHT):
          speedX = 0

  window.fill((255, 255, 255))
  window.blit(spaceship, [imgX, imgY])

  pygame.draw.rect(
    window, (0, 0, 0), [quadX, quadY, 100, 100]
  )

  imgX += speedX
  quadY += speedQuad

  if imgY < quadY + 100 and imgY + 128 > quadY:
    if imgX < quadX + 100 and imgX + 128 > quadX:
      sys.exit()

  if quadY > 580:
    quadY = 0
    quadX = random.randrange(0, 700)
    speedQuad += 1

  pygame.display.update()
  clock.tick(30)