from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark green")
screen.title("My Snake Game")
screen.tracer(0)
MIN_COR = -290
MAX_COR = 290

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
time1 = 0.1
while game_is_on:
    screen.update()
    time.sleep(time1)

    snake.move()

    #TODO: Collision with food
    if snake.head.distance(food) < 15:
        time1 -= 0.00005
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>MAX_COR or snake.head.xcor()<MIN_COR or snake.head.ycor()>MAX_COR or snake.head.ycor()<MIN_COR:
        scoreboard.reset()
        snake.reset()

    #TODO: DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()