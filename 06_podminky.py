# Hodnota typu bool
5 < 6 # Výsledek je True

vek = int(input("Zadej věk: "))

if vek >= 18:
    print("Můžeš vstoupit.")
else:
    print("Vstup zakázán.")

# Program vždy končí v první větvi, kde je podmínka splněna
if vek < 15:
    print("Utíkej za mámou.")
elif vek < 18:
    print("Chvíli počkej.")
elif vek == 18:
    # Pro porovnání musejí být znak "=" dvakrát za sebou, jinak je to pokus o přiřazení
    print("Máš to tak akorát.")
else:
    print("Můžeš vstoupit.")