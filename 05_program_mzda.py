"""
Program na výpočet čisté mzdy ze zadané hrubé mzdy.
"""

# Input vždy vrací string, i když uživatel zadá číslo
# Funkce input - uživatelský vstup
hruba_mzda = input("Zadej mzdu:")
# Teď máme hodnotu hruba_mzda jako string, musíme ji převést na int
# Převod provedeme pomocí funkce int()
# Lze provést i v jednom kroku
# Vkládání do sebe - pozor na pořadí - chléb a máslo (nejdříve opéct, potom namazat)
hruba_mzda = int(hruba_mzda)
superhruba_mzda = hruba_mzda *  1.338
dan_z_prijmu = superhruba_mzda * 0.15 - 2070
pojisteni = hruba_mzda * 0.11
cista_mzda = hruba_mzda - dan_z_prijmu - pojisteni
# Zde musíme naopak převést číslo na text
# Funkce print - výstup na konzoli
print("Tvoje čistá mzda bude: " + str(cista_mzda))
