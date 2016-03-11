
class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)

    def agregar(self, elemento):
        self.relaciones.update({elemento:[]})

    def relacionarUnilateral(self, origen, destino, costo):
        self.relaciones[origen].append( (destino,costo) )

    def sumaCostos(self,lista):
        total=0
        for i in lista:
            total = total + i[1]
        return total

    def amplitud(self,inicio,fin):
        frontera=[]
        frontera.append([(inicio,0)])
        cont=0
        while frontera:
            cont +=1
            camino = frontera.pop(0)
            nodo = camino[-1][0]
            if nodo== fin:
                print "Iteraciones: ",cont
                print "Costo delcamino: ",self.sumaCostos(camino)
                return camino
            else:
                for hijo in self.relaciones.get(nodo , []):
                    actual = list(camino)
                    actual.append(hijo)
                    frontera.append(actual)

    def profundidad(self,inicio,fin):
        frontera=[]
        frontera.append([(inicio,0)])
        cont=0
        while frontera:
            cont +=1
            camino = frontera.pop()
            nodo = camino[-1][0]
            if nodo== fin:
                print "Iteraciones: ",cont
                print "Costo delcamino: ",self.sumaCostos(camino)
                return camino
            else:
                for hijo in self.relaciones.get(nodo , []):
                    actual = list(camino)
                    actual.append(hijo)
                    frontera.append(actual)

    def costoUniforme(self,inicio,fin):
        frontera=[]
        frontera.append([(inicio,0)])
        cont=0
        while frontera:
            cont +=1
            camino = frontera.pop(0)
            nodo = camino[-1][0]
            if nodo== fin:
                print "Iteraciones: ",cont
                print "Costo delcamino: ",self.sumaCostos(camino)
                return camino
            else:
                for hijo in self.relaciones.get(nodo , []):
                    actual = list(camino)
                    actual.append(hijo)
                    frontera.append(actual)
                frontera.sort(key=lambda tup:self.sumaCostos(tup))