import numpy as np
# Calculates the probability of a entry appearing in a list.
# This will cause every entry in the matrix to be transformed to
# x/n, where x is the original entry and n is the sum of everything in the matrix.

def createfreqbigram(bigram:np.array) -> np.array:
    """Creates a frequency bigram from a normal bigram."""
    sums = 0
    newgram = np.full(bigram.shape,0)
    # Step 1: Get the sum of all occurences.
    for x in range(len(bigram)):
        for y in range(len(bigram)):
            sums += bigram[x][y]
    # Step 2: Get frequency (frequency = amount of times / sum)
    for x in range(len(bigram)):
        for y in range(len(bigram)):
            newgram[x][y] = bigram[x][y] / sums
    return newgram