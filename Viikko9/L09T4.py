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
# Tehtävä L09T4.py

# eof

import L09T4Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))

def paaohjelma():
    luettavaTiedosto = ""
    kirjoitettavaTiedosto = ""
    Lista = []
    Tulos = L09T4Kirjasto.TULOS()
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            luettavaTiedosto = L09T4Kirjasto.kysyTiedostonimi("Luettavan", luettavaTiedosto)
            Lista = L09T4Kirjasto.lueTiedosto(luettavaTiedosto)
        elif Valinta == 2:
            L09T4Kirjasto.analyysi(Lista, Tulos)      
        elif Valinta == 3:
            if Tulos.pieninArvo == 0 and Tulos.suurinArvo == 0:
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.\n")
            else:
                kirjoitettavaTiedosto = L09T4Kirjasto.kysyTiedostonimi("Kirjoitettavan", kirjoitettavaTiedosto)
                L09T4Kirjasto.kirjoitaTiedostoon(kirjoitettavaTiedosto, Tulos)
        elif Valinta == 0:
            print("Lopetetaan\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
paaohjelma()