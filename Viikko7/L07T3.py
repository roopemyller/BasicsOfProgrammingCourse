######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 17.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä LxTx.py

# eof


def paaohjelma():
    Tiedosto = input("Anna tiedoston nimi: ")
    t = open(Tiedosto, "r", encoding="utf-8")
    i = 1
    print("Kalastuskilpailun tulokset ovat seuraavat:")
    while True:
        rivi = t.readline()
        if len(rivi) == 0:
            break
        if i != 1:
            rivi = rivi[:-1]
            rivi = rivi.split(";")
            print("Joukkue '" + rivi[0] + "' sai kalan " + rivi[1] + ", joka oli " + rivi[2] + " cm.")
        i += 1
    print("Kiitos ohjelman käytöstä.")
    
paaohjelma()