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