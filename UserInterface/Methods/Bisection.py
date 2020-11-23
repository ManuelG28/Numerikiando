import numpy as np
import sys
import math
from sympy import *
from sympy.sets import Interval
from sympy.calculus.util import continuous_domain

# author Valeria

class BisectionMethod:
    
    def __init__(self, fu, a, b, n, t):
        self.fu = fu
        self.a = a
        self.b = b
        self.n = n
        self.t = t
    
    #bisection method
    def bisection(self):
        dataTable = []
        x = Symbol('x')
        f = lambda x: eval(self.fu)
        self.a = float(self.a)
        self.b = float(self.b)
        self.n = int(self.n)
        self.t = float(self.t)
        x0 = 0
        y0 = 0
        i = 1
        xm = (self.a + self.b) / 2
        result = f(xm)

        #Method data input control
        if float(self.n) < 1:
            print("Iterations must be greater than 0")
        elif result == 0:
            print(str(xm) + " Its a root")
        elif (f(self.a) * f(self.b)) > 0:
            print("There is no root in this interval")
        elif (continuous_domain(f(x), x, Interval(self.a, self.b)) == Interval(self.a, self.b)) == false:
            print ("It is not a continuous function")
        else:
            #First iteration
            print("Iter: " , i)
            print("a: " , self.a)
            print("xm: " , xm)
            print("b: " , self.b)
            print("f(xm): " , f(xm))
            print("E: ")
            print("")
            dataTable.append({"iter":i, "a":self.a, "xm":xm, "b":self.b, "f(xm)":f(xm), "E":0})
            i += 1

            #Loop start
            while (result != 0 and i <= self.n and abs(x0 - xm) > self.t):
                print("Iter: " , i)
                if (result * f(self.a) < 0):
                    self.a = self.a
                    self.b = xm
                else:
                    self.b = self.b
                    self.a = xm
                
                x0 = xm
                y0 = result
                xm = (self.a + self.b) / 2
                result = f(xm)
                i += 1

                print("a: " , self.a)
                print("xm: " , xm)
                print("b: " , self.b)
                print("f(xm): " , f(xm))
                print("E: " , (abs(x0 - xm)))
                print("")

                dataTable.append({"iter":(i-1), "a":self.a, "xm":xm, "b":self.b, "f(xm)":f(xm), "E":(abs(x0 - xm))})
            
            

        #Method data output control
        if (result == 0):
            print("An approximation of the root was found in " , (xm))
        elif (i > self.n):
            print("Iteration limit reached")
        elif (abs(x0 - xm) < self.t):
            print("The maximum tolerance permitted " , (self.t) , ". In the iteration " , (i) , " the maximum tolerance was reached " , (abs(x0 - xm)))
            print("Data in the last iteration")
            print("Iteration " , (i-1))
            print("xm= " , (xm))
            print("f(xm)= " , f(xm))
            print("E= " , (abs(x0 - xm)))
        
        return dataTable
