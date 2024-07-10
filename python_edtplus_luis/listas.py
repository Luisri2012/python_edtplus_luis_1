#listas en pytho []
numero = [1, 2, 3, 4, 5]
print(type(numero))

# listas de str o condena de texto
tareas = ["aprender python" , "resolver retos" , "resolver problemas"]
print(tareas)

#listas de diferentes tipos de datos

diferentes_tipos_de_datos = [1, "cadena de texto", True, False] 
print(diferentes_tipos_de_datos)

#indice a cada arreglo
print("mostrando el indice [0] del elemento del arreglo ->" , numero [0])
print("mostrando el indice [1] del arreglo -> , tareas[1]")
print("mostrando el indice [3] del arreglo del elemento diferente_tipos_datoas->", diferentes_tipos_de_datos[3])

# municion = modificar el arreglo original
tareas[1] = "ya he resuelto el reto 1"
tareas[2] = "ya he resuelto el reto 2"
print("lista modificada ->", tareas)

#slicing o recorte o pedazo
print(numero[:3])
print(numero[2:])
print(numero[1:5])

#operador in = en = booleano
print(True in diferentes_tipos_de_datos)
print("cadena de texto" in diferentes_tipos_de_datos)
print("otra cosa que no este" in diferentes_tipos_de_datos)