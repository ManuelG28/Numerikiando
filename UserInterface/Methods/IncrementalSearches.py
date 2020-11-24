import numpy as np
from sympy import *
from sympy.sets import Interval
from sympy.calculus.util import continuous_domain


class IncrementalSearchesMethod:
    def __init__(self, increase, previous, iteration, function):
        self.previous = previous
        self.increase = increase
        self.iteration = iteration
        self.function = function
        self.answer = ''

    def runSearch(self):
        x = Symbol('x')
        f = lambda x: eval(self.function)

        negative = False
        positive = False
        root = False
        valuePositive = 0
        valueNegative = 0
        self.increase = float(self.increase)
        self.previous = float(self.previous)
        self.iteration = int(self.iteration)

        for i in np.arange(self.previous, self.iteration, self.increase):
            value = float(f(i))
            if(value == 0):
                self.answer += str(i) + ' is a root of the function\n'
            else:
                if(value < 0):
                    negative = True
                    valuePositive = i
                
                if(value>0):
                    positive = True
                    valueNegative = i

                if(i != self.previous):
                    if((negative == True) and (positive == True)):
                        if(valueNegative < valuePositive):
                            self.answer += 'There is a root between [' + str(valueNegative) + " , " + str(valuePositive) + "]\n"
                        else:
                            self.answer += 'There is a root between [' + str(valuePositive) + " , " + str(valueNegative) + "]\n"
                        root = True
                        negative = positive = False
        
        if (root == False):
            self.answer += '\nThe root was not found\n'
            print("The root was not found")