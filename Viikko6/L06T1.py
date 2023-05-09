def tiedostoKirjoita(tiedostoNimi):
    tiedosto = open(tiedostoNimi, "w")
    while True:
        rivi = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if rivi == "":
            break
        tiedosto.write(rivi + "\n")
    tiedosto.close()
    return None

def tiedostoLue(tiedostoNimi):
    tiedosto = open(tiedostoNimi, "r")
    print(f"Tiedostoon '{tiedostoNimi}' on tallennettu seuraavat nimet:")
    for x in tiedosto:
        print(x, end="")
    tiedosto.close
    return None


def paaohjelma():
    tiedostoNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(tiedostoNimi)
    tiedostoLue(tiedostoNimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()