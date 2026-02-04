from turtle import Turtle, Screen
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.x_inc = 0.125
        self.y_inc = 0.09375

    def move(self):
        x = self.xcor()
        y = self.ycor()
        x += self.x_inc
        y += self.y_inc
        self.goto(x, y)

    def bounce_y(self):
        self.y_inc *= -1

    def bounce_x(self):
        self.x_inc *= -1

    def reset_position(self):
        self.setposition(0, randint(-150, 150))
        self.bounce_x()
