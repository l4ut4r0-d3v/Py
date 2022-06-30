# usar diccionario en py
# se usa doble comilla **+termino
# se da un for para recorrer los items

def listaDeJuegos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} {valor}')
# despues se hace un llamada a la def con los valores de el diccionario con key y valor
listaDeJuegos (COD = '- Call Of Duty', key = '- valor')
# se puede reutilizar el llamado a la variable

listaDeJuegos (AC = '- Assasins Creed')
