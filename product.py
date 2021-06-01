import miscellaneous as mis

def add(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio):
  texto1= 'AGREGAR ---> PRODUCTO'

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
        lisTamanoAux = ['S','M','L','XL']
        index = 0
    
        for i in range(len(lisTamanoAux)):
          index += 1
          print(index, lisTamanoAux[i])
        
        opcion = int(input('\nTamaño opción>>> '))
        if 1 <= opcion <= index:
          tamano = lisTamanoAux[opcion-1] #resta uno porque las posiciones inician en 0
        else:
          tamano = 'xxxx'

        precio = input('\nIngrese Precio del producto: ')

        mis.limpiar()
        print('='*50)
        print(texto1.center(50))
        print('='*50)      
        print('\n¿Desea agregar la siguiente información a la base de datos?\n')
        print(codigo, marca, nacionalidad, color, tamano, precio)
        guardar = mis.againEscapeNega(input('\nS/N >>> '))

        if guardar :
          lisCodigo.append(codigo)
          lisMarca.append(marca)
          lisNacionalidad.append(nacionalidad)
          lisColor.append(color)
          lisTamano.append(tamano)
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