import numpy as np
import sys

class LuSimpleMethod:
    def __init__(self, a, n, b):
        self.b = b
        self.ab = np.c_[a, b]
        self.n = n
        self.answer = ''

        self.l = np.identity(n)
        self.uz = self.gaussianElimination(self.ab, self.l)
        self.lb = np.c_[self.l,b]
        self.regressiveSubstitution(self.uz,self.n)

    def gaussianElimination(self,ab, l):
        ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
        l_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.l)
        self.answer += 'ETAPA 0\n\n'+'AB: '+"\n"+ab_string+"\n"+"\n" 
        self.answer += 'L: '+"\n"+l_string+"\n"+"\n" 
        for x in range(1, self.n):
            for i in range(x+1, self.n+1):
                scalar = ab[i-1][x-1] / ab[x-1][x-1]
                for j in range(x, self.n+2):
                    ab[i-1][j-1] = ab[i-1][j-1] - scalar*ab[x-1][j-1]
                print('Multipliers', i, ',', x, ':', scalar)
                l[i-1][x-1] = scalar   
            ab_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.ab)
            self.answer += 'ETAPA '+str(x)+"\n"+"\n"+'AB: '+"\n" +ab_string+"\n"+"\n" 
            self.answer += 'L: '+"\n"
            l_string =  '\n'.join('\t'.join('%0.3f' %x for x in y) for y in self.l)
            self.answer += l_string+"\n"+"\n"      
        return ab

    def regressiveSubstitution(self,uz,n):
        answers = [0]*n
        for i in range(n, 0, -1):
            ctrl = 0
            for p in range(i+1, n+1):
                ctrl = ctrl + uz[i-1][p-1] * answers[p-1]
            answers[i-1] = (uz[i-1][n]-ctrl)/uz[i-1][i-1]
            self.answer += 'x'+str(i)+' = '+str(answers[i-1])+"\n"+"\n" 


    def progressiveSubstitution(self,lb,n):
        z = [0]*n
        for i in range(len(lb)):
            ctrl = 0
            for j in range(i):
                ctrl = ctrl + lb[i][j] * z[j]
            z[i] = (lb[i][n] - ctrl) / lb[i][i]
        return z

