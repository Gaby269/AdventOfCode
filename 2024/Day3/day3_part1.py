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
regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
for line in lines :
  match = re.search(regex, line)
  while match != None :
    match_liste = match.group()
    premier = match_liste.split(",")[0].split("(")[-1]
    deuxieme = match_liste.split(",")[1].split(")")[0]
    resultat += int(premier)*int(deuxieme)
    line = line.replace(match.group(),"$")
    match = re.search(regex, line)
  
    

print("Le résultat des multiples est : ", resultat, "\n")

#CLOSING OF FILE
file.close()