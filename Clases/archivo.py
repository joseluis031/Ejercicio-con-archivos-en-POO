import csv
from msilib.schema import File

class archivos1:
    
    def __init__(self,lista):
        self.lista = lista
        
        
    def lectura(self):
        with open('calificaciones.csv') as self.File:
            reader = csv.reader(self.File, delimiter=';')
            next(reader, None)
            for i in reader:
                Apellidos = i[0]
                Nota_parcial1 = i[3]
                Nota_parcial2 = i[4]
                Asistencia = i[2]
                Practicas = i[7]
                self.lista.append(i)
                
                print(f"{Apellidos} con {Asistencia} de asistencia ha obetenido unas calificaciones de:" 
                    f"\n Nota del parcial1: {Nota_parcial1} \n Nota del parcial2: {Nota_parcial2} \n Nota en practicas: {Practicas}\n")
                
class archivos2:
    def __init__(self,lista):
        archivos1.__init__(self,lista)
        
    def lectura2(self):
        with open('calificaciones.csv',newline='') as f:
              r = csv.reader(f)
              data = [line for line in r]
        with open('calificaciones.csv','w',newline='') as f:
              w = csv.writer(f)
              w.writerow(['Nota_Total'])
              w.writerows(data)

import pandas as pd

class archivos2_1:
    def __init__(self,File):
        self.File = File
    
    def lectura2_1(self):
        leer = pd.read_csv(self.File, header = 0)
        lista = []
        lista_apellidos = list(leer["Apellidos"])
        lista_parcial1 = list(leer["Parcial1"])
        lista_parcial2 = list(leer["Parcial2"])
        lista_asistencia = list(leer["Asistencia"])
        lista_practicas = list(leer["Practicas"])
        
        