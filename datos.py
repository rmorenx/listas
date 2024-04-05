lista = []

print("BIENVENIDO, QUE DESEA MODIFICAR EN SU LISTA?   \n")

while True:

 print("""MENU:
      1. INSERTAR ELEMENTO
      2. ELIMINAR PRIMER ELEMENTO
      3. ELIMINAR ULTIMO ELEMENTO
      4. ELIMINAR TODOS LOS ELEMENTOS
      """)
 opcion= int(input("SELECCIONE LA OPCION A REALIZAR: "))


 if (opcion == 1):
   new_element = int(input ("INGRESE EL NUMERO QUE DESEE AGREGAR A SU LISTA:" ))
   lista.append(new_element)
   print(lista)

 elif (opcion == 2):
   lista.pop()
   print(lista)

 elif (opcion == 3):
    if lista:
       lista.pop(-1)
    else:
       print("no puedo")

 elif (opcion == 4):
    lista [:]= []
    print(lista)
    #lista.remove[new_element:]
    #rint(lista)
 else:
     print("esta opcion no esta disponible")

