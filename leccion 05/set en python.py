# set es un tipo de lista que no se puede modificar ni accepta valores repetidos,
# pero si se puede eliminar los valores y agregar nuevos
# no tiene indice
# en el elemento set no hay orden de valores

armas = {'ak-47', 'm18', 'kar98k', 'raygun'}
print(armas) # los elementos se imprimen de manera aleatoria

# saber el largo con len()
# print(len(armas))

# saber si un elemento esta en una variable
print('m18A1' in armas)

# agregar elemento con add
armas.add('m18A1')
print(armas)

# no permite elementos duplicados (en caso de hacerlo no se añadira a la variable)
armas.add('rpg-7')
print(armas)

# remover elementos da errores si no se escribe de manera correcta el elemento
armas.remove('rpg-7')
print(armas)

# se elimina el elemento pero si no esta no error










print(len(armas))