######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 14.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L010T2.py
import sys

def kysyNimi(kehote):
    return input("Anna " + kehote + " tiedoston nimi: ")

def lueTiedosto(Tiedosto):
    Sanakirja = {}
    try:
        Sanakirja = {}
        T = open(Tiedosto, "r", encoding="utf-8")
        T.readline()
        while True:
            Rivi = T.readline()
            if len(Rivi) == 0:
                break        
            Rivi = Rivi[:-1]
            Rivi = Rivi.split(";")
            Pvm = Rivi[1]
            Pvm = Pvm.split("-")
            Vuosi = Pvm[0]

            if len(Sanakirja) == 0:
                Sanakirja[Vuosi] = 1  
            else:
                EiLisattu = True
                for OlevaVuosi in Sanakirja.keys():
                    if Vuosi == OlevaVuosi:
                        Lkm = Sanakirja[Vuosi] + 1
                        Sanakirja[Vuosi] = Lkm
                        EiLisattu = False
                        break
                if EiLisattu:
                    Sanakirja[Vuosi] = 1
        T.close()   
        return Sanakirja
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def tulosta(Sanakirja):
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    Vuodet = Sanakirja.keys()
    Vuodet = sorted(Vuodet, reverse = True)
    Summa = 0
    for Vuosi in Vuodet:
        Summa += Sanakirja[Vuosi]
        print(Vuosi + ": " + str(Sanakirja[Vuosi]))
    print("Yhteensä " + str(Summa) + " autoa.")
    
    return None

def paaohjelma():
    LuettavaTiedosto = kysyNimi("luettavan")
    Sanakirja = lueTiedosto(LuettavaTiedosto)
    tulosta(Sanakirja)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof