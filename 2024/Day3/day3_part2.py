import sys
import re

#PARAMETERS
if (len(sys.argv) != 2):
  print(f"[USING] :\npython {sys.argv[0]} name_file")
  exit(1)

name_file = sys.argv[1]         #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lines = file.readlines()

#READING EACH LINE
resultat = 0
regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)'
actif = True
for line in lines :
  match = re.findall(regex, line)
  for mat in match :
    if mat == "do()" :
      actif = True
    elif mat == "don't()" :
      actif = False
    else :
      if actif :
        premier = int(mat.split(",")[0].split("(")[-1])
        deuxieme = int(mat.split(",")[1].split(")")[0])
        resultat += premier*deuxieme

print("Le résultat des multiples est : ", resultat, "\n")

#CLOSING OF FILE
file.close()