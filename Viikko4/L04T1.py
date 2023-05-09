AloitusArvo = int(input("Anna aloitusarvo: "))
LopetusArvo = int(input("Anna lopetusarvo: "))
print("\nToteutus for-lauseella:")
for Arvo in range(AloitusArvo, LopetusArvo + 1):
    print(Arvo, end = " ")
print("\n\nToteutus while-lauseella:")
while AloitusArvo <= LopetusArvo:
    print(AloitusArvo, end = " ")
    AloitusArvo += 1
print("\n\nKiitos ohjelman käytöstä.")