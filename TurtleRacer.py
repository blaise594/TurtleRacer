#Create two turtles and have them race across the screen from left to right.
#The turtle that goes the farthest is the winner.

import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)


#Set accumulator to begin at 0 for total distance traveled by lance
lanceTraveled=0
#Set accumulator to begin at 0 for total distance traveled by andy
andyTraveled=0
#Set loop to keep moving turtles and adding to accumulator until end of race (500px)
while lanceTraveled<=500 or andyTraveled<=500:
    #randomly decides how far lance moves each iteration of loop
    moveLance=random.randint(1, 2)
    #adds how far lance moved each iteration to lance's accumulator
    lanceTraveled+=moveLance
    #randomly decides how far andy moves each iteration of loop
    moveAndy=random.randint(1,2)
    #adds how far lance moved each iteration to lance's accumulator
    andyTraveled+=moveAndy
    #moves andy forward either 1 or 2 units forward depending on decision earlier in loop
    andy.forward(moveAndy)
    #moves lance forward either 1 or 2 units forward depending on decision earlier in loop
    lance.forward(moveLance)

wn.exitonclick()
