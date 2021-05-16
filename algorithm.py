import numpy as np
from mapper import createbigrams
from reducer import mergebigrams
from helper import createfreqbigram
from functools import reduce

target = "dutchtext"
# Stap 1: Lees bestand in
with open(target) as infile:
    linesnl = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigramsnl = list(map(createbigrams,linesnl))
# Stap 3: Voeg de bigrammen samen (reduce)
totalbigramnl = reduce(mergebigrams,bigramsnl)
freqbigramnl = createfreqbigram(totalbigramnl)

target = "englishtext"
# Stap 1: Lees bestand in
with open(target) as infile:
    linesen = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigramsen = list(map(createbigrams, linesen))
# Stap 3: Voeg de bigrammen samen (reduce)
totalbigramen = reduce(mergebigrams,bigramsen)
freqbigramen = createfreqbigram(totalbigramen)

# Variabelen voor de classifier:
labels = ["engels","nederlands"]
bigrams = [freqbigramen,freqbigramnl]

def entropy_classifier(matrix:np.array):
    """Classifies a given bigram matrix by comparing it to the other matrices in this file."""
    # 2 talen ingeprogrammeerd;

