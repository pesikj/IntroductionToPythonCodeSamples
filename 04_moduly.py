import math
# Popis funkcí v modulu je zde: https://docs.python.org/3/library/math.html

# Zaokrouhlování dolů
math.floor(3.2)
math.floor(3.5)
math.floor(3.9)
# Tato funkce "neumí" druhý parametr
# Tyto věci se neučíme nazpaměť, v případě potřeby se podíváme na web

# Zaokrouhlování nahoru
math.ceil(3.2)
math.ceil(3.5)
math.ceil(3.9)

# Cena hovoru do USA
delkaVSekundach = 549
# Platím za každou započetou minutu
math.ceil(delkaVSekundach/60) * 35

import random

# Hrací kostka
random.randint(1, 6)
# Náhodné číslo z rovnoměrného rozdělení
random.uniform(10, 15)

# Funkce můžeme i vkládat do sebe
round(random.uniform(10, 15), 2)
# Pozor, funkce se začínají vyhodnocovat zevnitř a předávají výsledek funkci venku
# Pokud to zatím není jasné, lze se tomu vyhnout. Stačí výsledek první funkce uložit do proměnné
# a ten předat další funkci.
nahodneCislo = random.uniform(10, 15)
zaokrouhleneCislo = round(nahodneCislo, 2)

# K čemu takové funkce jsou? Můžete například dělat simulace:
# https://www.washingtonpost.com/graphics/2020/world/corona-simulator/
