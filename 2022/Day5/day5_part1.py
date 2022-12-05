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
tab = []  #tab des element des colones
cptLine = 0  #cpt of number of line
for line in lines:  #for each line
	cptLine += 1
	cptEmpty = 0
	elem = line.split("    ")  #on split au niveau des espace
	print("elem", elem)
	if line[1] == "1": break
	for case in elem:
		if case == '' or case == '\n':
			cptEmpty += 1
			print("cptEmpty = ", cptEmpty)
			tab = tab.append(case)
		if case != '' and case != '\n':
			letters = case.split(' ')
			letters = [letters[i][1] for i in range(len(letters))]
			print("letters = ", letters)
			for let in letters:
				tab.append(let)
			print(tab)
			cptEmpty += 1
			#del elem[elem.index('')]

	print("cptLine = ", cptLine)

#CLOSING OF FILE
file.close()
