if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1,2 o 3):"))
    if main == 1:
        from Clases.archivo import archivos1
        
        uno = archivos1("calificaciones.csv")
        uno.lectura()