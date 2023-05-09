print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:")
print("1) Tulosta merkkijono etuperin")
print("2) Tulosta merkkijono takaperin")
print("3) Tulosta merkkijonon pituus")
print("0) Lopeta")
Valinta = int(input("Anna valintasi: "))
if Valinta != 0:
    Mjono = input("Anna merkkijono: ")
    if Valinta == 1:
        #Etuperin
        print(f"Merkkijono on etuperin '{Mjono}'.")
    elif Valinta == 2:
        #Takatperin
        print(f"Merkkijono on takaperin '{Mjono[::-1]}'.")
    elif Valinta == 3:
        #Pituus
        print(f"Merkkijonon pituus on {len(Mjono)}.")
print("Kiitos ohjelman käytöstä.")
