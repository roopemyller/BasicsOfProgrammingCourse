def paaohjelma():
    rivit = 0
    merkkia = 0
    tNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(tNimi, "r", encoding = "utf-8")
    for x in tiedosto:
        rivit += 1
        merkkia += len(x)
    print(f"Tiedostossa oli {rivit} nimeä ja {merkkia} merkkiä.")
    keskiArvo = float((merkkia - rivit) / rivit) 
    s = "{0:.0f}".format(keskiArvo)
    print(f"Keskimäärin nimen pituus oli {s} merkkiä.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
    