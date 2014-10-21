#!/usr/bin/python

import turtle

pen=turtle.Pen()
pen.speed(0)
size=pen.window_height()/8

squares_per_side=8

left_edge=-pen.window_width()//2
bottom_edge=-pen.window_height()//2

for y in range(8):
    
    pen.up()
    pen.setposition(left_edge,bottom_edge+y*size)
    pen.down()
    
    for x in range(8):
    
        if x%2==0:
            if y%2==0:
                pen.fillcolor("red")
            else:
                pen.fillcolor("black")
        else:
            if y%2==0:
                pen.fillcolor("black")
            else:
                pen.fillcolor("red")
    
        pen.begin_fill()
        
        for side in range(4):
            pen.forward(size)
            pen.left(90)
        
        pen.end_fill()
        pen.up()
        pen.forward(size)
        pen.down()
