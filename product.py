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

    #Solicitud de ingresar un nuveo producto o salir del ciclo principal
    mis.encabezado('AGREGAR ---> PRODUCTO')
    cond = mis.againEscapeNega(input('\n¿Desea agregar un nuevo producto? S/N >>> '))#Salida del While principal si no se desea agregar un nuevo producto

def show(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  texto= 'MOSTRAR ---> PRODUCTO'

  cond = True

  while cond :
    mis.limpiar()
    print('='*50)
    print(texto.center(50))
    print('='*50)
    mis.next()
    
    mis.limpiar()
    print('='*50)
    print(texto.center(50))
    print('='*50)
    
    if len(lisCodigo) > 0:
      for i in range(len(lisCodigo)):
        a = len(lisCodigo[i])
        b = len(lisMarca[i])
        c = len(lisNacionalidad[i])
        d = len(lisColor[i])
        e = len(lisTamano[i])
        f = len(lisPrecio[i])
        print('|'+ lisCodigo[i],' '*(4-a),end='')
        print('|'+ lisMarca[i],' '*(12-b),end='')
        print('|'+ lisNacionalidad[i],' '*(3-c),end='')
        print('|'+ lisColor[i],' '*(8-d),end='')
        print('|'+ lisTamano[i],' '*(2-e),end='')
        print('|'+ lisPrecio[i],' '*(7-f),'|')
      mis.next()
      cond = False
      
    else:
      print('\nNo hay productos registrados en la base de datos')
      mis.next()
      cond = False

def find(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  texto= 'CONSULTAR ---> PRODUCTO'

  cond = True

  while cond :
    mis.limpiar()
    print('='*50)
    print(texto.center(50))
    print('='*50)

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
        print('|'+ lisCodigo[i],' '*(4-a),end='')
        print('|'+ lisMarca[i],' '*(12-b),end='')
        print('|'+ lisNacionalidad[i],' '*(3-c),end='')
        print('|'+ lisColor[i],' '*(8-d),end='')
        print('|'+ lisTamano[i],' '*(2-e),end='')
        print('|'+ lisPrecio[i],' '*(7-f),'|')

        cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))
      
      else:
        print('\nEl código',codigo,'no existe en la base de datos')
        cond = mis.againEscapeNega(input('\n¿Realizar otra busqueda? S/N >>> '))
        
         
    else:
      print('\nNo hay productos registrados en la base de datos')
      mis.next()
      cond = False

def update(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  texto= 'ACTUALIZAR ---> PRODUCTO'

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

        print('\n¿Qué aspecto desea cambiar?')
        print('-'*20)
        print('1. Codigo')
        print('2. Marca')
        print('3. Nacionalidad')
        print('4. Color')
        print('5. Tamaño')
        print('6. Precio')
        print('7. Salir')
        item = mis.seleccionar()

        mis.limpiar()
        print('='*50)
        print(texto.center(50))
        print('='*50)
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

        if item == '1' :
          newCodigo = input('\nIngrese nuevo CÓDIGO >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisCodigo[i]) + ' por '+str(newCodigo)+' ? S/N >>>'))

          if conf:
            lisCodigo[i] = newCodigo
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '2' :
          newMarca = input('\nIngrese nueva MARCA >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisMarca[i]) + ' por '+str(newMarca)+' ? S/N >>>'))
          if conf:
            lisMarca[i] = newMarca
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '3' :
          newNal = input('\nIngrese nueva NACIONALIDAD >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisNacionalidad[i]) + ' por '+str(newNal)+' ? S/N >>>'))
          if conf:
            lisNacionalidad[i] = newNal
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '4' :
          newColor = input('\nIngrese nuevo COLOR >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisColor[i]) + ' por '+str(newColor)+' ? S/N >>>'))
          if conf:
            lisColor[i] = newColor
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '5' :
          newTamano = input('\nIngrese nuevo TAMAÑO >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisTamano[i]) + ' por '+str(newTamano)+' ? S/N >>>'))
          if conf:
            lisTamano[i] = newTamano
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '6' :
          newPrecio = input('\nIngrese nueva PRECIO >>> ')
          conf = mis.againEscapeNega(input('\n¿Desea Cambiar '+ str(lisPrecio[i]) + ' por '+str(newPrecio)+' ? S/N >>>'))
          if conf:
            lisPrecio[i] = newPrecio
            mis.limpiar()
            print('='*50)
            print(texto.center(50))
            print('='*50)
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
            print('\n¡Cambio Existoso!')
          else:
            None
        elif item == '7':
          cond = False
        
        cond = mis.againEscapeNega(input('\n¿Buscar otro código? S/N >>> '))
      
      else:
        print('\nEl código',codigo,'no existe en la base de datos')
        cond = mis.againEscapeNega(input('\n¿Buscar otro código? S/N >>> '))


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