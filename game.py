from pyglet import image, sprite, window, app


class Quad(sprite.Sprite):
    """
    This is a class for the Quad
    """
    sprite_sheet = image.load('quad.bmp')

    def __init__(self, window, x, y, scale=1):
        image_grid = image.ImageGrid(self.sprite_sheet, 1, 8)
        super(Quad, self).__init__(image_grid[1], x, y, batch=None)



game_window = window.Window()
quad_sprite = Quad(game_window, 0,0)


@game_window.event
def on_draw():
    game_window.clear()
    quad_sprite.draw()


if __name__ == "__main__":
    app.run()
