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
# Tehtävä L08T4Kirjasto.py

# eof

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
    T = open(Tiedosto, "r", encoding="utf-8")
    Lista = []
    while True:
        rivi = T.readline()
        if len(rivi) == 0:
            break        
        rivi = rivi [:-1]
        Lista.append(int(rivi))
    return Lista

def analyysi(Lista, Tulos):
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
    return None
    
def kirjoitaTiedostoon(tiedosto, Tulos):
    k = open(tiedosto, "w")
    k.write("Analyysin tulokset ovat seuraavat:\n")
    k.write("Datan pienin arvo on " + str(Tulos.pieninArvo) + ".\n")
    k.write("Datan suurin arvo on " + str(Tulos.suurinArvo) + ".\n")
    k.write("Datan summa on " + str(Tulos.summa) + ".\n")
    k.write("Datan keskiarvo on " + str(Tulos.keskiarvo) + ".\n")
    k.close()
    return None