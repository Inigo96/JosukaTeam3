#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run,request, template, post, jinja2_view
import requests
from BD import BdEvento,BdEventoLugar,BdLugar
from BD.BdLugar import Lugar
from BD.BdEventoLugar import EventoLugar


@route('/main')
def main():
     return '''
        <link href="http://fonts.googleapis.com/css?family=Lobster" rel="stylesheet" type="text/css">
        <style>
        </style>
        <form action="/crearEvento" method="post">​ <button type=submit>​Crear</button>​</form>
        <form action="/buscarEvento" method="post">​ <button type=submit>​Buscar</button>​</form>
        '''
@post('/crearEvento',method='POST') 
@jinja2_view('../Server/crearEvento.html')
def crearEvento():
    return {} 
 #request.forms.get('deporte').upper()
 
@post('/result') 
def resultForm():  
    deporte1= str(request.forms.get('deporte'))
    timeDia1= str(request.forms.get('timeDia'))
    timeMes1= str(request.forms.get('timeMes'))
    timeAnyo1= str(request.forms.get('timeAnyo'))
    timeIniHora1= str(request.forms.get('timeIniHora'))
    timeIniMin1= str(request.forms.get('timeIniMin'))
    timeFinHora1= str(request.forms.get('timeFinHora'))
    timeFinMin1= str(request.forms.get('timeFinMin'))
    localizacion1= str(request.forms.get('localizacionDir'))
    material1=str(request.forms.get('material'))
    precio1= str(request.forms.get('precio'))
    locationX1 = str(request.forms.get('localizacionX'))
    locationY1 = str(request.forms.get('localizacionY'))
    nombreEvent1 = str(request.forms.get("nombreEvent"))
         
    print deporte1, timeDia1,timeMes1,timeAnyo1,timeIniHora1,timeIniMin1,timeFinHora1,timeFinMin1,localizacion1,material1,precio1,locationX1,locationY1,nombreEvent1
          
    evento = BdEvento.Evento()
    id_evento = evento.insertar(deporte1, nombreEvent1, str(timeDia1)+str(timeMes1)+str(timeAnyo1), str(timeIniHora1)+str(timeIniMin1), str(timeFinHora1)+str(timeFinMin1), material1, precio1)
    evento.mostrar()
    evento.cerrar()
    
    lugar = Lugar()
    id_lugar = lugar.insertar(localizacion1, locationX1, locationY1)
    lugar.mostrar()
    lugar.cerrar()
    
    eventolugar = EventoLugar()
    eventolugar.insertar(id_lugar, id_evento)
    eventolugar.mostrar()
    eventolugar.cerrar()
    
    
    
    return '''<form action="/main" method="route">​ <button type=submit>​Volver</button>​</form> '''          

@post ('/buscarEvento')
def buscarEvento():
     return '''
        <link href="http://fonts.googleapis.com/css?family=Lobster" rel="stylesheet" type="text/css">
        <style>
        </style>
        <form action="/mapaEvento" method="post">​ <button type=submit>Mapa</button>​</form>
        ''' 
 
 
@post ('/mapaEvento')
def mapaEvento():
     return '''
        <html>
        <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
        <script type="text/javascript">
        var geocoder = new google.maps.Geocoder();
        
        function geocodePosition(pos) {
          geocoder.geocode({
            latLng: pos
          }, function(responses) {
            if (responses && responses.length > 0) {
              updateMarkerAddress(responses[0].formatted_address);
            } else {
              updateMarkerAddress('Cannot determine address at this location.');
            }
          });
        }
        
        function updateMarkerStatus(str) {
          document.getElementById('markerStatus').innerHTML = str;
        }
        
        function updateMarkerPosition(latLng) {
          document.getElementById('info').innerHTML = [
            latLng.lat(),
            latLng.lng()
          ].join(', ');
        }
        
        function updateMarkerAddress(str) {
          document.getElementById('address').innerHTML = str;
        }
        
        function initialize() {
          var latLng = new google.maps.LatLng(-34.397, 150.644);
          var map = new google.maps.Map(document.getElementById('mapCanvas'), {
            zoom: 8,
            center: latLng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          });
          var marker = new google.maps.Marker({
            position: latLng,
            title: 'Point A',
            map: map,
            draggable: true
          });
        
          // Update current position info.
          updateMarkerPosition(latLng);
          geocodePosition(latLng);
        
          // Add dragging event listeners.
          google.maps.event.addListener(marker, 'dragstart', function() {
            updateMarkerAddress('Dragging...');
          });
        
          google.maps.event.addListener(marker, 'drag', function() {
            updateMarkerStatus('Dragging...');
            updateMarkerPosition(marker.getPosition());
          });
        
          google.maps.event.addListener(marker, 'dragend', function() {
            updateMarkerStatus('Drag ended');
            geocodePosition(marker.getPosition());
          });
        }
        
        // Onload handler to fire off the app.
        google.maps.event.addDomListener(window, 'load', initialize);
        </script>
        </head>
        <body>
          <style>
          #mapCanvas {
            width: 500px;
            height: 400px;
            float: left;
          }
          #infoPanel {
            float: left;
            margin-left: 10px;
          }
          #infoPanel div {
            margin-bottom: 5px;
          }
          </style>
        
          <div id="mapCanvas"></div>
          <div id="infoPanel">
            <b>Marker status:</b>
            <div id="markerStatus"><i>Click and drag the marker.</i></div>
            <b>Current position:</b>
            <div id="info"></div>
            <b>Closest matching address:</b>
            <div id="address"></div>
          </div>
         </body>
         </html>
         '''
         
         
 
run(host='localhost', port=8080)