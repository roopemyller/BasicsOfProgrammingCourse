print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")
LopetusLuku = int(input("Kuinka monta merkkijonoa kysytään: "))
MinPituus = int(input("Mikä on merkkijonon minimipituus: "))
KielMerkki = input("Mitä merkkiä merkkijonossa ei saa olla: ")

Merkkijonot = []
while len(Merkkijonot) < LopetusLuku:
    Mjono = input("Anna merkkijono: ")
    if len(Mjono) < MinPituus:
        Merkkijonot.append(Mjono)
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        break
    elif KielMerkki in Mjono:
        Merkkijonot.append(Mjono)
        print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
        break
    else:
        Merkkijonot.append(Mjono)
if len(Merkkijonot) == LopetusLuku:
    print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")
print(f"Annoit {len(Merkkijonot)} merkkijonoa.")

Pisin = Merkkijonot[0]
for M in Merkkijonot:
    if len(M) > len(Pisin):
        Pisin = M

print(f"Pisin merkkijono oli '{Pisin}', jossa oli {len(Pisin)} merkkiä.")
print("Kiitos ohjelman käytöstä.")