# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 29.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T3.py
import sys
import jsonpickle

class TIEDOT(object):
    def __init__(self, Nimike, Tekija, ISBN, Varauksia, Niteita, Lisakappaleita, VarauksiaPerNide):
        self.Nimike = Nimike
        self.Tekija = Tekija
        self.ISBN = ISBN
        self.Varauksia = Varauksia
        self.Niteita = Niteita
        self.Lisakappaleita = Lisakappaleita
        self.VarauksiaPerNide = VarauksiaPerNide

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto")    
    print("2) Lue JSON tiedosto")
    print("3) Kirjoita CSV tiedosto")
    print("4) Kirjoita JSON tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))

def kysyTiedostoNimi(Kehote):
    Nimi = input("Anna " + Kehote + " tiedoston nimi: ")
    return Nimi


def lueCSV(Tiedosto, Kirjalista):
    try:
        L = open(Tiedosto, "r", encoding="utf-8")
        Rivi = L.readline()
        while True:
            Rivi = L.readline()
            Rivi = Rivi[:-1]
            if len(Rivi) == 0:
                break
            Rivi = Rivi.split(";")
            Kirja = TIEDOT(Rivi[0], Rivi[1], Rivi[2], int(Rivi[3]), int(Rivi[4]), int(Rivi[5]), float(Rivi[6]))
            Kirjalista.append(Kirja)
        L.close()
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu " + str(len(Kirjalista)) + " kirjan tiedot.")
    return Kirjalista

def lueJSON(Tiedosto, Kirjalista):
    try:
        L = open(Tiedosto, "r")
        Tiedot = L.read()
        Kirjalista = jsonpickle.decode(Tiedot)
        L.close()
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu " + str(len(Kirjalista)) + " kirjan tiedot.")
    return Kirjalista


def kirjoitaCSV(Tiedosto, Kirjalista):
    try:
        K = open(Tiedosto, "w", encoding="utf-8")
        K.write("Nimike;Tekijä;ISBN;Varauksia;Niteitä;Tilattuja lisäkappaleita;Varauksia / nide\n")
        for Kirja in Kirjalista:
            Rivi = Kirja.Nimike + ";" + Kirja.Tekija + ";" + Kirja.ISBN + ";" + str(Kirja.Varauksia) + ";" + str(Kirja.Niteita) + ";" + str(Kirja.Lisakappaleita) + ";" + str(Kirja.VarauksiaPerNide)
            K.write(Rivi + "\n")
        K.close()
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)    
    print("Tiedosto " + Tiedosto + " kirjoitettu.")
    return None

def kirjoitaJSON(Tiedosto, Kirjalista):
    try:
        K = open(Tiedosto, "w")
        Tiedot = jsonpickle.encode(Kirjalista, indent=4)
        K.write(Tiedot)
    
        K.close()
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)    
    print("Tiedosto " + Tiedosto + " kirjoitettu.")
    return None

def paaohjelma():
    CSVKirjat = []
    JSONKirjat = []
    while True:
        Valinta = valikko()
        if Valinta == 1:
            LuettavaCSV = kysyTiedostoNimi("luettavan CSV")
            CSVKirjat = lueCSV(LuettavaCSV, CSVKirjat)
        elif Valinta == 2:
            LuettavaJSON = kysyTiedostoNimi("luettavan JSON")
            JSONKirjat = lueJSON(LuettavaJSON, JSONKirjat)
        elif Valinta == 3:
            KirjoitettavaCSV = kysyTiedostoNimi("kirjoitettavan CSV")
            kirjoitaCSV(KirjoitettavaCSV, JSONKirjat)
        elif Valinta == 4:
            KirjoitettavaJSON = kysyTiedostoNimi("kirjoitettavan JSON")
            kirjoitaJSON(KirjoitettavaJSON, CSVKirjat)
        elif Valinta == 0:
            break
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print("")
    print("\nKiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof