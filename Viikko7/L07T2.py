######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 17.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä LxTx.py

# eof

class TILI:
    Nimi = ""
    Saldo = ""

def maaritteleTili(Tili):
    Tili.Nimi = input("Anna pankkitilin nimi: ")
    Tili.Saldo = float(input("Anna pankkitilin saldo: "))
    return Tili

def tulostaTili(Tili):
    print("Pankkitilillä '" + Tili.Nimi + "' on nyt rahaa " + str(round(Tili.Saldo, 2)) + "e.")

def paaohjelma():
    UusiTili = TILI()
    UusiTili = maaritteleTili(UusiTili)
    tulostaTili(UusiTili)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()