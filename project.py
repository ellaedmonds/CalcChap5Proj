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

#print(function)

xcoordlist=[]                               #x values
for i in range(x1,x2+1):
    if i == x2:
        xcoordlist.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            xcoordlist.append(round((i+m),2))
#print(xcoordlist)
    

ycoordlist=[]                               # y values
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
#print(ycoordlist)


ycoordlist1=[]                              #this will find the a+.001 for the dq
for r in xcoordlist:
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
#print(ycoordlist1)


ycoordlist2=[]                              #this will find the a+.001 for the sdq
for r in xcoordlist:
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
#print(ycoordlist2)


intervalnum=len(ycoordlist1)                #this tells us how long our cordinate lists are 
#print(intervalnum)                              #so we know how long to run the loop


derivlist=[]                                #here we will make a list of the derivatives
derivlist1=[]
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.001)
    derivlist1.append(round(deriv,2))
    derivlist.append(deriv)
#print (derivlist)


#deriv/x value/y value zip
xyderivzip=list(zip(xcoordlist, ycoordlist, derivlist))
#print(xyderivzip)


extremalist=[]                              #here we find where d1 = 0
increasinglist=[]                           #here we find the interval where it inc/dec
decreasinglist=[]
zero = []
b = -1
c = 1
e=len(xyderivzip)
for d in xyderivzip:
    B=xyderivzip[b]
    C=xyderivzip[c]
    if d[0] == xcoordlist[0]:
        if d[2] > 0:
            if d[1] < C[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > C[1]:
                print((d[0],round(d[1],2)),"is a local max")
        zero.append((' ',d[0],'+'))
        if d[2] < 0:
            if d[1] < B[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > B[1]:
                print((d[0],round(d[1],2)),"is a local max")
        zero.append((' ',d[0],'-'))
    elif d[0] == xcoordlist[-1]:
        if d[2] > 0:
            if d[1] < C[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > C[1]:
                print((d[0],round(d[1],2)),"is a local max")
            zero.append(('+',d[0],' '))
        if d[2] < 0:
            if d[1] < B[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > B[1]:
                print((d[0],round(d[1],2)),"is a local max")
            zero.append(('-',d[0],' '))
    else: 
        if B[2]*d[2] > 0:
            if d[2] > 0:
                increasinglist.append(d[0])
            elif d[2] < 0:
                decreasinglist.append(d[0]) 
        elif B[2]*d[2] <= 0:
            extremalist.append((d[0], d[1]))
            if B[2] < 0 and C[2] < 0:
                print((d[0],round(d[1],2)),"is just a 0")
            elif B[2] < 0 and C[2] > 0:
                print((d[0],round(d[1],2)),"is a local min")
                increasinglist.append(d[0])
            elif B[2] > 0 and C[2] < 0:
                print((d[0],round(d[1],2)),"is a local max")
                decreasinglist.append(d[0])
            if B[2] < 0:
                before = '-'
            elif B[2] > 0:
                before = '+'
            if C[2] < 0:
                after = '-'
            elif C[2] > 0:
                after = '+'
            if d[2] == 0:
                zero.append((before,d[0],after))
            elif B[2] != 0 and C[2] !=0:
                zero.append((before,(B[0]+d[0])/2,after))
    b+=1
    c+=1
    if c == e:
        c=0

#print(zero)

incstart = []
incend = []
decstart = []
decend = []
for d in zero:
    if d[0] == '+':
        incend.append(d[1])
    elif d[0] == '-':
        decend.append(d[1])
    if d[2] == '+':
        incstart.append(d[1])
    elif d[2] == '-':
        decstart.append(d[1])
        
#print(incstart)
#print(incend)
#print(decstart)
#print(decend)
if len(incstart) == 0:
    print("your function is never increasing.")
else:
    print("Your function is increasing from:")
    for d in incstart:
        m = incstart.index(d)
        print(d,"to",incend[m])

if len(decstart) == 0:
    print("Your function is never decreasing.")
else:
    print("Your function is decreasing from:")
    for d in decstart:
        m = decstart.index(d)
        print(d,"to",decend[m])    

    

'''

#second derivatives
y2coordlist1=[]
for d in derivlist:
    y2coordlist1.append(d+0.001)
    
y2coordlist2=[]
for d in derivlist:
    y2coordlist2.append(d-0.001)

interval2num=len(y2coordlist1)
print(interval2num)

deriv2list=[]
for i in range(interval2num):
    deriv2  = ((y2coordlist1[i])-(y2coordlist2[i]))/(2*0.001)
    deriv2list.append(round(deriv2,2))
print (deriv2list)

xyderiv2zip=list(zip(xcoordlist, ycoordlist, derivlist, deriv2list))
print(xyderiv2zip)

# points of inflection
poilist=[]
concaveuplist=[]
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]==0:
       poistlist.append((d[0], d[1]))
    elif d[3]>=0:
        concaveuplist.append(d[0])
    elif d[3]<=0:
        concavedownlist.append(d[0])
print (poilist)
print (concaveuplist)
print (concavedownlist)

# concave up interval(s)
concaveuplist=[]
for d in xyderiv2zip:
    if d[3]>=0:
        concaveuplist.append(d[0])
print (concaveuplist)
lengthconcaveup=len(concaveuplist)
print(lengthconcaveup)
#print('Your function is concave up from' concaveuplist[0] 'to' concaveuplist[lengthconcaveup])

#concave down interval(s)
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]<=0:
        concavedownlist.append(d[0])
print (concavedownlist)
lengthconcavedown=len(concavedownlist)
#print('Your function is concavedown from' concavedownlist[0] 'to' concavedownlist[lengthconcavedown])

'''


    
    
