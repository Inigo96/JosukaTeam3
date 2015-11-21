'''
Created on 21 de nov. de 2015

@author: Enara
'''
import json
from BD import BdLugar, BdEventoLugar,BdEvento
from BD.BdEvento import Evento
from BD.BdLugar import Lugar
from BD.BdEventoLugar import EventoLugar
def buscarEventos (coord_x, coord_y, rango, lista_deportes):
    lugar = BdLugar.Lugar()
    eventosx, eventosx2, eventosy, eventosy2, eventos3, eventos4, nombres = [], [], [], [], [], [], []
    for id in lugar.cursor.execute("SELECT * FROM lugares WHERE coord_x <= " + str(coord_x + rango)):
        eventosx.append(id[0])
    for id2 in lugar.cursor.execute("SELECT * FROM lugares WHERE coord_x >= " + str(coord_x - rango)):
        eventosx2.append(id2[0])
    for id in lugar.cursor.execute("SELECT * FROM lugares WHERE coord_y <= " + str(coord_y + rango)):
        eventosy.append(id[0])
    for id2 in lugar.cursor.execute("SELECT * FROM lugares WHERE coord_y >= " + str(coord_y - rango)):
        eventosy2.append(id2[0])
    lugar.cerrar()
    for id in (eventosx and  eventosx2 and eventosy and  eventosy2 ):
        eventos3.append(id)
    eventolugar = BdEventoLugar.EventoLugar()
    for id_lugar in eventos3:
        id_evento = eventolugar.cursor.execute("SELECT id_evento FROM eventolugar WHERE id_lugar = " + str(id_lugar))
        eventos4.append(eventolugar.cursor.fetchone()[0])
    eventolugar.cerrar()
    evento = BdEvento.Evento()
    for id_evento in eventos4:
        nombre = evento.cursor.execute("SELECT nombre FROM eventos WHERE id_evento= " + str(id_evento))
        nombres.append(evento.cursor.fetchone()[0])
    return nombres

def parsearPythonJavaScript(nombres):
    msg = json.dumps(nombres, separators=(',',':'))
  
    print msg
parsearPythonJavaScript(buscarEventos(2.0, 2, 1, 2))

    
