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
priority = 0                                                    #add priority of letter is in the part1 and part2
letters = string.ascii_letters                                  #concatenation of the lowercase letters [a-z] and the lowercase letters [A-Z]
cptLine = 0                                                     #cpt of line
while cptLine != len(lines) :                                   #while the file is not finish
    for line in lines :                                         #for each line
        line1 = lines[cptLine]                                  #line1
        line2 = lines[cptLine+1]                                #line2
        line3 = lines[cptLine+2]                                #line3
        cptLine+=3                                              #add the cunter of line of 3 because we read 3 lines
        break                                                   #we stop the reading of line
    commonLetter = []
    for letter1 in line1 :                                      #for each letter1 in line1
        for letter2 in line2 :                                  #for each letter2 in line2
            for letter3 in line3 :                              #for each letter3 in line3
                if letter1 == letter2 and letter2 == letter3 :  #if the same letter
                    if letter1 not in commonLetter and letter1 != '\n' :            #if the letter common is not find before now
                        commonLetter += letter1                 #add the commonLetter
                        priority += letters.index(letter1)+1    #add the current priority

print("The total priority is ", priority)


#CLOSING OF FILE
file.close() 