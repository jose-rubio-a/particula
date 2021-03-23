from particula import Particula

class Conjunto:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(id=101,origen_X=5,origen_Y=8,destino_X=3,destino_Y=6,velocidad=13,red=111,green=186,blue=50)
p02 = Particula(206,15,6,26,5,22,42,150,206)
conjunto = Conjunto()
conjunto.agregar_final(p01)
conjunto.agregar_inicio(p02)
conjunto.agregar_inicio(p01)
conjunto.mostrar()