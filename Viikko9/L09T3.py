######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 7.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T3.py

# eof
import sys

def lueTiedosto(Tiedosto, Lista):
    try:
        T = open(Tiedosto, "r", encoding="utf-8")
        while True:
            rivi = T.readline()
            if len(rivi) == 0:
                break        
            rivi = rivi [:-1]
            Lista.append(rivi)
        T.close()
        return Lista
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def analysoi(Lista):
    PalautettavaLista = []
    for Rivi in Lista:
        if len(PalautettavaLista) == 0:
            PalautettavaLista.append(Rivi) 
        elif Rivi != PalautettavaLista[len(PalautettavaLista) - 1]:
            PalautettavaLista.append(Rivi)
    return PalautettavaLista

def tulostaJaKirjoitaTiedostoon(Lista, KirjoitettavaTiedosto):
    print("Tiedostossa oli " + str(len(Lista)) + " eri automerkkiä.")
    try:
        K = open(KirjoitettavaTiedosto, "w", encoding="utf-8")
        for Merkki in Lista:
            print(str(Merkki))
            K.write(Merkki + "\n")
        K.close()
        return None
    except Exception:
        print("Tiedoston '" + KirjoitettavaTiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    

def paaohjelma():
    AutoMerkit = []
    LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    KirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    AutoMerkit = lueTiedosto(LuettavaTiedosto, AutoMerkit)
    if len(AutoMerkit) == 0:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        AutoMerkit = analysoi(AutoMerkit)
        tulostaJaKirjoitaTiedostoon(AutoMerkit, KirjoitettavaTiedosto)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()