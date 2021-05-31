#Función para sumar
def sumar(a,b):
  c = a + b
  return c

#Función para restar
def restar(a,b):
  c = a - b
  return c

#Función para multiplicar
def multiplicar(a,b):
  c = a * b
  return c

#Función para dividir
def dividir(a,b):
  if b != 0:
    c = a / b
  else:
    print('División entre cero no es permitida')
  return c

#Función para obetner el residuo de una división
def modulo(a,b):
  if b != 0:
    c = a % b
  else:
    print('División entre cero no es permitida')
  return c

##Función para obetner la parte entera de una división
def DivisionInt(a,b):
  if b != 0:
    c = a // b
  else:
    print('División entre cero no es permitida')
  return c

