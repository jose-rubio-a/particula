from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id = 0,origen_X = 0,origen_Y = 0,destino_X = 0,destino_Y = 0, velocidad = 0,red = 0,green = 0, blue = 0):
        self.__id = id
        self.__origen_x = origen_X
        self.__origen_y = origen_Y
        self.__destino_x = destino_X
        self.__destino_y = destino_Y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(x_1=origen_X, x_2=destino_X, y_1=origen_Y, y_2=destino_Y)
    def __str__(self):
        return(
            'ID: ' + str(self.__id) + '\n' +
            'Origen X: ' + str(self.__origen_x) + '\n' +
            'Origen Y: ' + str(self.__origen_y) + '\n' +
            'Destino X: ' + str(self.__destino_x) + '\n' +
            'Destino Y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Color: \n' +
            'red: ' + str(self.__red) + '\n' +
            'green: ' + str(self.__green) + '\n' +
            'blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n'
        )
