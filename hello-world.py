import turtle
import colorsys
import time

turtle_screen = turtle.Screen()
turtle_screen.title("Hello World Static")
turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.goto(0,0)
turtle_writer.write("Hello World", align="center", font=("Arial", 24, "normal"))
time.sleep(2)  # Pause to view
turtle_writer.clear()

def draw_rainbow_text(turtle_obj, text, font=("Arial", 48, "bold")):
    num_colors = 7
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle_obj.penup()
    turtle_obj.goto(-200, 0)
    for i, char in enumerate(text):
        turtle_obj.color(colors[i % num_colors])
        turtle_obj.write(char, font=font)
        turtle_obj.forward(30)

draw_rainbow_text(turtle_writer, "Hello World")
time.sleep(2)
turtle_writer.clear()