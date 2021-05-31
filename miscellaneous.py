import os

#Función para generar una pausa por medio de un input de pantalla
def next():
  input('\nPresione <enter> para continuar...')

def again():
  S_N = input('\n¿Desea intentar nuevamente? S/N...')
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = True
  elif S_N == 'n' or S_N == 'no' :
    w = False
 
  return w

def againEscapeAfir(S_N):
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = False
  elif S_N == 'n' or S_N == 'no' :
    w = True
 
  return w

def againEscapeNega(S_N):
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = True
  elif S_N == 'n' or S_N == 'no' :
    w = False
 
  return w
  
#Función para generar mensaje para selección de menu u opciones
def seleccionar():
  seleccion = input('\nIngrese la opción >>> ')
  return seleccion

#Función para establecer unidades de medidad de longitud
def msjUnidadMedida():
  texto = """
  Seleccione la unidad de medida de longitud a usar:
  1. cm
  2. m
  3. Km
  """
  print(texto)
  u = input('')
  if u == '1':
    uM = 'cm'
  elif u == '2':
    uM = 'm'
  else:
    uM = 'Km'
  return uM

#Función para establecer unidades de medidad de tiempo
def msjUnidadMedidaTiempo():
  texto = """
  Seleccione la unidad de medida de tiempo a usar:
  1. seg
  2. min
  3. Hrs
  """
  print(texto)
  u = input('')
  if u == '1':
    uM = 's'
  elif u == '2':
    uM = 'min'
  else:
    uM = 'h'
  return uM

#Función para borrar pantalla
def limpiar():
  if os.name == "posix":
    os.system ("clear")
  else:
    if((os.name == "ce") or (os.name == "nt") or (os.name == "dos")):
      os.system ("cls")

