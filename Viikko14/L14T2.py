# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 15.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
############################1##########################################
# Tehtävä L14T2.py

import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
import pubcode

class TIEDOT(object):
    def __init__(self, Nimike, Tekija, ISBN, Varauksia, Niteita, Lisakappaleita, VarauksiaPerNide):
        self.Nimike = Nimike
        self.Tekija = Tekija
        self.ISBN = ISBN
        self.Varauksia = Varauksia
        self.Niteita = Niteita
        self.Lisakappaleita = Lisakappaleita
        self.VarauksiaPerNide = VarauksiaPerNide

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

def kirjoitaPdf(Tiedosto, Kirjalista):
    Kanvaasi = canvas.Canvas(Tiedosto, pagesize=A4)
    LeveysMM = A4[0] / 210
    KorkeusMM = A4[1] / 297
    X = LeveysMM * 20
    Y = A4[1] - KorkeusMM * 20

    

    Kanvaasi.showPage()
    Kanvaasi.save()
    return None

def paaohjelma():
    Kirjalista = []
    #LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    #Kirjalista = lueCSV(LuettavaTiedosto, Kirjalista)
    KirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitaPdf(KirjoitettavaTiedosto, Kirjalista)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()