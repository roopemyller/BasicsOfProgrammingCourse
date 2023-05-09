PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'
def tulostaOhjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.\n")

def kysyMerkkijono(kehote):
    Mjono = input(f"{kehote} merkkijono 5-15 merkkiä (enter lopettaa): ")
    return Mjono

def tarkistaMerkkijono(Mjono):
    if len(Mjono) < PITUUS_MIN:
        print(f"Liian lyhyt, {len(Mjono)} merkkiä.")
        return False
    elif len(Mjono) > PITUUS_MAX:
        print(f"Liian pitkä, {len(Mjono)} merkkiä.") 
        return False
    elif EROTIN in Mjono:
        print(f"Merkkijonossa on kielletty merkki '{EROTIN}'.")
        return False
    return True

def tulostaHyvaksytyt(Mjonot):
    print("Annoit seuraavat hyväksytyt merkkijonot:")
    MjonoLista = Mjonot.split(EROTIN)
    for Mjono in MjonoLista:
        print(Mjono)

def paaohjelma():
    tulostaOhjeet()
    kehote = "Anna"
    Mjonot = ""
    while True:
        Mjono = kysyMerkkijono(kehote)
        if Mjono == "":
            break
        if tarkistaMerkkijono(Mjono):
            kehote = "Anna seuraava"
            Mjonot = Mjonot + EROTIN + Mjono
        else:
            kehote = "Anna uusi"

    print("")
    tulostaHyvaksytyt(Mjonot[1:])
    print("Kiitos ohjelman käytöstä.")


paaohjelma()