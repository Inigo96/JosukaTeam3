'''
Created on 20 de nov. de 2015

@author: Enara
'''
import sqlite3
class Usuario():
    conexion = None
    cursor = None
    def __init__ (self):
        self.conexion = sqlite3.connect(r'../BD/data/josukateam.db') 
        self.cursor = self.conexion.cursor()
    def crearTabla (self):
        self.cursor.execute("CREATE TABLE usuarios (id_usuario INT, usuario TEXT, contrasena TEXT, nombre TEXT, apellido TEXT, apellido2 TEXT, fecha_nacimiento INT)")
        self.conexion.commit()
    def borrarTabla (self):
        self.cursor.execute("DROP TABLE usuarios")
        self.conexion.commit()
    def insertar (self, usuario, contrasena, nombre, apellido, apellido2, fecha_nacimiento):
        self.cursor.execute("INSERT INTO usuarios VALUES(" + self.index() + ", '" + usuario + "', '" + contrasena + "', '" + nombre + "', '" + apellido + "', '" + apellido2 + "', " + fecha_nacimiento + ")")
        self.conexion.commit()
    def borrar (self, id_usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE id_usuario = " + id_usuario)
        self.conexion.commit()
    def modificar (self, id_usuario, campo, dato):
        if campo == "usuario" or campo == "nombre" or campo == "contrasena" or campo == "apellido" or campo == "apellido2":
            dato = "'" + dato + "'"
        self.cursor.execute("UPDATE usuarios SET " + campo + " = " + dato + " WHERE id_usuario = " + id_usuario)
        self.conexion.commit()
    def mostrar(self):
        for usuario in self.cursor.execute("SELECT * FROM usuarios"):
            print usuario
    def cerrar (self):
        self.conexion.close()
    def index (self):
        self.cursor.execute("SELECT max(id_usuario) FROM usuarios")
        try:
            index = self.cursor.fetchone()[0] + 1
        except:
            index = 0
        return str(index)

        
