import sys
import random
from pyglet import image, sprite, window, app, clock
from pyglet.gl import (
    glTexParameteri,
    glBindTexture,
    GL_TEXTURE_MAG_FILTER,
    GL_NEAREST
)

def no_anti_alias(image):
    texture = image.get_texture()
    glBindTexture(texture.target, texture.id)
    glTexParameteri(texture.target, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glBindTexture(texture.target, 0)
    return texture


class Quad(sprite.Sprite):
    """
    This is a class for the Quad
    """
    sprite_sheet = no_anti_alias(image.load('quad.bmp'))

    def __init__(self, window, x, y, scale=1):
        image_grid = image.ImageGrid(self.sprite_sheet, 1, 8)
        super(Quad, self).__init__(image_grid[1], x, y, batch=None)
        self.scale = scale
        self.px = x
        self.py = y

    def update(self, dt):
        self.px = self.x
        self.py = self.y
        self.x += self.x * 0.1 * dt
        self.y += self.y * 0.1 * dt


class GameWindow(window.Window):
    """
    This is the game window
    """

    def __init__(self):
        super(GameWindow, self).__init__()
        clock.schedule_interval(self.update, 1.0/60)

        self.quad_sprite = Quad(self, 100, 100, scale=3)
        app.run()

    def update(self, dt):
        """
        This is to update the game, not the drawing of the game
        """
        self.quad_sprite.update(dt)

    def on_draw(self):
        self.clear()
        self.quad_sprite.draw()


if __name__ == "__main__":
    sys.exit(GameWindow())
