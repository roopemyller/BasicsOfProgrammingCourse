print("Tämä ohjelma laskee risteilyhintoja.")
Hytti = input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
Sesonki = input("Onko sesonkiaika (k/e): ")
KantaA = input("Onko kanta-asiakas (k/e): ")
C = 79
B = round(1.1 * C)
A = round(1.6 * C)

if Hytti == "A":
    Hinta = A
    if Sesonki == "k" or Sesonki == "K":
        Hinta = Hinta * 2.75
    if KantaA == "k" or KantaA == "K":
        Hinta = Hinta * 0.9
elif Hytti == "B":
    Hinta = B
    if Sesonki == "k" or Sesonki == "K":
        Hinta = Hinta * 1.75
    if KantaA == "k" or KantaA == "K":
        Hinta = Hinta * 0.9
else:
    Hinta = C
    if Sesonki == "k" or Sesonki == "K":
        Hinta = Hinta * 1.5
    if KantaA == "k" or KantaA == "K":
        Hinta = Hinta * 0.9

print(f"{Hytti}-hytti maksaa {round(float(Hinta), 2)} euroa.")
print("Kiitos ohjelman käytöstä.")