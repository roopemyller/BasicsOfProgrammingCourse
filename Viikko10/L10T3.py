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
# Tehtävä L010T3.py

import numpy

def paaohjelma():
    print("Tämä ohjelma testaa numpy-matriisin käyttöä.")
    Rivit = 4
    Sarakkeet = 4
    MatriisiA = numpy.zeros((Rivit, Sarakkeet), int)
    for Rivi in range(Rivit):
        for Sarake in range(Sarakkeet):
            MatriisiA[Rivi][Sarake] = (Rivi + 1) * (Sarake + 1)
    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(MatriisiA)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for Rivi in range(Rivit):
        for Sarake in range(Sarakkeet):
            print(MatriisiA[Rivi][Sarake], end=';')
        print()
    print()

    MatriisiA = numpy.delete(MatriisiA, numpy.s_[:], None)   
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof
