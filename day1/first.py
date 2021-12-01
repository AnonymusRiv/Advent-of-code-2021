f = open("input.txt", "r")

res=0                                                                 #se guardará la solución
aux=0                                                                 #para ver que se lean todas las líneas

for linea in f:
    valor=int(linea)                                                  #transformamos el valor en entero
    if(aux==0):                                                       #en caso de que sea el 1, no se puede hacer una comparación y asignamos el 1 valor al valor anterior
        previus=valor
    else:
        if(previus<valor):                                            #si el valor anterior es menor que el actual incrementamos la solucion en 1
            res=res+1
        previus=valor
    aux+=1

print(f"Se han leido {aux} lineas")

print(f"La solucion es: {res}")

f.close()