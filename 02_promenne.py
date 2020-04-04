# Výpočet čisté mzdy

# Vzorec = hrubá mzda - daň z příjmu - pojištění

hruba_mzda = 50000
superhruba_mzda = hruba_mzda *  1.338
dan_z_prijmu = superhruba_mzda * 0.15 - 2070
pojisteni = hruba_mzda * 0.11
cista_mzda = hruba_mzda - dan_z_prijmu - pojisteni
cista_mzda

# Zkontrolovat to můžeme například zde: https://www.vypocet.cz/cista-mzda
# Nevychází to úplně přesně. Potřebovali bychom zaokrouhlování!

# Pracujeme kvalitně a tedy dostaneme přidáno
hruba_mzda = 44000
# Čistá mzda zůstane stejná
# Python upraví pouze hodnotu proměnné hruba_mzda, nic více!
cista_mzda
# K tomu, abych opět získal čistou mzdu, je potřeba znovu spustit výpočty
dan_z_prijmu = hruba_mzda * 1.34 * 0.15 - 2070
pojisteni = hruba_mzda * 0.11
cista_mzda = hruba_mzda - dan_z_prijmu - pojisteni
cista_mzda
