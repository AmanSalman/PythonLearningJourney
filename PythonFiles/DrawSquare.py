import turtle

def drawSquare():
  window = turtle.Screen()
  window.bgcolor("red")

  p = turtle.Turtle()
  p.shape("turtle")
  p.color("yellow")

  p.forward(100)
  p.right(90)

  p.forward(100)
  p.right(90)

  p.forward(100)
  p.right(90)

  p.forward(100)
  p.right(90)

  window.exitonclick()

drawSquare()