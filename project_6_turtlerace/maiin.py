import turtle
import time
import random

WIDTH,HEIGHT = 600,700
# Constant list of 10 random colors
COLORS = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "black",
    "cyan",
]

def get_racers():
    while True:
        racers = input("Enter the number of turtles(1-10): ")
        if racers.isdigit():
            pass
            racers = int(racers)
            if racers > 11:
                print("Numbers of racers should be less than 10!\n")
            elif racers <= 1:
                print("There should be at least 2 racers!\n")
                
            else:
                break
        else:
            print("Enter the Valid number\n")
            continue
    return racers

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH/(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH/2 + (i+1) * spacingx,-HEIGHT/2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def innit_turtle(): # function for turtle window
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("\n...Turtle Racing....\n")


racers = get_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(racers)

innit_turtle()

# create_turtles(COLORS)

winner = race(colors)

print(f"The winner is {winner} turtle")
time.sleep(5)