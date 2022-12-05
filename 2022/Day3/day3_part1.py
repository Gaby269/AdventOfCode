import sys, string

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
priority = 0                                                #add priority of letter is in the part1 and part2 
letters = string.ascii_letters                              #concatenation of the lowercase letters [a-z] and the lowercase letters [A-Z]
for line in lines :                                         #for each line
    demiTaille = int(len(line)/2)                           #len / 2 of line
    part1 = line[0:demiTaille]                              #part1 of line
    part2 = line[demiTaille:len(line)]                      #part2 of line
    print(part1)
    print(part2)
    commonLetter = []
    for letter1 in part1 :                                  #for each letter1 in part1
        for letter2 in part2 :                              #for each letter2 in part2
            if letter1 == letter2 :                         #if the same letter
                if letter1 not in commonLetter :            #if the letter common is not find before now
                    commonLetter += letter1                 #add the commonLetter
                    priority += letters.index(letter1)+1    #add the current priority


print("The total priority is ", priority)


#CLOSING OF FILE
file.close() 