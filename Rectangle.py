class point:  
    def __init__(self, pt):
        self.Xcord = Xcord
        self.Ycord = Ycord
        self.pt = (Xcord, Ycord)
   
   
 


class Rectangle(point):
    a = 0
    b = 0
    c = 0
    d = 0
    def __init__ (self, a,b,c,d,bottomLeftCorner, topRightCorner):
        x = point(bottomLeftCorner)
        y = point(topRightCorner) 
        x.pt =(a,b)
        y.pt = (c,d)

    def area(x,y)
  
