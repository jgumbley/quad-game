from pyglet import image, sprite, window, app

quad = image.load('quad.bmp')
quad_sprite = sprite.Sprite(quad)

game_window = window.Window()


@game_window.event
def on_draw():
    game_window.clear()
    quad_sprite.draw()


if __name__ == "__main__":
    app.run()
