import numpy as np

class CroutMethod:
    def __init__(self,a,b):
        self.answer = ''
        self.a=a 
        self.b=b 

    def Crout(self):
        cout = 0
        m, n = self.a.shape
        if (m !=n ):
            print("You can't use Crout for this matrix")
        else:
            l = np.zeros((n,n))
            u = np.zeros((n,n))
            s1 = 0
            s2 = 0

            for m in range(1,n+1):
                self.answer += '\n\nStage ' + str(m) + ': ' + '\n'
                print("Stage " + str(m) + ": ")
                for i in range(n):
                    l[i][0] = self.a[i][0]
                    u[i][i] = 1
                for j in range(1, n):
                    u[0][j] = self.a[0][j] / l[0][0]
                for k in range(1, n):
                    for i in range(k, n):
                        for r in range(k): s1 += l[i][r] * u[r][k]
                        l[i][k] = self.a[i][k] - s1
                        s1 = 0             #Initialize s1 after each summation=0
                    for j in range(k+1, n):
                        for r in range(k): s2 += l[k][r] * u[r][j]
                        u[k][j] = (self.a[k][j] - s2) / l[k][k]
                        s2 = 0                #Initialize s2 after each summation=0
                self.answer += 'U: \n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in u) + '\n' 
                print("U: ")
                print(u)

                self.answer += 'L: \n' + '\n'.join('\t'.join('%0.3f' %x for x in y) for y in l) + '\n' 
                print("L: ")
                print(l)

            
            y = np.zeros(n)
            s3 = 0
            y[0] = self.b[0] / l[0][0]    # First calculate the first x solution
            for k in range(1, n):
                for r in range(k):
                    s3 += l[k][r] * y[r]
                y[k] = (self.b[k]-s3) / l[k][k]
                s3 = 0

            x = np.zeros(n)
            s4 = 0
            x[n-1] = y[n-1]
            for k in range(n-2, -1, -1):
                for r in range(k+1, n):
                    s4 += u[k][r] * x[r]
                x[k] = y[k] - s4
                s4 = 0

            for i in range(n):
                self.answer += '\n\nx' + str(i + 1) + ' = ' +  str(x[i]) + '\n'
                print("x" + str(i + 1) + " = ", x[i])