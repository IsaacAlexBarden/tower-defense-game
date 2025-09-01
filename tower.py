"""Tower types module"""
import pygame

class Tower(pygame.sprite.Sprite):
    """
    Base class for towers in the game.
    
    Attributes
    ----------
        x, y : float
            Float position of the tower centre
        image : pygame.Surface
            The currently used tower image (can be rotated)
        rect : pygame.Rect
            The integer rect used for blitting and collisions
        direction : float
            Facing angle in degrees (0 = up, 180 = down), increases clockwise
    
    Methods
    -------
        rotate(angle: float) -> None
            Rotates the tower image by the given angle clockwise
    """
    def __init__(self, x: float, y: float, image: pygame.Surface):
        super().__init__()
        self.original_image: pygame.Surface = image  # Prevent blur from multiple rotations
        self.image: pygame.Surface = image
        self.rect: pygame.Rect = self.image.get_rect(center=(x, y))
        self.x: float = x
        self.y: float = y

        self.direction: float = 0  # 0 - 360, 0 indicates facing upwards

    def rotate(self, angle: float) -> None:
        """Rotate the tower by a given angle in the clockwise direction."""
        new_direction = (self.direction + angle) % 360
        self.image = pygame.transform.rotate(self.original_image, -new_direction)
        self.rect = self.image.get_rect(center=self.rect.center)

    def fire(self):
        pass