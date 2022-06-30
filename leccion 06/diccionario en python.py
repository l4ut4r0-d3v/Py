from cgi import print_directory


diccionario = {
	'IDE':'Integrated Development Environment',
	'OPP':'programacion orrientada a objetos',
	'DNMS':'Datebace Managemernt System',
	# cada diccionario se llama por la key
	# primero se da una key 
	'key/llave':'value/valor'
}

# saber el largo del diccionario
print(len(diccionario))

# llamar a un key (llave)
print(diccionario['IDE'])

# otra forma de llamar a un elemento
print(diccionario.get('OPP'))

# modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

print('')

# recorrer los elementos
for elemnto, valor in diccionario.items():
	print(elemnto,'-',valor)
# el else el aleatorio

print('')

# recuperar las llaves
for elemento in diccionario.keys():
	print(elemento)

print('')

# recuperamos los valores
for valor in diccionario.values():
	print(valor)

# saber si un elemento existe
print('IDE' in diccionario)

# agregar elementos
diccionario['VSC'] = 'Visual Studio Code'
print(diccionario)

# eliminar un elemento
diccionario.pop('IDE')
print(diccionario)

print('')

# eliminar diccionario sin eliminar la variable (clear)
diccionario.clear()
print('diccionario limpio', diccionario)

# eliminar variable por completo

del diccionario
print(diccionario)