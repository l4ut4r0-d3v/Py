# Se pueden crear expleciones mas complejas
ceondicional = 'rubn'

# Este da True por tener un valor, si tuviera una cadens seria false
condicional = 10 

# Este da False por no tener ningun tipo de valor
condicional = ''

# Py agreag automaticamente lineas de codigo y no {} como en otros lenguajes. Para que se haga un nuevo bloque de codigo. Se da un tabulador o un salto de 5 espacios

# if y else esperan un valor como los condicioneles por ejemplo el primero daria True por que ese es su valor booleano

# El segundo da True por que tienen un valor

# El ultimo da False ya que no tiene un valor, pero si se cambia da True

condicional = True

if condicional == True:
     print('El valor es verdadero')
elif condicional == False:
     print('el Valor es falso')
else:
     print('El valor es desconosido')

# Vercion simplificada de if else, solo se usa si hay pocas lines de codigo porque se puede volver confuso de leer. No se puede utilizar elif en el codigp

print('condicion verdadera') if condicional else print('condicion falsa')