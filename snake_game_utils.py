from turtle import Screen, Turtle
from random import randint


def make_screen(title, color, w, h):
    main_surface = Screen()
    main_surface.title(title)
    main_surface.bgcolor(color)
    main_surface.setup(width=w, height=h)
    main_surface.tracer(False)
    return main_surface


def make_turtle(tshape="square", tcolor="white"):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_food_position(snake_food):
    x = randint(-270, 270)
    y = randint(-270, 270)
    snake_food.goto(x, y)


def go_up(snake_head):
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down(snake_head):
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left(snake_head):
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right(snake_head):
    if snake_head.direction != "left":
        snake_head.direction = "right"


def move_snake(snake_head):
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)
    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)
    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)
    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)


def reset(head, bodies):
    head.goto(0, 0)
    head.direction = ""
    for body in bodies:
        body.hideturtle()

    bodies.clear()
