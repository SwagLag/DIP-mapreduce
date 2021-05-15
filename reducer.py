# Voegt letters en dergelijke bij elkaar.

import numpy as np

def mergebigrams(bigrama: np.array,bigramb: np.array):
    """Merges two given bigrams into one, preserving the shape
    but adding the values present in both bigrams onto eachother in place."""
    if bigrama.shape != bigramb.shape:
        raise Exception("bigram shape mismatch: A:{} and B:{}".format(bigrama.shape,bigramb.shape))
    bigramc = np.full(bigrama.shape,0)
    for x in range(len(bigrama)):
        for y in range(len(bigrama)):
            bigramc[x][y] = bigrama[x][y] + bigramb[x][y]
    return bigramc
