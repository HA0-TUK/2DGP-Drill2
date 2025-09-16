
from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

# 시작점 (왼쪽 아래)
x, y = 0, 90

# 오른쪽으로 이동 (아래 변)
while x < 800:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x += 2
    delay(0.01)

# 위로 이동 (오른쪽 변)
while y < 600:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y += 2
    delay(0.01)

# 왼쪽으로 이동 (위 변)
while x > 0:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x -= 2
    delay(0.01)

# 아래로 이동 (왼쪽 변)
while y > 90:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y -= 2
    delay(0.01)

close_canvas()