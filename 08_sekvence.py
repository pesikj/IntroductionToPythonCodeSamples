# Jednorozměrný seznam 

# Kolik jsem uběhl za týden
ubehnuto = [3, 0, 0, 15, 2, 5, 9]
ubehnuto[0] # První hodnota v seznamu
ubehnuto[6] # Poslední hodnota v seznamu

# Smíme hosta pustit na party?
pozvani_hoste = ['Hana', 'Pavel', 'Klára', 'Natálie', 'Roman', 'Matěj']
prichozi = 'Pavel'
# Operátor in - je v seznamu?
if prichozi in pozvani_hoste:
    print('Pusť ho dovnitř!')
else:
    print('Host není na seznamu.')

# Seznam může kombinovat datové typy
chaoticka_data = [32, 'test', 4.3, True]

# Lze mít i seznam v seznamu
vydaje = [
    ['Pavel', 'toaletní papír', 100],
    ['Natálie', 'vajíčka', 80],
    ['Roman', 'máslo', 50]
]

# Jaký byl první nákup?
vydaje[0]

#Jaký byl poslední nákup?
vydaje[-1]

# Kolik stála vajíčka?
vydaje[1][2]
