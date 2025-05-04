import time
from turtle import Screen

from Food import food
from Scoreboard import Scoreboard
from Snake import Snake

score_board = Scoreboard()

snake = Snake()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Snake game")
screen.tracer(0)

snake_food = food()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    for segment in snake.turtle_list[1:]:
        if snake.turtle_list[0].distance(segment) < 10:
            score_board.update_score()
            score_board.reset()
            snake.snake_reset()
    if snake.turtle_list[0].distance(snake_food) < 15:
        snake.extend()
        snake_food.refresh_location()
        score_board.increase_score()
        score_board.update_score()
    elif snake.turtle_list[0].xcor() > 310 or snake.turtle_list[0].xcor() < -310 or snake.turtle_list[0].ycor() > 310 or \
            snake.turtle_list[0].ycor() < -310:
        score_board.update_score()
        score_board.reset()
        snake.snake_reset()
screen.exitonclick()
