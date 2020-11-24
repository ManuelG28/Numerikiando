import numpy as np
import math

class CholeskyMethod:
    def __init__(self,A,b):
        self.A=A 
        self.b=b 
        self.answer = ''

    def cholesky(self):
        #Inicialización
        n = len(self.A)
        L = np.eye(n)
        U = np.eye(n)

        #factorization
        for i in range(n-1):
            suma = 0
            for j in range(i):
                suma += (L[i][j] * U[j][i])
            L[i][i] = math.sqrt(self.A[i][i] - suma)
            U[i][i] = L[i][i]

            for k in range(i+1,n):
                suma = 0
                for j in range(i):
                    suma += (L[k][j] * U[j][i])
                L[k][i] = (self.A[k][i] - suma) / U[i][i]

            for k in range(i+1,n):
                suma = 0
                for j in range(i):
                    suma += (L[i][j] * U[j][k])
                U[i][k] = (self.A[i][k] - suma) / L[i][i]

        suma = 0
        for j in range(n-1):
            suma += (L[n-1][j] * U[j][n-1])

        if((self.A[n-1][n-1] - suma) < 0.0): 
            self.answer += "This matrix cannot be solved. A division by zero was found"
            return None
            
        L[n-1][n-1] = math.sqrt(self.A[n-1][n-1] - suma)
        U[n-1][n-1] = L[n-1][n-1]

        self.answer += '\nMatrix L\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in L)
        print("Matriz L")
        print(L)

        self.answer += '\n\nMatrix U\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in U)
        print("Matriz U")
        print(U)
        z = self.frontSubstitution(L, self.b)
        x = self.backSubstitution(U, z)
        self.answer += '\n\n' + str(x)
        print(x)



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
