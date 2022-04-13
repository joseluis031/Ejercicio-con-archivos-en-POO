import csv
class archivo:
    
    def __init__(self,File):
        self.File = File
        
    def lectura(self):
        with open('calificaciones.csv') as self.File:
            reader = csv.reader(self.File, delimiter=';')
            for row in reader:
                print(row)
        
