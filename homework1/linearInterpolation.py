import numpy as np
import pandas as pd
from random import uniform

class Interpolation(object):

    def __init__(self, X, z):
        if isinstance(X, list):
            self.X = X
        elif isinstance(X, np.ndarray):
            self.X = X.tolist()        
        elif isinstance(X, pd.DataFrame):
            self.X = X.values
        else:
            raise TypeError('Wrong input for the function values')

        assert len(self.X) == 2, 'Wrong shape of input data; required length of 2'
        self.sorting_input()

        assert (z >= self.X[0][0]) & (z <= self.X[0][-1]), 'Z must be inside X values'
        self.z = z

    def sorting_input(self):
        indices = np.argsort(self.X[0])
        self.X = [[self.X[0][i] for i in indices],[self.X[1][i] for i in indices]]
        
    def linear_1d(self):
        x = self.X[0]
        y = self.X[1]
        ii = np.searchsorted(x, self.z)
        
        k = (y[ii] - y[ii-1]) / (x[ii] - x[ii-1])
        b = y[ii] - k * x[ii]

        return k * self.z + b


def test(eps = 1e-7):
    X = [[-2,-1,0,1,2],[-2,-1,0,1,2]]
    for i in range(10):
        ii = uniform(-2,2)
        if ii-Interpolation(X, ii).linear_1d() > eps:
            print('Test failed')
            return None
    print('Test successful')

if __name__ == '__main__':
    test()

    

