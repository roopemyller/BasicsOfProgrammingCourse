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
# Tehtävä L010T1.py
import sys

def kysyNimi(kehote):
    return input("Anna " + kehote + " tiedoston nimi: ")

def lueTiedosto(Tiedosto):
    Lista = []
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

def luoSanakirja(AutoMerkit):
    AutoSanakirja = {}
    AutonLukumaara = 0
    PohjaAuto = ""
    for Rivi in AutoMerkit:
        if len(AutoSanakirja) == 0:
            PohjaAuto = Rivi
            AutonLukumaara = 1
            AutoSanakirja[PohjaAuto] = AutonLukumaara
        else:
            if Rivi == PohjaAuto:
                AutonLukumaara += 1
                AutoSanakirja[PohjaAuto] = AutonLukumaara
            else:
                PohjaAuto = Rivi
                AutonLukumaara = 1
                AutoSanakirja[PohjaAuto] = AutonLukumaara
    return AutoSanakirja
    
def kirjoitaTiedosto(Tiedosto, AutoSanakirja):
    #Ensin printtaukset jotka lisätään listaan ja sit kirjoitetaan tiedosto listan avulla
    Tulostukset = []
    AutojenLkm = 0
    for Lkm in AutoSanakirja.values():
        AutojenLkm += Lkm
    print("Tunnistettiin " + str(len(AutoSanakirja)) + " automerkkiä ja " + str(AutojenLkm) + " autoa:")
    Tulostukset.append("Tunnistettiin " + str(len(AutoSanakirja)) + " automerkkiä ja " + str(AutojenLkm) + " autoa:")
    for Auto in AutoSanakirja.keys():
        if AutoSanakirja[Auto] == 1:
            print(Auto + ": " + str(AutoSanakirja[Auto]) + " auto")
            Tulostukset.append(Auto + ": " + str(AutoSanakirja[Auto]) + " auto")
        else:
            print(Auto + ": " + str(AutoSanakirja[Auto]) + " autoa")
            Tulostukset.append(Auto + ": " + str(AutoSanakirja[Auto]) + " autoa")
    try:
        K = open(Tiedosto, "w", encoding="utf-8")
        for Rivi in Tulostukset:
            K.write(Rivi + "\n")
        K.close()
    except Exception:
        print("Tiedoston '" + Tiedosto + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def paaohjelma():
    LuettavaTiedosto = kysyNimi("luettavan")
    KirjoitettavaTiedosto = kysyNimi("kirjoitettavan")
    AutoMerkit = lueTiedosto(LuettavaTiedosto)
    if len(AutoMerkit) == 0:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        AutoSanakirja = luoSanakirja(AutoMerkit)
        
        kirjoitaTiedosto(KirjoitettavaTiedosto, AutoSanakirja)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof