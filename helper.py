import numpy as np
# Calculates the probability of a entry appearing in a list.
# This will cause every entry in the matrix to be transformed to
# x/n, where x is the original entry and n is the sum of everything in the matrix.

def creatematrix()
    
def entropymatrix(matrix:np.array[np.array]):
    """Calculates the chance of a certain combination appearing in a given bigram matrix."""
    # Calculate sum first.
    sumtotal = 0
    for x in range(matrix):
        sumtotal += np.sum(matrix[x])
    # Calculate the new values
