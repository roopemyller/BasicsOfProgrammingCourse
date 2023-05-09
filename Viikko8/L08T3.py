######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T3.py

# eof
import datetime
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit")
    print("2) Laske ikä päivinä")
    print("3) Tulosta viikonpäivät")
    print("4) Tulosta kuukaudet")
    print("0) Lopeta")

def komponentit():
    pvmKlo = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    annettu = datetime.datetime.strptime(pvmKlo,  "%d.%m.%Y %H:%M")
    print("Annoit vuoden " + str(annettu.year))
    print("Annoit kuukauden " + str(annettu.month))
    print("Annoit päivän " + str(annettu.day))
    print("Annoit tunnin " + str(annettu.hour))
    print("Annoit minuutin " + str(annettu.minute))

def ikaPaivina():
    syntPvm = datetime.datetime.strptime(input("Anna syntymäpäivä muodossa pp.kk.vvvv: "), "%d.%m.%Y") 
    vertailuPvm = datetime.datetime(2000, 1, 1)
    erotus = vertailuPvm - syntPvm
    print("1.1.2000 henkilö oli " + str(erotus.days) + " päivää vanha.")

def viikonPaivat():
    paiva = datetime.datetime(2022, 10, 31)
    i = 0
    while i < 7: 
        print(paiva.strftime("%A"))
        paiva = paiva + datetime.timedelta(days=+1)
        i += 1

def kuukaudet():
    paiva = datetime.datetime(2022, 1, 1)
    i = 0
    while i < 12: 
        print(paiva.strftime("%b"))
        paiva = paiva + datetime.timedelta(days=+31)
        i += 1

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        valikko()
        Valinta = int(input("Anna valintasi: "))
        if Valinta == 0:
            print("Lopetetaan.\n")
            break
        elif Valinta == 1:
            komponentit()
        elif Valinta == 2:
            ikaPaivina()
        elif Valinta == 3:
            viikonPaivat()
        elif Valinta == 4:
            kuukaudet()
        else:
            print("Tuntematon valinta, yritä uudelleen.")
        print("")
    
    print("Kiitos ohjelman käytöstä.")
paaohjelma()