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
number = 1                          #number of elf witch have the max calorie 
cptNumber = 1                       #cunter of current number of elf
max = 0                             #cunter of calories max
cptCalorie = 0                      #cunter of current calories
for line in lines :                 #for each line
    if line != '\n' :               #if line is not empty
        cptCalorie += int(line)     #add the value of current line
    else :                          #if line is empty
        if max < cptCalorie :       #new max ?
            max = cptCalorie        #if yes we change max
            number = cptNumber      #change the current number max
        cptCalorie = 0              #put the cpt at 0
        cptNumber += 1              #add the current number of elf

print("Number of elf :", number, "\nNumber of calories :", max)

#CLOSING OF FILE
file.close()