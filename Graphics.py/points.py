from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    aPoint = Point(150,150)
    aPoint.draw(win)

    print( aPoint.getX())
    print(aPoint.getY())

    win.getMouse()
    win.close()

main()