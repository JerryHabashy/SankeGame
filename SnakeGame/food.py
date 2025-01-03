from turtle import Turtle
import random as r


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(0.5, 0.5)
		self.color("yellow")
		self.speed(0)
		self.newLocation()

	def newLocation(self):
		random_x = r.randint(-14, 14) * 20
		random_y = r.randint(-14, 14) * 20
		self.goto(random_x, random_y)

