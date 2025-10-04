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