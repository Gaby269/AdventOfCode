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
num_final = 0                           #num final of fool
for l in lines :                        #for each line
    
    if l[0] == "+" :
      num_final += int(l[1:])
    else :
      num_final -= int(l[1:])

print("La fréquence final est :", num_final)

#CLOSING OF FILE
file.close()
