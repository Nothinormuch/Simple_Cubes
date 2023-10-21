import math
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class line:
    def __init__(self,point1,point2,angle=None,c=None,m=None):
        if (point2.x-point1.x)!=0 and angle==None and c==None and m==None:
            self.slope=(point2.y-point1.y)/(point2.x-point1.x)
            self.intercept=point1.y-(self.slope*point1.x)
        elif point1.x==point2.x:
            self.slope = "infinite"
            self.intercept=point1.x
        else:
            if c==None and angle == 90:
                self.slope = "infinite"
                self.intercept=point1.x
            else:
                if m==None:
                    self.slope=math.tan(math.radians(angle))
                else:
                    self.slope=m
                self.intercept=c
                    
    def equation(line,point3):
        if line.slope=="infinite":
            return point3.x==line.intercept
        else:
            return point3.y==(((line.slope)*point3.x)+line.intercept)