Sana = input("Anna sana: ")
print("Antamasi sanan kolme ensimmäistä kirjainta ovat " + Sana[0:3])
print("Sanan neljä viimeistä kirjainta ovat " + Sana[-4:])
print("Kirjaimet 3, 4, 5 ja 6 ovat " + Sana[2:6])

print("\nSanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta: " + Sana[::3])
print("\nAntamasi sana '" + Sana + "' on takaperin '" + Sana[::-1] + "'.")

AloitusP = int(input("\nAnna aloituspaikka: "))
LopetusP = int(input("Anna lopetuspaikka: "))
Siirtyma = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla sana " + Sana + " tulostuu näin: " + Sana[AloitusP:LopetusP:Siirtyma])

print("\nAntamasi sanan pituus oli " + str(len(Sana)) + " merkkiä.")
print("Kiitos ohjelman käytöstä.")
