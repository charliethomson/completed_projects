import pyglet

from puck import Puck
from paddle import Paddle
from pyglet.window import key, mouse, Window

window = Window(width=1000, height=1000, resizable=True)
keys = key.KeyStateHandler()
puck = Puck(window)
player1 = Paddle(window, left=True)
player2 = Paddle(window, left=False)
players = player1, player2


def update(dt):
    window.clear()

    player1.draw()
    player1.update()
    player1.keep_in_bounds()

    player2.draw()
    player2.update()
    player2.keep_in_bounds()

    [puck.check_collision(player) for player in players]
    puck.draw()
    puck.update()

    player1.score = pyglet.text.Label(text=str(puck.get_score('player1')),
                                      font_name='Times New Roman', font_size=40,
                                      x=15, y=window.height-40)
    player2.score = pyglet.text.Label(text=str(puck.get_score('player2')),
                                      font_name='Times New Roman', font_size=40,
                                      x=window.width - 35, y=window.height-40)


    player1.score.draw()
    player2.score.draw()

@window.event
def on_key_press(k, mod):
    if keys[key.W]:    player1.move( 8)
    if keys[key.S]:    player1.move(-8)
    if keys[key.UP]:   player2.move( 8)
    if keys[key.DOWN]: player2.move(-8)

@window.event
def on_key_release(k, mod):
    if k == key.W or k == key.S: player1.move(0)
    if k == key.DOWN or k == key.UP: player2.move(0)

pyglet.clock.schedule_interval(update, 1/120.0)
if __name__ == "__main__":
    window.push_handlers(keys)
    pyglet.app.run()
