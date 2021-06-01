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

def encabezado(a):
  limpiar()
  print('='*50)
  print(a.center(50))
  print('='*50)

def menuOpcion(lista,item):
  listaAux = []
  index = 0

  for i in range(len(lista)):
    if not lista[i] in listaAux :
      listaAux.append(lista[i])
        
  for i in range(len(listaAux)):
    index += 1
    print(index, listaAux[i])
        
  print(index+1,'Otr@')

  opcion = int(input('\n' + str(item) + ' opción >>> '))
  
  if 1 <= opcion <= index:
    elemento = listaAux[opcion-1] #resto uno porque las posiciones inician en 0
    
  #Se ingresa nueva marca a la base de datos
  else:
    elemento = input('\nIngrese ' + str(item) + ' >>> ')
    #Se ingresa nacionalidad para nueva marca
  
  return elemento
  
def menuOpcionFijo(lista,item):
  index = 0

  for i in range(len(lista)):
    index += 1
    print(index, lista[i])
  
  opcion = int(input('\n' + str(item) + ' opción >>> '))
  
  if 1 <= opcion <= index:
    elemento = lista[opcion-1] #resta uno porque las posiciones inician en 0
  else:
    elemento = 'xxxx'

  return elemento
  
def encabezadoTabla():
  print('*'*50)
  print('|Cod  ',end='')
  print('|Marca        ',end='')
  print('|Nal ',end='')
  print('|Color    ',end='')
  print('|Tam',end='')
  print('|Precio  ','|')
  print('*'*50)

def tabla(a,b,c,d,e,f):
  print('|'+ a,' '*(4-len(a)),end='')
  print('|'+ b,' '*(12-len(b)),end='')
  print('|'+ c,' '*(3-len(c)),end='')
  print('|'+ d,' '*(8-len(d)),end='')
  print('|'+ e,' '*(2-len(e)),end='')
  print('|'+ f,' '*(7-len(f)),'|')
  print('-'*50)