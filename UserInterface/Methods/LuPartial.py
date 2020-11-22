import numpy as np
import sys


class LuPartialMethod:
    def __init__(self, a, n, b):
        self.b = b
        self.ab = np.c_[a, b]
        self.n = n
        self.answer = ''
        self.l = np.identity(self.n)
        self.uz = self.gaussianElimination(self.n, self.ab, self.l, self.b)
        self.lb = np.c_[self.l, self.b]
        self.regressiveSubstitution(self.uz, self.n)

    def gaussianElimination(self, n, matrix, l, b):
        ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
        l_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.l)
        self.answer += 'ETAPA 0\n\n'+'AB: '+"\n"+ab_string+"\n"+"\n" 
        self.answer += 'L: '+"\n"+l_string+"\n"+"\n" 
        for x in range(1, n):
            self.firstStep(matrix, x, n, b)
            for i in range(x+1, n+1):
                scalar = matrix[i-1][x-1] / matrix[x-1][x-1]
                for j in range(x, n+2):
                    matrix[i-1][j-1] = matrix[i-1][j-1] - \
                        scalar*matrix[x-1][j-1]
                print('Multipliers', i, ',', x, ':', scalar)
                self.l[i-1][x-1] = scalar
            ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
            self.answer += 'ETAPA '+str(x)+"\n"+"\n"+'AB: '+"\n" +ab_string+"\n"+"\n" 
            self.answer += 'L: '+"\n"
            l_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.l)
            self.answer += l_string+"\n"+"\n" 
        print(self.ab)
        return self.ab

    def regressiveSubstitution(self, uz, n):
        answers = [0]*n
        for i in range(n, 0, -1):
            ctrl = 0
            for p in range(i+1, n+1):
                ctrl = ctrl + uz[i-1][p-1] * answers[p-1]
            answers[i-1] = (uz[i-1][n]-ctrl)/uz[i-1][i-1]
            self.answer += 'x'+str(i)+' = '+str(answers[i-1])+"\n"+"\n" 
            print("x", i, "=", answers[i-1])

    def progressiveSubstitution(self, lb, n):
        z = [0]*n
        for i in range(len(lb)):
            ctrl = 0
            for j in range(i):
                ctrl = ctrl + lb[i][j] * z[j]
            z[i] = (lb[i][n] - ctrl) / lb[i][i]
        return z

    def firstStep(self, matrix, x, n, b):
        row = x-1
        column = x-1

        largest = np.abs(self.ab[row][column])

        '''
        I'll find the largest number in the column with it's row
        '''
        for i in range(x-1, n):
            aux = np.abs(self.ab[i][x-1])
            if(aux > largest):
                largest = aux
                row = i

        auxB = b[x-1]
        b[x-1] = b[row]
        b[row] = auxB
        if(row != x-1):
            for i in range(0, self.ab.shape[1]):
                aux = matrix[x-1][i]
                matrix[x-1][i] = matrix[row][i]
                matrix[row][i] = aux
