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
# Tehtävä L08T5Kirjasto.py

# eof
class TUOTE():
    Tuotetunniste = None
    Lkm = None
    Hinta = None

class VARASTO():
    Arvo = 0

def kysyTiedostonimi(Kehote, VanhaNimi):
    print("Anna " + Kehote + " tiedoston nimi, nykyinen on '" + VanhaNimi + "'.")
    uusi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if uusi == "":
        return VanhaNimi
    return uusi

def analyysi(TiedostonRivit, Tuotteet, Varasto):
    for rivi in TiedostonRivit:
        Tuote = TUOTE()
        rivi = rivi.split(";")
        Tuote.Tuotetunniste = rivi[0]
        Tuote.Lkm = float(rivi[1])
        Tuote.Hinta = float(rivi[2])
        Tuotteet.append(Tuote)
        Varasto.Arvo = Varasto.Arvo + float(rivi[1]) * float(rivi[2])
    return Tuotteet

def lueTiedosto(Tiedosto):
    T = open(Tiedosto, "r", encoding="utf-8")
    Lista = []
    while True:
        rivi = T.readline()
        if len(rivi) == 0:
            break        
        rivi = rivi [:-1]
        Lista.append(rivi)
    T.close()
    return Lista

def kirjoitaTiedostoon(tiedosto, Tuotteet):
    K = open(tiedosto, "w")
    for Tuote in Tuotteet:
        K.write("{0:.2f}".format(Tuote.Hinta * Tuote.Lkm) + "\n")
    K.close()
    return None