# el ciclo while es que si la condicion es True (verdadera) se imprime infinitamente hasta que sea False (falsa)

condicion = True
valor = input('')

while condicion:
    print (valor)

# el else es opcional
else:
    print(condicion)

contador = 5
# Forma de dar un fin al ciclo

while contador >= 0:
    print (contador)
    contador -= 1
else:
     print('Fin del ciclo.')