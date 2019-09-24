#python code to find distance between two points.

import math
x1=int(input("enter X1:"))
y1=int(input("enter Y1:"))
x2=int(input("enter X2:"))
y2=int(input("enter Y2:"))
distance=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
print("distance ({0},{1}) and ({2},{3}) is {4}".format(x1,x2,y1,y2,distance))
