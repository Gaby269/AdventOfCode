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
list_num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_numero = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
chaine_num = ""
somme_num = 0
cpt = 0
for line in lines :                 #for each line
  
  line_modif = line
  for i in range(len(line)) :
    chaine_courante_3 = line[i:i+3]
    chaine_courante_4 = line[i:i+4]
    chaine_courante_5 = line[i:i+5]

    for num in list_num:
      if num == chaine_courante_3:
        line_modif = line_modif.replace(num, str(list_numero[list_num.index(num)]))
      elif num == chaine_courante_4:
        line_modif = line_modif.replace(num, str(list_numero[list_num.index(num)]))
      elif num == chaine_courante_5:
        line_modif = line_modif.replace(num, str(list_numero[list_num.index(num)]))
        
  for c in line_modif :
    if not c.isalpha() :
      chaine_num += c

  chaine_num = chaine_num.strip()

  if chaine_num:  # Vérifiez si la chaîne_num n'est pas vide
    num_courant = int(chaine_num[0] + chaine_num[-1])
    somme_num += num_courant
    chaine_num = ""
    

print("Somme des nombre est : ", somme_num, "\n")

#CLOSING OF FILE
file.close()