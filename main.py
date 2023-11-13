import random
from turtle import *

# TODO 1 Сделать плашку котороый мы будем управлять


STARTING_POSITION = [(0, -200), (-20, -200), (-40, -200), (-60, -200)]
MOVE_DISTANCE = 20
pong_segments = []
LEFT_BORDER = -285
RIGHT_BORDER = 285

def add_pong(position):
    pong = Turtle(shape="square")
    pong.penup()
    pong.color("white")
    pong.goto(position)
    return pong


def create_pong():
    global pong_segments
    for position in STARTING_POSITION:
        pong_segment = add_pong(position)
        pong_segments.append(pong_segment)
    return pong_segments


def move_pong_left():
    global pong_segments
    x_rightmost = pong_segments[3].xcor()
    if x_rightmost > LEFT_BORDER:
        for pong_segment in pong_segments:
            x = pong_segment.xcor()
            pong_segment.setx(x - MOVE_DISTANCE)
        screen.update()


def move_pong_right():
    global pong_segments
    x_leftmost = pong_segments[0].xcor()
    if x_leftmost < RIGHT_BORDER:
        for pong_segment in pong_segments:
            x = pong_segment.xcor()
            pong_segment.setx(x + MOVE_DISTANCE)
        screen.update()


screen = Screen()
screen.setup(width=630, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)
screen.listen()
screen.onkeypress(move_pong_left, "Left")
screen.onkeypress(move_pong_right, "Right")




# TODO 2 сделать блоки
COLORS =["red", "orange", "blue", "green", "gray", "yellow", "purple"]
all_blocks = []
x = -283
y = 150


def create_blocks():
    global x, y, all_blocks
    for block in range(50):
        blocks = Turtle(shape="square")
        blocks.penup()
        blocks.shapesize(stretch_len=3, stretch_wid=1)
        blocks.color(random.choice(COLORS))
        blocks.goto(x,y)
        x += 62
        if (block + 1) % 10 == 0:  # Если блок - последний в ряду, уменьшаем y на 20
            y += 28
            x = -283
        all_blocks.append(blocks)


# TODO 3 Сделать шарик
x_move = 2
y_move = 2
move_speed = 0.1


def create_ball():
    ball = Turtle(shape="circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, -180)
    return ball
# TODO 4 Настроить управление шариком


def move_ball(ball):
    global x_move, y_move, move_speed
    ball.setx(ball.xcor() + x_move)
    ball.sety(ball.ycor() + y_move)
    screen.update()


def check_border_collision():
    global x_move, y_move
    if ball.xcor() > RIGHT_BORDER or ball.xcor() < LEFT_BORDER:
        x_move *= -1


def check_pong_collision():
    global x_move, y_move
    for pong_segment in pong_segments:
        if pong_segment.distance(ball) < 15:  # Расстояние до Pong, подберите значение по вашему усмотрению
            y_move *= -1




# TODO 5 настроить разбивание блоков
def check_block_collision():
    global x_move, y_move, all_blocks
    for block in all_blocks:
        if ball.distance(block) < 20:  # Расстояние до блока, подберите значение по вашему усмотрению
            all_blocks.remove(block)
            # Определите направление отскока в зависимости от расположения блока относительно мяча
            if ball.ycor() > block.ycor():
                y_move = abs(y_move)  # Если шарик сверху, изменяем направление по y на противоположное
            else:
                y_move = -abs(y_move)  # Если шарик снизу, изменяем направление по y на противоположное

            if ball.xcor() > block.xcor():
                x_move = abs(x_move)  # Если шарик справа, изменяем направление по x на противоположное
            else:
                x_move = -abs(x_move)  # Если шарик слева, изменяем направление по x на противоположное
            block.hideturtle()  # Скрыть блок


create_pong()
create_blocks()
ball = create_ball()
game = True
while game:
    move_ball(ball)
    check_border_collision()
    check_pong_collision()
    check_block_collision()
    screen.update()
    if ball.ycor() < -300:
        game = False