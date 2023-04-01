from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

controlador = controladorBD()

def ejecutarInsert():
    controlador.guardarUsuarios(varNombre.get(), varCorreo.get(), varContra.get())
    varNombre.set("")
    varCorreo.set("")
    varContra.set("")
    
def ejecutarSelect():
    usuario = controlador.consultarUsuario(varIdentificador.get())
    for usu in usuario:
        cadena = str(usu[0]) + " " + str(usu[1]) + " " + str(usu[2]) + " " + str(usu[3])
        print(cadena)
        txtEncontrado.insert("", "end", values=(usu[0], usu[1], usu[2], usu[3]))
        
def limpiarTreeview(tree):
    x = tree.get_children()
    if x != '()':
        tree.delete(*x)
        
def mostrarUsuarios():
    limpiarTreeview(txtUsuarios)
    usuarios = controlador.consultaGeneral()
    for usu in usuarios:
        cadena = str(usu[0]) + " " + str(usu[1]) + " " + str(usu[2]) + " " + str(usu[3])
        print(cadena)
        txtUsuarios.insert("", "end", values=(usu[0], usu[1], usu[2], usu[3]))

Ventana = Tk()
Ventana.title("Usuarios")
Ventana.geometry("830x390")
Ventana.resizable(0,0)
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
titulo = Label(pestana1, text="Registro de Usuarios", font=("Helvetica bold", 18), fg="hot pink").place(x=310, y=10)
varNombre = tk.StringVar()
lblNombre = Label(pestana1, text="Nombre", font=("Helvetica", 12))
txtNombre = Entry(pestana1, textvariable=varNombre, font=("Arial", 12), width=30)
lblNombre.place(x=390, y=50) 
txtNombre.place(x=290, y=70)
varCorreo = tk.StringVar()
lblCorreo = Label(pestana1, text="Correo", font=("Helvetica", 12))
txtCorreo = Entry(pestana1, textvariable=varCorreo, font=("Arial", 12), width=30)
lblCorreo.place(x=390, y=110)
txtCorreo.place(x=290, y=130)
varContra = tk.StringVar()
lblContra = Label(pestana1, text="Contraseña", font=("Helvetica", 12))
txtContra = Entry(pestana1, textvariable=varContra, font=("Arial", 12), width=30)
lblContra.place(x=375, y=170)
txtContra.place(x=290, y=190)

#Boton para guardar centrado y de color rosa
btnGuardar = Button(pestana1, text="Guardar", font=("Helvetica bold", 12), bg="pink", command=ejecutarInsert).place(x=385, y=240)

#Pestaña 2 Buscar Usuarios

titulo2 = Label(pestana2, text="Buscar Usuarios", font=("Helvetica bold", 18), fg="hot pink").place(x=340, y=10)

varIdentificador = tk.StringVar()
lblIdentificador = Label(pestana2, text="Identificador", font=("Helvetica", 12)).place(x=380, y=50)
txtIdentificador = Entry(pestana2, width=50, textvariable= varIdentificador).place(x=275, y=70)

btnBuscar = Button(pestana2, text="Buscar", font=("Helvetica bold", 12), bg="pink", command=ejecutarSelect).place(x=390, y=110)

varEncontrado = tk.StringVar()   
txtEncontrado = ttk.Treeview(pestana2, columns=("ID", "Nombre", "Correo", "Contraseña"), show="headings", height=5)
txtEncontrado.place(x=10, y=170)
txtEncontrado.heading("#0", text="")
txtEncontrado.heading("#1", text="ID")
txtEncontrado.heading("#2", text="Nombre")
txtEncontrado.heading("#3", text="Correo")
txtEncontrado.heading("#4", text="Contraseña")

btnLimpiar = Button(pestana2, text="Limpiar", font=("Helvetica bold", 12), bg="pink", command= lambda: limpiarTreeview(txtEncontrado)).place(x=390, y=310)

#pestana 3 Consultar Usuarios

titulo3 = Label(pestana3, text="Consultar Usuarios", font=("Helvetica bold", 18), fg="hot pink").place(x=315, y=10)
txtUsuarios = ttk.Treeview(pestana3, columns=("ID", "Nombre", "Correo", "Contraseña"), show="headings", height=11)
txtUsuarios.place(x=10, y=50)
txtUsuarios.heading("#0", text="")
txtUsuarios.heading("#1", text="ID")
txtUsuarios.heading("#2", text="Nombre")
txtUsuarios.heading("#3", text="Correo")
txtUsuarios.heading("#4", text="Contraseña")

btnActualizar = Button(pestana3, text="Actualizar", font=("Helvetica bold", 12), bg="pink", command=mostrarUsuarios).place(x=390, y=310)



Ventana.mainloop()
