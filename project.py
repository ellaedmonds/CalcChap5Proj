'''
project.py
Katie Naughton and Ella Edmonds

eval, with x predefined
def square(x):
    return x*x
    result=square(5)
print(square(5))
'''
from math import sin,cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2

function=input("What function would you like to analyze? ")
x1=int(input("Where do you want your interval to start? "))
x2=int(input("Where do you want your interval to end? "))
#step = float(input("What do you want the step to be? "))

print(function)

# y values
ycoordlist1=[]
for r in range(x1, (x2+1)):
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
print(ycoordlist1)

ycoordlist2=[]
for r in range(x1, (x2+1)):
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
print(ycoordlist2)

intervalnum=len(ycoordlist1)
print(intervalnum)

# derivatives
derivlist=[]
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.01)
    derivlist.append(deriv)
print (derivlist)

# extrema

# increasing intervals

# decreasing intervals

# points of inflection

# concave up intervals

# concave down intervals


    





    
    
