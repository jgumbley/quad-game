import sys
from pyglet import image, sprite, window, app, clock
from pyglet.gl import (
    glClearColor,
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
    sprite_sheet = no_anti_alias(image.load('quad.png'))

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



class Map(object):
    """
    Might as well hold the map in this.
    """

    TILE_SIZE=48

    rows = []

    def __init__(self, window, x, y):
        for j in range(10):
            self.rows.append ( [] )
            for i in range(14):
                self.rows[j].append(Grid(window, self.TILE_SIZE*i, 48*j))

    def draw(self):
        for row in self.rows:
            for sprite in row:
                sprite.draw()

    def on_mouse_press(self, x, y):
        self.rows[y/self.TILE_SIZE][x/self.TILE_SIZE].change()


class Grid(sprite.Sprite):
    """
    This is a class for Sand
    """
    sand_image = no_anti_alias(image.load("sand.bmp"))
    mark_image = no_anti_alias(image.load("sand2.bmp"))

    def __init__(self, window, x, y, batch=None):
        super(Grid, self).__init__(self.sand_image, x, y, batch=batch)
        self.scale = 3

    def change(self):
        self.image = self.mark_image


class GameWindow(window.Window):
    """
    This is the game window
    """
    def __init__(self):
        super(GameWindow, self).__init__()
        clock.schedule_interval(self.update, 1.0/60)
        
        self.quad_sprite = Quad(self, 100, 100, scale=3)
        self.game_map = Map(self, 0, 0)

        app.run()

    def update(self, dt):
        """
        This is to update the game, not the drawing of the game
        """
        self.quad_sprite.update(dt)

    def on_draw(self):
        glClearColor(1, 0.816, 0.451, 255)
        self.clear()
        self.game_map.draw()
        self.quad_sprite.draw()


    key_map = {
        window.key.UP       : Quad.UP,
        window.key.DOWN     : Quad.DOWN,
        window.key.LEFT     : Quad.LEFT,
        window.key.RIGHT    : Quad.RIGHT,
    }

    def on_key_press(self, symbol, modifiers):
        if symbol in self.key_map.keys():
            self.quad_sprite.move = self.key_map[symbol]


    def on_key_release(self, symbol, modifiers):
        self.quad_sprite.move = Quad.STOP


    def on_mouse_press(self, x, y, button, modifiers):
        self.game_map.on_mouse_press(x, y)


if __name__ == "__main__":
    sys.exit(GameWindow())
