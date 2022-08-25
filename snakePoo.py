from tkinter import*
class Carre(object):
	"Le carre"

	def __init__(self,canvas,cx = 0,cy = 0,tab = [],s = 5,colo = "yellow"):
		self.x = cx
		self.y = cy
		self.tabDir = tab
		self.surface = s
		self.color = colo
		self.canvas = canvas
		self.me = self.canvas.create_rectangle(0,0,0,0,fill = self.color) 
	def draw(self):
		canvas.coords(self.me,self.x,self.y,self.x + self.surface,self.y + self.surface)

class Serpent(object):
	"Serpent"
	def __init__(self,sens = "d",x = 0,y = 0,height = 10,length = 3):
		self.sens = sens
		self.surface = height
		self.corps = [Carre(canvas = canvas,cx = x,cy = y,tab = [self.sens],s = self.surface,colo = "red")]
		self.length = 0
		for x in range(length):
			self.append()


	def append(self):
		bat = []
		for x in range(len(self.corps[len(self.corps) - 1].tabDir) + 1):
			if x != 2 :
				bat.append(self.corps[len(self.corps) - 1].tabDir[0])
			else :
				bat.append(self.corps[len(self.corps) - 1].tabDir[x - 1])
		if self.corps[len(self.corps) - 1].tabDir[0] == "h" :
			y = self.corps[len(self.corps) - 1].y + self.surface 		
			x = self.corps[len(self.corps) - 1].x
		elif self.corps[len(self.corps) - 1].tabDir[0] == "b" :
			y = self.corps[len(self.corps) - 1].y - self.surface 		
			x = self.corps[len(self.corps) - 1].x
		elif self.corps[len(self.corps) - 1].tabDir[0] == "g" :
			x = self.corps[len(self.corps) - 1].x + self.surface 		
			y = self.corps[len(self.corps) - 1].y
		elif self.corps[len(self.corps) - 1].tabDir[0] == "d" :
			x = self.corps[len(self.corps) - 1].x - self.surface 		
			y = self.corps[len(self.corps) - 1].y

		self.corps.append(Carre(canvas = canvas,tab = bat,cx = x,cy = y,s = self.surface,colo = "yellow"))
		self.length += 1

	def move(self,sens):
		self.corps[0].tabDir[0] = sens
		for i in range(len(self.corps)):
			self.corps[i].tabDir[len(self.corps[i].tabDir) - 1] = sens
		for i in range(len(self.corps)):
			if self.corps[i].tabDir[0] == "h":
				self.corps[i].y -= self.surface
			elif self.corps[i].tabDir[0] == "b":
				self.corps[i].y += self.surface
			elif self.corps[i].tabDir[0] == "g":
				self.corps[i].x -= self.surface
			elif self.corps[i].tabDir[0] == "d":
				self.corps[i].x += self.surface
			del(self.corps[i].tabDir[0])	
			self.corps[i].tabDir.append(self.sens)	
			self.corps[i].draw()

def haut(e):
	global sens
	if sens != "b":
		sens = "h"
def bas(e):
	global sens
	if sens != "h":
		sens = "b"
def gauche(e):
	global sens
	if sens != "d":
		sens = "g"
def droite(e):
	global sens
	if sens != "g":
		sens = "d"

def go(e):
	global proof,permi
	if proof == 1 :
		permi = 0
		proof = 0
	else :	
		permi = 1
		bouger()
		proof = 1
def bouger():
	s.move(sens)
	if permi == 1 :
		ctx.after(100,bouger)


ctx = Tk()
canWi = 500
canHei = 500
canvas = Canvas(width = canWi,height = canHei,bg = "white")
button999 = Button(text = "Quittez",command = ctx.quit)
canvas.grid(row = 0,column = 0,columnspan = 10)
button999.grid(row = 5,column = 5)
permi = 1
proof = 0
ctx.bind("<Up>",haut)
ctx.bind("<Down>",bas)
ctx.bind("<Left>",gauche)
ctx.bind("<Right>",droite)
ctx.bind("<Return>",go)
sens = "d"
s = Serpent(sens = sens,x = canWi/2,y = canHei/2,height = 10,length = 100)
for x in s.corps:
	x.draw()
#bouger()
ctx.mainloop()