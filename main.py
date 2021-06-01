#Método Ingresar
import miscellaneous as mis
import product
import menu


lisCodigo = ['p1','p2','p3']
lisMarca = ['Specialized', 'Treck', 'BMC']
lisNacionalidad = ['Imp','Nal','Imp']
lisColor = ['Roja','Negra','R/N']
lisTamano = ['S','M','L']
lisPrecio = ['950000', '1100000', '1300000']

ejecutar = True

while ejecutar :
  item = menu.main()

  if item == '1':
    None
  
  elif item == '2':
    cond = True
    while cond:
      item = menu.product()
      if item == '1' :
        product.add(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio)
      elif item == '2' :
        product.show(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio)
      elif item == '3' :
        product.find(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio)
      elif item == '4' :
        product.update(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio)
      elif item == '5' :
        product.delete(lisCodigo,lisMarca,lisNacionalidad,lisColor,lisTamano,lisPrecio)
      elif item == '6' :
        cond = False
      else:
        print('Opción no validad')
        mis.next()  
 
  elif item == '3':
    None

  elif item == '4':
    None

  elif item == '5':
    ejecutar = False

  else:
    print('Opción no validad')
    mis.next()
   
