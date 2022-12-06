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

#READING EACH LINE pour avoir le tableau complet
tab = []  												#tab des element des colones
for line in lines:  									#for each line
	elem = line.split("    ")  							#on split au niveau des espaces grand pour avoir les [..]
	#print("elem", elem)
	if line[1] == "1": break							#si la ligne commence par un 1 alors on stop de lire
	for case in elem:									#pour chaque case de elem
		if case == '' or case == '\n':  				#si c'est une case vide ou un \n
			tab.append(case)  							#ajout de la case dans tab
		elif case != '' and case != '\n':				#sinon si la case est pas vide et pas egal a \n
			if case[0] != '[':  						#si c'est une case avec un espace devant car au milieu alors il lui manque un espace
				tab.append('')  						#on ajoute cet espace dans tab
				elem[elem.index(case)] = case[1:]		#on remplace la case dans elem par la case sans l'espace
				#print("tab = ", tab)
				letters = case[1:].split(' ')			#et on crée le tableau de lettre en splitant par les espace
				#print("letters :", letters)
			else:	
				letters = case.split(' ')				#sinon c'est ok on split direct par les espaces
			letters = [letters[i][1] for i in range(len(letters))]		#on enlve les crochet
			#print("letters = ", letters)
			for let in letters:							#pour chaque lettre 
				tab.append(let)							#on lajoute au tab
#print("tab :", tab)										#affichage de tab qui a donc tous les elements des colones et lignes

#READING TAB pour avoir une liste de liste de chaque éléments
line = 0								#on a un indice de ligne
colone = 0								#on a un indice de colonne
for case in tab:						#pour chaque case dans le tab
	if case != '\n':					#si c'est different de \n
		colone += 1						#on ajoute une colone
	else :								#sinon on ajoute une colone 
		colone += 1						
		break							#et on arrete
#print("colone = ", colone)				#affichage de la colonne

for case in tab:						#recparcour de tab
	if case == '\n' :					#si c'est un \n
		tab[tab.index(case)] = ''		#remplace le '\n' par ''
	line += 1							#et on ajoute tous les elemnt du tableau
line = line // colone					#on divise ce nombre par le nombre de colonne pour avoir les ligne
#print("line = ", line)					#affichage de ligne

#reecriture du tableau pour qu'il soit bien
colones = []							#on a le tableau des colones entiere
j = 0									#indice pour arriver au nombre de colone
while j != colone :						#tant que c'est ps le nombre de colone
	col = []							#on remet a zero la colonne courante
	for i in range(line):				#pour chaque indice parcourant les lignes
		col.append(tab[i * colone + j])	#on ajoute a col les elements du tableeau tab de chaqeu colonne
	#print(col)
	col.reverse()						#retouner la list
	colones.append(col)					#ajouter aux colones
	j += 1								#on passe au suivant

#print("colones = ", colones)

#enlver les ''
for colone in colones :
	case = ''
	colone_refaite = [value for value in colones[colones.index(colone)] if value != case]
	colones[colones.index(colone)] = colone_refaite

print("colones : ", colones)
#PARSEUR FINI DES COLONES


#MAINTENANT les moves
indications = []					#tableau des mouvements a faire
for line in lines :					#pour chaque ligne
	if line[0] == 'm' :				#si la ligne est un mouvement a faire
		phrase = line.split(' ')	#on split par les espaces
		indications.append([phrase[i] for i in [1,3,5]])	#et on ajoute a indications le tableau tel que ce soit le nombre de piece a bouger de la colonne X a la colonne Y
#print(indications)

#LECTURE de indications
for ind in indications :				#pour chaque indications
	print("Indicationn ", indications.index(ind))
	#RECUPERATION INFOS
	nb = int(ind[0])					#on stocke le nb de case a bouger
	de = int(ind[1])-1					#on stocke de quelle colone ca doit venir	
	pour = int(ind[2])-1				#on stocke pour quelle colone ca doit aller
	col_de = colones[de]				#on recupere les colones concerné
	col_pour = colones[pour]
	#TRAITEMENT
	col_pour.extend(col_de[-nb:])			#on ajoute les nb derniers elements 
	col_de = [c for c in col_de[:-nb]]		#et on supprier les nb dernier elem
	#REMET DANS COLONES
	colones[de] = col_de					#on remet col_de dans colones
	colones[pour] = col_pour				#on remet col_pour dans colones
	#print("new colone", colones)


#AFFICHAGE FINAL
dernierString = ''
for case in colones :
	#print(colones)
	dernierString = dernierString + case[-1]
print("La suite des derniers elements des colones est : ", dernierString)




#CLOSING OF FILE
file.close()