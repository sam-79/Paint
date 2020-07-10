from tkinter import *
from PIL import ImageGrab, ImageTk,Image
from album_art import get_art



def colour(color):
	global clr ,size
	size=30
	
	if(color=="yellow"):
		clr="yellow"
	elif(color=="green"):
		clr="green"
	elif(color=="red"):
		clr='red'
	elif(color=="white"):
		clr="white"
		size=90
	else:
		clr='black'
	w.bind("<Button1-Motion> <Button1-Motion>",draw)


def draw(event):
	
	w.create_oval(event.x,event.y,event.x+size,event.y+size,width=0,fill=clr)
	




root=Tk()
root.geometry("1040x2150")
#root.minsize(1000,1000)
root.title("Paint")
w=Canvas(root,background="white",width=1040,height=2010)
w.pack()

w.bind("<Button1-Motion> <Button1-Motion>",colour) 


yellow=Button(root,text="Yellow",command=lambda:colour(color="yellow"))
yellow.pack(side="left")

green=Button(root,text="Green",command=lambda:colour(color="green"))
green.pack(side="left",padx=5)

red=Button(root,text="Red",command=lambda:colour(color="red"))
red.pack(side="left",padx=5)

black=Button(root,text="black",command=lambda:colour(color="black"))
black.pack(side="left",padx=5)


erase=Button(root,text="erase",command=lambda:colour(color="white"))
erase.pack(side="left",padx=5)


#w.bind("<Button1-Motion>",draw)





root.mainloop()
