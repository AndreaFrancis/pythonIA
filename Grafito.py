grafo = {
		'a': [],
        'b': ['a'],
        'c': ['a'],
        'd': ['b', 'c', 'e'],
        'e': ['r'],
        'f': ['o'],
        'o': [],
        'h': ['q','p'],
        'p': ['q'],
        'q': [],
        'r': ['f'],
        'i': ['d', 'e', 'p'],
        }

def amplitud(grafo, inicio, fin):
	frontera=[]
	frontera.append([inicio])
	cont=0
	while frontera:
		cont +=1
		camino = frontera.pop(0)
		nodo = camino[-1]
		if nodo== fin:
			print "Objetivo Encontrado!!!"
			print "Numero de iteraciones: ",cont
			return camino
		else:
			for hijo in grafo[nodo]:
				actual = list(camino)
				actual.append(hijo)
				frontera.append(actual)

def profundidad(grafo, inicio, fin):
	cola=[]
	cola.append([inicio])
	cont=0
	while cola:
		cont +=1
		camino = cola.pop()
		nodo = camino[-1]
		if nodo== fin:
			print "Objetivo Encontrado!!!"
			print "Numero de iteraciones: ",cont
			return camino
		else:
			for hijo in grafo.get(nodo , []):
				actual = list(camino)
				actual.append(hijo)
				cola.append(actual)

print "Por amplitud: ", amplitud(grafo,'i','o')
print "Por profundidad: ", profundidad(grafo,'i' , 'o')	        
