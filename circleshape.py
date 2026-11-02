import pygame


# Base class for game objects. This code was provided by boot.dev
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass
# Till here  #

    def collides_with(self, asteroid: "CircleShape") -> bool:
        self.asteroid = asteroid
        r1 = self.radius
        r2 = asteroid.radius
        return self.position.distance_to(self.asteroid.position) < r1 + r2
        