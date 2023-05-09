######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 31.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py

# eof
import math
import random
def valikko():
    print("Mitä haluat tehdä?")
    print("1) Laske absoluuttinen arvo")
    print("2) Laske kertoma")
    print("3) Laske potenssi")
    print("4) Laske neliöjuuri")
    print("5) Arvo satunnaisluku")
    print("0) Lopeta")

def paaohjelma():
    random.seed(1)
    while True:
        valikko()
        Valinta = int(input("Anna valintasi: "))
        if Valinta == 0:
            print("Lopetetaan\n")
            break
        elif Valinta == 1:
            luku = float(input("Minkä luvun absoluuttinen arvo selvitetään: "))
            print("Luvun absoluuttinen arvo on " + str(round(math.fabs(luku), 1)))
        elif Valinta == 2:
            luku = int(input("Minkä luvun kertoma lasketaan: "))
            print("Luvun kertoma on " + str(math.factorial(luku)))
        elif Valinta == 3:
            luku = float(input("Mikä luku korotetaan potenssiin: "))
            potenssi = float(input("Mitä eksponenttia käytetään: "))
            print("Luku korotettuna eksponenttiin on " + str(round(math.pow(luku, potenssi), 1)))
        elif Valinta == 4:
            luku = float(input("Mikä luvun neliöjuuri lasketaan: "))
            print("Luvun neliöjuuri on " + str(round(math.sqrt(luku), 1)))
        elif Valinta == 5:
            print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
            min = int(input("Anna minimi (otetaan mukaan): "))
            max = int(input("Anna maksimi (otetaan mukaan): "))
            print("Arvottiin satunnaisluku " + str(random.randint(min, max)))
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print("")

    print("Kiitos ohjelman käytöstä.")
paaohjelma()
