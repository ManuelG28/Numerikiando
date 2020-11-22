import numpy as np
import sys
import math
from sympy import *
from sympy.sets import Interval
from sympy.calculus.util import continuous_domain

# author Valeria

class MultipleRootsMethod:
    
    def __init__(self, fu, x0, n, t):
        self.fu = fu
        self.x0 = x0
        self.n = n
        self.t = t
    
    #bisection method
    def roots(self):
        dataTable = []
        x = Symbol('x')
        f = lambda x: eval(self.fu)
        f1 = diff(self.fu,x)
        f2 = diff(self.fu,x,x)
        df1 = lambda x: eval(str(f1))
        df2 = lambda x: eval(str(f2))
        self.x0 = float(self.x0)
        self.n = int(self.n)
        self.t = float(self.t)
        resultf = f(self.x0)
        resultf1 = df1(self.x0)
        resultf2 = df2(self.x0)
        i = 0

        #Method data input control
        if self.n < 1:
            print("Iterations must be greater than 0")

        if resultf == 0:
            print(self.x0 + "Its a root")
        
        #First iteration (iteration 0)
        print("Iter: " , i)
        print("x0: " ,self.x0)
        print("f(xi): " , f(self.x0))
        print("E: ")
        print("")
        dataTable.append({"iter":i, "xi":self.x0,"f(xi)":f(self.x0), "E":0})
        i += 1
        xi = self.x0 - ((resultf * resultf1) /(math.pow(resultf1, 2) - (resultf * resultf2)))

        #Loop start
        while(resultf != 0 and i <= self.n and abs(xi - self.x0) > self.t):
            error = abs(xi - self.x0)
            self.x0 = xi
            resultf = f(self.x0)
            resultf1 = df1(self.x0)
            resultf2 = df2(self.x0)
            xi = self.x0 - ((resultf * resultf1) / (math.pow(resultf1, 2) - (resultf * resultf2)))

            print("Iter: " , i)
            print("x0: " , self.x0)
            print("f(xi): " , resultf)
            print("E: " , error)
            print("")
            dataTable.append({"iter":i, "xi":self.x0,"f(xi)":resultf, "E":error})
            i += 1

        if resultf == 0:
            print("An approximation of the root was found in " , (xi))
        elif i > self.n:
            print("Iteration limit reached")
        elif (abs(xi - x0) < self.t):
            print("The maximum tolerance permitted " , (self.t) , ". In the iteration " , (i) , " the maximum tolerance was reached " , abs(xi - self.x0))
            print("Data in the last iteration")
            print("Iteration " , (i - 1))
            print("x0= " , (self.x0))
            print("f(x0)= " + f(self.x0))
            print("E= " , (abs(xi - self.x0)))
        
        return dataTable