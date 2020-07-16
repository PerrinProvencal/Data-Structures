class point: 
    
    def __init__(self, pt):
        Xcord = 0
        Ycord = 0 
        self.pt = (Xcord, Ycord)
   


class Rectangle(point):
    a=0
    b=0
    c=0
    d=0


    def __init__ (self,a,b,c,d):
        bottomLeftCorner = ()
        topRightCorner = ()
        x = point(bottomLeftCorner)
        y = point(topRightCorner) 
        x.pt =(a,b)
        y.pt = (c,d)

    def area(self,x,y):
        ar = (y.pt[0] - x.pt[0]) * (y.pt[1]-x.pt[1])
        return ar

    def perimeter(self,x,y):
        per = 2*(y.pt[0] - x.pt[0]) + (y.pt[1]-x.pt[1])
        return per

r1 =  Rectangle(1,2,4,5)
x = point()
y=point()
print(r1.area(x,y))
print(r1.perimeter(x,y))
