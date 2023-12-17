import turtle

# Function to create a paddle
def create_paddle(x, y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("black")
    paddle.shapesize(stretch_wid=6, stretch_len=2)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

# Function to create the ball
def create_ball():
    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = -5
    return ball

# Function to update the score
def update_score():
    score_display.clear()
    score_display.write("Left Player: {} Right Player: {}".format(left_player, right_player),
                        align="center", font=("Courier", 24, "normal"))

# Function to move the left paddle up
def paddleaup():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Function to move the left paddle down
def paddleadown():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Function to move the right paddle up
def paddlebup():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Function to move the right paddle down
def paddlebdown():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Main code
# Create screen
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("white")
screen.setup(width=1000, height=600)

# Create paddles and ball
left_paddle = create_paddle(-400, 0)
right_paddle = create_paddle(400, 0)
ball = create_ball()

# Initialize the score
left_player = 0
right_player = 0

# Create a turtle for score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("blue")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
update_score()

# Keyboard bindings
screen.listen()
screen.onkeypress(paddleaup, "e")
screen.onkeypress(paddleadown, "x")
screen.onkeypress(paddlebup, "Up")
screen.onkeypress(paddlebdown, "Down")

# Game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check borders
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.dy *= -1

    # Check if the ball passes the paddles
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        update_score()

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        update_score()

    # Paddle-ball collision
    if (360 > ball.xcor() > 350 and
        right_paddle.ycor() + 40 > ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(350)
        ball.dx *= -1

    if (-360 < ball.xcor() < -350 and
        left_paddle.ycor() + 40 > ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-350)
        ball.dx *= -1
