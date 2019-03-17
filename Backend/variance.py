import numpy as np

# calculates variance of data
def variance (dir):
    data = np.loadtxt(dir, delimiter=" ")
    var = np.var(data)
    return var