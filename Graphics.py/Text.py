from Graphics import *

def main():
    win = GraphWin("win", 300,300)
    message = Text(Point(100,100), "Eng")
    message.draw(win)
    win.getMouse()
    win.close()

main()