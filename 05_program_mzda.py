"""
Program na výpočet čisté mzdy ze zadané hrubé mzdy.
"""

# Pokud skládáme funkce, vyhodnocují se vždy zprava doleva
# Input vždy vrací string, i když uživatel zadá číslo
hruba_mzda = float(input("Zadej mzdu:"))
dan_z_prijmu = hruba_mzda * 1.34 * 0.15 - 2070
pojisteni = hruba_mzda * 0.11
cista_mzda = hruba_mzda - dan_z_prijmu - pojisteni
# Zde musíme naopak převést číslo na text
print("Tvoje čistá mzda bude: " + str(cista_mzda))
