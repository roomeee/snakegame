import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=1000)
# Create the turtle
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  # Fastest speed
pattern_turtle.width(2)

# Define the pattern parameters
radius = 20  # Radius of the circles
num_circles = 36  # Number of circles in the pattern
num_layers = 6  # Number of layers in the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # Colors for each circle

# Draw the pattern
for layer in range(num_layers):
    color = random.choice(colors)
    pattern_turtle.color(color)
    for _ in range(num_circles):
        pattern_turtle.circle(radius)
        pattern_turtle.left(360 / num_circles)
    radius += 20

    # Move turtle to start a new layer
    pattern_turtle.penup()
    pattern_turtle.goto(0, -radius)
    pattern_turtle.pendown()

# Hide the turtle
pattern_turtle.hideturtle()

# Exit on click
wn.exitonclick()
