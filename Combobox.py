from tkinter import*
from tkinter import ttk
from tkinter import messagebox


ventana = Tk()
ventana.geometry("300x500")
ventana.configure(bd=10)
ventana.configure(bg="Medium Purple")
ventana.title("Color")
ventana.resizable(0, 0)

colores  = ["Medium Purple","Deep Sky Blue","Slate Blue","Green Yellow","Dark Orange","Deep Pink",
"Medium Slate Blue", "Deep Sky Blue", "Dark Turquoise", "Spring Green", "Gold", "Orange Red", "Violet Red", "Dark Violet", "Firebrick"]

def colorear(event):
	try:
		nuevo = combo.get()
		ventana.configure(bg=nuevo)
	except:
		messagebox.showinfo(message="El color no existe 😜 / Color does not exist 😛", title="Error (︶^︶)")

combo = ttk.Combobox(ventana, width=43, values=colores)
combo.current(0)
combo.grid(column=0, row=0)

combo.bind("<<ComboboxSelected>>", colorear)
combo.bind("<Return>", colorear) 

ventana.mainloop()
