# CalcChap5Proj
Q2 Mr. Donnelly Calc Project Katie and Ella

USER MANUAL:

Insert your equation in python format in the first input bubble
  Equations that can be handled:
   - Quadratics, all in format: x3 = (x**3) and (x+2)^2 must be written as a polynomial
   - Trig: sin(x), cos(x), tan(x), asin(x), acos(x), atan(x)
   - Logarithmic, only: e, log, log10, log2
   - Other usable math tools: sqrt, pi, exp, expm1
   You can combine these attributes as you would like (ex:(x**2)*sin(x))

*****In addition for log and square root functions the interval you select must be in the domain of the function, the program will remind you of this.*****

Insert the starting point and then the end point of the interval for which you would like to analyze the function. THESE NUMBERS MUST BE INTEGERS! (note that the longer the interval, the longer the analyzation process will take)

ISSUES REMAINING: 
Unfortunately, our program has an issue running 1/x functions due to python’s difficulty in dealing with asymptotes. It is able to print some of the correct values for maxs and mins, and was graphing at one point. However, in order to fully fix the issue we would have had to sacrifice the program’s ability to run smoothly with virtually any other function. 
