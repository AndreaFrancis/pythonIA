class Grafo(object):
    def __init__(self):
        self.funcionSucesor=[self.llena10, self.llena7, self.llena3,self.vacia10,self.vacia7,self.vacia3,self.vaciar10_7,self.vaciar10_3,self.vaciar7_10,self.vaciar7_3,self.vaciar3_10,self.vaciar3_7]
    def __str__(self):
        return str(self.relaciones)
 
    ##################################################
    def llena10(self,estado):
        if estado[0] <10:
            return (10, estado[1], estado[2])
        else:
            return (-1,0,0)

    def llena7(self,estado):
        #codigo

    def llena3(self,estado):
       #codigo

    def vacia10(self,estado):
      #codigo

    def vacia7(self,estado):
	#codigo

    def vacia3(self,estado):
	#codigo

    def vaciar10_7(self,estado):
	#codigo

    def vaciar10_3(self,estado):
        if estado[0]>0:
            if (estado[0]+estado[2])>=3:
                return (estado[0]-(3-estado[2]), estado[1],3)
            else:
                return (0, estado[1],estado[0]+estado[2]) 
        else:
            return (-1,0,0)

    def vaciar7_10(self,estado):
 	#codigo
                   

    def vaciar7_3(self,estado):
        #codigo
	
    def vaciar3_10(self,estado):
	#codigo

    def vaciar3_7(self,estado):
	#codigo
                            
    def esValido(self,estado):
         #codigo
 
    def testObjetivo(self, estado):
        #codigo

             
    def amplitud(self):
	#codigo
