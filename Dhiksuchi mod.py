from tkinter import  *
from tkinter import filedialog

root = Tk()
root.title("DHIKSUCHI")
root.geometry("350x350")

entry =Text(root,height=30,width=41,wrap=WORD,bg='black',fg='white',borderwidth=10)
entry.place(x=5,y=70)


scrollbar = Scrollbar(root,bg='yellow',borderwidth=5)
scrollbar.pack(side=RIGHT,fill=Y)

text = Text(root, yscrollcommand=scrollbar.set) 

#text.pack(fill=BOTH) 

scrollbar.config(command=text.yview) 

root.minsize(height = 500,width =380)
root.maxsize(height = 500,width =380)


def save_file():
	open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt',)
	if open_file is None:
		return
	text = str(entry.get(1.0,END))
	open_file.write(text)
	open_file.close()
	
b1=Button(root,text="save file",padx=7 ,pady=3,command=save_file,bg='yellow',fg='blue',borderwidth=10)
b1.place(x=10,y=10)

def clear_file():
	entry.delete(1.0,END)

b2 =Button(root,text="clear",command=clear_file,padx=7,pady=3,bg='yellow',fg='blue',borderwidth =10)
b2.place(x=95,y=10)

def open_file():
	file=filedialog.askopenfile(mode='r',defaultextension='.txt')
	if file is not None:
		content = file.read()
		entry.insert(INSERT,content)

b3 =Button(root,text="open file",command=open_file,padx=7,pady=3,bg='yellow',fg='blue',borderwidth=10)
b3.place(x=165,y=10)

def DHIKSUCHI():pass


b4 =Button(root,text="DHIKSUCHI",command=DHIKSUCHI,padx=7,pady=3,bg='black',fg='white',borderwidth=10,state=DISABLED)
b4.place(x=255,y=10)




root.mainloop()