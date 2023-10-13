from operator import le
from snake_game_utils import *
from time import sleep


score = 0
main_surface = make_screen("snake Game",
                           "black", 600, 600)


snake_head = make_turtle("square", "blue")
snake_head.direction = ""

snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

score_board = make_turtle()
score_board.goto(0, 260)
score_board.write(f"Score: {score}", align="center", font=("Termina", 22))
score_board.hideturtle()
main_surface.listen()
main_surface.onkeypress(lambda: go_up(snake_head), "Up")
main_surface.onkeypress(lambda: go_down(snake_head), "Down")
main_surface.onkeypress(lambda: go_left(snake_head), "Left")
main_surface.onkeypress(lambda: go_right(snake_head), "Right")
running = True
snake_bodies = []
while running:
    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
        new_tail = make_turtle("square", "cyan")
        snake_bodies.append(new_tail)

    for i in range(len(snake_bodies) - 1, 0, -1):
        x = snake_bodies[i-1].xcor()
        y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(x, y)

    if len(snake_bodies):
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_bodies[0].goto(x, y)

    if snake_head.xcor() > 290 or\
            snake_head.xcor() < -290 or\
            snake_head.ycor() > 290 or \
            snake_head.ycor() < -290:

        reset(snake_head, snake_bodies)

    move_snake(snake_head)

    for body in snake_bodies:
        if snake_head.distance(body) < 20:
            reset(snake_head, snake_bodies)

    sleep(0.2)
