import sys, string

#PARAMETERS
if (len(sys.argv) != 2):
	#print(f"[USING] :\npython3 {sys.argv[0]} name_file")
	exit(1)

name_file = sys.argv[1]  #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lines = file.readlines()

#READING EACH LINE before more
dossiers = ''								#structure qui caracterise dans quel dossier ont est
fichiers = [] 
dossierCourant = ''
for line in lines :
	if line[0] == '$' :					#si on est une commande
		#print(line)
		l = line.split(' ')
		#print(l)
		if l[1] == 'cd' :
			if l[2] == '/\n' :						#si c'est le repertoire pere
				dossiers += '/'
				#print("dossiers / : ", dossiers)
			elif l[2] == '..\n' :					#si on descend
				i = len(dossiers)-1					#i pour dossier
				cpt = 0
				while i>0 :							#tant que c'est pas a zero donc pas tout parcouru
					if dossiers[-i] == '/' :
						cpt =+ 1
						if (cpt == 1) :
							dossiers = dossiers[:-i+1]		#-2 car a/ par ex
						elif cpt == 2 :
							dossierCourant = dossiers[-i+1:len(dossiers)].strip()+'/'
							break
					i -= 1
					dossierCourant = (l[2]).strip()+'/'
				#print("dossiers .. : ", dossiers)
			else :
				dossiers += l[2]						#ajouter la lettre
				dossiers = dossiers[:-1]				#enlever le \n
				dossiers += '/'							#ajouter /
				#print("dossiers lettre ", dossiers)
				dossierCourant = (l[2]).strip()+'/'
				print(dossierCourant, "dossierCourant")
		else : 											#je suis ls
			
			#print("dossier[-2:", dossierCourant)
			fichiers.append([dossierCourant.strip()])	#ajout du nom du dossier dans le tableau des fichiers pour avoir un nouveau dossier
			#print("fichiers : ", fichiers)
			continue									#on passe a la ligne suivante
	else :												#si on est pas une commande on fait un affichage
		#print("fichiers[-1]", fichiers[-1])
		fichiers[-1].append(line.strip())
print("fichiers apres ajouts du fichier : ", fichiers)
#on a dans fichiers la listes des dossiers et fichiers de chaque dossiers


#CLOSING OF FILE
file.close()


#PARCOURS DES FICHIERS
tabTaille = []
tailleDossier = 0
index = 0
for dossier in fichiers :						#parcours des fichiers contenu dans fichiers
	print("dossier", dossier)
	nomDossier = dossier[0][0]					#nom du dossier est dossier[0][0] sans le /
	#print("nomDossier = ", nomDossier)
	for fichier in dossier[1:] :					#pour chaque dossier sans le nom du dossier
		f = fichier.split(' ')
		#print("Liste des fichiers dans le dossier",nomDossier,":", f)
		if f[0] == 'dir' :
			d = f[1]
			#print("d: ", d)
			for i in range(len(fichiers)) :
				if fichiers[i][0] == d+'/' :
					#print("fichier", fichiers[i][0])
					index = i
			dossierCourant = fichiers[index]
			#print("dossierCourant : ", dossierCourant)
			for i in range(len(dossierCourant)) :
				if dossierCourant[i][:3] != "dir" and dossierCourant[i][-1] != '/' :
					number = ''
					for c in dossierCourant[i] :
						if c in string.digits :
							number += c
					tailleDossier += int(number)
			tabTaille.append([f[1], tailleDossier])
			#print("tab", tabTaille)
			tailleDossier = 0
		else :
			tailleDossier += int(f[0])
			#print("tailleDossier")

somme = 0
for dossier in tabTaille :
	if dossier[1] >= 100000 :
		#print(tabTaille[tabTaille.index(dossier)])
		tabTaille.pop(tabTaille.index(dossier))
	
for dossier in tabTaille : 
	somme += tabTaille[tabTaille.index(dossier)][1]
#print("tabTaille Finale :", tabTaille)

for dossier in tabTaille :
	print(tabTaille.index(dossier))
	for dossier2 in tabTaille.pop(tabTaille.index(dossier)) :
		for i in range(len(fichiers)) :
			print(fichiers[i])
			print(dossier2[0])
			if fichiers[i][0] == dossier2[0]+'/' :
				print("fichier", fichiers[i][0])
				index = i
		dossierCourant = fichiers[index]
		
		print("dossier", dossier)
		for case in dossierCourant :
			print("case", case[-1],dossier[0])
			if case[-1] == dossier[0] :
				#print("ouii")
				somme += dossier[1]
		
		print(dossier[1])

print("La somme est donc : ", somme)
