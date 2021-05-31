#Método Ingresar
import miscellaneous as mis

lisCodigo = ['p1','p2','p3']
lisMarca = ['Specialized', 'Treck', 'BMC']
lisNacionalidad = ['Importada','Nacional','Importada']
lisColor = ['Roja','Negra','Roja - Negra']
lisTamaño = ['S','M','L']
lisPrecio = ['950000', '1100000', '1300000']


texto1= 'INGRESAR ---> PRODUCTO'


cond = True

while cond :
  mis.limpiar()
  
  cond2 = True
  while cond2 : 
    mis.limpiar()
    print('='*50)
    print(texto1.center(50))
    print('='*50)

    verificacion = input('Ingrese código del producto: ')
    if not verificacion in lisCodigo : 
      codigo = verificacion
      
      #Selección de Marca
      print('\n-------->Marca:')
      lisMarcaAux = []
      index = 0

      for i in range(len(lisMarca)):
        if not lisMarca[i] in lisMarcaAux :
          lisMarcaAux.append(lisMarca[i])
      
      for i in range(len(lisMarcaAux)):
        index += 1
        print(index, lisMarcaAux[i])
      
      print(index+1,'Otra')

      opcion = int(input('\nMarca opción>>> '))
      if 1 <= opcion <= index:
        marca = lisMarcaAux[opcion-1] #resto uno porque las posiciones inician en 0
        indexnacionalidad = lisMarca.index(marca)
        nacionalidad = lisNacionalidad[indexnacionalidad] 

      #Se ingresa nueva marca a la base de datos
      else:
        marca = input('\nIngrese la marca: ')
        #Se ingresa nacionalidad para nueva marca
        lisNacionalidadAux = []
        index = 0
        print('\n-------->Nacionalidad:')   
        #Crea lista para menú de nacioanlidades 
        for i in range(len(lisNacionalidad)):
          if not lisNacionalidad[i] in lisNacionalidadAux :
            lisNacionalidadAux.append(lisNacionalidad[i])
        #Crea menú de nacionalidades
        for i in range(len(lisNacionalidadAux)):
          index += 1
          print(index, lisNacionalidadAux[i])
        #Asigna la nacionalidad al producto, y un código para error
        indexNal = int(input('\nNacionalidad opción>>>  '))
        if 1 <= indexNal <= 2:
          nacionalidad = lisNacionalidadAux[indexNal-1]
        else:
          nacionalidad = 'xxxx'

      #Selección de Color
      print('\n-------->Color:')
      lisColorAux = []
      index = 0

      for i in range(len(lisColor)):
        if not lisColor[i] in lisColorAux :
          lisColorAux.append(lisColor[i])
      
      for i in range(len(lisColorAux)):
        index += 1
        print(index, lisColorAux[i])
      
      print(index+1,'Otro')     
      opcion = int(input('\nColor opción>>> '))
      if 1 <= opcion <= index:
        color = lisColorAux[opcion-1] #resta uno porque las posiciones inician en 0
      else:
        color = input('\nIngrese color: ')
      
      #Selección de Tamaño
      print('\n-------->Tamaño:')
      lisTamañoAux = ['S','M','L','XL']
      index = 0
  
      for i in range(len(lisTamañoAux)):
        index += 1
        print(index, lisTamañoAux[i])
       
      opcion = int(input('\nTamaño opción>>> '))
      if 1 <= opcion <= index:
        tamaño = lisTamañoAux[opcion-1] #resta uno porque las posiciones inician en 0
      else:
        tamaño = 'xxxx'

      precio = input('\nIngrese Precio del producto: ')

      lastItem = len(lisCodigo) - 1
  
      mis.limpiar()
      print('='*50)
      print(texto1.center(50))
      print('='*50)      
      print('\n¿Desea agregar la siguiente información a la base de datos?\n')
      print(codigo, marca, nacionalidad, color, tamaño, precio)
      guardar = mis.againEscapeNega(input('\nS/N >>> '))

      if guardar :
        lisCodigo.append(codigo)
        lisMarca.append(marca)
        lisNacionalidad.append(nacionalidad)
        lisColor.append(color)
        lisTamaño.append(tamaño)
        lisPrecio.append(precio)
        cond2 = False
      
      else:
        cond2 = mis.againEscapeNega(input('¿Reingresar información?\nS/N>>> '))        

    else:
      mis.limpiar()
      print('='*50)
      print(texto1.center(50))
      print('='*50)
      print('\nEl código',verificacion, 'ya existe en la base de datos')
      cond2 = mis.again()

  mis.limpiar()
  print('='*50)
  print(texto1.center(50))
  print('='*50)
  cond = mis.againEscapeNega(input('\n¿Desea agregar un nuevo producto? S/N >>> '))

print(lisCodigo)
print(lisMarca)
print(lisNacionalidad)
print(lisColor)
print(lisTamaño)
print(lisPrecio)

  
