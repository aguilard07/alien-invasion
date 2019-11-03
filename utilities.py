import math
from decimal import *
import re

#Filtro de las coordenadas
def layerCoordFilter(stringValue):
	filteredString = re.sub('[^a-zA-Z \n\.]', '0', stringValue)
	return filteredString

#Función para determinar las distintas capaz de la nave.
def getDifferentLayers(layersCoords):
	layersDic = {}
	layersList = []
	for row in layersCoords:
		for i in range(0,len(row)):
			if(layersList.count(row[i]) == 0 and row[i] != '0'):
				layersList.append(row[i])
	for layer in layersList:
		layersDic[layer] = [] 
	return layersDic

#Función para desplegar las coordenadas de los centros de comando de cada capa.
def separateLayerCoords(layersDic,layersCoords):
	for layer in layersDic:
		#Recorriendo cada capa del escudo
		for i in range(0,len(layersCoords)):
			#recorriendo las coordenadas relativas en Y de cada capa.
			for j in range(0,len(layersCoords[i])):
				#recorriendo las coordenadas en X de cada capa.
				if(layersCoords[i][j] == layer):
					layersDic[layer].append([j+0.5, i+0.5])
	return layersDic


#Función que calcula el tamaño relativo (área) de la capa y su centroide:
def calculaLayerSizeAndCenter(layersDic,scale):
	centers = {}
	for layer in layersDic:
		centers[layer] = []
		xcoords = []
		ycoords = []
		for coord in layersDic[layer]:
			xcoords.append(coord[0])
			ycoords.append(coord[1])
		xmin 	= min(xcoords)
		xmax 	= max(xcoords)
		ymin 	= min(ycoords)
		ymax 	= max(ycoords)
		size 	= (xmax-xmin)*(ymax-ymin)
		xcenter = xmin +0.5*(xmax-xmin)
		ycenter	= ymin +0.5*(ymax-ymin)
		centers[layer].append(size)
		centers[layer].append(round(Decimal(ycenter*scale),3))
		centers[layer].append(round(Decimal(xcenter*scale),3))
	return centers;

#Calcular promedio para numero pequeño de medidas

#Transformar diccionario a Lista
def dicToList(dic):
	l = []
	for key in dic:
		aux = []
		aux.append(key)
		aux.append(dic[key][0])
		aux.append(dic[key][1])
		aux.append(dic[key][2])
		l.append(aux)
	return l

#Ordenando la lista de secuencia de ataques por orden alfabético y numérico
def setAttackSeq(layersInfo):
	#Seteando contador
	i = 0
	#Creando lista auxiliar:
	aux = []
	#Creando lista ordenada
	orderedAttack = []
	#Transformando diccionario a lista
	unorderedAttack = dicToList(layersInfo)
	#Ordenando la lista en base orden ascendente de áreaÑ
	unorderedAttack.sort(key = lambda x: x[1])
	#print(unorderedAttack)
	pastSize = unorderedAttack[0][1]
	for i in range(0,len(unorderedAttack)):
		currentSize = unorderedAttack[i][1]
		if(currentSize != pastSize):
		 	aux.sort(key= lambda x: x[0].upper(), reverse = True)
		 	orderedAttack+=aux
		 	aux = []
		aux.append(unorderedAttack[i])
	orderedAttack+=aux
	return orderedAttack

