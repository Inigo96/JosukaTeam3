'''
Created on 21 de nov. de 2015

@author: Enara
'''
import sqlite3
class EventoLugar():
    conexion = None
    cursor = None
    def __init__ (self):
        self.conexion = sqlite3.connect(r'../BD/data/josukateam.db') 
        self.cursor = self.conexion.cursor()
    def crearTabla (self):
        self.cursor.execute("CREATE TABLE eventolugar (id_eventolugar INT, id_lugar INT, id_evento INT)")
        self.conexion.commit()
    def borrarTabla (self):
        self.cursor.execute("DROP TABLE eventolugar")
        self.conexion.commit()
    def insertar (self, id_lugar, id_evento):
        self.cursor.execute("INSERT INTO eventolugar VALUES(" + self.index() + ", " + id_lugar + ", " + id_evento + ")")
        self.conexion.commit()
    def borrar (self, id_eventolugar):
        self.cursor.execute("DELETE FROM eventolugar WHERE id_eventolugar = " + id_eventolugar)
        self.conexion.commit()
    def modificar (self, id_eventolugar, campo, dato):
        self.cursor.execute("UPDATE eventolugar SET " + campo + " = " + dato + " WHERE id_eventolugar = " + id_eventolugar)
        self.conexion.commit()
    def mostrar(self):
        for relacion in self.cursor.execute("SELECT * FROM eventolugar"):
            print relacion
    def cerrar (self):
        self.conexion.close()
    def index (self):
        self.cursor.execute("SELECT max(id_eventolugar) FROM eventolugar")
        try:
            index = self.cursor.fetchone()[0] + 1
        except:
            index = 0
        return str(index)

    
