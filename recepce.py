zamestanciVPraci = ["Hana", "Klara", "Natalie", "Roman"]

zamestanciVPraci.append("Pavel")
hledamOsobu = "Pavel"

if hledamOsobu in zamestanciVPraci:
  print("Můžeš volajícího přepojit.")
else:
  print(f"{hledamOsobu} ještě není přítomen.")