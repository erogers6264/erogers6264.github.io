#!/usr/bin/python3

import turtle

window = turtle.Screen()
# window.bgcolor("black")
window.title = "Serpenski Triangle"

# sherry = turtle.Turtle

skk = turtle.Turtle()
skk.speed(0)

for j in range(45):
	for i in range(4): 
	    skk.forward(200) 
	    skk.right(90) 
	skk.right(10)
      
turtle.done() 