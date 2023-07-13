import turtle

wn = turtle.Screen()
wn.bgcolor("black")

spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest speed
spiral_turtle.color("white")
spiral_turtle.width(2)

start_radius = 1  # Starting radius
angle = 91  # Angle between each line segment
multiplier = 1.02  

# Draw the spiral
for i in range(400):
    spiral_turtle.forward(start_radius)
    spiral_turtle.left(angle)
    start_radius *= multiplier

spiral_turtle.hideturtle()

# Exit on click
wn.exitonclick()
