# Operadores

num1 = int(5)
num2 = int(4)

num3 = int(6)
num4 = int(9)

num5 = int(2)
num6 = int(2)

print('La suma es:', num1 + num2)

# Otra forma de imprimir (forma actual de imprimir)
print(f'La suma es > {num1 + num2} | la suma de 6+9 en {num3 + num4}')

print(f'la resta es: {num5 - num6}')
print(f'la multi es: {num5 * num6}')
print(f'la div(float) es: {num5 / num6}')
# las diviciones se imprimen en float pero con // no lo hacen
print(f'la div es: {num5 // num6}')
print(f'la div residuo (modulo) es: {num5 % num6}')
print(f'el exponente es: {num5 ** num6}')

# incremento con reasignacion

num1 = int(5)
print(num1)

# Incrementar un valor
num1 = num1 + 1
print(num1)

# Forma simplificada. Esto funciona con los otros operando
num1 += 1
print(num1)

# ----------------------------------------

# Comparaciones

a = 7
b = 6

# operador de igual igual == 
# si ambos numeros de las variables son iguales da True y si no da False

print(f' a = {a} b = {b}')

resultado = a == b 
print(f'resultado de == : {resultado}')

# saber si las variables son diferentes
resultado = a != b
print(f'resultado de != : {resultado}')

# Operadador mayor que >
resultado = a > b
print(f'resultado major que > : {resultado}')

# Operadador menor que <
resultado = a < b
print(f'resultado de menor que < : {resultado}')

# Operador igual que
resultado = a >= b
print(f'resultado de igual o mayor >= : {resultado}')

# Operador igual menor que 
resultado = a <= b
print(f'resultado de menor igual que <= : {resultado}')

num1 = True
num2 = False

# and es un valor boolenan, el cual da True si los dos valores son True. si los valores son diferentes da False
resul = num1 and num2
print(f'resultado de and: {resul} -- ambos valores tienen que ser true para dar true')

# or es si un valor regresa True toda la explecion regresa True
resul = num1 or num2
print(f'resultado de or: {resul} -- un valor tiene que ser true para dar true')

# el operador not invierte los valores de las variables
resul = not num2
print(f'resultado de not: {resul} -- invierte el valor ')