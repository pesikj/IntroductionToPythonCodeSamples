pozadujeEuro = input("Kolik potrebujete euro? ")
pozadujeEuro = int(pozadujeEuro) #Toto je velmi důležité!
kurz = 27.84
cena = 12 * kurz
cena = round(cena)
print(f"Cena je {cena} Kc") # Novější zápis - od verze 3.6
print("Cena je " + str(cena) + " Kc") # Starší zápis - důležité je str()