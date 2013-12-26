import sys
from pyglet import image, sprite, window, app


class Quad(sprite.Sprite):
    """
    This is a class for the Quad
    """
    sprite_sheet = image.load('quad.bmp')


    def __init__(self, window, x, y, scale=1):
        image_grid = image.ImageGrid(self.sprite_sheet, 1, 8)
        super(Quad, self).__init__(image_grid[1], x, y, batch=None)


class GameWindow(window.Window):
    """
    This is the game window
    """

    def __init__(self):
        super(GameWindow, self).__init__()
        self.quad_sprite = Quad(self, 0, 0)
        app.run()


    def on_draw(self):
        self.clear()
        self.quad_sprite.draw()


if __name__ == "__main__":
    sys.exit(GameWindow())
