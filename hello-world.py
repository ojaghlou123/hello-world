import turtle
import colorsys
import time

your_name = "Ghoochali"

turtle_screen = turtle.Screen()
turtle_screen.title("Hello World Static")
turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()
turtle_writer.goto(0,0)
turtle_writer.write("Hello", align="center", font=("Arial", 24, "normal"))
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
        turtle.Screen().bgcolor(colors[(i + 3) % num_colors])  # Change background color
text = "Hello "
if your_name == "":
    text += "World"
else:
    text += your_name

draw_rainbow_text(turtle_writer, text)
time.sleep(2)
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

draw_rainbow_text(turtle_writer, text)
time.sleep(2)
turtle_writer.clear()

# Step 4: Motion Hello World filled with moving rainbow gradient
turtle_screen.title("Hello World Moving Rainbow Gradient")

width, height = 600, 200
turtle_screen.setup(width, height)
turtle_screen.bgcolor("black")
turtle_screen.tracer(0, 0)  # turn off animation for smooth update

turtle_writer.goto(-width//2 + 20, 0)
font_size = 48

def get_rainbow_colors(length):
    colors = []
    for i in range(length):
        hue = i / length
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)  # HSV to RGB
        colors.append((int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))
    return colors

length = len(text)
rainbow_colors = get_rainbow_colors(length)
pos_x = -width//2 + 20

while True:
    turtle_writer.clear()
    for i, char in enumerate(text):
        col = rainbow_colors[(i) % length]
        turtle_writer.color(col)
        turtle_writer.goto(pos_x + i * (font_size * 0.6), 0)
        turtle_writer.write(char, font=("Arial", font_size, "bold"))
    pos_x += 5
    if pos_x > width//2:
        pos_x = -width//2
    turtle_screen.update()
    time.sleep(0.1)