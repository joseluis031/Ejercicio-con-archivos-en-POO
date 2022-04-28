# Ejercicio-con-archivos-en-POO

El link de este repositorio es:[GitHub](https://github.com/joseluis031/Ejercicio-con-archivos-en-POO.git)

## Codigo del ejercicio
```
import csv

class archivos1:
    
    def __init__(self,lista):
        self.lista = lista
        
        
    def lectura(self):
        with open('calif_ejerc1.csv') as self.File:
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
        self.file = pd.read_csv(File)
    
    def lectura2_1(self):
        lista = []
        
        for i in range(len(self.file)):
            cosita1 = 0.3*int(self.file["Parcial1"][i])
            cosita2 = 0.3*int(self.file["Parcial2"][i])
            cosita3 = 0.4*int(self.file["Practicas"][i])
            append =  cosita1 + cosita2 + cosita3
            lista.append(append)
        self.file["Nota Final"] = lista
        lista1 = []
        for i in range(len(self.file)):    
            if self.file["Asistencia"][i] >= 0.75 and self.file["Parcial1"][i]>=4 and self.file["Parcial2"][i]>=4 and self.file["Practicas"][i]>=4 and self.file["Nota Final"][i]>=5:
                cosita4 = True
            else:
                cosita4 = False
            lista1.append(cosita4)
        
        self.file["Aprobados"] = lista1
        print(self.file) 



```

## Main del ejercicio
```
if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1 o 2):"))
    if main == 1:
        from Clases.archivo import archivos1
        lista = []
        uno = archivos1(lista)
        uno.lectura()
    if main ==2:
        from Clases.archivo import archivos2_1
        File = "calificaciones.csv"
        hola = archivos2_1(File)
        hola.lectura2_1()
```
