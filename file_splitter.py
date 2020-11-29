# -*- coding: cp1252 -*-

import string
import os
import sys
 
ruta = sys.argv[1] # Archivo a dividir
nombre_archivo = os.path.basename(ruta) # Obtener nombre real del archivo
tamano_trozo = sys.argv[2] # Tama�o de los trozos (Bytes xDDDD)
destino = sys.argv[3] # Destino de los Trozos
destino2 = destino
tamano_trozo = int(tamano_trozo) # Pasamos argumento de String a Integer
tamano = os.path.getsize(ruta) # Tama�o del Archivo (Bytes)
print "\nTama�o: " + repr(tamano) + " Bytes\n\nParticionando Archivo, por favor espere..." # Imprimir Tama�o del Archivo (Bytes)
datos = '' # Datos del buffer
posicion = 0 # Para posicionarse en los datos a leer
i = 0 # Para Hacer .0, .1, .2, .3, .4, etc...
wrote = 0
trozo = 0
megabyte = 1048576
f = open (ruta, 'rb') # Abrimos archivo
while wrote < tamano: # Creamos bucle que diga que si posicion menor o igual que tama�o hago lo que esta a continuaci�n
    destino = destino + nombre_archivo + "." + repr(i) # Crear nombre del archivo prueba.jpg.0, prueba.jpg.1, prueba.jpg.*
    print "Creado: " + destino
    trozo = 0
    j = open (destino, 'ab') # Creamos el archivo prueba.jpg.*
    while trozo<tamano_trozo:
        datos = f.read (megabyte)
        trozo = trozo + len(datos) # bucle infinito
        j.write (datos)
        if len(datos) == 0:
            break
    wrote = wrote + trozo
    j.close()
    i = i + 1
    destino = destino2
f.close() # Cerramos archivo principal

x = open (destino2 + nombre_archivo + ".bat", 'w') # A partir de aqu� creamos el .bat para pegar archivos
x.write('copy /b "'+ nombre_archivo + '.0" "' + nombre_archivo + '"\n')
z = 1
while z<i:
    x.write('copy /b "'+ nombre_archivo +'"+"'+ nombre_archivo +'.'+ repr(z)+ '"\n')
    z = z + 1
x.close()

x = open (destino2 + nombre_archivo + ".sh", 'w') # Creamos el equivalente .bat para Linux es decir para Bash
x.write('#!/bin/bash\n# Pegador para Linux\n\ncp' + nombre_archivo + '.0" "' + nombre_archivo + '"\n')
z = 1
while z<i:
    x.write('join "'+nombre_archivo+'" "'+nombre_archivo +'.'+repr(z)+'"\n')
    z = z + 1
x.close()
