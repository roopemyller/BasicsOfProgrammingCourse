######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 17.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä LxTx.py

# eof

class AUTO():
    Merkki = ""
    Hinta = 0

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("3) Tallenna autojen tiedot tiedostoon")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))

def uusiAuto(Lista):
    UusiAuto = AUTO()
    UusiAuto.Merkki = input("Anna auton merkki: ")
    UusiAuto.Hinta = input("Anna auton hinta: ")
    Lista.append(UusiAuto)
    print("")
    return Lista

def tulostaAutot(Lista):
    print("Listalta löytyy seuraavat autot ja hinnat:")
    for Auto in Lista:
        print(Auto.Merkki, Auto.Hinta)
    print("")
    return None

def tallennaAutotTiedostoon(tallennettavaTiedosto, Lista):
    t = open(tallennettavaTiedosto, "w", encoding="utf-8")
    t.write("Auton merkki;Auton hinta\n")
    for Auto in Lista:
        t.write(Auto.Merkki + ";" + Auto.Hinta + "\n")
    print("Tapahtumat kirjoitettu tiedostoon '" + tallennettavaTiedosto + "'.\n")
    t.close()
    return None

def paaohjelma():
    tallennettavaTiedosto = input("Anna tallennettavan tiedoston nimi: ")
    Lista = []
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Lista = uusiAuto(Lista)
        elif Valinta == 2:
            tulostaAutot(Lista)
        elif Valinta == 3:
            tallennaAutotTiedostoon(tallennettavaTiedosto, Lista)
        elif Valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
paaohjelma()