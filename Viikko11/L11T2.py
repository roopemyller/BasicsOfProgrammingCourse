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
# Tehtävä L11T2.py
def kaniPopulaatio(Kuukausi):
    Lista = [1, 2]
    while len(Lista) < Kuukausi:
        Lista.append(Lista[len(Lista) - 2] + Lista[len(Lista) - 1])
    print("Kanipariskuntia on " + str(Kuukausi) + " kuukauden kuluttua " + str(Lista[Kuukausi - 1]))
    return None

def paaohjelma():
    Kk = int(input("Anna kuukausien lukumäärä: "))
    kaniPopulaatio(Kk)
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
# eof
