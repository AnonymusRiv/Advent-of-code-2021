f = open("input.txt", "r")

res=0                                                                 #se guardará la solución
aux=0                                                                 #para ver que se lean todas las líneas
lista=[]

for linea in f:
    valor=int(linea)                                                  #transformamos el valor en entero
    lista.append(valor)                                               #cargamos los elementos del fichero al final de la lista
    aux+=1

for index,current in enumerate(lista):                                #buscamos en esa lista la posición (index) y el actual (current)
    if(index>2):                                                      #empezará en el valor 3 ya que cada "bloque" es cada 3 líneas
        suma1=lista[index-3]+lista[index-2]+lista[index-1]            #se sumarán los 3 valores anteriores
        suma2=lista[index-2]+lista[index-1]+current                   #se sumarán los 2 valores anteriores y el valor actual
        if(suma1<suma2):                                              #si la primera suma es menor que la segunda, se incrementa en 1 la solucion
            res+=1

print(f"Se han leido {aux} lineas")

print(f"La solucion es: {res}")

f.close()