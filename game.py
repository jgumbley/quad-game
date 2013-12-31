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

    STOP = 7
    UP = 2
    DOWN = 6
    LEFT = 4
    RIGHT = 0

    SPEED = 6

    def __init__(self, window, x, y, scale=1):
        self.image_grid = image.ImageGrid(self.sprite_sheet, 1, 8)
        tile_x = x*48
        tile_y = y*48
        super(Quad, self).__init__(self.image_grid[5], tile_x, tile_y, batch=None)
        self.scale = scale
        self.mx = tile_x
        self.my = tile_y 
        self.move = self.UP

    def update(self, dt):
        self.move = self.STOP
        if (self.x < self.mx):
            self.x += self.SPEED
            self.move = self.RIGHT
        elif (self.y < self.my):
            self.y += self.SPEED
            self.move = self.UP
        elif (self.x > self.mx):
            self.x -= self.SPEED
            self.move = self.LEFT
        elif (self.y > self.my):
            self.y -= self.SPEED
            self.move = self.DOWN
        self.image = self.image_grid[self.move]


    def on_mouse_press(self, x, y):
        if (self.x < x):
            self.move_to(x, y)
        elif (self.y < self.my):
            self.y += self.SPEED * dt
            self.move = self.UP
 
        self.move_to(x, y)

    def move_to(self, mx, my):
        self.mx = mx*48
        self.my = my*48


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
        self.rows[y][x].change()


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
    TILE_SIZE = 48

    updates = 0
    draws = 0

    def __init__(self):
        super(GameWindow, self).__init__()
        clock.schedule_interval(self.on_update, 1.0/60)
        
        self.quad_sprite = Quad(self, 1, 1, scale=3)
        self.game_map = Map(self, 0, 0)

        app.run()

    def on_update(self, dt):
        """
        This is to update the game, not the drawing of the game
        """
#        for i in range(1000000):
#            a = 23 / 1000
        self.quad_sprite.update(dt)
        self.updates+=1
        print "updates: %s draws: %s" % (self.updates, self.draws)

    def on_draw(self):
        glClearColor(1, 0.816, 0.451, 255)
        self.clear()
        self.game_map.draw()
        self.quad_sprite.draw()
        self.draws += 1

    def on_mouse_press(self, x, y, button, modifiers):
        tile_y = y/self.TILE_SIZE
        tile_x = x/self.TILE_SIZE
        #self.game_map.on_mouse_press(tile_x, tile_y)
        self.quad_sprite.on_mouse_press(tile_x, tile_y)


if __name__ == "__main__":
    sys.exit(GameWindow())
