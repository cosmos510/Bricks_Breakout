from turtle import Turtle

MOVE_DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('light blue')
        self.shape('square')
        self.penup()
        self.shapesize(1, 12)
        self.goto(x=0, y=-435)

    # Avoid the paddle to go off-screen
    def wall_checker(self):
        while self.xcor() > 520:
            self.backward(0.1)

        while self.xcor() < -520:
            self.forward(0.1)

    def move_left(self):
        self.wall_checker()
        self.backward(MOVE_DIST)

    def move_right(self):
        self.wall_checker()
        self.forward(MOVE_DIST)
