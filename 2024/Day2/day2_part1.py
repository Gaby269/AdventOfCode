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
somme_sur =0

for line in lines :
  line_split = [int(x) for x in line.split()]
  if len(line_split) != 0 :
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
      if sur == True :
        somme_sur+=1
    
    # Liste monte
    if line_split[0] <= line_split[1] :
      sur = True
      for i in range(len(line_split)-1) :
        if line_split[i] > line_split[i+1]:
          sur = False
          break
        if abs(line_split[i] - line_split[i+1]) < 1 or abs(line_split[i] - line_split[i+1]) > 3 :
          sur = False
          break
      if sur == True :
        somme_sur+=1
        
    

print("Somme des sur est : ", somme_sur, "\n")

#CLOSING OF FILE
file.close()