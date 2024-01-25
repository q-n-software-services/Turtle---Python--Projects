import math
import random
import time
import turtle


# Set key parameters
gravity = -0.005  # pixels/(time of iteration)^2
y_velocity = 1  # pixels/(time of iteration)
x_velocity = 0.25  # pixels/(time of iteration)
energy_loss = 0.95

shot_on_target = 0

wn = turtle.Screen()
wn.setup(width =700, height =500)
wn.tracer(0)
wn.title("Q N Software Services")

stage = turtle.Turtle()


def draw_stage():
    stage.showturtle()
    stage.penup()
    stage.speed(100)
    stage.goto(-50, 200)
    stage.pendown()
    stage.pensize(72)
    stage.write("Basketball Game")
    stage.penup()
    stage.goto(-300, -100)
    stage.pensize(6)
    stage.pendown()
    stage.forward(600)
    stage.goto(250, -100)
    stage.left(90)
    stage.forward(200)
    stage.left(180)
    stage.forward(30)
    stage.right(90)
    stage.pensize(3)
    stage.forward(30)
    stage.back(2.5)
    stage.left(90)
    stage.forward(1.5)
    stage.color('yellow')
    stage.begin_fill()
    stage.forward(25)
    stage.left(90)
    stage.forward(20)
    stage.left(90)
    stage.forward(25)
    stage.end_fill()
    stage.penup()
    stage.home()
    stage.hideturtle()


draw_stage()

position = 10
position *= 29
player = turtle.Turtle()
player.speed(100)


def create_player(position):
    if position > 180:
        position = 180
    player.penup()
    player.pensize(24)
    player.goto(150, 150)
    player.pendown()
    player.write("Shots on Target :\t{}".format(shot_on_target))
    player.penup()
    player.goto(position, -100)
    player.pensize(5)
    player.pendown()
    player.forward(12)
    player.left(120)
    player.forward(24)
    player.left(120)
    player.forward(24)
    player.right(180)
    player.forward(24)
    player.left(30)
    player.forward(42)
    player.right(90)
    player.circle(12)
    player.right(90)
    player.forward(18)
    player.left(120)
    player.forward(18)
    x = player.xcor()
    y = player.ycor()
    player.left(180)
    player.forward(18)
    player.right(155)
    player.forward(24)
    player.penup()
    player.home()
    player.hideturtle()

    return x,y

ball = turtle.Turtle()
ball.speed(1)
ball.penup()
ball.color("orange")
ball.shape("circle")


play = True
while play:

    position = random.randint(-290, 290)

    x, y = create_player(position)

    ball.setx(x + 5)
    ball.sety(y + 5)
    wn.update()

    angle = int(input("Enter an angle between 0 and 90 for making a shot : \t"))
    while angle < 0 or angle > 90:
        angle = int(input("PLEASE Enter an angle between 0 and 90 for making a shot : \t"))
    angle = math.radians(angle)
    speed = int(input("Enter speed between 0 and 100 units/second for throwing the basketball : \t"))
    while speed < 0 or speed > 100:
        speed = int(input("PLEASE Enter speed between 0 and 100 units/second for throwing the basketball : \t"))

    x_distance = math.fabs(((speed * speed) * (math.cos(angle))) / (19.62 * (math.sin(angle))))
    y_distance = math.fabs(((speed * (math.sin(angle))) ** 2) / 19.62)
    x_velocity = math.fabs(speed * (math.cos(angle))) / 25
    y_velocity = math.fabs(speed * (math.sin(angle))) / 25

    time.sleep(5)
    reverted = False
    # Main loop
    while True:
        time.sleep(0.0000001)
        # Move ball
        ball.sety(ball.ycor() + y_velocity)
        ball.setx(ball.xcor() + x_velocity)

        # Bounce off the walls (left and right)
        if (ball.ycor() > (y + y_distance)) or (ball.xcor() > ((x_distance + x) / 2))and reverted == False:
            y_velocity = -y_velocity
            reverted = True

        wn.update()

        if 222 < ball.xcor() < 243:
            if 43 < ball.ycor() < 70:
                shot_on_target += 1

        if ball.xcor() > 300 or ball.ycor() < -90:
            break

    choice = input("Enter Y to continue playing and N to exit").upper()
    while choice != 'Y' and choice != 'N':
        choice = input("PLEASE Enter Y to continue playing and N to exit").upper()
    if choice == 'N':
        play = False
    print("\n\n\n")


    wn.update()

    player.reset()
    position = 0

