# Mapper is een functie die je uitvoert over elk element in een lijst.
# In ons geval is dit elk woord in een zin, waar in. Daarom willen wij
# per woord dan gaan kijken naar het aantal letters wat er in zit.
import numpy as np

alphabetkey = "abcdefghijklmnopqrstuvwxyz \"\'0123456789#:.!?"

def padding(segment:str) -> str:
    """Prepares a given segment for reading."""
    return " " + segment + " "

def pairing(segment:str):
    """Gets all letterpairs from a given text (use infile.readlines()!)"""
    # print(segment)
    offset = segment
    pairs = []
    length = len(offset)  # Lengte van alles.
    for i in range(length-1):
        pairs.append("{}{}".format(offset[i],offset[i+1]))
    return pairs

def createbigram(pairs:str) -> np.array:
    """Creates a base numpy array for putting frequencies of certain combinations
    into. Uses a built-in alphabet key, and the index of a character in this key
    translates directly to the index on the matrix."""
    base = np.full((len(alphabetkey), len(alphabetkey)), 0)
    for pair in pairs:
        base[alphabetkey.find(pair[0])][alphabetkey.find(pair[1])] = 1
    return base
