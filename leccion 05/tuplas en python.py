# en una lista se puede modificar pero una tupla no
# si se modifica da el siguinte error: AttributeError: 'tuple' object has no attribute 'append'
# si la tupla tiene un valor tiene que poner una , al final de ese valor ('lauty',)
nombres = ('lauty', 'ruben', 'facu', 'edgar')
print(len(nombres))

# para imprimir los elementos de la tupla en un un ciclo for en linea se utiliza end=
for nombre in nombres:
    print(nombre, end='-')

# combertir tupla a lista
tutlaLista = list(nombres)
tutlaLista[0] = 'jorge'
nombres = tuple(tutlaLista)
print(nombres)