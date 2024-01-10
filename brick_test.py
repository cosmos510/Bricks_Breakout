from turtle import Turtle
import random

COLORS = ['yellow', 'green', 'orange', 'red']


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()

    def create_bricks(self):
        y = 200

        for color in COLORS:
            for row in range(2):
                x = -560
                y += 25
                while x < 600:
                    new_brick = Turtle("square")
                    new_brick.quantity = random.choice(range(1, 3))
                    new_brick.left_wall = self.xcor() - 30
                    new_brick.right_wall = self.xcor() + 30
                    new_brick.upper_wall = self.ycor() + 15
                    new_brick.bottom_wall = self.ycor() - 15
                    new_brick.penup()
                    new_brick.shapesize(stretch_wid=1, stretch_len=3)
                    new_brick.color(color)
                    new_brick.goto(x, y)
                    self.all_bricks.append(new_brick)
                    x += 65
