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
print(lines)

#READING EACH LINE
num_final = 0                           #num final of fool
liste_vue = []        
num_repet = 0
while num_repet == 0:
  
  if not lines:  # Si la line est vide, cela signifie que nous avons atteint la fin du fichier
    file.seek(0)  # Revenir au début du fichier
    continue  # Reprendre la lecture depuis le début
  else :
    for l in lines :                        #for each line
      if l[0] == "+" :
          num_final += int(l[1:])
          if num_final not in liste_vue :
            liste_vue.append(num_final)
          else :
            num_repet = num_final
            break
          break
      else :
          num_final -= int(l[1:])
          if num_final not in liste_vue :
            liste_vue.append(num_final)
          else :
            num_repet = num_final
            break
          break

print("La fréquence de répétition est est :", num_repet)

#CLOSING OF FILE
file.close()
