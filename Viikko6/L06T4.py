def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    return int(input("Anna valintasi: "))
        
def kysyTiedostonimi(Kehote, VanhaNimi):
    print(f"{Kehote} tiedoston nimi on '{VanhaNimi}'.")
    uusi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if uusi == "":
        return VanhaNimi
    else:
        return uusi
    
def tiedostonMin(luettava):
    l = open(luettava, "r")
    min = 9999999999
    while True:
        rivi = l.readline()
        if len(rivi) == 0:
            l.close()
            return min
        if int(rivi) < min:
            min = int(rivi)

def tiedostonMax(luettava):
    l = open(luettava, "r")
    max = -1
    while True:
        rivi = l.readline()
        if len(rivi) == 0:
            l.close()
            return max
        if int(rivi) > max:
            max = int(rivi)

def kirjoitaTiedostoon(k, min, max):
    k.write("Analyysin tulokset ovat seuraavat:\n")
    k.write(f"Datan pienin arvo on {min}.\n")
    k.write(f"Datan suurin arvo on {max}.\n")
    return None

def paaohjelma():
    min = 0
    max = 0
    luettavaTiedosto = ""
    kirjoitettavaTiedosto = ""
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if kirjoitettavaTiedosto != "":
            k = open(kirjoitettavaTiedosto, "w")
        if Valinta == 1:
            print("Anna tiedostonimet")
            luettavaTiedosto = kysyTiedostonimi("Luettavan", luettavaTiedosto)
            kirjoitettavaTiedosto = kysyTiedostonimi("Kirjoitettavan", kirjoitettavaTiedosto)
            print("")
        elif Valinta == 2:
            print("Suoritetaan analyysi")
            min = tiedostonMin(luettavaTiedosto)
            max = tiedostonMax(luettavaTiedosto)
            print("")
        elif Valinta == 3:
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoitaTiedostoon(k, min, max)
            print("")
        elif Valinta == 0:
            print("Lopetetaan\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    print("Kiitos ohjelman käytöstä.")
    k.close()
paaohjelma()