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
points1 = 0                         #cunter of current point of player 1
points2 = 0                         #cunter of current point of player 2
#X perdre
#Y nul
#Z gagnerd

for line in lines :                                         #for each line
    letters = line.split(" ")                               #letters
    if letters[0] == 'A' :                                  #if letter of the first player is A, pierre 1
        points1 += 1                                        #add point of rock
        if letters[1] == 'X' or letters[1] == 'X\n' :       #if match is lost
            points2 += 3                                    #add point of scissor for lost
            points1 += 6                                    #add match win by the player 1
        elif letters[1] == 'Y'  or letters[1] == 'Y\n' :    #if match is nul
            points2 += 1                                    #add point of rock
            points1 += 3                                    #add match nul
            points2 += 3                                    #add match nul
        elif letters[1] == 'Z'  or letters[1] == 'Z\n' :    #if match is win
            points2 += 2                                    #add point of paper
            points2 += 6                                    #add match win for player 1
    elif letters[0] == 'B' :                                #if letter of the first player is B, papier 2
        points1 += 2                                        #add point of paper
        if letters[1] == 'X'  or letters[1] == 'X\n' :      #if letter of the second player is X, pierre 1
            points2 += 1                                    #add point of rock
            points1 += 6                                    #add match win for player 1
        elif letters[1] == 'Y'  or letters[1] == 'Y\n' :    #if letter of the second player is Y, papier 2
            points2 += 2                                    #add point of paper
            points1 += 3                                    #add match nul for player 1
            points2 += 3                                    #add match nul for player 2
        elif letters[1] == 'Z'  or letters[1] == 'Z\n' :    #if letter of the second player is Z, ciseau 3
            points2 += 3            #add point of scissor
            points2 += 6                                    #add match win for player 2
    elif letters[0] == 'C':                                 #if letter of the first player is C, ciseau 3
        points1 += 3                                        #add point of scissor
        if letters[1] == 'X'  or letters[1] == 'X\n' :      #if letter of the second player is X, pierre 1
            points2 += 2                                    #add point of rock
            points1 += 6                                    #add match win for player 1
        elif letters[1] == 'Y'  or letters[1] == 'Y\n' :    #if letter of the second player is Y, papier 2
            points2 += 3                                    #add point of paper
            points1 += 3                                    #add match nul for player 1
            points2 += 3                                    #add match nul for player 2
        elif letters[1] == 'Z'  or letters[1] == 'Z\n' :    #if letter of the second player is Z, ciseau 3
            points2 += 1                                    #add point of scissor
            points2 += 6                                    #add match win for player 2



print("Points of player 1 :", points1)
print("Points of player 2 :", points2)
if max(points1, points2) == points1 :
    print("The winner is the player 1 ")
else :
    print("The winner is the player 2 ")

print("So the response is ", points2)
#CLOSING OF FILE
file.close() 