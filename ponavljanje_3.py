def kreiraj_pozdrav(ime):
  pozdravna_poruka = f"Pozdrav, {ime}!!"
  return pozdravna_poruka
pozdrav_za_anu = kreiraj_pozdrav("Ana")
pozdrav_za_marka = kreiraj_pozdrav("Marko")
print(pozdrav_za_anu)
print(pozdrav_za_marka)