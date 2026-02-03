from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        x = 0
        for _ in range(3):
            new_turtle = Turtle('square')
            new_turtle.color('green')
            new_turtle.penup()
            new_turtle.speed('slow')
            new_turtle.setposition(x, 0)
            x -= 20
            self.turtles.append(new_turtle)

    def extend_snake(self):

        new_turtle = Turtle('square')
        new_turtle.color('green')
        new_turtle.penup()
        new_turtle.speed('slow')
        new_turtle.setposition(self.turtles[-1].position())
        self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.turtles[0].fd(20)

    # it was tempting to do it like this but angela's way make the code shorter
    # def up(self):
    #     if self.turtles[0].heading() == 270:
    #         self.turtles[0].setheading(270)
    #     else:
    #         self.turtles[0].setheading(90)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
