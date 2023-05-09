def tulostaOhjeet(): 
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi\nlukujen lukumäärän.\n")

def kysyLuku(kehote):
    Luku = int(input(f"Anna {kehote}: "))
    return Luku

def vertaileLukuja(Luku1, Luku2):
    if int(Luku1) < int(Luku2):
        print(f"Annetuista luvuista pienempi oli {Luku1}.")
        return int(Luku1)
    elif int(Luku1) > int(Luku2):
        print(f"Annetuista luvuista pienempi oli {Luku2}.")
        return int(Luku2)
    else:
        print(f"Annetuista luvuista pienempi oli {Luku1}.")
        return int(Luku1)
        
def tulostaTiedot(PieniLuku, LukujenLkm):
    if LukujenLkm == 1:
        print(f"\nAnnoit yhden luvun, joka oli {PieniLuku}.")
    else:
        print(f"\nAnnoit {LukujenLkm} lukua.")
        print(f"Annetuista luvuista pienin oli {PieniLuku}.")
        
def paaohjelma():
    tulostaOhjeet()
    PieniLuku = 0
    LukujenLkm = 1

    while True:
        if LukujenLkm == 1:
            PieniLuku = kysyLuku("positiivinen kokonaisluku")
            Vertailtava = kysyLuku("vertailtava positiivinen kokonaisluku (0 lopettaa)")
            if Vertailtava == 0:
                break
            PieniLuku = vertaileLukuja(PieniLuku, Vertailtava)
        else:
            Vertailtava = kysyLuku("uusi positiivinen kokonaisluku (0 lopettaa)")
            if Vertailtava == 0:
                break
            PieniLuku = vertaileLukuja(PieniLuku, Vertailtava)
        LukujenLkm += 1
    tulostaTiedot(PieniLuku, LukujenLkm)
    print("Kiitos ohjelman käytöstä.")
    
paaohjelma()