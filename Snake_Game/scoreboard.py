from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.highest_score = int(data.read())
        self.setposition(0, 275)
        self.pencolor('white')
        self.hideturtle()
        self.penup()

    def calculate_score(self):
        self.clear()
        self.score += 1
        return self.score

    def write_score(self):
        self.write(f'Score = {self.score}   Highest Score {self.highest_score}', False, 'center',
                   ('arial', 11, 'normal'))

    def game_over(self):
        self.pencolor('red')
        self.setposition(0, 0)
        self.write('GAME OVER', False, 'center', ('arial', 33, 'normal'))

    def high_score(self):
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(str(self.score))


