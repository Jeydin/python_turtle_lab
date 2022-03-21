# Jeydin Pham
# 3/21/2022
# 4th Period

import turtle

def drawSquare(aTurtle, length):
  aTurtle = turtle.Turtle()
  lenght = int(length)

  for x in range(0, 4):
    aTurtle.forward(lenght)
    aTurtle.right(90)
  input("I drew the square! Press Enter to continue")
  aTurtle.reset()

def drawSemicircle(radius):
  aTurtle = turtle.Turtle()
  radius = int(radius)

  aTurtle.circle(radius, 180)
  input("I drew the semicircle! Press Enter to continue")
  aTurtle.reset()

def drawRegPentagon(length):
  length = int(length)
  aTurtle = turtle.Turtle()

  aTurtle.setheading(0)
  for x in range(0,5):
    aTurtle.forward(length)
    aTurtle.left(72)
  input("I drew the pentagon! Press Enter to continue")
  aTurtle.reset()