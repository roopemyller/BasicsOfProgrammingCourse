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
# Tehtävä L09T2.py

# eof


def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")
    
def kysyValinta():
    while True:
        try:
            Valinta = int(input("Valintasi: "))
            return Valinta
        except ValueError:
            print("Anna Valinta kokonaislukuna.")

def indexError():
    Lista = [11,22,33,44,55]
    Indeksi = int(input("Anna indeksi 0-4: "))
    try:
        print("Listan arvo on " + str(Lista[Indeksi]) + " indeksillä " + str(Indeksi) + ".")
    except IndexError:
        print("Tuli IndexError, indeksi " + str(Indeksi) + ".")
    return None

def zeroDivisionError():
    Numero = 4
    Jakaja = int(input("Anna jakaja: "))
    try:
        print(str(Numero) + "/" + str(Jakaja) + " on " + "{0:.2f}".format(Numero / Jakaja) + ".")

    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja 0.")
    return None

def typeError():
    try:
        Numero = input("Anna numero: ")
        Tulo =  Numero * Numero
    except TypeError:
        print("Tuli TypeError, " + str(Numero) + "*" + str(Numero) + " merkkijonoilla ei onnistunut.")

def paaohjelma():
    while True:
        valikko()
        Valinta = kysyValinta()
        if Valinta == 0:
            print("Lopetetaan\n")
            break
        elif Valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.")
        elif Valinta == 2:
            indexError()
        elif Valinta == 3:
            zeroDivisionError()
        elif Valinta == 4:
            typeError()
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print("")
    
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()