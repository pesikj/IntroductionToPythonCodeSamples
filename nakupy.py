nakupy = [
  ["Pavel", "toaletní papír", 100],
  ["Ondra", "Savo", 80]
]

prvniNakup = nakupy[0]
# prvniNakup = ["Pavel", "toaletní papír", 100]
#print(f"{prvniNakup[0]} nakoupil {prvniNakup[1]} za {prvniNakup[2]} Kč.")

nakupy.append(["Ondra", "prací prášek", 500])

# posledniNakup = nakupy[-1]
# print(posledniNakup)

cenaPrasku = nakupy[-1][-1]

print(cenaPrasku)
