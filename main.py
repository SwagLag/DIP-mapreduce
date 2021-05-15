from functools import reduce

# Variabelen
doelbestandnederlands = "dutchtext"
doelbestandengels = "englishtext"
doelbestandgemixt = "target"

# Importeer de juiste tools en funcs.
from mapper import createbigrams
from reducer import mergebigrams, mergesubbigrams
# Laad het bestand in
# with open(doelbestandnederlands) as infile:
#     stdinnl = infile.readlines()
# with open(doelbestandengels) as infile:
#     stdinen = infile.readlines()
with open(doelbestandgemixt) as infile:
    stdinmx = infile.readlines()
# Mapper 0: maakt een kleine voorbereiding per segment; door een padding toe te voegen worden ook de eerste en laatste letters
# meegeteld.
# paddednl = list(map(padding,stdinnl))
# paddeden = list(map(padding,stdinen))
# paddedmx = list(map(padding,stdinmx))
# Mapper 1: haalt de letterparen op.
# pairingnl = list(map(pairing,paddednl))
# pairingen = list(map(pairing,paddeden))
# pairingmx = list(map(pairing,paddedmx))
# Mapper 2: maakt van ieder paar een bigram
# matricesnl = list(map(createbigram,pairingnl))
# matricesen = list(map(createbigram,pairingen))
# matricesmx = list(map(createbigram,pairingmx))

# TODO: Al deze functies/calls kunnen samengevoegd worden in een grote functie.
# Reducer 1: voegt de aparte bigrams samen (hoeft eigenlijk alleen maar gebruikt te worden voor het trainen)
# bigmatricenl = reduce(mergebigrams, matricesnl)
# bigmatriceen = reduce(mergebigrams, matricesen)
preredbigmatrices = list(map(createbigrams, stdinmx))
print(preredbigmatrices)
# redbigmatrices = reduce(mergesubbigrams, preredbigmatrices)
print("debug access")
# Eerste reducer; breng alles onder tot een matrix (bigram) per regel.
# print(stdin)
# print(pairing[0])
# print(bigmatricenl)
# print(mapfunc("Hallo"))