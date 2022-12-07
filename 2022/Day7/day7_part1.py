import sys, string

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
dossiers = ''								#structure qui caracterise dans quel dossier ont est
fichiers = [] 
for line in lines :
	if line[0] == '$' :					#si on est une commande
		#print(line)
		l = line.split(' ')
		#print(l)
		if l[1] == 'cd' :
			if l[2] == '/\n' :			#si c'est le repertoire pere
				dossiers += '/'
				#print("dossiers / : ", dossiers)
			elif l[2] == '..\n' :		#si on descend
				dossiers = dossiers[:-2]			#-2 car a/ par ex
				#print("dossiers .. : ", dossiers)
			else :
				dossiers += l[2]				#ajouter la lettre
				dossiers = dossiers[:-1]			#enlever le \n
				dossiers += '/'					#ajouter /
				#print("dossiers lettre ", dossiers)
		else : 									#je suis ls
			fichiers.append([dossiers[-2:].strip()])	#ajout du nom du dossier dans le tableau des fichiers pour avoir un nouveau dossier
			#print("fichiers : ", fichiers)
			continue					#on passe a la ligne suivante
	else :								#si on est pas une commande on fait un affichage
		#print(fichiers[-1])
		fichiers[-1].append(line.strip())
#print("fichiers apres ajouts du fichier : ", fichiers)
#on a dans fichiers la listes des dossiers et fichiers de chaque dossiers


#CLOSING OF FILE
file.close()


#PARCOURS DES FICHIERS
tabTaille = []
tailleDossier = 0
index = 0
for dossier in fichiers :						#parcours des fichiers contenu dans fichiers
	nomDossier = dossier[0][0]					#nom du dossier est dossier[0][0] sans le /
	print("nomDossier = ", nomDossier)
	for fichier in dossier[1:] :					#pour chaque dossier sans le nom du dossier
		f = fichier.split(' ')
		print("Liste des fichiers dans le dossier",nomDossier,":", f)
		if f[0] == 'dir' :
			d = f[1]
			print("d: ", d)
			for i in range(len(fichiers)) :
				if fichiers[i][0] == d+'/' :
					print("fichier", fichiers[i][0])
					index = i
			dossierCourant = fichiers[index]
			print("dossierCourant : ", dossierCourant)
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
			#tailleDossier += int(f[0])
			print("tailleDossier")

somme = 0
for dossier in tabTaille :
	if dossier[1] >= 100000 :
		#print(tabTaille[tabTaille.index(dossier)])
		tabTaille.pop(tabTaille.index(dossier))
	
for dossier in tabTaille : 
	somme += tabTaille[tabTaille.index(dossier)][1]
print("tabTaille Finale :", tabTaille)

for dossier in tabTaille :
	for i in range(len(fichiers)) :
		if fichiers[i][0] == dossier[0]+'/' :
			print("fichier", fichiers[i][0])
			index = i
	dossierCourant = fichiers[index]
	print("dossierCourant", dossierCourant)
	print(dossier)
	print("coucou", ('dir '+dossier[0]) in fichiers[fichiers.index(dossierCourant)])

	print(dossier[0])
	if 'dir '+dossier[0] in fichiers[fichiers.index(dossierCourant)][0][0] in dossier[0] :
		print("ouii")
	print(dossier[1])

print("La somme est donc : ", somme)
