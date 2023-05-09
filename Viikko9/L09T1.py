######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 7.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T1.py

# eof
import sys

def lueTiedosto(Tiedosto):
    try:
        T = open(Tiedosto, "r", encoding="utf-8")
        Lista = []
        while True:
            rivi = T.readline()
            if len(rivi) == 0:
                break        
            rivi = rivi [:-1]
            Lista.append(int(rivi))
        T.close()
        print("Tiedoston '" + Tiedosto + "' lukeminen onnistui, " + str(len(Lista)) + " riviä.")
        return Lista
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)


def kirjoitaTiedostoon(Tiedosto, TiedostonRivit):
    try:
        T = open(Tiedosto, "w", encoding="utf-8")
        for Rivi in TiedostonRivit:
            T.write(str(Rivi) + "\n")
        T.close()
        print("Tiedoston '" + Tiedosto + "' kirjoittaminen onnistui.")
        return None
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)



def paaohjelma():
    TiedostonRivit = []
    LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    TiedostonRivit = lueTiedosto(LuettavaTiedosto)
    KirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitaTiedostoon(KirjoitettavaTiedosto, TiedostonRivit)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()