grafo = {
	'pando':{
		'color':0,
		'hijos': ['lapaz','beni']
	},
	'lapaz':{
		'color':0,
		'hijos': ['pando','beni','cbba','oruro']
	},
	'beni':{
		'color':0,
		'hijos': ['pando','lapaz','cbba','scruz']
	},
	'oruro':{
		'color':0,
		'hijos': ['lapaz','cbba','potosi']
	},
	'cbba':{
		'color':0,
		'hijos': ['scruz','beni','lapaz','oruro','potosi','chuqui']
	},
	'scruz':{
		'color':0,
		'hijos': ['beni','cbba','chuqui']
	},
	'potosi':{
		'color':0,
		'hijos': ['tarija','chuqui','cbba','oruro']
	},
	'chuqui':{
		'color':0,
		'hijos': ['scruz','cbba','potosi','tarija']
	},
	'tarija':{
		'color':0,
		'hijos': ['chuqui','potosi']
	}
}

def amplitud(grafo, inicio, colorInicial):
	frontera = []
	grafo[inicio]['color'] = colorInicial
	frontera.append(inicio)
	visitados = []
	while frontera:
		nodo = frontera.pop(0)
		if(nodo not in visitados):
			if grafo[nodo]['color'] == 1:
				c1= 2
				c2 = 3
			if grafo[nodo]['color'] == 2:
				c1= 1
				c2 = 3
			if grafo[nodo]['color'] == 3:
				c1 = 1
				c2 = 2
			encontrado = False
			ind = 0
			hijos = list(grafo[nodo]['hijos'])
			while hijos and (encontrado is False) :
				hijo = hijos.pop(0)
				if grafo[hijo]['color'] != 0:
					encontrado = True
					if grafo[hijo]['color'] == c1:
						if ind % 2 != 0:
							aux = c1
							c1 = c2
							c2 = aux
					else:
						if ind % 2 == 0:
							aux = c1
							c1 = c2
							c2 =  aux
				ind += 1
			hijos = grafo[nodo]['hijos']
			ind  = 0
			print ">>>>Estoy en ", nodo, " y pinto con c1: ", c1, " c2: ", c2
			for hijo in hijos:
				if ind % 2 == 0:
					print hijo, " : ",c1
					grafo[hijo]['color'] = c1
				else:
					print hijo, " : ",c2
					grafo[hijo]['color'] = c2
				ind +=1
				frontera.append(hijo)
			visitados.append(nodo)

amplitud(grafo, 'pando',1)
for ciudad in grafo :
	print (ciudad , ">",grafo[ciudad]['color'])

