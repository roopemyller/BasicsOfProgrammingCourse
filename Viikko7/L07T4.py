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


class TULOS():
    pieninArvo = 0
    suurinArvo = 0
    summa = 0
    keskiarvo = 0.0

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Lue tiedosto")
    print("3) Analysoi")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))

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
    
def kirjoitaTiedostoon(k, Tulos):
    k.write("Analyysin tulokset ovat seuraavat:\n")
    k.write("Datan pienin arvo on " + str(Tulos.pieninArvo) + ".\n")
    k.write("Datan suurin arvo on " + str(Tulos.suurinArvo) + ".\n")
    k.write("Datan summa on " + str(Tulos.summa) + ".\n")
    k.write("Datan keskiarvo on " + str(Tulos.keskiarvo) + ".\n")
    return None    

def paaohjelma():
    luettavaTiedosto = ""
    kirjoitettavaTiedosto = ""
    Lista = []
    Tulos = TULOS()
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if kirjoitettavaTiedosto != "":
            k = open(kirjoitettavaTiedosto, "w")
        if Valinta == 1:
            print("Anna tiedostonimet")
            luettavaTiedosto = kysyTiedostonimi("Luettavan", luettavaTiedosto)
            kirjoitettavaTiedosto = kysyTiedostonimi("Kirjoitettavan", kirjoitettavaTiedosto)
            print("")
        elif Valinta == 2:
            Lista = lueTiedosto(luettavaTiedosto)
            print("Tiedosto '" + luettavaTiedosto + "' luettu.\n")
        elif Valinta == 3:
            analyysi(Lista, Tulos)
            print("Analyysi suoritettu.\n")
        elif Valinta == 4:
            kirjoitaTiedostoon(k, Tulos)
            print("Tulokset kirjoitettu tiedostoon.\n")
        elif Valinta == 0:
            print("Lopetetaan\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
    k.close()
paaohjelma()