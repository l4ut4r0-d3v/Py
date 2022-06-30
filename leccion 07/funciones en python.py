# definir una funcion en py
# def + 'nombre de la funcion'(parametros):
# def nombre(nombre):

def mi_funcion(nombre, apellido):
    print('hola')
    print(f'nombre: {nombre}, apellido:{apellido}')

# los valores que se usan como argumento se da el valor a los parametros 
mi_funcion('ruben', 'diaz')

print('')

# la funcion se puede reutilizar tanta veces como queramos
mi_funcion('tiago', 'facundo')

# normalmente da error al querer imprimirlo sin que tengan ningun argumento pero poniendo los valores por defout
def suma(a=0,b=0):
    return a+b

# se puede dar los resultado de la funcion con una variable
# resultado = suma(10.2)
# print(f'resultado: {resultado}')

# tambien se puede poner la suma directamente al print
print(f'resultado: {suma(10,5)}')

# si no sabemos cuantos elementos irian en una funcion se utiliza un asterisco * def 'nombre' (*nombre)

# normalmente en la documentacion de py se encuentra los atributos en (*args)
def nombresA(*nombres): 
    for nombre in nombres:
        print(nombre)

nombresA('jorge', 'mario', 'ruben')

nombresA.remove('jorge')
