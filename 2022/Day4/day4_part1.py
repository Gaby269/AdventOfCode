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
cptPair = 0                                                 #ctp of number of pairs witch fully contain the other
for line in lines :                                         #for each line
    pairs = line.split(",")                                 #we split in 2 part
    pair1 = pairs[0].split("-")                             #we split in 2 part to know the begin and the end
    pair2 = pairs[1].split("-")                             #we split in 2 part to know the begin and the end
    if (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])) or (int(pair2[0]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1])):      #if contain in a sens and other sens
        cptPair+=1                                          #add the cunter

print("The total of pair witch fully contain the other is ", cptPair)


#CLOSING OF FILE
file.close() 