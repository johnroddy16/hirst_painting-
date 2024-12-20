#!/usr/bin/env python3  

import random 
import turtle as t 

ben = t.Turtle()
ben.speed(0)
t.colormode(255)

color_list = [(231, 238, 233), (242, 233, 237), (186, 160, 139), (143, 166, 178), (148, 173, 156), (122, 94, 83), (183, 148, 158), (126, 81, 91), (81, 107, 125), (218, 202, 145), (86, 111, 96), (167, 105, 118), (174, 105, 95), (214, 178, 186), (175, 202, 186), (218, 180, 172), (102, 144, 116), (89, 142, 156), (143, 136, 98), (170, 200, 207), (114, 43, 54), (184, 189, 203), (117, 124, 146), (46, 54, 67), (62, 55, 50), (66, 51, 61), (97, 51, 46), (49, 61, 85), (50, 61, 57), (52, 71, 59), (69, 67, 52), (45, 70, 76)]

# we will create a dot painting using the colors in color_list 
# there should be 10 x 10 dots and each dot should be diameter 20 and 50 or so steps apart 
# 4 this we need to figure out how to create a colored dot and then move 50 paces straight ahead until we have 
# done that 10 times and then move 50 paces up and start from left of screen again 

ben.hideturtle() 
ben.penup() 
ben.setposition(-250, -250)
x, y = ben.position()
for i in range(100):
    if i != 0 and i % 10 == 0:
        y += 50
        ben.setposition(x, y)
    ben.dot(20, random.choice(color_list))
    ben.forward(50) 






screen = t.Screen()
screen.exitonclick() 
screen.title('hirst painting')