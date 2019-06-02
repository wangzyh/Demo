import turtle

distance = 100
turtle.left(90)
turtle.penup()
turtle.backward(150)
turtle.pendown()


def fractel(distance):
    if distance > 5:
        turtle.forward(distance)
        turtle.right(30)
        fractel(distance-15)

        turtle.left(60)
        fractel(distance-15)

        turtle.right(30)
        turtle.backward(distance)


if __name__ == '__main__':
    fractel(distance)
    turtle.exitonclick()
