# region Importing modules
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# endregion

# region Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# endregion

# region Snake game setup
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# endregion

# region Game loop
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.05)
	snake.move()

	# Detect collision with food
	if snake.head.distance(food) < 5:
		food.newLocation()
		scoreboard.addPoint()
		snake.extend()

	# Detect collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		food.newLocation()
		scoreboard.resetScore()
		snake.resetBody()

	# detect collision with tail
	for body_part in snake.body[1: -1]:
		if snake.head.distance(body_part) < 5:
			food.newLocation()
			scoreboard.resetScore()
			snake.resetBody()

# I have no idea why this is not working, but ALT + F4 still works :D
screen.exitonclick()
# endregion