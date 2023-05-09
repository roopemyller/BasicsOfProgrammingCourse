import string
def kirjoitaTiedostoon(tiedosto, alkuperRivi, muokatRivi):
    tiedosto.write(alkuperRivi + "\n")
    tiedosto.write("----> " + muokatRivi + "\n")
    return None
def tarkistaPalindromi(Mjono):
    tarkasteltava = ""
    # tarkistetaan onko numeroita ja poistetaan välilyönnit
    for char in Mjono:
        if char.isdigit():
            return -1
        elif char == " ":
            continue
        elif char.isalpha():
            tarkasteltava += char.lower()    
    # poistetaan välimerkit
    if tarkasteltava == tarkasteltava[::-1] and len(tarkasteltava) > 2:
        return tarkasteltava
    else:
        return -1
def paaohjelma():
    luettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    k = open(kirjoitettavaTiedosto, "w", encoding="utf-8")
    luettavaTiedosto = open(luettavaTiedosto, "r", encoding="utf-8")
    for rivi in luettavaTiedosto: 
        rivi = rivi[:len(rivi) - 1]
        Palindromi = tarkistaPalindromi(rivi)
        if Palindromi != -1:
            print(f"OK: '{rivi}'")
            kirjoitaTiedostoon(k, rivi, Palindromi)
        else:
            print(f"Ei OK: '{rivi}'")
    luettavaTiedosto.close()
    print("Kiitos ohjelman käytöstä.")
paaohjelma()