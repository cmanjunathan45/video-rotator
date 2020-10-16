from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
from moviepy.editor import *
import webbrowser
import os
from datetime import datetime

root=tk.Tk()
root.title("Video Rotator | Manjunathan C")
root.geometry("600x600")
root.config(bg="#4285f4")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))

def rotate():
		a=pathEntry.get()
		try:
			clip = VideoFileClip(a)
		except:
			messagebox.showerror("PATH Error","Enter a valid path")
		b=durMin.get()
		if b=="":
			b=0
		else:
			b=int(durMin.get())
		c=durMax.get()
		if c=="":
			c=duration = clip.duration
		else:
			c=int(durMin.get())
		now=datetime.now()
		current_time = now.strftime("%H%M%S")
		clip1 = clip.subclip(b,c) 
		d=rotangleEntry.get()
		if d=="":
			d=0
		else:
			d=int(rotangleEntry.get())
		clip2 = clip1.rotate(d) 
		clip2.ipython_display(width = 1600) 
		file="/root/python/tkinter/rotate/__temp__.mp4"
		temp="/root/python/tkinter/rotate/video_"+current_time+".mp4"
		os.rename(file,temp)
		messagebox.showinfo("Successful","File Saved Successfully")

def clear():
	pathEntry.delete(0,END)
	durMin.delete(0,END)
	durMax.delete(0,END)
	rotangleEntry.delete(0,END)

pathLabel=Label(root,text="Enter Your Video Path or Browse",bg="#4285f4",fg="black",font=("courier",15,"bold italic"))
pathLabel.place(x=50,y=20)

pathEntry=Entry(root,fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=30,borderwidth=6)
pathEntry.place(x=50,y=50)

labelDur=Label(root,text="Duration of the clip you want \n(Max and Default is full video length) ",bg="#4285f4",fg="black",font=("courier",15,"bold italic"))
labelDur.place(x=30,y=100)

labelMinDur=Label(root,text="Min (in Sec's):",bg="#4285f4",fg="black",font=("courier",15,"bold italic"))
labelMinDur.place(x=50,y=150)

durMin=Entry(root,fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=10,borderwidth=6)
durMin.place(x=70,y=180)

labelMaxDur=Label(root,text="Max (in Sec's):",bg="#4285f4",fg="black",font=("courier",15,"bold italic"))
labelMaxDur.place(x=250,y=150)

durMax=Entry(root,fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=10,borderwidth=6)
durMax.place(x=270,y=180)

labelAngle=Label(root,text="Angles You want rotate in Degree's \n(Maximum is 360)",bg="#4285f4",fg="black",font=("courier",15,"bold italic"))
labelAngle.place(x=30,y=250)

rotangleEntry=Entry(root,fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=10,borderwidth=6)
rotangleEntry.place(x=70,y=300)

buttonRotate=Button(root,text="Rotate",fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=rotate)
buttonRotate.place(x=210,y=350)


buttonClear=Button(root,text="Clear",fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=clear)
buttonClear.place(x=210,y=400)

buttonExit=Button(root,text="Exit",fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=root.destroy)
buttonExit.place(x=210,y=450)

buttonContact=Button(root,text="Contact",fg="#4285f4",bg="black",font=("courier",15,"bold italic"),width=7,borderwidth=6,activebackground="white",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonContact.place(x=210,y=500)

root.mainloop()

