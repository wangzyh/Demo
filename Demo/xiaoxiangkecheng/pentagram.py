import turtle

distance = 20

for i in range(10):
    if i == 0:
        turtle.forward(distance/2)
    else:
        turtle.forward(distance + distance/2)
    for _ in range(4):
        # turtle.forward(distance)
        turtle.right(144)
        turtle.forward(distance)

    turtle.right(144)
    turtle.forward(distance/2)

    distance += 10

turtle.exitonclick()
