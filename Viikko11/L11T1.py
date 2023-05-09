######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 21.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä LxTx.py
def nelioJuuri(Luku):
    I = 1
    Pieni = 0
    while True:
        Potenssi = I * I
        if Potenssi  == Luku:
            print("Neliöjuuri on " + str(I))
            break
        elif Potenssi < Luku:
            Pieni = I
        else:
            if abs(Luku - (Pieni * Pieni)) < abs(Luku - (I * I)):
                print("Neliöjuuri on " + str(Pieni))
                break
            else:
                print("Neliöjuuri on " + str(I))
                break
        I += 1
    return None

def paaohjelma():
    Luku = int(input("Anna luku: "))
    nelioJuuri(Luku)
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof
