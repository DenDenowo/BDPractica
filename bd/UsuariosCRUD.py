from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

controlador = controladorBD()

def ejecutarInsert():
    controlador.guardarUsuarios(varNombre.get(), varCorreo.get(), varContra.get())

Ventana = Tk()
Ventana.title("Usuarios")
Ventana.geometry("420x300")
Ventana.resizable(0,0)
Ventana.config(bg="lightblue")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

panel.add(pestana1, text="Formulario Usuarios")
panel.add(pestana2, text="Buscar Usuarios")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuarios")

#Pestaña 1 Formulario Usuarios
titulo = Label(pestana1, text="Registro de Usuarios", font=("Arial", 20), bg="white").place(x=10, y=10)
varNombre = tk.StringVar()
lblNombre = Label(pestana1, text="Nombre", font=("Arial", 12), bg="white").place(x=10, y=50)
txtNombre = Entry(pestana1, textvariable=varNombre, font=("Arial", 12), width=30).place(x=10, y=70)

varCorreo = tk.StringVar()
lblCorreo = Label(pestana1, text="Correo", font=("Arial", 12), bg="white").place(x=10, y=100)
txtCorreo = Entry(pestana1, textvariable=varCorreo, font=("Arial", 12), width=30).place(x=10, y=120)

varContra = tk.StringVar()
lblContra = Label(pestana1, text="Contraseña", font=("Arial", 12), bg="white").place(x=10, y=150)
txtContra = Entry(pestana1, textvariable=varContra, font=("Arial", 12), width=30).place(x=10, y=170)

btnGuardar = Button(pestana1, text="Guardar", font=("Arial", 12), bg="white", command=ejecutarInsert).place(x=10, y=200)

Ventana.mainloop()