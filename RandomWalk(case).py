from math import sqrt
from random import *
import matplotlib.pyplot as plt

n = int(input("How many steps do you want?"))
x = x0 = 0
y = y0 = 0
xLst = [0] 
yLst = [0] 
sumDist = 0
for i in range(n):
    a=randrange(100)
    if a>=0 and a<20:
        y+=1
    elif a>=20 and a<50:
        y-=1
    elif a>=50 and a<95:
        x+=1
    else:
        x-=1
    xLst.append(x)
    yLst.append(y)
sumDist = sumDist + sqrt((x - x0)**2 + (y - y0)**2)

plt.plot(xLst, yLst,linestyle='dashdot')
plt.text(0,0,"start point (0,0)")
plt.text(x,y,"end point ("+str(x)+','+str(y)+')')
point1=[0,0]
point2=[x,y]
x_values=[point1[0],point2[0]]
y_values=[point1[1],point2[1]]
plt.plot(x_values,y_values,linestyle="--")
plt.text(x/2,y/2,"distance = "+str(sumDist),
         bbox = dict(facecolor = 'red', alpha = 0.5))
plt.title('random walks of an entity with '+str(n)+' steps')

numTests = int(input("How many test do you want?"))
sumDist = 0
for j in range(numTests):
    x = x0
    y = y0
    for i in range(n):
        a=randrange(100)
        if a>=0 and a<20:
            y+=1
        elif a>=20 and a<50:
            y-=1
        elif a>=50 and a<95:
            x+=1
        else:
            x-=1
    sumDist = sumDist + sqrt((x - x0)**2 + (y - y0)**2)
avgDist = sumDist/numTests
print("The average distance traveled from " + str(numTests) 
      + " random walks with " + str(n) + " steps is " 
      + str(avgDist))
print("Here is an example of a random walk path with " 
      + str(n) + " steps") 