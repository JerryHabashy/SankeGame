from turtle import Screen, Turtle

MOVE_DISTANCE = 20


class Snake:
	def __init__(self):
		self.body = []
		self.head = Turtle()
		self.createSnake()

	# add body part to snake
	def extend(self):
		self.addBody(self.body[-1].xcor(), self.body[-1].ycor())

	def addBody(self, pos_x, pos_y):
		turtle = Turtle("square")
		self.body.append(turtle)
		self.body[-1].color("white")
		self.body[-1].penup()
		self.body[-1].goto(pos_x, pos_y)

	def move(self):
		for body_num in range(len(self.body) - 1, 0, -1):
			new_x = self.body[body_num - 1].xcor()
			new_y = self.body[body_num - 1].ycor()
			self.body[body_num].goto(new_x, new_y)
		self.head.forward(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != 270:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() != 90:
			self.head.setheading(270)

	def left(self):
		if self.head.heading() != 0:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() != 180:
			self.head.setheading(0)

	def resetBody(self):
		for snake_part in self.body:
			snake_part.goto(2000, 2000)
		self.body.clear()
		self.createSnake()

	def createSnake(self):
		for i in range(3):
			self.addBody(i * -20, 0)
		self.head = self.body[0]

