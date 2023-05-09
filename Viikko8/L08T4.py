######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T4.py

# eof

import L08T4Kirjasto

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
    Tulos = L08T4Kirjasto.TULOS()
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            luettavaTiedosto = L08T4Kirjasto.kysyTiedostonimi("Luettavan", luettavaTiedosto)
            Lista = L08T4Kirjasto.lueTiedosto(luettavaTiedosto)
            print("Tiedosto '" + luettavaTiedosto + "' luettu.\n")
        elif Valinta == 2:
            L08T4Kirjasto.analyysi(Lista, Tulos)
            print("Analyysi suoritettu.\n")
        elif Valinta == 3:
            kirjoitettavaTiedosto = L08T4Kirjasto.kysyTiedostonimi("Kirjoitettavan", kirjoitettavaTiedosto)
            L08T4Kirjasto.kirjoitaTiedostoon(kirjoitettavaTiedosto, Tulos)
            print("Tulokset kirjoitettu tiedostoon.\n")
        elif Valinta == 0:
            print("Lopetetaan\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
paaohjelma()