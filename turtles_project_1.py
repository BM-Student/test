import turtle
import numpy as np

def draw_lines(l,n):
    turtle.screensize(canvwidth=400, canvheight=400, bg="#336633")
    turtle.pen(pencolor="#FFFFCC", pensize=1.5)
    turtle.turtlesize(0.1, 0.1, 0.1)

    x_axis_pos = np.arange(l,l*(n+1),l)
    x_axis_neg = -1*x_axis_pos.copy()

    y_axis_pos = x_axis_pos.copy()
    y_axis_neg = x_axis_neg.copy()

    # x-pos y-neg lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_pos[n-1-i],0)
        turtle.pendown()
        turtle.goto(0,y_axis_neg[i])

    # x-neg y-neg lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_neg[n-1-i],0)
        turtle.pendown()
        turtle.goto(0,y_axis_neg[i])

    # x-neg y-pos lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_neg[n-1-i],0)
        turtle.pendown()
        turtle.goto(0,y_axis_pos[i])

    # x-pos y-pos lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_pos[n-1-i], 0)
        turtle.pendown()
        turtle.goto(0, y_axis_pos[i])

# Draw a circle with only lines
def draw_circle_with_lines(l,n):
    turtle.screensize(canvwidth=400, canvheight=400, bg="#336633")
    turtle.pen(pencolor="#FFFFCC", pensize=1.5)
    turtle.turtlesize(0.1, 0.1, 0.1)

    x_axis_pos = np.arange(l,l*(n+1),l)
    x_axis_neg = -1*x_axis_pos.copy()

    y_axis_pos = x_axis_pos.copy()
    y_axis_neg = x_axis_neg.copy()

    axis_length = l*n

    # x-pos y-neg lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_pos[n-1-i]-axis_length, axis_length)
        turtle.pendown()
        turtle.goto(-axis_length, y_axis_neg[i]+axis_length)

    # x-neg y-neg lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_neg[n-1-i]+axis_length, axis_length)
        turtle.pendown()
        turtle.goto(axis_length, y_axis_neg[i]+axis_length)

    # x-neg y-pos lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_neg[n-1-i]+axis_length, -axis_length)
        turtle.pendown()
        turtle.goto(axis_length, y_axis_pos[i]-axis_length)

    # x-pos y-pos lines
    for i in range(len(x_axis_pos)):
        turtle.penup()
        turtle.goto(x_axis_pos[n-1-i]-axis_length, -axis_length)
        turtle.pendown()
        turtle.goto(-axis_length, y_axis_pos[i]-axis_length)

running = True
while running:
    draw_circle_with_lines(30, 10)
    draw_lines(30, 10)
    stop = input('Press any button to stop')
    if len(stop) >= 0:
        running = False