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
repCourant = ''
rep = ''
for l in lines :
	print("l : ",l)
	line = l.split(' ')
	line = [l.strip() for l in line]
	print("line : ", line, "\n\n")
	if line[0] == '$' :
		if line[1] == "cd" :
			if line[2] == '/':				#je suis dans le boss
				repCourant = line[2]		#je suis dans le repetoire courant /
				rep += line[2]				#je lajoute a la liste des repetoires
				print("apres ajout : ", rep)
			elif line[2] == ".." :			#je veux descendre
				i = 1
				cpt = 0;						#compteur pour savoir cb de fois on le fait
    			while i<len(rep) : 
                    if rep[-i] == '/' :
                        cpt+=1
                        rep.pop(rep[-i+1:])
                        repCourant = rep[-1]
                    i+=1
				print("new rep : ", rep)
			else : 
				print(",dkkv")
		else :
			print("nfnvz")
	else : print("d,kfnzikf")

while i<len(rep)+1 :			#parcour a lenvers de rep
					#print("ancien rep : ", rep)
					if rep[-i] == '/' :		#si on trouve /
						cpt+=1				#on ajoute le fait que ce soit le rep qu'on sup
						rep.pop(rep[-i+1:])					#sup du rep le dernier rep
					#else :
					i+=1
#CLOSING OF FILE
file.close()