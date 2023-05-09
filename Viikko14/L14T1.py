# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 15.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
############################1##########################################
# Tehtävä L14T1.py

import math

def paaohjelma():
    VuotuisetKilometrit = float(input("Anna vuotuiset kilometrit: "))
    Kulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    PoltHinta = float(input("Anna polttoaineen hinta (€/l): "))
    Ika = int(input("Anna auton ikä vuosissa: "))
    Vakuutus = float(input("Anna vakuutusten määrä (euroissa): "))
    Bonus = int(input("Anna bonusprosentti kokonaislukuna: "))
    Verot = float(input("Anna verojen määrä: "))
    i = 1
    Yhteensa = 0
    while i <= 5:
        Summa = (VuotuisetKilometrit / 100) * (Kulutus * PoltHinta) + (Vakuutus - (Vakuutus * (Bonus / 100)) + Verot + 200 * math.sqrt(Ika))
        print(str(i) + ". vuosi: " + str(int(round(Summa, 0))))
        Yhteensa += Summa
        Ika += 1
        i += 1
    print("Viiden vuoden aikana autoon käytettiin rahaa " + str(int(round(Yhteensa, 0))) + " euroa.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof