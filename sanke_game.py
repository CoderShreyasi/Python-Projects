import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Function to create a window screen
def create_screen():
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("blue")
    wn.setup(width=600, height=600)
    wn.tracer(0)
    return wn

# Function to create the snake head
def create_head():
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"
    return head

# Function to create the food
def create_food():
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)
    return food

# Function to create the pen for scoring
def create_pen():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))
    return pen

# Functions to move the snake
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Check for collisions with the screen borders
def check_border_collisions():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        handle_collision()

# Function to handle collisions
def handle_collision():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"
    colors = random.choice(['red', 'blue', 'green'])
    shapes = random.choice(['square', 'circle'])
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    global score
    score = 0
    global delay
    delay = 0.1
    pen.clear()
    pen.write("Score : {} High Score : {} ".format(score, high_score),
              align="center", font=("candara", 24, "bold"))

# Function to check for collisions with the food
def check_food_collision():
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        global delay
        delay -= 0.001
        global score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score),
                  align="center", font=("candara", 24, "bold"))

# Function to move the snake segments
def move_segments():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

# Function to check for collisions with the snake's own body
def check_body_collision():
    for segment in segments:
        if segment.distance(head) < 20:
            handle_collision()

# Main Gameplay
wn = create_screen()
head = create_head()
food = create_food()
pen = create_pen()

wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

segments = []

while True:
    wn.update()
    check_border_collisions()
    check_food_collision()
    move_segments()
    check_body_collision()
    move()
    time.sleep(delay)

wn.mainloop()
