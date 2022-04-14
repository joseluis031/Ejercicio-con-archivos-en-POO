import csv
class archivos1:
    
    def __init__(self,File):
        self.File = File
        
    def lectura(self):
        with open('calificaciones.csv') as self.File:
            reader = csv.reader(self.File, delimiter=';')
            next(reader, None)
        lista = []
        for i in reader:
            Apellidos = i[0]
            Nota_parcial1 = i[3]
            Nota_parcial2 = i[4]
            Asistencia = i[2]
            Practicas = i[7]
            lista.append(i)
            print(f"{Apellidos} con {Asistencia} % de asistencia ha obetenido unas calificaciones de: \n Nota del parcial1: {Nota_parcial1} \n Nota del parcial2: {Nota_parcial2} \n Nota en practicas: {Practicas}")