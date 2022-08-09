# Python 3 Pong
import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A  0  -  0  Player B", align="center", font=("Courier", 24, "normal"))

# Scores
score_player_a = 0
score_player_b = 0


# Functions
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


def update_display_score():
    pen.clear()
    pen.write(f"Player A  {score_player_a}  -  {score_player_b}  Player B", align="center",
              font=("Courier", 24, "normal"))


# Keyboard controls binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "i")
window.onkeypress(paddle_b_down, "k")

# Main Loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_player_a += 1
        update_display_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_player_b += 1
        update_display_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collisions
    collision_paddle_a = ball.xcor() < -340 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50)
    collision_paddle_b = ball.xcor() > 340 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50)

    if collision_paddle_a or collision_paddle_b:
        ball.dx *= -1
