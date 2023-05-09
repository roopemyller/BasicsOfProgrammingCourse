print("Selvitetään tuotteen alennusprosentti ja myyntihinta.")
Hinta = float(input("Mikä on tuotteen listahinta: "))
print("Lasketaanko hinta")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")
Valinta = int(input("Anna valintasi: "))
if Valinta == 1:
    KaytettyValinta = "Yhdellä monihaaraisella"
    if Hinta >= 300:
        AlennusProsentti = 30
        Hinta = Hinta * 0.7
    elif Hinta >= 200:
        AlennusProsentti = 20
        Hinta = Hinta * 0.8        
    elif Hinta >= 100:
        AlennusProsentti = 10
        Hinta = Hinta * 0.9   
    print(f"{KaytettyValinta} valintarakenteella tulokset ovat seuraavat:")
    print(f"Tuotteen alennus on {AlennusProsentti}% ja hinnaksi jää {round(Hinta, 2)}e.")   
elif Valinta == 2:
    KaytettyValinta = "Monella erillisellä"
    if Hinta >= 300:
        AlennusProsentti = 30
        Hinta = Hinta * 0.7
    if Hinta >= 200:
        AlennusProsentti = 20
        Hinta = Hinta * 0.8 
    if Hinta >= 100:
        AlennusProsentti = 10
        Hinta = Hinta * 0.9      
    print(f"{KaytettyValinta} valintarakenteella tulokset ovat seuraavat:")
    print(f"Tuotteen alennus on {AlennusProsentti}% ja hinnaksi jää {round(Hinta, 2)}e.")
else:
    print("Tuntematon valinta.")
    print(f"Tuotteen alennus on 0% ja hinnaksi jää {round(Hinta, 2)}e.")
print("Kiitos ohjelman käytöstä.")