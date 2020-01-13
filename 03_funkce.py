# Absolutní číslo
abs(-10)

# Funkce Round
round(2.3)
round(2.9)

# Nestandardní chování
round(2.5)
round(3.5)
round(4.5)
round(5.5)

# Převody mezi typy
int('3') + 5
'3' + str(5)

float('5.5')

# Převod na stejný typ nehlásí chybu, ale je zbytečný
int(47)
float(47.47)
str('ahoj')

# Služba - zasílání výzvy k vyzvednutí zásilky
cislo_zasilky = '4509933'
vyzvednout_do = '22. 1. 2020'
dobirka = 350.5
print("Výzva k vyzvednutí zásilky " +  cislo_zasilky +" do " + vyzvednout_do+", dobírka " + str(dobirka) +" Kč.")
# Funkce format - přehlednější, nemusím převádět na str
print("Výzva k vyzvednutí zásilky {} do {}, dobírka {} Kč.".format(cislo_zasilky, vyzvednout_do, dobirka))

# Z tohoto bloku bychom mohli vytvořit vlastní funkci