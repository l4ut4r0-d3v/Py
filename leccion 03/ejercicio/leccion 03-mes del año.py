mes = int(input('Por favor de una mes del 1 al 12 (Enero a Diciembre): '))
# El valor None quiere decir que la variable no contiene ningun valor (esto tambien se puede hacer con cadena vacia), en otros lenguajes se le llama null
estacion = None
mesAño = None

if mes == 1:
    mesAño = 'Enero'
elif mes == 2:
    mesAño = 'Febrero'
elif mes == 3:
    mesAño = 'Marzo'
elif mes == 4:
    mesAño = 'Abril'
elif mes == 5:
    mesAño = 'Mayo'
elif mes == 6:
    mesAño = 'Junio'
elif mes == 7:
    mesAño = 'Julio'
elif mes == 8:
    mesAño = 'Agosto'
elif mes == 9:
    mesAño = 'Septiembre'
elif mes == 10:
    mesAño = 'Octubre'
elif mes == 11:
    mesAño = 'Noviembre'
elif mes == 12:
    mesAño = 'Diciembre'
else:
    mesAño = 'Valor incorecto'

print(f'Su valor {mes} es el mes {mesAño} ')