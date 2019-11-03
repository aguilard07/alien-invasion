import sys
import re
import collections
from utilities import *

if(len(sys.argv) < 2):
	print('Por favor, ingrese la ruta del archivo de entrada de datos')
else:
	
	try:
		f = open(sys.argv[1], 'r')
	except Exception as e:
		print('No es un parámetro adecuado')
	else:
		#Borrando los resultados de una anterior operación
		outFile = open('output.txt','w')
		outFile.close()

		# Obteniendo el número de naves N
		nCases 		= 	int(f.readline())
		for i in range(0,nCases):		
			# Obteniendo información de la nave
			
			shipData 	= 	f.readline().split()
			
			height 		= 	int(shipData[0])
			width		=	int(shipData[1])
			scale		=	float(shipData[2])
			
			#Lista para las coordenadas de las capas.
			layersCoords = 	[]

			#Recorriendo la matriz de coordenadas
			for i in range(0,height):
				row = layerCoordFilter(f.readline()).split()
				
				layersCoords.append(row)
			
			#Obteniendo los identificadores de las distintas capas
			layersDic 		= 	getDifferentLayers(layersCoords)
			#Obteniendo las coordenadas de cada capa.
			layersDic 		= 	separateLayerCoords(layersDic,layersCoords)
			#Calculando el centroide y el área de cada capa.
			layersInfo 		= 	calculaLayerSizeAndCenter(layersDic,scale)
			#Intentando ordernar las capas.
			orderedAttack = setAttackSeq(layersInfo)

			
			outFile = open('output.txt','a')
			for row in orderedAttack:
				outFile.write("{}:{},{};".format(row[0],str(row[2]),str(row[3])))
			outFile.write("\n")
		outFile.close()
			

			
		
				

