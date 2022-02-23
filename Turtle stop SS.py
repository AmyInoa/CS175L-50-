#Amy Inoa
#CS 175L
#Turtle Graphics STOP Sign

import math
import turtle

#Named Variables
Window_Width = 400
Window_Height = 400
Animation_Speed = 0
Num_sides = 8
Length = 100
Angle = 45
Text_X = -5
Text_Y = -10

turtle.color("black","red")

#how to make the stop sign
turtle.penup()
turtle.goto(-50,145)
turtle.pendown()
turtle.begin_fill()


for x in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.end_fill()

#font
turtle.color("white")
turtle.penup()
turtle.goto(0,0)
turtle.write("Stop", align = "center", font=("Calibri", 35, "bold"))
