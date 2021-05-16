import numpy as np
from mapper import createbigrams
from reducer import mergebigrams, getsummatrice, differencebigrams, labelreducer
from helper import createfreqbigram
from functools import reduce

# In deze main opgave stellen we twee kansverdelingstabellen op die gebruikt worden in
# het klassificeer-algoritme en passen we dit algoritme toe op teksten met gemixte talen.

englishtarget = "englishtext"
dutchtarget = "dutchtext"
mixedtarget = "target"

# Mapreduce 1: Nederlandse kansverdelingmatrix ophalen
# Stap 1: Lees bestand in
with open(dutchtarget) as infile:
    linesnl = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigramsnl = list(map(createbigrams,linesnl))
# Stap 3: Voeg de bigrammen samen (reduce)
totalbigramnl = reduce(mergebigrams,bigramsnl)
# Stap 4: Maak er een kansverdeling van (waardes
# worden vertaald naar 0-1 waar waarde = waarde/n, waar n de som is van alle elementen)
freqbigramnl = createfreqbigram(totalbigramnl)

# Mapreduce 2: Engelse kansverdelingmatrix ophalen
target = "englishtext"
# Stap 1: Lees bestand in
with open(target) as infile:
    linesen = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigramsen = list(map(createbigrams, linesen))
# Stap 3: Voeg de bigrammen samen (reduce)
totalbigramen = reduce(mergebigrams,bigramsen)
# Stap 4: Maak er een kansverdeling van (waardes
# worden vertaald naar 0-1 waar waarde = waarde/n, waar n de som is van alle elementen)
freqbigramen = createfreqbigram(totalbigramen)  # Een enkele matrix is terugegeven, map() is niet persee nodig hier.

# Mapreduce 3: Klassificeer de regels uit het gemixte bestand.
# Om dit te kunnen doen (en door limitaties van python en map()) stellen we de functie hier op.
# Door dit te doen kunnen we de matrixen inbouwen in de functie en kan de functie gewoon gebruikt
# worden in de map() functie.

def entropy_classifier(matrix:np.array):
    """Classifies a given bigram matrix by comparing it to the other matrices in this file."""
    # 2 talen ingeprogrammeerd, we moeten dus de 'error' uitrekenen tussen twee matrixen.
    labels = ["engels", "nederlands"]
    bigrams = [freqbigramen, freqbigramnl]
    preerrors = [0,0]
    errors = list(map(differencebigrams,bigrams,[matrix] * len(preerrors)))
    abserrors = list(map(abs,errors))
    sums = list(map(getsummatrice,abserrors))
    return labels[sums.index(min(sums))]

# Stap 1: Lees het bestand eerst weer in.
with open(mixedtarget) as infile:
    lines = infile.readlines()
# Stap 2: Maak bigrams van alle regels (map)
bigrams = list(map(createbigrams,lines))
# Stap 3: Maak van alle bigrams frequentietabellen (map)
freqbigrams = list(map(createfreqbigram, bigrams))
# Stap 4: Klassificeer de matrixen met het eerder opgestelde algoritme (map)
labels = list(map(entropy_classifier, freqbigrams))
# Stap 5: Breng de labels samen tot een enkele dictionary (reduce)
labeldict = reduce(labelreducer,labels,{"engels":0,"nederlands":0})
print(labeldict)