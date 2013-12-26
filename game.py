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

    STOP = 9
    UP = 2
    DOWN = 6
    LEFT = 4
    RIGHT = 0

    def __init__(self, window, x, y, scale=1):
        self.image_grid = image.ImageGrid(self.sprite_sheet, 1, 8)
        super(Quad, self).__init__(self.image_grid[5], x, y, batch=None)
        self.scale = scale
        self.px = x
        self.py = y
        self.move = self.STOP

    def update(self, dt):
        self.py = self.y
        self.px = self.x
        if (self.move == self.STOP):
            return
        elif (self.move == self.UP):
            self.y += 100 * dt
        elif (self.move == self.DOWN):
            self.y -= 100 * dt
        elif (self.move == self.LEFT):
            self.x -= 100 * dt
        elif (self.move == self.RIGHT):
            self.x += 100 * dt
        self.image = self.image_grid[self.move]


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

    def on_key_press(self, symbol, modifiers):
        if (symbol == window.key.UP):
            self.quad_sprite.move = Quad.UP
        elif (symbol == window.key.DOWN):
            self.quad_sprite.move = Quad.DOWN
        elif (symbol == window.key.LEFT):
            self.quad_sprite.move = Quad.LEFT
        elif (symbol == window.key.RIGHT):
            self.quad_sprite.move = Quad.RIGHT

    def on_key_release(self, symbol, modifiers):
        self.quad_sprite.move = Quad.STOP

if __name__ == "__main__":
    sys.exit(GameWindow())
