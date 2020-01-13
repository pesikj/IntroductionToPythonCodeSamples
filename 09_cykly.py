# Lze mít i seznam v seznamu
vydaje = [
    ['Pavel', 'toaletní papír', 100],
    ['Natálie', 'vajíčka', 80],
    ['Roman', 'máslo', 50]
]

suma_celkem = 0
for vydaj in vydaje:
    suma_celkem += vydaj[2]
