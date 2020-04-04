# Jednorozměrný seznam 

# Kolik jsem uběhl za týden
ubehnuto = [3, 0, 0, 15, 2, 5, 9]
ubehnuto[0] # První hodnota v seznamu
ubehnuto[6] # Poslední hodnota v seznamu

# Kdo už je v práci?
zamestnanciVPraci = ['Hana', 'Klára', 'Natálie', 'Roman']

hledamOsobu = 'Pavel'
# Operátor in - je v seznamu?
if hledamOsobu in zamestnanciVPraci:
  print(f'{hledamOsobu} už na vás čeká.')
else:
  print(f'{hledamOsobu} tu zatím není.')

zamestnanciVPraci.append("Pavel")
if hledamOsobu in zamestnanciVPraci:
  print(f'{hledamOsobu} už na vás čeká.')
else:
  print(f'{hledamOsobu} tu zatím není.')

# Seznam může kombinovat datové typy
chaoticka_data = [32, 'test', 4.3, True]

# Lze mít i seznam v seznamu
vydaje = [
  ['Pavel', 'toaletní papír', 100],
  ['Natálie', 'vajíčka', 80]
]

zapomenutyNakup = ['Roman', 'máslo', 50]
vydaje.append(zapomenutyNakup)
print(vydaje)

# Jaký byl první nákup?
vydaje[0]

#Jaký byl poslední nákup?
vydaje[-1]

# Kolik stála vajíčka?
vydaje[1][2]
