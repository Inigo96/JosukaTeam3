'''
Created on 20 de nov. de 2015

@author: Enara
'''
import sqlite3
class Evento():
    conexion = None
    cursor = None
    def __init__ (self):
        self.conexion = sqlite3.connect(r'../BD/data/josukateam.db') 
        self.cursor = self.conexion.cursor()
    def crearTabla (self):
        self.cursor.execute("CREATE TABLE eventos (id_evento INT,deporte TEXT, nombre TEXT, fecha INT, hora_inicio INT, hora_fin INT, material TEXT, precio DOUBLE)")
        self.conexion.commit()
    def borrarTabla (self):
        self.cursor.execute("DROP TABLE eventos")
        self.conexion.commit()
    def insertar (self, deporte, nombre, fecha, hora_inicio, hora_fin, material, precio):
        id1 = self.index()
        self.cursor.execute("INSERT INTO eventos VALUES(" + id1 + ", '" + deporte + "', '" + nombre + "', " + fecha + "," + hora_inicio + ", " + hora_fin + ", '"+material+"', " + precio + ")")
        self.conexion.commit()
        return id1
    def borrar (self, id_evento):
        self.cursor.execute("DELETE FROM eventos WHERE id_evento = " + id_evento)
        self.conexion.commit()
    def modificar (self, id_evento, campo, dato):
        if campo == "nombre" or campo == "material" or campo == "deporte":
            dato = "'" + dato + "'"
        self.cursor.execute("UPDATE eventos SET " + campo + " = " + dato + " WHERE id_evento = " + id_evento)
        self.conexion.commit()
    def mostrar(self):
        for evento in self.cursor.execute("SELECT * FROM eventos"):
            print evento
    def cerrar (self):
        self.conexion.close()
    def index (self):
        self.cursor.execute("SELECT max(id_evento) FROM eventos")
        try:
            index = self.cursor.fetchone()[0] + 1
        except:
            index = 0
        return str(index)
