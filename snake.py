from tkinter import*
from random import randrange



def replace(tab,rempla,index): #io mremplace zavatra ao anaty tableau a l'indice index
	tempo = []
	for x in range(len(tab)):
		if (x == index):
			tempo.append(rempla)
		else :
			tempo.append(tab[x])	

	return tempo		

def delete(tab,indice): # mamafa element anankiray ao anaty tableau
	newTab = []
	for x in range(len(tab)):
		if (x == indice):
			pass
		else:	
			newTab.append(tab[x])
	return newTab	
			

def move(): #Eto izy no mihetsika
	# global cx,cy
	global coordoX,coordoY
	global tabSens
	if (flag == 1):
		for x in range(len(square)):# ny isan'ireo carre
			if(x == 0): # pour la tete du serpent 
				way = tabSens[x][0]
			else: 
			# Pour le corps du serpent ca consiste a lire l'element 0 et de remplacer le dernier sens avec celui du premier
				way = tabSens[x][0]
				tempo = delete(tabSens[x],0)
				tempo.append(tabSens[0][0])
				tabSens = replace(tabSens,tempo,x)
				
				# del(tabSens[x][0])
				# tabSens[x].append(tabSens[0] [0])

				# tabSens[x].append(tabSens[x - 1] [len(tabSens[x - 1]) - 1])
			if (way == "h"):
				cx = coordoX[x] + 0
				cy = coordoY[x] - lg
			if (way == "b"):
				cx = coordoX[x] + 0
				cy = coordoY[x] + lg
			if (way == "g"):
				cx = coordoX[x] - lg
				cy = coordoY[x] + 0
			if (way == "d"):
				cx = coordoX[x] + lg
				cy = coordoY[x] + 0
                                                                      
			coordoX = replace(coordoX,cx,x)
			coordoY = replace(coordoY,cy,x)
			canvas.coords(square[x],coordoX[x] - lg / 2,coordoY[x] - lg / 2,coordoX[x] + lg / 2,coordoY[x] + lg / 2)
			
			# if (coordoX[x] >= canWi or coordoX[x] <= 0):
			# 	pauseMove()
			# elif(coordoY[x] >= canHei or coordoY[x] <= 0):
			# 	pauseMove()	
			
			# On met a jours les coordonnes
		# print(coordoX)
		# print(tabSens)
		# coordoX = replace(coordoX,cx,x)
		# coordoY = replace(coordoY,cy,x)
		ctx.after(100,move)
	else :
		pass	


def letMove():
	if (flag == 1):
		move()

color = ["black","green","blue","turquoise","magenta","purple"]	
deb = []
# le append ne comporte pas de probleme , ca vient plutot d'un autre bloc de code
def append(): # ajouter un nouveau carre
	global tabSens
	global coordoX,coordoY
	send = [] #Juste temporaire
	count = 1
	for x in range(len(tabSens[len(tabSens) - 1]) + 1): # le tableau de sens de chaque corps est +1 de celui de son precedent
		# On copie 2 fois le premier element du tab precedent 
		# Principe de rattrapage du corps precedent leizy
		if(x >= 2):
			send.append(tabSens[len(tabSens) - 1][count]) # On copie l'integralite de tabSens du tab precedent a partir de count = 1
			count += 1
		else:
			send.append(tabSens[len(tabSens) - 1][0]) # On doit copier le premier element du tab precedent




	tabSens.append(send)
	index = randrange(5)
	colo = color[index]
	lx = len(coordoX)
	ly = len(coordoY)
	
	# On lit dans quelle sens le precedent corps va se deplacer
	# c-a-d que On lit le premier element du tabSens deu corps precedent
	if (tabSens[len(tabSens) - 1][0] == "h"):
		sensoX = 0
		sensoY = lg
	if (tabSens[len(tabSens) - 1][0] == "b"):
		sensoX = 0
		sensoY = -lg
	if (tabSens[len(tabSens) - 1][0] == "g"):
		sensoX = lg
		sensoY = 0
	if (tabSens[len(tabSens) - 1][0] == "d"):
		sensoX = -lg
		sensoY = 0
	nx = coordoX[lx - 1] + sensoX
	ny = coordoY[ly - 1] + sensoY
	carre = canvas.create_rectangle(nx - lg / 2 ,ny - lg / 2,nx + lg / 2 ,ny + lg / 2,fill = colo)
	square.append(carre)
	coordoX.append(nx)
	coordoY.append(ny)


def startMove():
	global flag,proof,deb
	flag = 1
	if (proof == 1):
		letMove()
	else :
		pass
	proof = -1

def pauseMove():
	global flag,proof
	flag = 0
	proof = 1
	letMove()


def replaceAll(tab,sensa): # C'est specifique pour le serpent
		#On met a jour le tabSens de chacun des corps 
	for i in range(len(tab)):
		tempo = replace(tab[i],sensa,len(tab[i]) - 1)
		tab = replace(tab,tempo,i)
	return tab	


# Je ne sais pas encore si c'est une question de timing ou bien autre chose mais ca ne marche pas encore


#C pour le changemnt de sens
def haut(event):
	global tabSens
	sand = "h"
	tabSens = replaceAll(tabSens,sand)
	# tabSens = replace(tabSens,sand,0)
	# print(tabSens[0][0])
def bas(event):
	global tabSens
	sand = "b"
	tabSens = replaceAll(tabSens,sand)
	# tabSens = replace(tabSens,sand,0)
def gauche(event):
	global tabSens
	sand = "g"
	tabSens = replaceAll(tabSens,sand)
	# tabSens = replace(tabSens,sand,0)
def droite(event):
	global tabSens
	sand = "d"
	tabSens = replaceAll(tabSens,sand)
	# tabSens = replace(tabSens,sand,0)

ctx = Tk()

canWi = 500
canHei = 500
canBg = "white"

flag = 0

dcx = canWi / 2
dcy = canHei / 2
carreColo = "red"
lg = 20
vit = 10


deb = 5

proof = 1

# Ireto no tene base anle izy
# mBola ts niditra P.O.O mou zah no nanao anle de voatery natao tableau ny caracteristique anle serpent
tabSens = [] #C pour stocker les sens de chaque corps 
square = [] #Isan le objet carre
# C pour les coodonnes de chaque corps du serpent
coordoX = [] 
coordoY = []

canvas = Canvas(width = canWi,height = canHei,bg = canBg)

start = Button(text = "Commencez",command = startMove)
pause = Button(text = "Pause",command = pauseMove)
button999 = Button(text = "Quittez",command = append)


canvas.grid(row = 0,rowspan = 10)

start.grid(row = 0,column = 2)
pause.grid(row = 1,column = 2)

ctx.bind("<Up>",haut)
ctx.bind("<Down>",bas)
ctx.bind("<Left>",gauche)
ctx.bind("<Right>",droite)
button999.grid(row = 9,column = 2)

sens = ["d"] # Initiation du sens premier du serpent
carre = canvas.create_rectangle(dcx - lg / 2,dcy - lg / 2,dcx + lg / 2,dcy + lg / 2,fill = carreColo)
square.append(carre)
coordoX.append(dcx)
coordoY.append(dcy)
tabSens.append(sens)
ctx.mainloop()

