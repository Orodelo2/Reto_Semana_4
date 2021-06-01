import miscellaneous as mis

def main():
  mis.limpiar()
  texto1 = 'ALMACEN  MARKET-CICLE'
  texto2 = 'MENÚ PRINCIPAL'
  texto3 = '[1].  Asesor'
  texto4 = '[2].  Productos'
  texto5 = '[3].  Clientes'
  texto6 = '[4].  Ventas'
  texto7 = '[5].  Salir'


  print('='*50)
  print(texto1.center(50))
  print(texto2.center(50))
  print('-'*50)
  print(' '*13,texto3)
  print(' '*13,texto4)
  print(' '*13,texto5)
  print(' '*13,texto6)
  print(' '*13,texto7)
  print('='*50)

  opcion = input('\nIngrese opción >>> ')

  return opcion

def product():
  mis.limpiar()
  texto1 = 'ALMACEN  MARKET-CICLE'
  texto2 = 'CRUD - PRODUCTO'
  texto3 = '[1].  Agregar'
  texto4 = '[2].  Mostrar'
  texto5 = '[3].  Consultar'
  texto6 = '[4].  Actualizar'
  texto7 = '[5].  Eliminar'
  texto8 = '[6].  Salir'

  
  print('='*50)
  print(texto1.center(50))
  print(texto2.center(50))
  print('-'*50)
  print(' '*15,texto3)
  print(' '*15,texto4)
  print(' '*15,texto5)
  print(' '*15,texto6)
  print(' '*15,texto7)
  print(' '*15,texto8)
  print('='*50)

  opcion = input('\nIngrese opción >>> ')

  return opcion