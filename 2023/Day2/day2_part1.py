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
base = [12,13,14]
couleurs = ['rouge', 'bleu', 'vert']

chaine_num = ""
somme_num = 0
dico = {}
for line in lines :                 #for each line
  print(line)
  jeux = line.split(':')
  print(jeux)
  cubes = jeux[1].split(';')
  print(cubes)
  dico[jeux[0]] = []
  for c in cubes :
    lance = c.split(',')
    print(lance)
    dico[jeux[0]].append(lance)
print(dico)

for cle in dico.keys() :
  print(cle)
  print(dico[cle])
  for values in dico[cle] :
    print(values)
    for v in values :
      print(v)
      v = v.strip()
      s = v.split(" ")
      print(s)
      if (s[1] == 'red') :
        if s[0] > base[0] :
          break
  



print("\nSomme des nombre est : ", somme_num, "\n")

#CLOSING OF FILE
file.close()