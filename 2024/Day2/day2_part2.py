import sys

#PARAMETERS
if (len(sys.argv) != 2):
  print(f"[USING] :\npython {sys.argv[0]} test.txt")
  exit(1)

name_file = sys.argv[1]         #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lines = file.readlines()



def verifSur(line_split, somme_sur) :
  # Liste déscend
    if line_split[0] > line_split[1] :
      sur = True
      for i in range(len(line_split)-1) :
        if line_split[i] < line_split[i+1] :
          sur = False
          break
        if abs(line_split[i] - line_split[i+1]) < 1 or abs(line_split[i] - line_split[i+1]) > 3 :
          sur = False
          break
    
    # Liste monte
    if line_split[0] < line_split[1] :
      sur = True
      for i in range(len(line_split)-1) :
        if line_split[i] > line_split[i+1]:
          sur = False
          break
        if abs(line_split[i] - line_split[i+1]) < 1 or abs(line_split[i] - line_split[i+1]) > 3 :
          sur = False
          break

    if line_split[0] == line_split[1] :
      sur = False
    
    if sur == True :
      somme_sur+=1

    return somme_sur


#READING EACH LINE
somme_sur = 0

for line in lines :
  line_split = [int(x) for x in line.split()]
  
  if len(line_split) != 0 :
    somme_sur_tempo = verifSur(line_split, 0)
    somme_sur = somme_sur + somme_sur_tempo
    if somme_sur_tempo == 0 :
      line_split_total = line_split.copy()
      taille = len(line_split)
      for i in range(taille) :
        element_sup = line_split_total.pop(i)
        somme_tempo = verifSur(line_split_total, 0)
        if somme_tempo != 0:
          somme_sur += 1
          line_split_total = [int(x) for x in line.split()]
          break
        else :
          line_split_total = [int(x) for x in line.split()]

print("Somme des sur est : ", somme_sur, "\n")

#CLOSING OF FILE
file.close()