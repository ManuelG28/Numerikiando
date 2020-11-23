import numpy as np
import sys
import math

class InterNewtonMethod:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.answer = ''

    def newton(self):
        n = len(self.x1)
        A = []
        for i in range(n):
            A.append([0]*n)
        for j in range(0,n):
            A[j][0] = self.y1[j]
        
        p = 0
        for k in range(0,n):
            p = 0
            for i in range(k+1,n):
                A[i][k + 1] = (A[i][k] - A[i - 1][k]) / (self.x1[i] - self.x1[p])
                p = p + 1
            
        
        print("Table of divided differences: ")
        self.answer += "Table of divided differences: \n"
        for i in range(0,n):
            for j in range(0,n):
                print(A[i][j] , end = "     ")
                self.answer += str(A[i][j]) + "     "
            
            print("")
            self.answer += "\n"
        

        print("\nNewton's Polynomial coefficients: ")
        self.answer += "\nNewton's Polynomial coefficients: \n"
        for j in range(0,n):
            print(A[j][j] ,end= "     ")
            self.answer += str(A[j][j]) + "      "
        
        print("")
        self.answer += "\n"
        print("\nNewton's Polynomial: ")
        self.answer += "\nNewton's Polynomial: \n"
        for j in range(0,n):
            if (j==0):
                print(A[j][j], end="")
                self.answer += str(A[j][j])
            else:
                if(A[j][j]>0):
                    print(" + " , A[j][j], end="")
                    self.answer += " + " + str(A[j][j])
                    for i in range(0,j): 
                        if(self.x1[i]>0):
                            print("(x - " , self.x1[i] , ")", end="");
                            self.answer += "(x - " + str(self.x1[i]) + ")"
                        else:
                            print("(x + " , abs(self.x1[i]) , ")", end="")
                            self.answer += "(x + " + str(abs(self.x1[i])) + ")"
                        
                    
                else:
                    print(" - " , abs(A[j][j]), end="")
                    self.answer += " - " + str(abs(A[j][j]))
                    for i in range(0,j):
                        if(self.x1[i]>0):
                            print("(x - " , self.x1[i] , ")", end="")
                            self.answer += "(x - " + str(self.x1[i]) + ")"
                        else:
                            print("(x + " , abs(self.x1[i]) , ")", end="")
                            self.answer += "(x + " + str(abs(self.x1[i])) + ")"
                        
                    
                
            
        
        print("")
        self.answer += "\n"