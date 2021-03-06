'''
Created on Mar 7, 2020

@author: ITAUser
'''
#PSEUDOCODE:
#import turtle
import turtle

#create function 
def drawing:
turtle.setup(width=600, height=500)
turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor('black')

# create variable x and c with zero value
c = 0
x = 0

# write color for color control. 
#By writing it in a string the colors changes 
# multiplying it by a number tells how many times the colors changes 
colors = ["orange","red","yellow","green","blue"]*6

#write loop to give directions  
# use forward, right, and left to give directions 
#add values to variables 
while x < 2000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1.5
    c = c + 0.1
   
# create a way to stop drawing
turtle.exitonclick()

