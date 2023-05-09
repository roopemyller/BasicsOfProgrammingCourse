# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 28.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T1.py
TARKISTUSMERKKI = {
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : "a",
    11 : "b",
    12 : "c",
    13 : "d",
    14 : "e",
    15 : "f",
    16 : "h",
    17 : "j",
    18 : "k",
    19 : "l",
    20 : "m",
    21 : "n",
    22 : "p",
    23 : "r",
    24 : "s",
    25 : "t",
    26 : "u",
    27 : "v",
    28 : "w",
    29 : "x",
    30 : "y",
}

def tarkistaHT(HTunnus):
    HTunnus = HTunnus.lower()
    if len(HTunnus) != 11:
        print("Henkilötunnusta ei hyväksytä.")
        return None
    else:
        HTunnus = HTunnus.split("-")
        ppkkvv = HTunnus[0]
        nnnt = HTunnus[1]
        t = nnnt[-1]
        nnn = nnnt[:-1]
        ppkkvvnnn= ppkkvv + nnn
        tarkistusmerkkiPitasOlla = int(ppkkvvnnn) % 31
        if str(TARKISTUSMERKKI[tarkistusmerkkiPitasOlla]) == t:
            print("Henkilötunnus hyväksytty.")
        else:
            print("Henkilötunnusta ei hyväksytä.")
            
    return None

def paaohjelma():
    HTunnus = input("Anna henkilötunnus: ")
    tarkistaHT(HTunnus)


    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()