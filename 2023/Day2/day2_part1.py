import sys

#PARAMETERS
if (len(sys.argv) != 2):
  print(f"[USING] :\npython3 {sys.argv[0]} name_file")
  exit(1)

name_file = sys.argv[1]         #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lines = file.readlines()

#READING EACH LINE
base = [12,14,13]
couleurs = ['rouge', 'bleu', 'vert']
liste_num = []
couleurs = []
somme_num = 0
dico = {}
for line in lines :                 #for each line
  print("\n\nline : ", line)
  jeux = line.split(':')
  cubes = jeux[1].split(';')
  dico[jeux[0]] = []
  for c in cubes :
    lance = c.split(',')
    print("lance : ", lance)
    for la in lance :
      coul = la.strip().split(" ")
      couleurs.append([coul[1], coul[0]])
      
    print("couleurs : ", couleurs)
    dico[jeux[0]].append(couleurs)
    couleurs = []
    
    
    
print("\n\ndico : ", dico)

for cle in dico.keys() :
  print("\nClé : ", cle)
  print(dico[cle])
  for values in dico[cle] :
    print("Values : ", values)
    for v in values :
      print(" V : ", v)
      if ('red' in v[0]) :
        if int(v[1]) > base[0] :
          if (int(cle.strip().split(" ")[1]) not in liste_num) :
            liste_num.append(int(cle.strip().split(" ")[1]))
            print(liste_num)
            continue # on passe à au v suivant
      if ('green' in v[0]) :
        if int(v[1]) > base[1] :
          if (int(cle.strip().split(" ")[1]) not in liste_num) :
            liste_num.append(int(cle.strip().split(" ")[1]))
            print(liste_num)
            continue
      if ('blue' in v[0]) :
        if int(v[1]) > base[2] :
          if (int(cle.strip().split(" ")[1]) not in liste_num) :
            liste_num.append(int(cle.strip().split(" ")[1]))
            print(liste_num)
            continue # on passe à au v suivant
    
    
    print(liste_num)
    if liste_num != [] :
      for li in liste_num :
        somme_num+= li
      liste_num = []



print("\nSomme des nombre est : ", somme_num, "\n")

#CLOSING OF FILE
file.close()