# imports 
import turtle as trtl


#  Maze Configurations 
walls = trtl.Turtle() # initializing wall as a turtle. This will be the turtle that makes up the maze walls
walls.pensize(5) # set the thickness of the walls 
walls.hideturtle()
walls.speed(0) # this will speed up drawing the maze
wallLength = 15
wallCut = 25
barrier = 20

# Maze Runner Configurations
avatar = trtl.Turtle() # avatar that will run throughout the entire maze
avatar.setx(-30)
avatar.sety(0)
avatar.shape("turtle")
avatar.turtlesize(0.75)
avatar.color("blue")
avatar.pencolor("gray")


# functions for our avtar to go the direction the user wants the avatar to go 
def goDown():
    avatar.setheading(270)
    
def goUp():
    avatar.setheading(90)

def goRight():
    avatar.setheading(0)
    
def goLeft():
    avatar.setheading(180)

def move():
    avatar.forward(1)

# iteration that will draw out the actual maze. pu() will raise the turtle pen and not draw (in this case) the maze. pd() will put the pen back down and continue (in this case) drawing our maze.
for i in range (28): 
    walls.left(90)
    walls.forward(wallCut)
    walls.pu()
    walls.forward(wallCut)
    walls.pd()
    walls.left(90)
    walls.forward(barrier)
    walls.back(barrier)
    walls.right(90)
    walls.forward(wallLength)
    wallLength += 20
    

# config to display turtle
display = trtl.Screen()

# key presses for our avatar to go through the maze
display.onkeypress(goDown,'m')
display.onkeypress(goUp, 'i')
display.onkeypress(goRight, 'l')
display.onkeypress(goLeft,'j')
display.onkeypress(move, 'k')
display.listen()
display.mainloop()