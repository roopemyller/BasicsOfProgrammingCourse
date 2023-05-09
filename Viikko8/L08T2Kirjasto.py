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
# Tehtävä L08T2Kirjasto.py

# eof

VERSIO = "1.0"

def litraGalloniksi(tilavuus):
    return tilavuus / 3.79

def litraPintiksi(tilavuus):
    return tilavuus / 0.47

def litraCupiksi(tilavuus):
    return tilavuus / 0.24

def litraFluidOunceksi(tilavuus):
    return tilavuus / 0.0296

def gallonLitroiksi(tilavuus):
    return tilavuus * 3.79
    
def pintLitroiksi(tilavuus):
    return tilavuus * 0.47

def cupLitroiksi(tilavuus):
    return tilavuus * 0.24

def fluidOunceLitroiksi(tilavuus):
    return tilavuus * 0.0296

