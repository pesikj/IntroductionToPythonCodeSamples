# Lze mít i seznam v seznamu
vydaje = [
    ['Pavel', 'toaletní papír', 110],
    ['Natálie', 'vajíčka', 80],
    ['Roman', 'máslo', 50]
]

for vydaj in vydaje:
  print(f"{vydaj[0]} koupil(a) {vydaj[1]} za {vydaj[2]} Kč")

vydaje = [
    ['Pavel', 'toaletní papír', 110.45],
    ['Natálie', 'vajíčka', 80.22],
    ['Roman', 'máslo', 5025]
]

# Hledání chyb v datech.
for vydaj in vydaje:
  if vydaj[2] > 1000:
    print(f"{vydaj[0]} koupil(a) {vydaj[1]} za {vydaj[2]} Kč")

sumaCelkem = 0
for vydaj in vydaje:
  sumaCelkem += vydaj[2]

print(f"Celkove castka je {sumaCelkem} Kč")