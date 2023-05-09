Lukumaara = 0
Summa = 0
while True:
    Paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
    if Paino == 0:
        break
    elif Paino <= 130 and Paino >= 30:
        Summa = Summa + Paino
        Lukumaara += 1
    else:
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
print(f"Painojen keskiarvo on {round(Summa / Lukumaara, 1)}.")
print("Kiitos ohjelman käytöstä.")