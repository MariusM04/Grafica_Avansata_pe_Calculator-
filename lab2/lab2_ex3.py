from graphics import * 
def main():
    win = GraphWin('My Graphics', 300, 250)           # fereastra de 300 x 250 pixeli
    g   = Rectangle(Point(25,25), Point(75,75))       # patrat de 100 x 100 pixeli
    g.setFill('green')                                # primul patrat este verde
    g1   = Rectangle(Point(75,75), Point(125,125))    # patrat de 70 x 70 pixeli
    g1.setFill('red')                                 # al doilea patrat este rosu
    g2   = Rectangle(Point(25,75), Point(75,125))     # patrat de 50 x 50 pixeli
    g2.setFill('cyan')                                # al treilea patrat este albastru deschis
    g.draw(win)     
    g1.draw(win)                        
    g2.draw(win)
    win.getMouse()
    win.close()
main()
