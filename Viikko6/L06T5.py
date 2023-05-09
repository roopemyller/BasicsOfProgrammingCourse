def tallenna(tiedosto, pvm, kulutus):
    k = "{0:.0f}".format(kulutus)
    valit = (5 - len(k)) * " "
    tiedosto.write(pvm + ":" + valit + k + "\n")
    return None

def paaohjelma():
    luettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    tallennettavaTiedosto = input("Anna tallennettavan tiedoston nimi: ")

    t = open(tallennettavaTiedosto, "w", encoding="utf-8")
    t.write("       Pvm:  kWh\n")
    
    #Luetaan rivi muokataan se sopivaksi kutsutaan tannella funktiota
    l = open(luettavaTiedosto, "r", encoding="utf-8")
    i  = 0
    pvm = ""
    kulutus = 0
    while True:
        rivi = l.readline()
        if i != 0:
            if len(rivi) == 0:
                tallenna(t, pvm, kulutus)
                break
            rivi = rivi[:-1]    
            rivi = rivi.split(" ")
            uusiRiviPvm = rivi[0]
            kulutusAlkiot = rivi[1].split(";")
            if pvm == uusiRiviPvm: 
                kulutus += float(kulutusAlkiot[1]) + float(kulutusAlkiot[2])
            else:
                if pvm != "":
                    tallenna(t, pvm, kulutus)
                pvm = uusiRiviPvm
                kulutus = float(kulutusAlkiot[1]) + float(kulutusAlkiot[2])
        i += 1
    l.close()
    t.close()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()