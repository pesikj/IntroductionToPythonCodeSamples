# Funkce Round
round(2.3343534)
round(2.9353434)

# Vstup může být proměnná
prumerZnamek = 2.3
round(prumerZnamek)

# Výstup můžu uložit do proměnné
znamkaNaVysvedceni = round(prumerZnamek)

# Můžu zaokrouhlit na daný počet desetinných místo
# Funkce může mít i více než jeden parametr
round(2.9353434, 2)
round(2.9353434, 3)

# Nestandardní chování
round(2.5)
round(3.5)
round(4.5)
round(5.5)

# Rychlá kontrola - telefonní číslo (bez předvolby) má mít 9 znaků
len("734123")

# Opuštění terminálu
exit()