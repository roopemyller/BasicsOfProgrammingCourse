def valikko(): 
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Määritä askel")
    print("3) Tulosta merkkijono")
    print("0) Lopeta")
    while True:
        Valinta = int(input("Anna valintasi: "))
        if Valinta == 1:
            return 1
        elif Valinta == 2:
            return 2
        elif Valinta == 3:
            return 3
        elif Valinta == 0:
            print("Lopetetaan.\n")
            return 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")

def kysyMerkkijono():
    Mjono = input("Anna merkkijono: ")
    print("")
    return Mjono
    
def kysyAskel():
    Askel = int(input("Anna tulostuksessa käytettävä askel: "))
    print("")
    return Askel
def tulostaMerkkijono(Mjono, Askel):
    if Askel == 0:
        #Tulostus asteittain
        while len(Mjono) > 0:
            print(Mjono)
            Mjono = Mjono[:len(Mjono)-1]
        print("")
    else:
        #Tulostus suoraan merkkijonon leikkausoperaattorissa.
        print(Mjono[::Askel])
    print("")
def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Mjono = kysyMerkkijono()
        elif Valinta == 2:
            Askel = kysyAskel()
        elif Valinta == 3:
            tulostaMerkkijono(Mjono, Askel)
        else:
            break
    print("Kiitos ohjelman käytöstä.")


paaohjelma()