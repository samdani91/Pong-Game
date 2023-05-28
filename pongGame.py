import turtle
import os


def start_game():
    # score
    score_a = 0
    score_b = 0

    # paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)  # animation speed
    paddle_a.shape("square")
    paddle_a.shapesize(5, 1)
    paddle_a.color("blue")
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)  # animation speed
    paddle_b.shape("square")
    paddle_b.shapesize(5, 1)
    paddle_b.color("red")
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)  # animation speed
    ball.shape("circle")
    ball.color("lime")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1 * 0.09
    ball.dy = 1 * 0.09

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A:0   Player B:0", align="center", font=("Courier", 20, "normal"))

    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    # Main game loop
    while True:
        wn.update()

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.xcor() >= 380:
            # ball.setx(390)
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(score_a, score_b), align="center",
                      font=("Courier", 20, "normal"))

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() <= -380:
            # ball.setx(-390)
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A:{}   Player B:{}".format(score_a, score_b), align="center",
                      font=("Courier", 20, "normal"))

        # Paddle and ball collisions

        if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            os.system("aplay bounce.wav&")

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            os.system("aplay bounce.wav&")


wn = turtle.Screen()
wn.bgcolor('black')
wn.title("pong game")
wn.setup(800, 600)
wn.tracer(0.001)
wn.bgpic("blue.gif")


# Wait for the Enter key press to start the game
def wait_for_enter():
    while True:
        if wn.textinput("", "Press Enter to start the game:") == "":
            break


wait_for_enter()
start_game()
