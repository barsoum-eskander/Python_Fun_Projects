from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.setposition(0, 220)
        self.pencolor('white')
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f'{self.l_score}         {self.r_score}', False, 'center', ('arial', 50, 'normal'))