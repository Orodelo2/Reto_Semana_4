import miscellaneous as mis

def add(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  #Inicialización de ciclo While principal
  cond = True
  while cond :
    mis.limpiar()
    #Inicialización de ciclo Whilw secundario
    cond2 = True
    while cond2 : 
      mis.encabezado('AGREGAR ---> PRODUCTO')

      #Validación del código ingresado
      verificacion = input('\nIngrese código del producto >>> ')
      
      #Inicio de captura de datos si el código es nuevo
      if not verificacion in lisCodigo : 
        #Se asigna el código ingresado
        codigo = verificacion
        
        #Selección de Marca
        mis.encabezado('AGREGAR ---> PRODUCTO')
        print('\n-------->Marca:')
        marca = mis.menuOpcion(lisMarca,'Marca')
     
        #Selección de Nacionalidad
        if not marca in lisMarca:
          mis.encabezado('AGREGAR ---> PRODUCTO')
          print('\n-------->Nacionalidad:')   
          nacionalidad = mis.menuOpcionFijo(['Imp','Nal'],'Nacionalidad') 
        else:
          indexNal = lisMarca.index(marca)
          nacionalidad = lisNacionalidad[indexNal]

        #Selección de Color
        mis.encabezado('AGREGAR ---> PRODUCTO')
        print('\n-------->Color:')
        color = mis.menuOpcion(lisColor,'Color')
        
        #Selección de Tamaño
        mis.encabezado('AGREGAR ---> PRODUCTO')
        print('\n-------->Tamaño:')
        tamano = mis.menuOpcionFijo(['S','M','L','XL'],'Tamaño')      
        
        #Asignación de precio
        mis.encabezado('AGREGAR ---> PRODUCTO')
        precio = input('\nIngrese Precio del producto: ')
        
        #Confirmación de ingreso de datos
        mis.encabezado('AGREGAR ---> PRODUCTO')     
        print('\n¿Desea agregar la siguiente información a la base de datos?\n')
        mis.encabezadoTabla()
        mis.tabla(codigo, marca, nacionalidad, color, tamano, precio)

        guardar = mis.againEscapeNega(input('\nS/N >>> '))
        if guardar :
          lisCodigo.append(codigo)
          lisMarca.append(marca)
          lisNacionalidad.append(nacionalidad)
          lisColor.append(color)
          lisTamano.append(tamano)
          lisPrecio.append(precio)
          cond2 = False  #Salida del While secundario si if es verdadero   
        else:
          cond2 = mis.againEscapeNega(input('¿Reingresar información?\nS/N>>> ')) #Salida del While secundario si if 'guardar' es falso       
      #Opción de introducir un código diferente si se digitó uno existente o salir
      else:
        mis.encabezado('AGREGAR ---> PRODUCTO')
        print('\nEl código',verificacion, 'ya existe en la base de datos')
        cond2 = mis.again() #Salida del While secundario si if 'verificación' es falso

    #Solicitud de ingresar un nuveo producto o salir del ciclo principal de producto
    mis.encabezado('AGREGAR ---> PRODUCTO')
    cond = mis.againEscapeNega(input('\n¿Desea agregar un nuevo producto? S/N >>> '))#Salida del While principal si no se desea agregar un nuevo producto

def show(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  #Inicialización de ciclo While principal
  cond = True
  while cond :
    #Impresión en pantalla del encabezado de la opción
    mis.encabezado('MOSTRAR ---> PRODUCTO')
    mis.next()
    
    #Creación de la tabla con todos los elementos de la Base de Datos
    mis.limpiar()
    mis.encabezado('MOSTRAR ---> PRODUCTO')
    mis.encabezadoTabla()
    if len(lisCodigo) > 0:
      for i in range(len(lisCodigo)):
        mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
      mis.next()
      cond = False
    #Salida del while si la base de datos está vacía.
    else:
      print('\nNo hay productos registrados en la base de datos')
      mis.next()
      cond = False

def find(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  #Inicializando while principal
  cond = True
  while cond :
    #Impresión en pantalla del encabezado de la opción
    mis.encabezado('CONSULTAR ---> PRODUCTO')
    
    #Validación de que la base de datos no esté vacía.
    if len(lisCodigo) > 0 :
      #Inicio de la busqueda con la solictud del código
      codigo = input('\nIngrese código del producto >>> ')

      mis.encabezado('CONSULTAR ---> PRODUCTO')
      mis.encabezadoTabla()
      #Crear tabla de salida de existir el código, si no existe envía mensaje de realizar nueva busqueda.
      if codigo in lisCodigo:
        i = lisCodigo.index(codigo)
        mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

        cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))
      
      else:
        print('\nEl código',codigo,'no existe en la base de datos')
        cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))
        
    else:
      print('\nNo hay productos registrados en la base de datos')
      mis.next()
      cond = False

def update(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  #Inicialización del while principal
  cond = True
  while cond :
    #Validación de que la base de datos no está vacía
    if len(lisCodigo) > 0 :
      mis.encabezado('ACTUALIZAR ---> PRODUCTO')
      #Solicitud del código para el prodcuto a modificar
      codigo = input('\nIngrese código del producto >>> ')

      if codigo in lisCodigo:
        #Se obtiene el indice del codigo para traer sus elementos asociados
        i = lisCodigo.index(codigo)
        #Inicialización del while secundario
        cond2 = True
        while cond2:
          #Creación de encabezado
          mis.encabezado('ACTUALIZAR ---> PRODUCTO')
          mis.encabezadoTabla()
          mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
         
          #Creación de menu de aspectos a cambiar
          print('\n¿Qué aspecto desea cambiar?')
          print('-'*20)
          item = mis.menuOpcionFijo(['Codigo','Marca','Nacionalidad','Color','Tamaño','Precio','Salir'],'Digite')

          #crea nuevamente encabezado con la tabla
          mis.encabezado('ACTUALIZAR ---> PRODUCTO')
          mis.encabezadoTabla()
          mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

          #Modificación del Código
          if item == 'Codigo' :
            newCodigo = input('\nIngrese nuevo CÓDIGO >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
            
            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisCodigo[i]) + ' por '+str(newCodigo)+' ? S/N >>>'))
            if conf:
              lisCodigo[i] = newCodigo
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None
          #Modificación de la marca
          elif item == 'Marca' :
            newMarca = input('\nIngrese nueva MARCA >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisMarca[i]) + ' por '+str(newMarca)+' ? S/N >>>'))
            if conf:
              lisMarca[i] = newMarca
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None      
          #Modificación de la nacionalidad
          elif item == 'Nacionalidad' :
            newNal = input('\nIngrese nueva NACIONALIDAD >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisNacionalidad[i]) + ' por '+str(newNal)+' ? S/N >>>'))
            if conf:
              lisNacionalidad[i] = newNal
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None
          #Modificación del Color
          elif item == 'Color' :
            newColor = input('\nIngrese nuevo COLOR >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisColor[i]) + ' por '+str(newColor)+' ? S/N >>>'))
            if conf:
              lisColor[i] = newColor
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None
          #Modificación del Tamaño
          elif item == 'Tamaño' :
            newTamano = input('\nIngrese nuevo TAMAÑO >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])

            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisTamano[i]) + ' por '+str(newTamano)+' ? S/N >>>'))
            if conf:
              lisTamano[i] = newTamano
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None
          #Modificación del Precio
          elif item == 'Precio' :
            newPrecio = input('\nIngrese nueva PRECIO >>> ')
            mis.encabezado('ACTUALIZAR ---> PRODUCTO')
            mis.encabezadoTabla()
            mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
            
            conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisPrecio[i]) + ' por '+str(newPrecio)+' ? S/N >>>'))
            if conf:
              lisPrecio[i] = newPrecio
              mis.encabezado('ACTUALIZAR ---> PRODUCTO')
              mis.encabezadoTabla()
              mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
              print('\n¡Cambio Existoso!')
              mis.next()
            else:
              None
          #Salir de modificaciones
          elif item == 'Salir':
            cond2 = False
          
          #Solicitud cambio de otro aspecto para el mismo producto, o salida del while secundario
          mis.encabezado('ACTUALIZAR ---> PRODUCTO')
          mis.encabezadoTabla()
          mis.tabla(lisCodigo[i], lisMarca[i], lisNacionalidad[i], lisColor[i], lisTamano[i], lisPrecio[i])
          cond2 = mis.againEscapeNega(input('\n¿Modificar otro aspecto? S/N >>> '))
        
        #Solicitud busqueda de producto para modificar, o salida del while principal
        mis.encabezado('ACTUALIZAR ---> PRODUCTO')
        cond = mis.againEscapeNega(input('\n¿Buscar otro código? S/N >>> '))
      
      #Solicitud busqueda de otro producto para modificar si se digito uno que no existe, o salida del while principal
      else:
        print('\nEl código',codigo,'no existe en la base de datos')
        cond = mis.againEscapeNega(input('\n¿Buscar otro código? S/N >>> '))

    #Se sale del while a menú prodcutos por estar la base de datos vacía
    else:
      print('\nNo hay productos registrados en la base de datos')
      mis.next()
      cond = False

def delete(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  texto= 'ELIMINAR ---> PRODUCTO'

  cond = True

  while cond :
    
    if len(lisCodigo) > 0 :
      mis.limpiar()
      print('='*50)
      print(texto.center(50))
      print('='*50)

      codigo = input('\nIngrese código del producto >>> ')
      mis.limpiar()
      print('='*50)
      print(texto.center(50))
      print('='*50)  

      if codigo in lisCodigo:
        i = lisCodigo.index(codigo)

        a = len(lisCodigo[i])
        b = len(lisMarca[i])
        c = len(lisNacionalidad[i])
        d = len(lisColor[i])
        e = len(lisTamano[i])
        f = len(lisPrecio[i])
        print('|Cod  ',end='')
        print('|Marca        ',end='')
        print('|Nal ',end='')
        print('|Color    ',end='')
        print('|Tam',end='')
        print('|Precio  ','|')
        print('-'*50)
        print('|'+ lisCodigo[i],' '*(4-a),end='')
        print('|'+ lisMarca[i],' '*(12-b),end='')
        print('|'+ lisNacionalidad[i],' '*(3-c),end='')
        print('|'+ lisColor[i],' '*(8-d),end='')
        print('|'+ lisTamano[i],' '*(2-e),end='')
        print('|'+ lisPrecio[i],' '*(7-f),'|')

        delete = mis.againEscapeNega(input('\n¿Eliminar la información relacionada? S/N >>> '))

        if delete:
          del lisCodigo[i]
          del lisMarca[i]
          del lisColor[i]
          del lisTamano[i]
          del lisPrecio[i]
          del lisNacionalidad[i]
          print('\n¡Acción exitosa!')
          cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))

        else:
          mis.limpiar()
          print('='*50)
          print(texto.center(50))
          print('='*50)
          cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))

    else:
        print('\nNo hay productos registrados en la base de datos')
        mis.next()
        cond = False