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

delka_zpravy = len("Moje zpráva")
print("Zpráva byla dlouhá " + str(delka_zpravy) + " znaků")

