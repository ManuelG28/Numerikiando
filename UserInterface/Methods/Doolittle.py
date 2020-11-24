import sympy as sm
import math
import sys
import json
import base64
import numpy as np

class DoolittleMethod():
    def __init__(self,A,b,size):
        self.answer=''
        self.A=A 
        self.b=b 
        self.size=size


    def doolittle(self):
        A = np.array(self.A)
        b = np.array(self.b)
        L = np.eye(self.size)
        U = np.eye(self.size)
        self.answer += '\n\nStage 0\n' + '\nMatrix L\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in L) + '\nMatrix U\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in U) + '\n'
        
        print("Etapa 0:")
        print("Matriz L: ")
        print(L)
        print("Matriz U: ")
        print(U)
        for i in range(self.size):
            self.answer += '\n\nStage ' + str(i+1) + '\n'
            print("Etapa " + str(i+1))
            for k in range(i, self.size): 
                suma = 0;
                for j in range(i):
                    suma += (L[i][j] * U[j][k]);
                U[i][k] = self.A[i][k] - suma;
            for k in range(i, self.size):
                if (i == k):
                    L[i][i] = 1;
                else:
                    suma = 0;
                    for j in range(i):
                        suma += (L[k][j] * U[j][i]);
                    L[k][i] = ((self.A[k][i] - suma)/U[i][i]);

            self.answer += '\nMatrix L:\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in L) + '\nMatrix U:\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in L) + '\n'

            print("Matriz L: ")
            print(L)
            print("Matriz U: ")
            print(U)
        z = self.frontSubstitution(L, b)
        x = self.backSubstitution(U, z)
        self.printResultVector(x)

    def frontSubstitution(self,A, b):
        n = len(A)
        x = np.zeros((n))
        for i in range(n):
            sum = 0
            for j in range(i):
                sum +=  A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]
        return x

    def backSubstitution(self,A, b):
        n = len(A)
        x = np.zeros((n))
        for i in range(n-1, -1, -1):
            sum = 0.0
            for j in range (i+1, n):
                sum += A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]
        return x

    def printResultVector(self,vector):
        n = len(vector)
        self.answer += '\n\n'
        for i in range(n):
            self.answer += 'x' + str(i + 1) + ': ' + str(vector[i]) + '\n'
            print('x' + str(i + 1) + ': ' + str(vector[i]))