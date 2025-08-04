from object1.point import Point
class Pen:
    def __init__(self,cp): #attributes mein woh cheezein likh hain jo ke user defne kareyga
        self.cp= cp
        self.position=Point(0,0)  #position and path dono defaukt set kiye hain or internally handle kiya hai isliyen usko uper attributes mein nahi likha  
        self.path=[]
    """ self.position=position
       #and main mein object create karenge then use it
       e.g: start=Point(5,5)
             pen=Pen(0,start)"""
    def moveto(self,point):
        self.position=point
        self.path.append((point.x,point.y))
    
    def lineto(self,point):
        self.path.append((self.position.x,self.position.y))
        self.position=point
        
    
    def display(self):
        print(self.path)