from Grafo import *

espacio = Grafo();

espacio.agregar("Arad")
espacio.agregar("Timisora")
espacio.agregar("Zerind")
espacio.agregar("Oradea")
espacio.agregar("Sibiu")
espacio.agregar("Lugoj")
espacio.agregar("Mehadia")
espacio.agregar("Drobeta")
espacio.agregar("Craiova")
espacio.agregar("Rimnicu")
espacio.agregar("Fagaras")
espacio.agregar("Pitesti")
espacio.agregar("Bucarest")
espacio.agregar("Giurgiu")
espacio.agregar("Urziceni")

espacio.relacionarUnilateral("Arad","Zerind",75)
espacio.relacionarUnilateral("Arad","Sibiu",140)
espacio.relacionarUnilateral("Arad","Timisora",118)

espacio.relacionarUnilateral("Zerind","Oradea",71)

espacio.relacionarUnilateral("Sibiu","Fagaras",99)
espacio.relacionarUnilateral("Sibiu","Rimnicu",80)


espacio.relacionarUnilateral("Timisora","Lugoj",111)

espacio.relacionarUnilateral("Oradea","Sibiu",151)

espacio.relacionarUnilateral("Fagaras","Bucarest",211)

espacio.relacionarUnilateral("Rimnicu","Pitesti",97)
espacio.relacionarUnilateral("Rimnicu","Craiova",146)

espacio.relacionarUnilateral("Lugoj","Mehadia",70)

espacio.relacionarUnilateral("Mehadia","Drobeta",75)

espacio.relacionarUnilateral("Pitesti","Bucarest",101)

espacio.relacionarUnilateral("Drobeta","Craiova",120)
espacio.relacionarUnilateral("Craiova","Pitesti",138)


###print espacio
print "Por profundidd : ",espacio.amplitud("Arad","Bucarest")
print "Por amplitud : ",espacio.profundidad("Arad","Bucarest")
print "por costo uniforme : ",espacio.costoUniforme("Arad","Bucarest")
