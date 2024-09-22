from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    aCircle = Circle(Point(150,150), 100)
    aCircle.draw(win)
    aCircle.setFill("blue")

    win.getMouse()
    win.close()

main()