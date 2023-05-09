from re import A


print("Selvitetään sanojen aakkosjärjestys.")
Sana1 = input("Anna sana 1: ")
Sana2 = input("Anna sana 2: ")
if Sana1 < Sana2:
    print(f"'{Sana1}' on aakkosissa aiemmin kuin '{Sana2}'.")
elif Sana1 > Sana2:
    print(f"'{Sana2}' on aakkosissa aiemmin kuin '{Sana1}'.")
else:
    print(f"Sanat ovat samoja, '{Sana1}'.")


print("\nSelvitetään merkin sisältyminen merkkijonoon.")
Mjono = input("Anna merkkijono: ")
Merkki = input("Anna etsittävä merkki: ")
if Merkki in Mjono:
    print(f"Merkki '{Merkki}' sisältyy merkkijonoon '{Mjono}'.")
else:
    print(f"Merkki '{Merkki}' ei sisälly merkkijonoon '{Mjono}'.")

print("\nSelvitetään, onko sana palindromi.")
Sana = input("Anna testattava sana: ")
if Sana == Sana[::-1]:
    print(f"Sana '{Sana}' on palindromi.")
else:
    print(f"Sana ei ole palindromi.")
    print(f"Sana on etuperin '{Sana}' ja takaperin '{Sana[::-1]}'.")

print("Kiitos ohjelman käytöstä.")