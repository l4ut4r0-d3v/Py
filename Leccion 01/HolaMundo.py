# #Tipo int o entero 
a=10

# Tipo string o cadena
b = 'hola'

# Dato float o flotante
c = 10.5

# Dato tipo boolean (puede ser True o False respectando las mayus o minusculas) 
d = True
e = False

# # Con type se sabe el tipo de dato que se estan imprimiendo
print ('>Tipo int:', type(a), a)
print('')
print('>Tipo string', type(b), b)
print('')
print('>Tipo float/flotante', type(c), c)
print('')
print('>Tipo boolean', type(d), d,'/',e)

print('------>>concatenacion<<------')
print('')
# La concatenacion se usa para unir variables pero si se quiere hacer una suma se unen las numeros y no da el resultado

# Error
num1 = '1'
num2 = '5'
print('concatena variables:' ,num1 + num2)

# Aqui se usa el int en el print para imprimir la suma
num1 = '5'
num2 = '2'
print('suma con int:' ,int(num1) + int(num2))

# Aqui se hace la suma
num1 = 1
num2 = 5
print('suma con sumero normal:' ,num1 + num2)

print('')
print('------>>funcion input<<------')

# Funcion input. Hace que el usuario de un valor y despues se imprima
# Dentro de la funcion input se manda un mensaje a consola que le dice al usuario que debe hacer
nombre = input('Escriba su nombre: ')
apellido = input('Escriba su apellido: ')
print('nu nombre completo es: ', nombre, apellido)

# El valor no se imprime si no esta el valor que da usuario
print('Us ha sido selecsionado para la grasa, es hora de hornear unos momos')

print('')

# Si se quiere que el usuario de una valor numerico se tiene que combertir el input a un int,
# ya que por defecto sale un tipo str
num1 = int (input('escribe un numero: '))
num2 = int (input('escribe un numero: '))
print('suma de los resulrados:', num1 + num2)

dia = int(input('del 1 al 10 como estuvo tu dia?:'))
print('Mi dia estuvo de: ', dia)

titulo = input('Su libro favorito: ')
autor = input('Su autor fue: ')
print('El libro:', titulo, 'fue escrito por: ', autor)