#!/bin/python3

import turtle
import random
elsa = turtle.Turtle()

turtle.Screen().bgcolor("grey")
kleuren = ["cyan", "purple", "white", "blue"]

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

def zijtak():
  for i in range(3):
    for i in range(3):
      elsa.forward(30)
      elsa.backward(30)
      elsa.right(45)
    elsa.left(90)
    elsa.backward(30)
    elsa.left(45)
  elsa.right(90)
  elsa.forward(90)

for i in range(8):
    zijtak()
    elsa.left(45)

# elsa.color(random.choice(kleuren))