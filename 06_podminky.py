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
    dost_penez = input("Máš 500 Kč [y/n] ? ")
    if dost_penez == 'y':
        print("Můžeš vstoupit.")
    else:
        print("Bez peněz sem nelez.")
else:
    print("Vstup zakázán.")

# Program vždy končí v první větvi, kde je podmínka splněna
if vek < 15:
    print("Utíkej za mámou.")
elif vek <= 17:
    print("Chvíli počkej.")
elif vek == 18:
    # Pro porovnání musejí být znak "=" dvakrát za sebou, jinak je to pokus o přiřazení
    print("Máš to tak akorát.")
else:
    print("Můžeš vstoupit.")
