# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 21.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T3.py
def tulostus(Sana, Lukumaara, Indeksi):
    if Indeksi <= Lukumaara:
        print("Sana on '" + Sana + "', " + str(Indeksi) + ". kerta.")
        return tulostus(Sana, Lukumaara, Indeksi + 1)
    else:
        return None

def paaohjelma():
    Sana = input("Anna tulostettava sana: ")
    Lukumaara = int(input("Anna tulostuskertojen määrä: "))
    tulostus(Sana, Lukumaara, 1)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof