print("Anna kaksi kokonaislukua.")
Luku1 = int(input("Anna luku 1: "))
Luku2 = int(input("Anna luku 2: "))

print("Selvitetään, ovatko antamasi luvut parillisia.")
if Luku1 %2 == 0:
    print(f"Luku {Luku1} on parillinen.")
else:
    print(f"Luku {Luku1} on pariton.")
if Luku2 %2 == 0:
    print(f"Luku {Luku2} on parillinen.")
else:
    print(f"Luku {Luku2} on pariton.")

print("Selvitetään, kumpi antamistasi luvuista on pienempi.")
if Luku1 == Luku2:
    print(f"Luvut {Luku1} ja {Luku2} ovat yhtäsuuria.")
elif Luku1 > Luku2:
    print(f"Luku {Luku2} on pienempi.")
else:
    print(f"Luku {Luku1} on pienempi.")

print("Kiitos ohjelman käytöstä.")