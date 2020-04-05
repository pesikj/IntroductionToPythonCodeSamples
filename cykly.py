for znak in "martin":
  print(znak)

  print("Ahoj")

nakupy = [
  ["Pavel", "toaletní papír", 100],
  ["Ondra", "Savo", 80]
]
celkovaHodnota = 0
for nakup in nakupy:
  print(f"{nakup[0]} nakoupil {nakup[1]} za {nakup[2]} Kč.")
  celkovaHodnota = celkovaHodnota + nakup[2]
print(f"Celková hodnota je {celkovaHodnota} Kč.")