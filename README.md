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

# Instructies
Om de code zelf te runnen moet je eerst ervoor zorgen dat alles in
requirement.txt is gedownload. In principe is dat alleen maar numpy voor de arrays;
voor de rest wordt gebruik gemaakt van ingebouwde python modules.

Om doelwitbestanden aan te wijzen voor trainen van Nederlands en Engels,
en de uiteindelijk te classificeren bestand, kan je een paar variabelen in
main.py aanpassen;

- englishtarget: definieert het tekstbestand waarmee getraind wordt op
engelse zinnen.
- dutchtarget: hetzelfde als englishtarget, maar dan op nederlandse zinnen.
- mixedtarget: de uiteindelijk te classificeren tekst met regels.

Verder kan je ook de alfabetkey aanpassen; dit is een string waar alleen de
characters die voorkomen in de string meegeteld worden in de matrixen.
Verder vertaalt de index van een character in deze string zich ook naar
de plaats waar hij hoort te staan in de matrix.

Als dit allemaal ingesteld is is het heel simpel om de code te draaien;
run simpelweg gewoon main.py.

# Screenshots & Uitleg code
De code werkt als volgt;

In de eerste stap wordt er een bigram kansverdeling matrix opgesteld
van de nederlandse en engelse oefenteksten. Dit wordt gedaan natuurlijk via
een map/reduce structuur; in de mapper wordt de tekst omgezet naar paren,
waarna ze opgenomen worden in een matrix (waarbij de index op de matrix
overeenkomt met de 'alfabetkey' die in mapper.py gedefinieerd is). Deze
matrix wordt dan samengevoegd met een reduce tot een enkele matrix
waarin alle voorkomens van bepaalde combinaties zijn opgenomen en
tenslotte met een aparte functie omgezet wordt tot een kansverdelingstabel.

Voorbeeld array van kansverdeling voor Nederlands:

![screenshot see in github](https://github.com/SwagLag/DIP-mapreduce/blob/main/docimages/pycharm64_3eY3OltY9j.png?raw=true)

In de tweede stap wordt van de tekst met engelse en nederlandse
regels door elkaar deels hetzelfde gedaan; van regels naar paren
naar matrixen per regel, maar de matrixen worden hier niet samengevoegd
met een reduce. Wel worden ze ook per regel omgezet naar een kansverdelings-
matrix.

Tussentijds wordt de functie gedefinieerd om zo de teksten te kunnen
klassificeren; hiervoor moet in de functie de matrixen ingebouwd
worden van de kansverdelingen voor combinaties voor engels en
nederlands. Als dit gedaan is, wordt de 'gemixte' array vergeleken met
de andere taalmatrixen. Degene waar de matrix het meeste op lijkt, wordt gebruikt als
label voor de regel. Deze functie kan en wordt zo overigens gemapt over alle
beschikbare regels. Tenslotte wordt met een reduce de resultaten samengevoegd
tot een dictionary die presenteerbaar is.

Onderstaande afbeelding is ook meteen de performance van mijn
algoritme. Uiteindelijk klassificeerde hij in totaal 12 labels fout (het hoort
119 labels voor Engels te zijn en 73 voor Nederlands).

Uiteindelijke output:

![screenshot see in github](https://github.com/SwagLag/DIP-mapreduce/blob/main/docimages/pycharm64_lXcrSmeuW6.png?raw=true)