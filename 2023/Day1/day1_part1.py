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
chaine_num = ""
somme_num = 0
for line in lines :                 #for each line
    for l in line :
        if not l.isalpha() :
            chaine_num += l
    chaine_num = chaine_num.strip()
    #print(chaine_num[0], chaine_num[-1])
    num = chaine_num[0] + chaine_num[-1]
    #print("chaine : ", num)
    somme_num += int(num)
    chaine_num = ""
    

print("Somme des nombre est : ", somme_num, "\n")

#CLOSING OF FILE
file.close()