# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 25.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T4.py

import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    Lista = []
    try:
        T = open(Nimi, "r")
        while True:
            rivi = T.readline()
            if len(rivi) == 0:
                break        
            rivi = rivi [:-1]
            Lista.append(int(rivi))
        T.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    Lista.sort()
    PieniIndeksi = 0
    SuuriIndeksi = len(Lista) - 1
    while PieniIndeksi < len(Lista):
        Pieni = Lista[PieniIndeksi]
        Suuri = Lista[SuuriIndeksi]
        if Pieni < (Suuri / 3):
            Luvut.Pienempi = Pieni
            Luvut.Suurempi = Suuri
            return Luvut
        PieniIndeksi += 1
        SuuriIndeksi -= 1
    return Luvut


def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    print(str(Aika))
    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
###########################################################################
# eof
