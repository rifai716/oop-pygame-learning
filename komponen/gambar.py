import pygame

class Gambar:
  def __init__(self, tampilan):
    self.tampilan = tampilan
    self.background = pygame.image.load('assets/bg_saturnus.jpg')
    self.plane = pygame.image.load('assets/plane.jpg')
  
  def draw(self):
    self.tampilan.blit(self.background, [0, 0])
    self.tampilan.blit(self.plane, [350, 200])