from persistencia import guardar_pedido #Importamod metodo guardar_pedido de archivo persistencia.py

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")

pedidos = {"nombre": "Pedro", "apellidos": "Gil de Diego"},{"nombre": "Michael", "apellidos": "Jordan"} #Definicion de lista con 2 Diccionarios.
 
 #def guardar_pedido(pedidos):
 
for cliente in pedidos:    #Accedemos a cada elemento de la lista (en este caso cada elemento es un diccionario).
     for k, v in cliente.items(): #accedemos a cada llave(k), valor(v) de cada diccionario.
         guardar_pedido(k, v)
         #print(k,v);
 
file.close()
     

