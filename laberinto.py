class Grafo(object):
    def __init__(self):#init constructor
        self.funcionSucesor=[self.abajo,self.arriba,self.derecha,self.izquierda]
    def __str__(self):#str destructor
        return str(self.relaciones)

    ##################################################
    def abajo(self,estado):
        if estado[i+1][j]==0 and j <=6:
            estado[i+1][j]=2
            return (True)
        else:
            return (False)

    def arriba(self,estado):
        if estado[i-1][j]==6 and j>=0:
            estado [i-1][j]=2
            return (True)
        else:
            return (False)

    def derecha(self,estado):
        if estado[i][j+1]==0 and j<=5:
            estado[i][j+1]=2
            return (True)
        else:
            return (False)


    def izquierda(self,estado):
        if estado[i][j-1]==6 and j>=0:
            estado[i][j-1]=2
        else:
            return (False)

    def esValido(self,estado, restricciones):

        if estado[i+1][j]== True and estado [i-1][j]== True and estado[i][j+1]==True and estado[i][j-1] and estado not in restricciones:
            return True
        else:
            return False
    def testObjetivo(self, estado):
        if estado[j] == 5  and estado[i] ==5:
            return True
        else:
            return False

    def amplitud(self,estado, restricciones):
        frontera=[]
        frontera.append([estado])
        cont=0
        while frontera:
            cont +=1
            camino = frontera.pop(0)
            nodo = camino[-1]
            if (self.testObjetivo(nodo)):
                print "Objetivo alcanzado!!!"
                print "Numero de iteraciones: ",cont
                return camino
            else:
                for f in self.funcionSucesor:
                    resultado=f(nodo)
                    if self.esValido(resultado, restricciones):
                            actual=list(camino)
                            actual.append(resultado)
                            frontera.append(actual)
g=Grafo()
print g.amplitud([0,0])

