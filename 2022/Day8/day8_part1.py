import sys

#PARAMETERS
if (len(sys.argv) != 2):
	print(f"[USING] :\npython3 {sys.argv[0]} name_file")
	exit(1)

name_file = sys.argv[1]  #name of file witch use

#READING OF FILE
file = open(name_file, "r")

#READING OF LINES
lignes = file.readlines()

#READING EACH LINE before more
colones = []						#tableau des colones
c = []								#tableau des colones courante
lines = []							#meme chose pour les lignes

#LIGNES
for line in lignes :				#pour chaqeu lignes
	l = []							#on met les lignes intermediaire
	l += line.strip()				#on ajoute a l les lignes separer en enlevant les \n
	#print(l)				
	lines.append(l)					#et on ajoute le tout a lines
print("Lignes : ", lines)

#COLONES.0
for i in range(len(lignes)) : 
	c = []							#on met les lignes intermediaire
	for line in lignes :			#pour chaqeu lignes
		c += line[i].strip()		#on ajoute a l les lignes separer en enlevant les \n
		#print(l)				
	colones.append(c)				#et on ajoute le tout a lines
print("Colones :", colones)

#CLOSING OF FILE
file.close()


somme_Visible = 0 									#COMPTEUR POUR SAVOIR  cb de arbre sont visibles

#VERIFICATION DES COLONES
cpt = 0
for li in lines :									#pour chaque ligne de lines
	for l in li[1:-1] :								#on prend que les 
		cpt+=1										#compteur pour l'indice de l
		visible = 0									#compteur qui nous dis cb de fois c'est visible
		if li[:cpt] != [] : 						#si la liste n'est pas vide 
			for c in li[:cpt] :						#on regarde les autre
				#print("l in ", li[1:-1], ": ", l, "/////c in ", li[:cpt], ":", c)
				if c < l :				
					visible += 1
		if visible == len(li[:cpt]) : 
			somme_Visible += 1						#si il est visible je le met
		else :										#sinon je fais la suite
			visible = 0								#compteur qui nous dis cb de fois c'est visible
			if li[cpt:] != [] : 					#SI LA LISTE N'EST PAS VIDE
				for c in li[cpt:]  :				#on regarde les autre
					#print("l in ", li[1:-1], ": ", l, "/////c in ", li[cpt:], ":", c)
					if c < l :		
						visible += 1
			if visible == len(li[cpt:]) :
				somme_Visible += 1					#si il est visible je le met


print(somme_Visible)