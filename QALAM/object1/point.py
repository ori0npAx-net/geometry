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
        
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
          
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    @classmethod
    def copy(cls,self,other_point):
        return(self.other_point.x,self.other_point.y)
    
    