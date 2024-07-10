"""
lista = []
dict = {}
tuple()
"""
mi_diccionario = {}
print("la forma en que lo representa python", type (mi_diccionario))

# los diccionario se representa por teneer llave-> valor (ingles: key - volue)
mi_diccionario = {
    "key": "value"
    "llave": "valor",
    "nombre": "luis",
    "vida": "es necesario para saber que estamos vivos",
    "edad": 11 
}
print(mi_diccionario)

# para saber la longitud de nuestro diccionario se aplica el metodo len

longitud_dict = len(mi_diccionario)
print("esta es la longitud de nuestro diccionario ->, longitud_dict")

#obtener valores segun su palabra clave (key o llave)

print( "el valor de la palabra clave vida es ->, mi_diccionario["vida"])
print( "el valor de la palabra clave vida es ->, mi_diccionario["edad"])
      
# metodo para obtener el valor segun su palabra clave
print("este metodo get me permite obtener el valor segun su llave ->, mi_diccionario.get("vida")

#metodo in para saber si el key esta dentro del diccionario
print("saber si esta key esta en el diccionario y retorna un booleano -., "nombre" in mi_diccionario)