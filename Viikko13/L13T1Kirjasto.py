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
# Tehtävä L13T1Kirjasto.py

import sys

class HENKILO():
    Nimi = None
    PuhNro = None
    Ika = None

def kysyNimi(Kehote):
    return input("Anna " + Kehote + " tiedoston nimi: ")

def lueTiedosto(Tiedosto, Lista):
    try:
        Lista.clear()
        L = open(Tiedosto, "r", encoding="utf-8")
        while True:
            Rivi = L.readline()
            if len(Rivi) == 0:
                break
            Rivi = Rivi[:-1]
            Rivi = Rivi.split(";")
            Henkilo = HENKILO()
            Henkilo.Nimi = Rivi[0]
            Henkilo.PuhNro = int(Rivi[1])
            Henkilo.Ika = int(Rivi[2])
            Lista.append(Henkilo)
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return Lista

def tulostaTiedot(HenkiloLista):
    for Henkilo in HenkiloLista:
        print(Henkilo.Nimi + " on " + str(Henkilo.Ika) + " vuotta vanha ja hänen puhelinnumero on 0" + str(Henkilo.PuhNro) + ".")
    return None

def kirjoitaTiedosto(Tiedosto, HenkiloLista):
    MinIka = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
    KirjoitettavatHenkilot = []
    for Henkilo in HenkiloLista:
        if Henkilo.Ika >= MinIka:
            KirjoitettavatHenkilot.append(Henkilo)
    try:
        K = open(Tiedosto, "w", encoding="utf-8")
        K.write("Tiedostossa on mukana " + str(len(KirjoitettavatHenkilot)) + " vähintään " + str(MinIka) + " vuotiasta henkilöä:\n")
        for x in KirjoitettavatHenkilot:
            K.write(x.Nimi + ";0" + str(x.PuhNro) + ";" + str(x.Ika) + "\n")
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None
# eof