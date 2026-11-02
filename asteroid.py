import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
  def __init__(self, x: float, y: float, radius: float) -> None:
      super().__init__(x, y, radius)
      self.x = x
      self.y = y
      self.radius = radius

  def draw(self, screen: pygame.Surface) -> None:
      pygame.draw.circle (
          screen,
          "white",
          self.position,
          self.radius,
          LINE_WIDTH
      )

  def update(self, dt: float) -> None:
      self.position += self.velocity * dt

  def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
          return
      log_event("asteroid_split")
      nangle = random.uniform(20, 50)
      split1 = self.velocity.rotate(nangle)
      split2 = self.velocity.rotate(-nangle)
      nradius = self.radius - ASTEROID_MIN_RADIUS
      a1 = Asteroid(self.position.x,self.position.y,nradius)
      a2 = Asteroid(self.position.x,self.position.y,nradius)
      a1.velocity = split1 * 1.2
      a2.velocity = split2 * 1.2


      
      