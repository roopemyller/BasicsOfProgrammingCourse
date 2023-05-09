print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")

while True:
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    if Valinta == 1:
        print("Syötä tiedot")
        Luku1 = int(input("Anna luku 1: "))
        Luku2 = int(input("Anna luku 2: "))
        print("")
    elif Valinta == 2:
        print("Laske\n")
        Summa = Luku1 + Luku2
    elif Valinta == 3:
        print("Tulosta tulokset")
        print(f"Lukujen summa on {Summa}.\n")
    elif Valinta == 0:
        print("Lopetetaan.\n")
        break
    else:
        print("Tuntematon valinta, yritä uudestaan.\n")
print("Kiitos ohjelman käytöstä.")
        