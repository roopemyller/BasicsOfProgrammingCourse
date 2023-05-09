
def tulostaOhjeet(): 
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna nimesi kahdessa osassa.")

def kysyNimi(kehote):
    print("Tämä aliohjelma kysyy nimen.")
    Nimi = input(f"Anna {kehote}: ")
    return Nimi

def tulostaTulokset(Etunimi, Sukunimi):
    print("Tämä aliohjelma tulostaa nimesi.")
    print(f"Hei {Etunimi} {Sukunimi}")

def paaohjelma():
    tulostaOhjeet()
    Etunimi = kysyNimi("etunimi")
    Sukunimi = kysyNimi("Sukunimi")
    tulostaTulokset(Etunimi, Sukunimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()


