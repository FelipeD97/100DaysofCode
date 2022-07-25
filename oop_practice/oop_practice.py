# from turtle import Turtle, Screen


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("darkolivegreen")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

characters = ["Iron Man", "Superman", "Starfire", "Scarlet Witch"]
teams = ["Avengers, Illuminati", "Justice League", "Teen Titans", "Avengers"]


table = PrettyTable()
table.add_column("Character Name", characters)
table.add_column("Team", teams)
table.align = "l"

print(table)
