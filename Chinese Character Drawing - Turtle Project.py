import time
import turtle

me = turtle.Turtle()
me.pensize(29)


# drawing the basic square in the chinese character selected i.e. 25
def draw_square():
    me.penup()
    me.goto(-110, -10)
    me.pendown()
    me.forward(220)
    me.left(90)
    me.forward(150)
    me.left(90)
    me.forward(220)
    me.left(90)
    me.forward(150)


# drawing the horizontal line inside the square
def tieline():
    me.penup()
    me.goto(-75, 90)
    me.pendown()
    me.left(90)
    me.forward(152)


# drawing the hook seen on bottom left side of shape for character 25
def side_hook_left():
    me.penup()
    me.goto(-117, -50)
    me.right(110)
    me.pendown()
    me.forward(55)


# drawing the hook seen on bottom right side of shape for character 25
def side_hook_right():
    me.penup()
    me.goto(110, -50)
    me.left(50)
    me.pendown()
    me.forward(48)


# drawing the hook seen on center bottom of shape for character 25
def mid_hook():
    me.penup()
    me.goto(0, -38)
    me.pendown()
    me.forward(32)


# drawing the open-cup shaped design seen below the square in character 25
def bottom_design():
    me.penup()
    me.goto(-80, -45)
    me.right(30)
    me.pendown()
    me.forward(65)
    me.left(90)
    me.forward(140)
    me.left(75)
    me.forward(45)


# drawing the curved line and inclined line in center of square for character 25
def center_design():
    me.penup()
    me.home()

    me.goto(-70, 27)
    me.pendown()
    me.circle(75, 90)
    me.forward(6)

    me.penup()
    me.goto(0, 68)
    me.right(122)
    me.pendown()
    me.forward(84)


# calling all the functions sequentially to draw the chinese character assigned i.e. character 25
draw_square()
tieline()
side_hook_left()
side_hook_right()
mid_hook()
bottom_design()
center_design()

time.sleep(122)
