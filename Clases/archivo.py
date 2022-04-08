class archivo:
    
    def __init__(self,fichero,calif,datos):
        self.fichero = fichero
        self.calif = calif
        self.datos = datos
    def lectura(self):
        with open(self.fichero, "r") as self.calif:
            self.datos = []
            self.lista_diccionario = dict()