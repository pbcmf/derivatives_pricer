import numpy as np
import matplotlib.pyplot as plt


def interliner(x, y, z):
    
    return np.interp(z, x, y)
    
def test(x, y, z):
    
    plt.plot(x, y)
    plt.plot(z, interliner(x, y, z), marker="o", markersize=10, markeredgecolor="red")
    
    return 


test([5, 6, 7, 8], [1, 1.5, 2, 0], 6.5)
