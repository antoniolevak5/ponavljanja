def kreiraj_pozdrav(ime):
  pozdravna_poruka = f"Pozdrav, {ime}!!"
  return pozdravna_poruka
pozdrav_za_manuela = kreiraj_pozdrav("Manuel")
pozdrav_za_tea = kreiraj_pozdrav("Teo")
print(pozdrav_za_manuela)
print(pozdrav_za_tea)
