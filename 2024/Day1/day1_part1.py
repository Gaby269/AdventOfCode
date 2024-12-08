import sys

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
chaine_num = ""
somme_num = 0
list1 = []
list2 = []
for line in lines :                 #for each line
  list_line = line.split()
  if len(list_line) != 0 :
    list1.append(int(list_line[0]))
    list2.append(int(list_line[1]))
    
list1.sort()
list2.sort()

somme_distance = 0
for l, m in zip(list1, list2) :
  somme_distance = somme_distance + abs(l-m)
  

print("Somme des distances est : ", somme_distance, "\n")

#CLOSING OF FILE
file.close()