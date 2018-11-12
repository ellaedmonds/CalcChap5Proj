'''
project.py
Katie Naughton and Ella Edmonds

eval, with x predefined
def square(x):
    return x*x
    result=square(5)
print(square(5))

TO DO: 
have figure out how to tell if extrema is abs/local or max/min
have to figure our when decreasing or increasing interval is a union
'''
from math import sin,cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2

#inputs
function=input("What function would you like to analyze? ")
x1=int(input("Where do you want your interval to start? "))
x2=int(input("Where do you want your interval to end? "))
#step = float(input("What do you want the step to be? "))

#function
print(function)

#x values
xcoordlist=[]                               #x values
for i in range(x1,x2+1):
    if i == x2:
        xcoordlist.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            xcoordlist.append(i+m)
print(xcoordlist)
    
# y values
ycoordlist=[]                               # y values
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
print(ycoordlist)

ycoordlist1=[]                              #this will find the a+.001 for the dq
for r in xcoordlist:
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
print(ycoordlist1)

ycoordlist2=[]                              #this will find the a+.001 for the sdq
for r in xcoordlist:
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
print(ycoordlist2)

intervalnum=len(ycoordlist1)                #this tells us how long our cordinate lists are 
print(intervalnum)                              #so we know how long to run the loop

# derivatives
derivlist=[]                                #here we will make a list of the derivatives
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.01)
    derivlist.append(deriv)
print (derivlist)

#deriv/x value/y value zip
xyderivzip=list(zip(xcoordlist, ycoordlist, derivlist))
print(xyderivzip)

# extrema
extremalist=[]
for d in xyderivzip:
   if d[2]==0:
    extremalist.append((d[0], d[1]))
print (extremalist)

# increasing interval(s)
increasinglist=[]
for d in xyderivzip:
    if d[2]>=0:
        increasinglist.append(d[0])
print (increasinglist)
lengthincreasing=len(increasinglist)
print(lengthincreasing)
#print('Your function is increasing from' increasinglist[0] 'to' increasinglist[lengthincreasing])

#decreasing interval(s)
decreasinglist=[]
for d in xyderivzip:
    if d[2]<=0:
        decreasinglist.append(d[0])
print (decreasinglist)
lengthdecreasing=len(decreasinglist)
#print('Your function is decreasing from' decreasinglist[0] 'to' decreasinglist[lengthdecreasing])


#second derivative list 
y2coordlist1=[]
for d in derivlist:
    y2coordlist1.append(d+0.001)
    

y2coordlist2=[]
for d in derivlist:
    y2coordlist2.append(d-0.001)

interval2num=len(y2coordlist1)
print(interval2num)

#  second derivatives
deriv2list=[]
for d in range(interval2num):
    deriv2  = ((y2coordlist1[d])-(y2coordlist2[d]))/(2*0.01)
    deriv2list.append(deriv)
print (deriv2list)

secondderivlist=list(zip(xcoordlist, derivlist, deriv2list))
print(secondderivlist)

# points of inflection

# concave up intervals

# concave down intervals



    





    
    
