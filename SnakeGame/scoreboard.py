from turtle import Turtle
import os 

FONT = ("New Times Roman", 16, "bold")
HIGH_SCORE_FILE = os.path.join(os.path.dirname(__file__), "highScore.txt")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.goto(0, 260)
		self.score = 0
		with open(HIGH_SCORE_FILE) as hs_file:
			self.high_score = int(hs_file.read())
		self.pencolor("white")
		self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=FONT)

	def addPoint(self):
		self.score += 1
		self.updateScoreboard()

	def resetScore(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open(HIGH_SCORE_FILE, mode="w") as hs_file:
				hs_file.write(f"{self.high_score}")
		self.score = 0
		self.updateScoreboard()

	def updateScoreboard(self):
		self.clear()
		self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=FONT)


