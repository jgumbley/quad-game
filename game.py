from pyglet import image, sprite, window, app

quad = image.load('quad.bmp')
quad_animation = image.ImageGrid(quad, 1, 8)
quad_sprite = sprite.Sprite(quad_animation[1])

game_window = window.Window()


@game_window.event
def on_draw():
    game_window.clear()
    quad_sprite.draw()


if __name__ == "__main__":
    app.run()
