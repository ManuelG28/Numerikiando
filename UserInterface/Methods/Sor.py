import numpy as np
import sys
import math

class SorMethod:
    def __init__(self, a, b, x0, t, iter, w):
        self.a = a
        self.b = b
        self.x0 = x0
        self.t = t
        self.iter = iter
        self.w = w
        self.answer = ''

    def sor(self) :
        self.t = float(self.t)
        self.iter = int(self.iter)
        self.w = float(self.w)
        n = len(self.a)
        l = len(self.a)
        
        D = np.diag(np.diag(self.a))
        U = -np.triu(self.a,1)
        L = -np.tril(self.a,-1)
        T = (np.dot((np.linalg.inv(D-(self.w*L))), ((1-self.w)*D+(self.w*U))))
        C = (self.w*np.dot((np.linalg.inv(D-(self.w*L))), self.b))
        print("T: ")
        print(T)
        self.answer += "T: \n" + str(T) + "\n"
        print("C:")
        print(C)
        self.answer += "C: \n" + str(C) + "\n"
        values, normalized_eigenvectors = np.linalg.eig(T) # T es la matriz
        spectral_radius = max(abs(values))
        print("\nSpectral Radius: ", spectral_radius)
        self.answer += "\nSpectral Radius: " + str(spectral_radius) + "\n"
        if spectral_radius>1:
            print("The method does not converge because the spectral radius is greater than 1")
        else:
            if (n != l) :
                print("A is not a square matrix.")
                self.answer += "A is not a square matrix. \n"
                return 0
            else:
                x = [None]*n
                aux = 0
                cont = 0
                E = self.t + 1.0
                iteration = 1
                while (E > self.t and cont <= self.iter):
                    print("iter: " , iteration)
                    self.answer += "iter: " + str(iteration) + "\n"
                    E = 0
                    for i in range(0,n):
                        suma = 0
                        for j in range(0,n):
                            if (i != j):
                                suma = suma + self.a[i][j] * self.x0[j]
                        x[i] = self.w * ((self.b[i] - suma) / self.a[i][i]) + (1 - self.w) * self.x0[i]
                        aux = x[i] - self.x0[i]
                        E = E + math.pow(aux, 2)
                        self.x0[i] = x[i]
                        print("x" , str(i + 1) , ": " , str(self.x0[i]))
                        self.answer += "x" + str(i + 1) + ": " + str(self.x0[i]) + "\n"
                    
                    E = math.pow(E, 0.5)
                    print("E = " , E)
                    print("")
                    self.answer += "E = " + str(E) + "\n\n"
                    iteration = iteration + 1
                    cont = cont+1
                
                if (E < self.t):
                    return x
                else:
                    print("Can not find a solution in " , str(iter) , " iterations")
                    self.answer += "Can not find a solution in " + str(iter) + " iterations \n"
                    return 0
                
            

