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


#CLOSING the file 
file.close()

#READING EACH LINE
top1 = 0                             #cunter of calories top1
top2 = 0                             #cunter of calories top2
top3 = 0                             #cunter of calories top3
cptCalorie = 0                       #cunter of current calories

for line in lines :                     #for each line
    if line != '\n' :                   #if line is not empty
        cptCalorie += int(line)         #add the value of current line
    else :                              #if line is empty
        if top1 < cptCalorie :          #new top ?
            top3 = top2                 #we change the top 3   
            top2 = top1                 #top 2 also
            top1 = cptCalorie           #and the top1
        elif top2 < cptCalorie :        #else if number 2 ?
            top3 = top2                 #we change the top 3   
            top2 = cptCalorie           #and the top2
        elif top3 < cptCalorie :        #else if number 3 ?
            top3 = cptCalorie
        cptCalorie = 0                  #put the cpt at 0


#FOR READING THE LAST ELF (if we don't add 2 '\n' in file text)
i = -1                      #cpt for while
nb_last_lines = 0           #number of last lines for the last elfe
while lines[i] != '\n' :    #while the line is not for an other elfe
    nb_last_lines += 1      #add number of last lines
    i -= 1

last_lines = [lines[i] for i in range (-nb_last_lines, 0)]      #add the last lines for the last elf 

#LAST ELF TREATMENT
cptCalorie = 0
for line in last_lines : 
    cptCalorie += int(line)          #put the cpt at 0
    if top1 < cptCalorie :          #new top ?
        top3 = top2                 #we change the top 3   
        top2 = top1                 #top 2 also
        top1 = cptCalorie           #and the top1
    elif top2 < cptCalorie :        #else if number 2 ?
        top3 = top2                 #we change the top 3   
        top2 = cptCalorie           #and the top2
    elif top3 < cptCalorie :        #else if number 3 ?
        top3 = cptCalorie

print("Number total of calories :", top1+top2+top3)

