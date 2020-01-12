vek = int(input("Zadej věk: "))

if vek >= 18:
    print("Můžeš vstoupit.")
else:
    print("Vstup zakázán.")

if vek >= 18:
    print("Můžeš vstoupit.")
elif vek >= 15:
    print("Chvíli počkej.")
else:
    print("Utíkej za mámou.")