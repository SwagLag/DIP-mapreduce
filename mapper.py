# Mapper is een functie die je uitvoert over elk element in een lijst.
# In ons geval is dit elk woord in een zin, waar in. Daarom willen wij
# per woord dan gaan kijken naar het aantal letters wat er in zit.
import numpy as np

# alphabetkey = "abcdefghijklmnopqrstuvwxyz \"\',0123456789#:.!?"
alphabetkey = "abcdefghijklmnopqrstuvwxyz ,"
def padding(segment:str) -> str:
    """Prepares a given segment for reading."""
    return " " + segment + " "

def pairing(segment:str):
    """Gets all letterpairs from a given text (use infile.readlines()!)"""
    # print(segment)
    padding = " " + segment + " "
    pairs = []
    length = len(padding)  # Lengte van alles.
    for i in range(length-1):
        pairs.append("{}{}".format(padding[i],padding[i+1]))
    return pairs

# def createbigram(pairs:str) -> np.array:
#     """Creates a base numpy array for putting frequencies of certain combinations
#     into. Uses a built-in alphabet key, and the index of a character in this key
#     translates directly to the index on the matrix."""
#     base = np.full((len(alphabetkey), len(alphabetkey)), 0)
#     for pair in pairs:
#         base[alphabetkey.find(pair[0])][alphabetkey.find(pair[1])] = 1
#     return base

def createbigrams(segment:str):
    """Creates a set of bigrams from a given segment for each pair. These should
    be reduced later using the reducer function; mergebigrams(a,b)."""
    # Step 1: add padding to the given segment (which should be a rule ('regel'))
    # additionaly initiate all the variables that we're going to use.
    padding = " " + segment + " "
    length = len(padding)-1  # Exclude last index, else we will get a IndexError.
    bigram = np.full((len(alphabetkey), len(alphabetkey)), 0)  # Bigram for the pair.
    pairs = []  # Where pairs will be stored later.
    # Step 2: Get the pairs out of the rule.
    for i in range(length):
        pairs.append("{}{}".format(padding[i],padding[i+1]))
    # Step 3: Create bigram
    for pair in pairs:
        try:
            # str.find(letter) geeft -1 terug als hij geen valide letter vindt. We kunnen dat goed benutten op deze manier;
            # Hiermee slaan we letters die niet in de alphabetkey zitten over, door er None van te maken en een exception
            # te veroorzaken en zo bij de except te komen.
            firstletter = alphabetkey.find(pair[0].lower()) if alphabetkey.find(pair[0].lower()) >= 0 else None
            secondletter = alphabetkey.find(pair[1].lower()) if alphabetkey.find(pair[1].lower()) >= 0 else None
            bigram[firstletter][secondletter] += 1
        except:
            # print("DEBUG: Could not find letters in alphabetkey: pair: ({}{})".format(pair[0],pair[1]))
            continue
    return bigram