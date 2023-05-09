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
# Tehtävä L12T2.py
def muunnaKymmenKantaiseksi(Bin):
    BinTakaperin = Bin[::-1]
    Potenssi = 0
    Luku = 0
    for Numero in BinTakaperin:
        Luku += int(Numero) * pow(2, Potenssi)
        Potenssi += 1
    return Luku

def paaohjelma():
    Bin1 = input("Anna ensimmäinen binaariluku: ")
    Bin2 = input("Anna toinen binaariluku: ")
    Num1 = muunnaKymmenKantaiseksi(Bin1)
    print("Bittijonosi " + Bin1 + " on kymmenkantaisena kokonaislukuna " + str(Num1))
    Num2 = muunnaKymmenKantaiseksi(Bin2)
    print("Bittijonosi " + Bin2 + " on kymmenkantaisena kokonaislukuna " + str(Num2))       

    print("Lukujen " + str(Num1) + " ja " + str(Num2) + " erotus on " + str(Num1 - Num2))
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()