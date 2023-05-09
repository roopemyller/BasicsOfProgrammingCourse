print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")
Alaraja = int(input("Anna lukualueen alaraja: "))
Ylaraja = int(input("Anna lukualueen yläraja: "))
Loytyko = False
while Alaraja <= Ylaraja:
    if Alaraja % 5 == 0:
        if Alaraja % 7 == 0:
            print(f"Luku {Alaraja} on jaollinen 5:llä ja 7:llä.")
            Loytyko = True
            break
        else:
            print(f"{Alaraja} ei ole jaollinen seitsemällä, hylätään.")
    else:
        print(f"{Alaraja} ei ole jaollinen viidellä, hylätään.")
    Alaraja += 1
if Loytyko == False:
    print("Alueelta ei löytynyt sopivaa lukua.")
if Alaraja < Ylaraja:
    print("Lopetetaan etsintä.")
print("Kiitos ohjelman käytöstä.")
