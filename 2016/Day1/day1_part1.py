import sys
import re

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
num_right = 0                       #nombre de patté de maison à droite
num_left = 0                        #nombre de patté de maison à gauche
num 
for line in lines :                 #for each line
    liste = re.findall(r'\w+',line)
    for l in liste :
        
        if l[0] == "R" :
            num_right += int(l[1])
        elif l[0] == "L" :
            num_left+=int(l[1])
    print(num_right, num_left)

print("Chemin le plus court :", num_right+num_left)

#CLOSING OF FILE
file.close()