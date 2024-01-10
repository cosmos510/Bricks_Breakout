import turtle as tr
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ui import UI
from brick_test import Bricks
import time

screen = tr.Screen()
screen.setup(width=1200, height=1000)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

ui = UI()
ui.header(game_on=False)

score = Scoreboard(lives=1)
bricks = Bricks()
bricks.create_bricks()
paddle = Paddle()
ball = Ball()

game_paused = True
playing_game = True


def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True


def play_again():
    screen.clear()
    exec(open("./main.py").read())


screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key='space', fun=pause_game)
screen.onkey(key='y', fun=play_again)


def check_collision_with_walls():
    global ball, score, playing_game, ui, game_paused

    # detect collision with left and right walls:
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    # detect collision with upper wall
    if ball.ycor() > 435:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    # detect collision with bottom wall
    if ball.ycor() < -440:
        ball.reset()
        score.decrease_lives()
        paddle.goto(0, -435)
        game_paused = True
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_collision_with_paddle():
    global ball, paddle
    # record x-axis coordinates of ball and paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    # check if ball's distance from paddle is less than width of paddle and ball
    if ball.distance(paddle) < 120 and ball.ycor() < -415:

        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collision_with_bricks():
    global ball, score, bricks

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity < 1:
                brick.hideturtle()
                bricks.all_bricks.remove(brick)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)


while playing_game:
    screen.update()
    ui.header(game_on=True)

    if not game_paused:

        time.sleep(0.01)
        ball.move()

        check_collision_with_walls()

        check_collision_with_paddle()

        check_collision_with_bricks()

        if len(bricks.all_bricks) == 0:
            ui.game_over(win=True)
            break

    else:
        ui.paused_status()

tr.mainloop()
