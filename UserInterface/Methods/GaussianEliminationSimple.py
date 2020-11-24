import numpy as np

class GaussianEliminationSimpleMethod:
    def __init__(self,n,matrix):
        self.answer = ''
        self.n=n 
        self.matrix=matrix
        
    def Gaussian(self):
        self.answer += 'Original matrix\n'
        print("Original matrix")
        self.answer += '\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.matrix)

        for k in range(1, self.n):
            self.answer += '\nMultipliers: \n' + str(k) + '\n' + str(k) + "," + str(k) + "= " + str(self.matrix[k-1][k-1]) 
            print("Stage " + str(k))
            print("Goal: Fill with zeros under the element A " + str(k) + "," + str(k) + "= " + str(self.matrix[k-1][k-1]))
            print("\nMultipliers: ")
            for i in range(k+1, self.n+1):
                multiplier = self.matrix[i-1][k-1] / self.matrix[k-1][k-1]
                for j in range(k, self.n+2):
                    self.matrix[i-1][j-1] = self.matrix[i-1][j-1] - multiplier * self.matrix[k-1][j-1]
                self.answer += '\n\nMultipliers ' + str(i) + ' , ' + str(k) + ': ' + str(multiplier)
                print("Multipliers " + str(i) + " , " + str(k) + ": " + str(multiplier))
            print(" ")
            self.answer += '\n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.matrix)
        
        x = [None]*self.n
        print("Backward substitution")
        for i in range(self.n, 0, -1):
            summ = 0
            for p in range(i+1, self.n+1):
                summ = summ + self.matrix[i-1][p-1] * x[p-1]
            x[i-1] = (self.matrix[i-1][self.n] - summ) / self.matrix[i-1][i-1]
            self.answer += '\n\nX' + str(i) + ' = ' + str(x[i-1]) + '\n'
            print("X" + str(i) + " = " + str(x[i-1]))

    