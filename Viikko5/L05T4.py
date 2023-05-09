def valikko():
    while True:
        print("Valitse haluamasi toiminto:")
        print("1) Syötä tiedot")
        print("2) Laske")
        print("3) Tulosta tulokset")
        print("0) Lopeta")
    
        Valinta = kysyLuku("Anna valintasi: ")
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
            print("Tuntematon valinta, yritä uudestaan.\n")

def kysyLuku(kehote):
    Luku = int(input(kehote))
    return Luku

def summa(Luku1, Luku2):
    return Luku1 + Luku2

def erotus(Luku1, Luku2):
    return Luku1 - Luku2

def tulostaTulokset(Luku1, Luku2, Summa, Erotus):
    print(f"Luvut ovat {Luku1} ja {Luku2}.")
    print(f"Lukujen summa on {Summa} ja erotus on {Erotus}.\n")

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        Valinta = valikko()
        if Valinta == 1:
            print("Syötä tiedot")
            Luku1 = kysyLuku("Anna kokonaisluku 1: ")
            Luku2 = kysyLuku("Anna kokonaisluku 2: ")
            print("")
        elif Valinta == 2:
            print("Laske")
            Summa = summa(Luku1, Luku2)
            Erotus = erotus(Luku1, Luku2)
            print("")
        elif Valinta == 3:
            print("Tulosta tulokset")
            tulostaTulokset(Luku1, Luku2, Summa, Erotus)
        else:
            break
    print("Kiitos ohjelman käytöstä.")

paaohjelma()