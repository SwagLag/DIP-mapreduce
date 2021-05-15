# DIP-mapreduce
Code for the DIP assignment 2 - character frequencies of the Hogeschool Utrecht DIP course.

# Architectuur
- main.py 

Bevat de code die gerunt hoeft te worden. Hierin wordt
een gegeven text als doel genomen (het doel kan je aanpassen als variabele
aan het begin), en daar wordt geteld hoeveel regels engels zijn en hoeveel
regels nederlands zijn.

- mapper.py

Bevat de functies voor de mapperfuncties, hierin wordt overigens
ook dutchbigram.py en englishbigram.py gerunt om zo de bigramtabellen
op te halen voor gebruik in de functies waarmee regels geclassificeerd worden.

- reducer.py

Bevat de functies voor het samenvoegen van de bigramtabellen waarbij
het structuur behouden wordt en alleen de waardes bij elkaar opgeteld
worden.

- englishbigram.py en dutchbigram.py

Dit zijn mapreduce programma's waarmee de frequentietabellen
opgesteld worden voor de nederlandse en engelse taal.