import sys

#PARAMETERS
if (len(sys.argv) != 2):
  print(f"[USING] :\npython3 {sys.argv[0]} name_file")
  exit(1)

name_file = sys.argv[1]         #name of file witch use

# Vairable d'initialisation
freq_courante = 0
freq_vue = set()  # Use a set to store frequencies that have been seen

# Liste des fréquence à partir du fichier en prenant les negatif comme des -
liste_freq = [int(line.strip()) for line in open(name_file)]

while True:
    # Iterate through the list of freqs
    for freq in liste_freq:
        freq_courante += freq

        # Si la fréquence est présente deux fois
        if freq_courante in freq_vue:
            print("Première fréquence qui aparait 2 fois :", freq_courante)
            exit()  # On sort du programme

        # Ajouter la frequence vue au set
        freq_vue.add(freq_courante)
