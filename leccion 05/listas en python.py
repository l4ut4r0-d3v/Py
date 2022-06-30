# listas en py

# con los corchetes [] se crea una lista
# en una lista, cada valor tiene un indice que se muestra abajo
# de izquierda a derecha comienza con 0
# de derecha a izquierda comienza con -1

nombres = ['diego', 'mauri', 'karina', 'el diego']

# 0		  1		    2			3
# nombre = ['diego', 'mauri', 'karina', 'el diego']
# -4      -3        -2			-1

# print(nombre)

# se puede imprimit cada valor de la lista si se usa un valor numerico

# print(nombre[0])
# print(nombre[-3])

# imprimir un rango, quiere decir que le damos dos indices y se imprime los que pidamos
print(nombres[0:2])

# --
print('')
# --

# se imprime en orden pero no imprime el indice dado
print(f'{nombres[:1]}')

# ..
print('')
# --

# imprimir todos los indices de una lista
print([nombres[1:]])


# cambiar valor de la lista
nombres[3] = 'ivan' # se crea una variable con el nombre de la lista y el indice a modificar
print(nombres) # depues se imprime el nuevo valor

# interar elementos en una lista
for nombre in nombres:
	print(nombre)
# si se quiere puede hacer un else
else:
	print('fin de la imprecion')

# saber cuantos elementos tiene una lista con len()
print(len(nombres))

# poner un nueva elemento a la lista
nombres.append('facu')
print(nombres)

# insertar un valor en un indice espesifico
# se utiliza el nombre de la variable y un valor
nombres.insert(3, 'lauty') 
print(f' >{nombres}')

# eliminar un valor
nombres.remove('facu')
print(nombres)

# eliminar ultimo agregado
nombres.pop()
print(nombres)

# eliminar por indices
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# eliminar lista por completo
# esto dara de error de NameError: name 'nombres' is not defined
del nombres
print(nombres)