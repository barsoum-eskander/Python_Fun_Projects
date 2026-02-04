from turtle import Turtle


class Paddle (Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_(x, y)

    def create_(self, x, y):
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x, y)
        self.showturtle()

    def up(self):
        self.setposition(x=self.xcor(), y=self.ycor() + 20)
        if self.ycor() >= 250:
            self.setposition(x=self.xcor(), y=250)

    def down(self):
        self.setposition(x=self.xcor(), y=self.ycor() - 20)
        if self.ycor() <= -250:
            self.setposition(x=self.xcor(), y=-250)
