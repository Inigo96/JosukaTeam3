'''
Created on 21 de nov. de 2015

@author: Enara
'''
import sqlite3
class UsuarioEvento():
    conexion = None
    cursor = None
    def __init__ (self):
        self.conexion = sqlite3.connect(r'../BD/data/josukateam.db') 
        self.cursor = self.conexion.cursor()
    def crearTabla (self):
        self.cursor.execute("CREATE TABLE usuarioevento (id_usuarioevento INT, id_usuario INT, id_evento INT, admin INT)")
        self.conexion.commit()
    def borrarTabla (self):
        self.cursor.execute("DROP TABLE usuarioevento")
        self.conexion.commit()
    def insertar (self, id_usuario, id_evento, admin):
        self.cursor.execute("INSERT INTO usuarioevento VALUES(" + self.index() + ", " + id_usuario + ", " + id_evento + ", " + admin + ")")
        self.conexion.commit()
    def borrar (self, id_usuarioevento):
        self.cursor.execute("DELETE FROM usuarioevento WHERE id_usuarioevento = " + id_usuarioevento)
        self.conexion.commit()
    def modificar (self, id_usuarioevento, campo, dato):
        self.cursor.execute("UPDATE usuarioevento SET " + campo + " = " + dato + " WHERE id_usuarioevento = " + id_usuarioevento)
        self.conexion.commit()
    def mostrar(self):
        for relacion in self.cursor.execute("SELECT * FROM usuarioevento"):
            print relacion
    def cerrar (self):
        self.conexion.close()
    def index (self):
        self.cursor.execute("SELECT max(id_usuarioevento) FROM usuarioevento")
        try:
            index = self.cursor.fetchone()[0] + 1
        except:
            index = 0
        return str(index)

