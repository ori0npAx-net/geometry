from object1.point import Point
from object1.pen import Pen

p_1=Point(0,0)
p_2=Point(0,0)
p_1.set(1,2)
p_1.get()
p_2.set(4,5)
p_2.get()
p_1.display()
p_2.display()
A=p_1.__add__(p_2)
S=p_1.__sub__(p_2)
A.display()
S.display()
dollar=Pen(0)
dollar.moveto(A)
dollar.lineto(S)
dollar.display()


