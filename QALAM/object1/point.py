class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def set(self,x,y):
        self.x=x
        self.y=y
        
    def get(self):
        return(self.x,self.y)
    
    def display(self):
        print(self.x,self.y)
        
    def __str__(self):
        return f"({self.x},{self.y})"
        
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
          
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    def distance(self,other):
        return((self.x - other.x) **2 + (self.y - other.y) **2 )**0.5
    
    @classmethod
    def copy(cls,self,other_point):
        return(self.other_point.x,self.other_point.y)
    
    