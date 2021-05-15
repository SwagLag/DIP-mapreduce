from mapper import createbigrams
from reducer import mergebigrams
from functools import reduce
target = "dutchtext"
# Stap 1: Lees bestand in
with open(target) as infile:
    lines = infile.readlines()
# Stap 2: Maak bigrams van alle regels.
bigrams = map(createbigrams, lines)
# Stap 3: Voeg de bigrammen samen