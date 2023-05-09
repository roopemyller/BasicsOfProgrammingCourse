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
# Tehtävä L08T5.py

# eof
import L08T5Kirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    return None

def paaohjelma():
    luettavaTiedosto = ""
    kirjoitettavaTiedosto = ""
    TiedostonRivit = []
    Tuotteet = []
    Varasto = L08T5Kirjasto.VARASTO()
    while True:
        valikko()
        Valinta = int(input("Valintasi: "))
        if Valinta == 1:
            luettavaTiedosto = L08T5Kirjasto.kysyTiedostonimi("luettavan", luettavaTiedosto)
            TiedostonRivit = L08T5Kirjasto.lueTiedosto(luettavaTiedosto)
            print("Tiedosto '" + luettavaTiedosto + "' luettu, " + str(len(TiedostonRivit)) + " riviä.\n")
        elif Valinta == 2:
            Tuotteet = L08T5Kirjasto.analyysi(TiedostonRivit, Tuotteet, Varasto)
            print("Tiedot analysoitu, varaston arvo on " + ("{0:.2f}".format(Varasto.Arvo)) + " EUR.\n")
        elif Valinta == 3:
            kirjoitettavaTiedosto = L08T5Kirjasto.kysyTiedostonimi("kirjoitettavan", kirjoitettavaTiedosto)
            L08T5Kirjasto.kirjoitaTiedostoon(kirjoitettavaTiedosto, Tuotteet)
            print("Tulokset tallennettu tiedostoon '" + kirjoitettavaTiedosto + "'.\n")
        elif Valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()