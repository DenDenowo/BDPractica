from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Deni/Documents/GitHub/BDPractica/bd/BDUsuario.db")
            print("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print("Error al conectar")
        return conexion
    
    def guardarUsuarios(self, nom, cor, con):
        #1. Usamos una conexion
        conx = self.conexionBD()
        #2. Validar parametros vacíos
        if(nom== "" or cor=="" or con==""):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        else:
            #preparamos cursor, datos, query
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom, cor, conH)
            qrInsert = "INSERT INTO TBRegistrados(Nombre, Correo, Contra) VALUES(?,?,?)"
            #ejecutamos query y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Información", "Registro exitoso")
    
    def encriptarCon(self, con):
        conPlana = con.encode('utf-8')
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana, sal)
        print(conHa)
        return conHa
    
    def consultarUsuario(self, id):
        conx= self.conexionBD()
        print(id)
        if(id == ""):
            messagebox.showinfo("Cuidado", "ID vacío")
        else:
            try:
                cursor = conx.cursor()
                selectQry = "SELECT * FROM TBRegistrados WHERE ID ="+id
                cursor.execute(selectQry)
                rsUsuario = cursor.fetchall()
                return rsUsuario
                
            except sqlite3.OperationalError:
                messagebox.showinfo("Cuidado", "ID no encontrado")
                
    def consultaGeneral(self):
        try:
            conx = self.conexionBD()
            cursor = conx.cursor()
            selectQry = "SELECT * FROM TBRegistrados"
            cursor.execute(selectQry)
            rsUsuarios = cursor.fetchall()
            return rsUsuarios
        
        except sqlite3.OperationalError:
            messagebox.showinfo("Cuidado", "No se encontraron registros")