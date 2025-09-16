from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90
radius = 255
center_x, center_y = 400, 345

while True:

    # 우하단 이동 
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

    # 우상단 이동
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

    # 좌상단 이동
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)

    # 좌하단 이동
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)

    # 중앙복귀
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)


    # 원운동 
    for degree in range(270, -90, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)

        rad = degree / 360 * 2 * math.pi
        cx = center_x + radius * math.cos(rad)
        cy = center_y + radius * math.sin(rad)
        character.draw_now(cx, cy)
        delay(0.01)