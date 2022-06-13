import turtle
import pandas as pd

data = pd.read_csv("canada_data.csv")

# ------------------------------------------ Creating objects
screen = turtle.Screen()
screen.title("Name all US States")
screen.setup(width=600,height=600)
image = "blankcanada.gif"
screen.addshape(image)
turtle.shape(image)


pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()

score = 0
FONT = ("arial",12,"bold")
while True:

    user_guess = screen.textinput(f"Name provinces in Canada {score}/13",prompt=" Full name or abbreviation")
    # Check if the guess is abbreviation
    if len(user_guess) == 2:
        match = data[data.code == user_guess.upper()]
        if not match.empty:
            pointer.goto(float(match.x), float(match.y))
            pointer.write(arg=f"{match.name.item()}\n {match.code.item()}",font=FONT,align="center")
            score += 1
            continue

    match = data[data.name == user_guess]
    if not match.empty:
        pointer.goto(float(match.x), float(match.y))
        pointer.write(arg=f"{match.name.item()}\n {match.code.item()}", font=FONT, align="center")
        score += 1



screen.exitonclick()