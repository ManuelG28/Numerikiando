import numpy as np
import sys
import math

class LagrangeMethod:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.answer = ''

    def lagrange(self):
        n = len(self.x1)
        aux = []
        den = 0
        mul = 1
        print("Lagrange interpolating polynomials:")
        self.answer += "Lagrange interpolating polynomials: \n"
        for i in range(n):
            print("L" , i , "= ", end=" ")
            self.answer += "L" + str(i) + "= "
            for j in range(n):
                if(i!=j):
                    den = (self.x1[i]-self.x1[j])
                    mul=mul*den
                    if self.x1[j] > 0:
                        print("(x - " , self.x1[j] , ")", end=" ")
                        self.answer += "(x - " + str(self.x1[j]) + ")"
                    else:
                        print("(x + " , abs(self.x1[j]) , ")", end=" ")
                        self.answer += "(x + " + str(abs(self.x1[j])) + ")"
                
            
            print(" " , ((1/mul)*self.y1[i]) ,"\n")
            self.answer += " " + str(((1/mul)*self.y1[i])) + "\n"
            mul=1
        
        self.answer += "\n\nPolynomial: \n"
        for i in range(n):
            if i == n-1:
                print("(", str(self.y1[i]) ,"*L" , i ,")", end=" " )
                self.answer += "(" + str(self.y1[i]) + "*L" + str(i) +")\n"
            else:
                print("(", str(self.y1[i]) ,"*L" , str(i) ,")+", end=" " )
                self.answer += "(" + str(self.y1[i]) + "*L" + str(i) +") +"