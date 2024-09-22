from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    aG = Polygon(Point(50,50), Point(50,200), Point(300,50))
    aG.draw(win)


    win.getMouse()
    win.close()

main()