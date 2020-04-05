vek = 20
if vek >= 18:
  print("Můžeš si koupit lístek.")
  print("Už jsi plnoletý.")
else:
  print("Jsi moc mladý.")
  print("Vrať se za pár let.")

print("Konec programu.")

vek = 15
penize = 1000

if vek >= 18:
  print("Už jsi plnoletý.")
  if penize > 200:
    print("Můžeš si koupit lístek.")
  else:
    print("Nemáš dost peněz.")
else:
  print("Jsi moc mladý.")

body = 55

if body < 50:
  znamka = "F"
elif body < 60:
  znamka = "E"
elif body < 70:
  znamka = "D"
elif body < 80:
  znamka = "C"
elif body < 90:
  znamka = "B"
else:
  znamka = "A"
print(znamka)
