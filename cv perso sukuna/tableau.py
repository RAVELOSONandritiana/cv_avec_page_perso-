from tkinter import *
import time
def clean():
	liste = can.find_all()
	for i in liste:
		if i == txt_taille:pass
		else:can.delete(i)
def general(event):
	global stylo,taille
	if stylo % 2 == 0:
		x = event.x
		y = event.y
		s = change_color()
		if(len(s)==0):
			dessin = can.create_oval(x,y,x+taille,y+taille,fill="black",outline="black")
		else:
			dessin = can.create_oval(x,y,x+taille,y+taille,fill=s,outline=s)
	else:
		x = event.x
		y = event.y
		s = change_color()
		if(len(s)==0):
			dessin = can.create_rectangle(x,y,x+10+taille,y+10+taille,fill="black",outline="black")
		else:
			dessin = can.create_rectangle(x,y,x+10+taille,y+10+taille,fill=s,outline=s)
def change_color():
	couleur = txt.get()
	return couleur
def curseur():
	global stylo
	stylo+=1
	if stylo % 2 == 1:
		but_stylo.config(text="RECTANGLE")
	else:
		but_stylo.config(text="STYLO")
def cls(event):
	x = event.x
	y = event.y
	w = event.widget.find_closest(x,y)
	can.delete(w)
def habe(event):
	global taille
	if event.keysym == "Up":
		taille+=2
	elif event.keysym == "Down":
		taille-=2
	can.itemconfig(txt_taille,text=str(taille))
taille = 0
stylo = 0
fen = Tk()
fen.geometry("500x500")
fen.resizable(False,False)
fen.title("Tableau magique")
can = Canvas(fen,height=450,width=500,bg="grey")
can.pack(side="top")
but_quitter = Button(fen,text="QUITTER",fg="red",bg="green",height=1,width=25,command=fen.destroy)
but_quitter.place(x=1,y=450)

txt_taille = can.create_text(10,10,text=str(taille))

txt_tuto = can.create_text(250,10,text="Clic droit pour effacer manuellement",fill="green")

but_stylo = Button(fen,text="STYLO",fg="red",bg="green",height=1,width=25,command=curseur)
but_stylo.place(x=180,y=450)

but_clean = Button(fen,text="CLEAN",fg="red",bg="green",height=1,width=25,command=clean)
but_clean.place(x=350,y=450)
txt = Entry(fen,font=("",10,'italic'),bg="blue",width=35)
txt.place(x=0,y=480)
but_couleur = Button(fen,text="COULEUR",fg="red",bg="green",height=1,width=35,command=change_color)
but_couleur.place(x=250,y=475)
can.bind_all("<B1-Motion>",general)
can.bind_all("<B3-Motion>",cls)
can.bind_all("<Up>",habe)
can.bind_all("<Down>",habe)
fen.mainloop()
