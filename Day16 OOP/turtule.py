# from turtle import Turtle , Screen


# timmy = Turtle()
# timmy.shape("turtle")
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["pikachu", "ss", "yy"])
table.add_column("Type", ["electric", "fire", "ice"])
table.align = "l"
print(table)

