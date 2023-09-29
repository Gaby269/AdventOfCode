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
cpt_base = 0                        #cpt pour savoir l'etage de sous sol en premier
for line in lines :                 #for each line
    for l in line :
        cpt_base+=1
        if l == "(" :
            num_fool+=1
            
        elif l == ")" :
            num_fool-=1
            if num_fool == -1 :
                break
            

print("The position of charactere that causes Santa in basement for the first time is :", cpt_base)

#CLOSING OF FILE
file.close()