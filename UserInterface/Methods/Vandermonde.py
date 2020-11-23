import numpy as np
import sys
import math

class VandermondeMethod:

    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.answer = ''
        self.positions = []

    def gaussianElimination(self, ab):
        n = len(self.x1)
        for x in range(1,n):
            #firstStep(x);
            row = x-1
            column = x-1

            largest = abs(ab[row][column])

            for i in range(x-1,n):
                for j in range(x-1, n):
                    aux = abs(ab[i][j])
                    if(aux > largest):
                        largest = aux
                        row = i
                        column = j

            if(largest == 0):
                print("This method can't be executed")
                self.answer += "This method can't be executed\n"
                sys.exit(0)
            else:
                if(column != x-1):
                    for i in range(0, n):
                        aux = ab[i][x-1]
                        ab[i][x-1] = ab[i][column]
                        ab[i][column] = aux
                    auxPositions = self.positions[x-1]
                    self.positions[x-1] = column
                    self.positions[column] = auxPositions

                if(row != x-1):
                    for i in range(0, n+1):
                        aux = ab[x-1][i]
                        ab[x-1][i] = ab[row][i]
                        ab[row][i] = aux
                    
                
            
            #_______________________________________________________________________

            for i in range(x+1, n+1):
                scalar = ab[i-1][x-1] / ab[x-1][x-1]
                for j in range(x, n+2):
                    ab[i-1][j-1] = ab[i-1][j-1] - scalar*ab[x-1][j-1]
        #regressiveSubstitution()
        answers = [0]*n
        for i in range(n, 0, -1):
            ctrl = 0
            for p in range(i+1, n+1):
                ctrl = ctrl + ab[i-1][p-1] * answers[p-1]
            answers[i-1] = (ab[i-1][n]-ctrl)/ab[i-1][i-1]
        
        print("Polynomial coefficients:  ")
        self.answer += "Polynomial coefficients:  \n"
        for i in range(0,n):
            print(answers[i] , end="  ")
            self.answer += str(answers[i]) + "  "
        
        print("")
        self.answer += "\n"
        print("\nPolynomial:  ")
        self.answer += "\nPolynomial:  \n"
        cont=len(answers)-1
        for i in range(0,n):
            if(cont==0):
                print(answers[i])
                self.answer += str(answers[i]) + "\n"
            else:
                if(answers[i+1]<0):
                    print(answers[i] , "x^" , cont , end = " ")
                    self.answer += str(answers[i]) + "x^"+ str(cont) + " "
                    cont= cont-1
                else:
                    print(answers[i] , "x^" , cont , " +", end=" ")
                    self.answer += str(answers[i]) + "x^"+ str(cont) + " + "
                    cont= cont-1
                
            
        
        #_______________________________________

    def fillPositions(self):
        for i in range(0,len(self.positions)):
            self.positions[i] = i
        


    def vandermonde(self):
        n = len(self.x1)
        ab = []
        for i in range(n):
            ab.append([0]*(n+1))
        expo = n - 1
        for i in range(0, len(ab)):
            for j in range(0, len(ab[i])):
                if (j == (n)):
                    ab[i][j] = self.y1[i]
                else:
                    ab[i][j] = math.pow(self.x1[i], expo)
                    expo= expo -1
                
            
            expo = n - 1;
        print("\nVandermonde Matrix:")
        self.answer += "\nVandermonde Matrix: \n"
        for f in range(0,len(ab)):
            for c in range(0, len(ab[f])):
                print(ab[f][c] , end ="   ")
                self.answer += str(ab[f][c]) + "    "
            
            print("")
            self.answer += "\n"
        
        print("")
        self.answer += "\n"
        self.fillPositions()
        self.gaussianElimination(ab)
