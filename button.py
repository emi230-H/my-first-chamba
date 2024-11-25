import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    nomb= nombre.get()
    age= edad.get()
    messagebox.showinfo("mensaje", f"Hello {nomb} welcome to the program, your age is {age}")
#crear  la ventana principal
ventana= tk.Tk()
ventana.title("Example of GUI")

#crear una etiqueta
etiqueta = tk.Label(ventana, text="Enter your name")
etiqueta.grid(row=0, column=0, padx=5, pady=10)
#crear una caja de texto (Entry)
nombre = tk.Entry(ventana, width=40)
nombre.grid(row=0,column=1, padx=5, pady=10)

etiqueta = tk.Label(ventana, text="Enter your age")
etiqueta.grid(row=1, column=0, padx=5, pady=10)
edad=tk.Entry(ventana,width=40 )
edad.grid(row=1,column=1, padx=5, pady=10)

#crear un boton y asignar la funcion
boton = tk.Button(ventana, text="hey there", command=mostrar_mensaje)
boton.grid(row=2, column=0, columnspan=2, pady=10)
#iniciar el bucle de eventos
ventana.mainloop()