from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.count()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        """is_on = False"""
        """score.game_over()"""
        score.reset()
        snake.reset()
        print("You hit the wall")

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            """is_on = False"""
            """score.game_over()"""
            score.reset()
            snake.reset()
            print("You hit the snake body")

screen.exitonclick()
