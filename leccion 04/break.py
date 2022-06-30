# break en py 

for nombre in 'lautaro':
    if nombre == 'o':
        print(f'Valor encontrdo: {nombre}')
        break #la palabra break rompe con el ciclo for por ende no se ejecuta el else
# el else es opcional
else:
    print('fin')