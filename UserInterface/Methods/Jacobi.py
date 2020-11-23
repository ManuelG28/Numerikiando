import numpy as np
import sys
import math

class JacobiMethod:
    def __init__(self, a, b, x0, t, iter):
        self.a = a
        self.b = b
        self.x0 = x0
        self.t = t
        self.iter = iter
        self.answer = ''

    def jacobi(self):
        self.t = float(self.t)
        self.iter = int(self.iter)
        n = len(self.a)
        l = len(self.a)
        if (n != l):
            print("A is not a square matrix.")
            self.answer += "A is not a square matrix.\n"
            return 0
        else:
            x = []
            for i in range(n):
                x.append(i)
            T = []
            for i in range(n):
                T.append([0]*n)
            C = []
            for i in range(n):
                C.append(i)
            aux = 0
            cont = 0
            E = self.t + 1.0
            iteration = 1
            while (E > self.t and cont <= self.iter):
                print("\niter: " , str(iteration))
                self.answer += "\niter: " + str(iteration) + "\n"
                E = 0.0
                for i in range(n):
                    sum = 0
                    for j in range(n):
                        if (i != j):
                            sum = sum + self.a[i][j] * self.x0[j]
                            T[i][j] = -self.a[i][j] / self.a[i][i]
                            C[i] = self.b[i] / self.a[i][i]
                        
                    
                    x[i] = (self.b[i] - sum) / self.a[i][i]
                    aux = x[i] - self.x0[i]
                    E = E + math.pow(aux, 2)
                values, normalized_eigenvectors = np.linalg.eig(T) # T es la matriz
                spectral_radius = max(abs(values))
                if spectral_radius>1:
                    print("The method does not converge because the spectral radius is greater than 1")
                    self.answer += "The method does not converge because the spectral radius is greater than 1\n"
                    break
                else:
                    E = math.pow(E, 0.5)
                    print("E = " , E)
                    self.answer += "E = "+ str(E) + "\n"
                    for i in range(n):
                        self.x0[i] = x[i]
                        print("x" , (i + 1) , ": " , self.x0[i])
                        self.answer += "x"+ str(i + 1) + ": " + str(self.x0[i]) + "\n"
                    
                    print("")
                    self.answer += "\n"
                    iteration = iteration + 1
                    cont = cont + 1
                
            print("\nT: ")
            self.answer += "\nT: \n"
            for i in range(0,n):
                for j in range(0,n):
                    print(T[i][j] , end="      ")
                    self.answer += str(T[i][j]) + "       "
                print(" ")
                self.answer += "\n"
            print("\nC: ")
            self.answer += "\nC: \n"
            for i in range(0,n):
                print(C[i] , end= "      ")
                self.answer += str(C[i]) + "     "
            print(" ")
            print(" ")
            self.answer += "\n\n"
            print("Spectral Radius: ", str(spectral_radius))
            self.answer += "Spectral Radius: " + str(spectral_radius) + "\n"

        if (E < self.t):
            return x
        else:
            print("Can not find a solution in " + str(iter) + " iterations");
            self.answer += "Can not find a solution in " + str(iter) + " iterations\n"
            return 0 
        

