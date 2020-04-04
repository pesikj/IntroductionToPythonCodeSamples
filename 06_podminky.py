# Hodnota typu bool
5 < 6 # Výsledek je True

vek = int(input("Zadej věk: "))

# Vysvětlit odsazené bloky
if vek >= 18:
  print("Můžeš vstoupit.")
else:
  print("Vstup zakázán.")

# Podmínka v podmínce
if vek >= 18:
  dostPenez = input("Máš 500 Kč [y/n] ? ")
  if dostPenez == 'y':
    print("Můžeš vstoupit.")
  else:
    print("Bez peněz sem nelez.")
else:
  print("Vstup zakázán.")

# Program vždy končí v první větvi, kde je podmínka splněna
pocetBodu = 55
if pocetBodu < 60:
  znamka = 5
elif pocetBodu < 70:
  znamka = 4
elif pocetBodu < 80:
  znamka = 3
elif pocetBodu < 90:
  znamka = 2
else:
  znamka = 1
print(f"Znamka z testu je {znamka}")