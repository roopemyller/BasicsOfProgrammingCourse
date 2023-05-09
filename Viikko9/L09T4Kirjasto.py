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
# Tehtävä L09T4Kirjasto.py

# eof
import sys

VERSIO = "1.0"

class TULOS():
    pieninArvo = 0
    suurinArvo = 0
    summa = 0
    keskiarvo = 0.0

def kysyTiedostonimi(Kehote, VanhaNimi):
    print(Kehote + " tiedoston nimi on '" + VanhaNimi + "'.")
    uusi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if uusi == "":
        return VanhaNimi
    else:
        return uusi

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
        print("Tiedosto '" + Tiedosto + "' luettu.\n")
        return Lista
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def analyysi(Lista, Tulos):
    if len(Lista) == 0:
        print("Ei analysoitavia tietoja, ei analysoitu.\n")
        return None
    min = 99999999999999999999999
    max = -1
    summa = 0
    for x in Lista:
        if x > max:
            max = x
        if x < min:
            min = x
        summa += x
    Tulos.pieninArvo = min
    Tulos.suurinArvo = max
    Tulos.summa = summa
    Tulos.keskiarvo = float(round(Tulos.summa / len(Lista)))
    print("Analyysi suoritettu.\n")
    return None
    
def kirjoitaTiedostoon(Tiedosto, Tulos):
    try:
        k = open(Tiedosto, "w")
        k.write("Analyysin tulokset ovat seuraavat:\n")
        k.write("Datan pienin arvo on " + str(Tulos.pieninArvo) + ".\n")
        k.write("Datan suurin arvo on " + str(Tulos.suurinArvo) + ".\n")
        k.write("Datan summa on " + str(Tulos.summa) + ".\n")
        k.write("Datan keskiarvo on " + str(Tulos.keskiarvo) + ".\n")
        k.close()
        print("Tulokset kirjoitettu tiedostoon.\n")
        return None
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)