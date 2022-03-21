import turtle
import main
import os

scrn = turtle.Screen()
print("====== Setup ======")
x = input("What is your Turtle window name?\nAnswer: ")
os.system("clear")

print("====== Square ======")
print("I will draw a square as my first shape.")
y = input("How long should each side of the square be?\nAnswer: ")

main.drawSquare(x, y)
os.system("clear")

print("====== Semicircle ======")
print("I will now draw a semicircle as my second shape.")
x = input("What should the radius be?\nAnswer: ")

main.drawSemicircle(x)
os.system("clear")

print("====== Pentagon ======")
print("I will now draw a pentagon as my third and final shape.")
x = input("How long should each side of the pentagon be?\nAnswer: ")

main.drawRegPentagon(x)
os.system("clear")

print("====== Final Words ======")
print("Thank you for running my Turtle graphics lab!")

scrn.mainloop()