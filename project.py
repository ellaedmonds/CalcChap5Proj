'''
project.py
Katie Naughton and Ella Edmonds
'''

function=input("What function would you like to analyze? ")
a=int(input("Where do you want your interval to start? "))
b=int(input("Where do you want your interval to end? "))

print(function)
funclist=list(function)
print(funclist)

length=len(funclist)
print(length)

func2 = lambda x: (2*x)-3
for x in range(a, (b+1)): 
    print(func2(x))

#for r in 
'''
ycoord=[]
for x in range(a, (b+1)):
    print (function)

#linearization= lamba a: f(a)+ fp(a)(x-a)
#for x in range(a,(b+1)):
'''
    
    
