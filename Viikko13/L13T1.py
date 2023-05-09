# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 5.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
############################1##########################################
# Tehtävä L13T1.py

import L13T1Kirjasto

def valikko():
    print("1) Anna tiedoston nimi")
    print("2) Lue tiedosto")
    print("3) Tulosta tiedot")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))


def paaohjelma():
    HenkiloLista = []
    LuettavaTiedosto = None
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            LuettavaTiedosto = L13T1Kirjasto.kysyNimi("luettavan")
        elif Valinta == 2:  
            if LuettavaTiedosto == None:
                print("Ei tietoja luettaksi, kysy tiedostonimi ennen lukemista.")
            else:
                HenkiloLista = L13T1Kirjasto.lueTiedosto(LuettavaTiedosto, HenkiloLista)
        elif Valinta == 3:
            if len(HenkiloLista) == 0:
                print("Ei tietoja tulostettavaksi, lue tiedot ennen tulostamista.")
            else:
                L13T1Kirjasto.tulostaTiedot(HenkiloLista)
        elif Valinta == 4:
            if len(HenkiloLista) == 0:
                print("Ei tietoja kirjoitettavaksi, lue tiedot ennen kirjoittamista.")
            else:
                L13T1Kirjasto.kirjoitaTiedosto("tulos.txt", HenkiloLista)
        elif Valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print("")    

    print("Kiitos ohjelman käytöstä.")
    HenkiloLista.clear()
    return None

paaohjelma()

# eof