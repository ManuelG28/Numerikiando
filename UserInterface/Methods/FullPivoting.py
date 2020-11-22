import numpy as np
import sys

class FullPivotingMethod:
    def __init__(self, ab, n):
        self.ab = ab
        self.n = n
        self.positions = [0]*self.n
        self.answer = ''

    def gaussianElimination(self):
        ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
        self.answer += 'ETAPA 0\n'+ab_string+"\n"+"\n" 
        for x in range(1, self.n):
            self.firstStep(x)
            for i in range(x+1, self.n+1):
                scalar = self.ab[i-1][x-1] / self.ab[x-1][x-1]
                for j in range(x, self.n+2):
                    self.ab[i-1][j-1] = self.ab[i-1][j-1] - scalar*self.ab[x-1][j-1]
            ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
            self.answer += 'ETAPA '+str(x)+"\n" +ab_string+"\n"+"\n" 
        self.regressiveSubstitution()
        print(self.answer)


    def firstStep(self, x):
        row = x-1
        column = x-1

        largest = np.abs(self.ab[row][column])

        for i in range(x-1, self.n):
            for j in range(x-1, self.n):
                aux = np.abs(self.ab[i][j])
                if(aux > largest):
                    largest = aux
                    row = i
                    column = j

        if(column != x-1):
            for i in range(0, self.ab.shape[0]):
                aux = self.ab[i][x-1]
                self.ab[i][x-1] = self.ab[i][column]
                self.ab[i][column] = aux
            auxPositions = self.positions[x-1]
            self.positions[x-1] = column
            self.positions[column] = auxPositions

        if(row != x-1):
            for i in range(0, self.ab.shape[1]):
                aux = self.ab[x-1][i]
                self.ab[x-1][i] = self.ab[row][i]
                self.ab[row][i] = aux


    def regressiveSubstitution(self):
        answers = [0]*self.n
        for i in range(self.n, 0, -1):
            ctrl = 0
            for p in range(i+1, self.n+1):
                ctrl = ctrl + self.ab[i-1][p-1] * answers[p-1]
            answers[i-1] = (self.ab[i-1][self.n]-ctrl)/self.ab[i-1][i-1]
            self.answer += 'x'+str(self.positions[i-1]+1)+' = '+str(answers[i-1]+1)+"\n"+"\n"  
            print("x", (self.positions[i-1]+1), "=", answers[i-1])


    def fillPostions(self):
        for i in range(len(self.positions)):
            self.positions[i] = i
