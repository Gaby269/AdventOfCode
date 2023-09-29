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
num_fool = 0                        #num final of fool
for line in lines :                 #for each line
    for l in line :
        if l == "(" :
            num_fool+=1
        elif l == ")" :
            num_fool-=1

print("Number of fool :", num_fool)

#CLOSING OF FILE
file.close()