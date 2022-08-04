from turtle import *

speed(10)

sides = int(input("Enter number of sides: "))

length = int(input("Enter the length: "))

color = input("Enter the color: ")

pencolor(color)

for i in range(sides):
    
    forward(length)

    lt(360/sides)

ht()

