import csv

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
        with open('calificaciones.csv') as self.File:
            reader = csv.reader(self.File, delimiter=';')
            next(reader, None)
            for i in reader:
                Apellidos = i[0]
                Nota_parcial1 = i[3]
                Nota_parcial2 = i[4]
                Asistencia = i[2]
                Practicas = i[7]
                Nota_final = i[3] + 0.3 * i[4] + 0.4 * i[7]
                self.lista.append(i)
                
                print(f"{Apellidos} con {Asistencia} de asistencia ha obetenido unas calificaciones de:" 
                    f"\n Nota del parcial1: {Nota_parcial1} \n Nota del parcial2: {Nota_parcial2} \n Nota en practicas: {Practicas}\n"
                    f"Su nota final es: {Nota_final}")

lista = []
dos = archivos2(lista)
dos.lectura2()