from mapper import createbigrams
from reducer import mergebigrams
from helper import createfreqbigram
from functools import reduce
target = "englishtext"
# Stap 1: Lees bestand in
with open(target) as infile:
    lines = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigrams = list(map(createbigrams, lines))
# Stap 3: Voeg de bigrammen samen (reduce)
totalbigram = reduce(mergebigrams,bigrams)
freqbigram = createfreqbigram(totalbigram)
