import sys

#PARAMETERS
if (len(sys.argv) != 2):
  print(f"[USING] :\npython3 {sys.argv[0]} name_file")
  exit(1)

name_file = sys.argv[1]         #name of file witch use

# Vairable d'initialisation
carburant_courant = 0
carburant_total = 0

with open(name_file, "r") as fichier:
    for l in fichier:
        carb = int(l)
        carburant_courant = int(carb/3) - 2
        carburant_total += carburant_courant

print("Le carburant nécessaire est ", carburant_total)
        
        
    