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
# Tehtävä L08T2.py

# eof
import L08T2Kirjasto
def valikko():
    print("Minkä muunnoksen haluat tehdä?")
    print("1) Anna muunnettava tilavuus")
    print("2) Muunna litra gallon'ksi")
    print("3) Muunna litra pint'ksi")
    print("4) Muunna litra cup'ksi")
    print("5) Muunna litra fluid ounce'ksi")
    print("6) Muunna gallon litroiksi")
    print("7) Muunna pint litroiksi")
    print("8) Muunna cup litroiksi")
    print("9) Muunna fluid ounce litroiksi")
    print("0) Lopeta")
def paaohjelma():
    print("Käytetään kirjaston versiota " + L08T2Kirjasto.VERSIO)
    while True:
        valikko()
        Valinta = int(input("Anna valintasi: "))
        if Valinta == 0:
            print("Lopetetaan\n")
            break
        elif Valinta == 1:
            Tilavuus = float(input("Anna muunnettava tilavuus desimaalilukuna: "))
        elif Valinta == 2:
            print("Litrat muutettuina gallon'ksi: " + str(round(L08T2Kirjasto.litraGalloniksi(Tilavuus), 2)))
        elif Valinta == 3:
            print("Litrat muutettuina pint'ksi: " + str(round(L08T2Kirjasto.litraPintiksi(Tilavuus), 2)))
        elif Valinta == 4:
            print("Litrat muutettuina cup'ksi: " + str(round(L08T2Kirjasto.litraCupiksi(Tilavuus), 2)))
        elif Valinta == 5:
            print("Litrat muutettuina fluid ounce'ksi: " + str(round(L08T2Kirjasto.litraFluidOunceksi(Tilavuus), 2)))
        elif Valinta == 6:
            print("Gallon't muutettuina litroiksi: " + str(round(L08T2Kirjasto.gallonLitroiksi(Tilavuus), 2)))
        elif Valinta == 7:
            print("Pint't muutettuina litroiksi: " + str(round(L08T2Kirjasto.pintLitroiksi(Tilavuus), 2)))
        elif Valinta == 8:
            print("Cup't muutettuina litroiksi: " + str(round(L08T2Kirjasto.cupLitroiksi(Tilavuus), 2)))
        elif Valinta == 9:
            print("Fluid ounce't muutettuina litroiksi: " + str(round(L08T2Kirjasto.fluidOunceLitroiksi(Tilavuus), 2)))
        else:
            print("Tuntematon valinta, yritä uudelleen.")      
        print("")
    print("Kiitos ohjelman käytöstä.")
paaohjelma()