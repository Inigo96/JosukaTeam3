'''
Created on 21 de nov. de 2015

@author: Enara
'''
'''
Created on 21 de nov. de 2015

@author: Enara
'''
import sqlite3
class Lugar():
    conexion = None
    cursor = None
    def __init__ (self):
        self.conexion = sqlite3.connect(r'../BD/data/josukateam.db') 
        self.cursor = self.conexion.cursor()
    def crearTabla (self):
        self.cursor.execute("CREATE TABLE lugares (id_lugar INT, nombre TEXT, coord_x DOUBLE, coord_y DOUBLE)")
        self.conexion.commit()
    def borrarTabla (self):
        self.cursor.execute("DROP TABLE lugares")
        self.conexion.commit()
    def insertar (self, nombre, coord_x, coord_y):
        id1 = self.index()
        self.cursor.execute("INSERT INTO lugares VALUES(" + id1 + ", '" + nombre + "', " + coord_x + ", " + coord_y +")")
        self.conexion.commit()
        return id1
    def borrar (self, id_lugar):
        self.cursor.execute("DELETE FROM lugares WHERE id_lugar = " + id_lugar)
        self.conexion.commit()
    def modificar (self, id_lugar, campo, dato):
        self.cursor.execute("UPDATE lugares SET " + campo + " = " + dato + " WHERE id_lugar = " + id_lugar)
        self.conexion.commit()
    def mostrar(self):
        for lugar in self.cursor.execute("SELECT * FROM lugares"):
            print lugar
    def cerrar (self):
        self.conexion.close()
    def index (self):
        self.cursor.execute("SELECT max(id_lugar) FROM lugares")
        try:
            index = self.cursor.fetchone()[0] + 1
        except:
            index = 0
        return str(index)
