import sys

#PARAMETERS
if (len(sys.argv) != 2):
	print(f"[USING] :\npython3 {sys.argv[0]} name_file")
	exit(1)

name_file = sys.argv[1]  #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lines = file.readlines()

#READING EACH LINE before more
taille = len(lines[0])
line = []
for i in range(taille) :
	if len(lines[0][:14]) == 14 :
		line.append(lines[0][:14])							 #comme on a qu'une seule ligne
		lines[0] = lines[0][1:]

lui = 0
for case in line :
	lettres = [case[i] for i in range(14)]
	if lettres.count(lettres[0]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[1]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[2]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[3]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[4]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[5]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[6]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[7]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[8]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[9]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[10]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[11]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	if lettres.count(lettres[12]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	elif lettres.count(lettres[13]) != 1 :				#si le nombre delement du premier element n'est pas egal a 1 pas bon
		continue
	else :
		lui = line.index(case)
		break
print("Le numero est donc : ", lui + 14)




#CLOSING OF FILE
file.close()
