NAULAA_KILOINA = 0.4536
JALKAA_SENTTEINA = 30.48
TUUMAA_SENTTEINA = 2.540
JALKAA_TUUMINA = 12

print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")
Paino = int(input("Anna paino kiloina: "))
print(f"Paino on {float(Paino)} kg eli {round(float(Paino) / NAULAA_KILOINA, 1)} naulaa.")
 
Pituus = int(input("\nAnna pituus sentteinä: "))
Jalkaa = Pituus // JALKAA_SENTTEINA
Tuumaa = Pituus / TUUMAA_SENTTEINA - Jalkaa * JALKAA_TUUMINA

print(f"Pituus on {Pituus / 100} metriä eli ", end="")
print(f"amerikkalaisittain {Jalkaa} jalkaa ", end="")
print(f"ja {round(Tuumaa, 1)} tuumaa.")
            
print("Kiitos ohjelman käytöstä.")
