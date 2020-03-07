'''
Created on Mar 7, 2020

@author: ITAUser
'''
import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c = 0
x = 0

colors = ["orange","red","yellow","green","blue"]*6

    
while x < 2000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1.5
    c = c + 0.1
   
       

turtle.exitonclick()