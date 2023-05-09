######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Roope Myller
# Opiskelijanumero: 000389129
# Päivämäärä: 17.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# -
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä LxTx.py

# eof
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää tuote listaan")
    print("2) Poista tuote listasta")
    print("0) Lopeta")
    return int(input("Valintasi: "))

def lisaaTuote(Ostoslista):
    Tuote = input("Anna lisättävä tuote: ")
    Ostoslista.append(Tuote)
    return Ostoslista

def poistaTuote(Ostoslista):
    print("Ostoslistassasi on " + str(len(Ostoslista)) + " tuotetta.")
    while True:
        Jarjestysnumero = int(input("Anna poistettavan tuotteen järjestysnumero: "))
        if Jarjestysnumero < 1 or Jarjestysnumero > len(Ostoslista):
            print("Indeksiä " + str(Jarjestysnumero) + " ei löydy.")
            print("Tuotteiden järjestysnumerot alkavat numerosta 1.")
        else:
            break
    del Ostoslista[Jarjestysnumero - 1]
    return Ostoslista

def tulostaLista(Ostoslista):
    Tulostus = ""
    for Tuote in Ostoslista:
        Tulostus = Tulostus + Tuote + " " 
    print(Tulostus)
    return None     

def paaohjelma():
    Ostoslista = []
    while True:
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        tulostaLista(Ostoslista)
        Valinta = valikko()
        if Valinta == 1:
            Ostoslista = lisaaTuote(Ostoslista)
            print("")
        elif Valinta == 2:
            Ostoslista = poistaTuote(Ostoslista)
            print("")
        elif Valinta == 0:
            print("Lopetetaan")
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            tulostaLista(Ostoslista)
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()

















