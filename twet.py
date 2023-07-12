import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create the turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest speed
spiral_turtle.color("white")
spiral_turtle.width(2)

# Define the parameters for the spiral
start_radius = 1  # Starting radius
angle = 91  # Angle between each line segment
multiplier = 1.02  # Increase in radius with each line segment

# Draw the spiral
for i in range(400):
    spiral_turtle.forward(start_radius)
    spiral_turtle.left(angle)
    start_radius *= multiplier

# Hide the turtle
spiral_turtle.hideturtle()

# Exit on click
wn.exitonclick()
