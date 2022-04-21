import pygame

class Shape:
  def __init__(self, tampilan):
    self.tampilan = tampilan
    self.RED = (255, 0, 0)
    self.GREEN = (0, 255, 0)
    self.BLUE = (0, 0, 255)
    self.BLACK = (0, 0, 0)
  
  def kotak(self):
    pygame.draw.rect(self.tampilan, self.RED,  [55, 50, 20, 25])
    pygame.draw.rect(self.tampilan, self.GREEN,  [75, 70, 20, 25], 0)
    pygame.draw.rect(self.tampilan, self.BLUE,  [115, 110, 50, 25], 1)
    pygame.draw.rect(self.tampilan, self.BLACK,  [145, 140, 50, 25], 0, 20)
    pygame.draw.rect(self.tampilan, self.RED,  [205,200, 150, 125], 0, 20, 0, 0, 60, 0)
  
  def garis(self):
    pygame.draw.line(self.tampilan, self.RED, [0, 0], [100, 100], 5)
    pygame.draw.line(self.tampilan, self.GREEN, [0, 0], [70, 100], 5)
    pygame.draw.line(self.tampilan, self.BLUE, [0, 0], [50, 100], 5)
    pygame.draw.line(self.tampilan, self.BLACK, [0, 0], [30, 100], 5)
  
  def poligon(self):
    pass
  
  def lingkaran(self):
    pass
  
  def elips(self):
    pass
  
  def arcs(self):
    pass