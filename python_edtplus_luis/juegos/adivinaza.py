import random
# Paso 1: Crear una lista de palabras
palabras = ["manzana", "perro", "gato", "libro", "mesa"]

# Paso 2: Seleccionar una palabra al azar
palabra_secreta = random.choice(palabras)

# Paso 3: Ocultar la palabra
palabra_oculta = ["_"] * len(palabra_secreta)

# Contador de intentos
intentos = 0

# Bucle principal del juego
while "_" in palabra_oculta and intentos < 10:
    print("\nPalabra secreta:", "".join(palabra_oculta))
    letra = input("Adivina una letra: ").lower()
    
    # Verificar si la letra está en la palabra secreta
    for i in range( len(palabra_secreta)):
        if letra == palabra_secreta[i]:
            palabra_oculta[i] = letra
    
    # Actualizar el contador de intentos
    intentos += 1

# Determinar el resultado
if "_" not in palabra_oculta:
    print("\n¡Felicidades Has adivinado la palabra.")
else:
    print("\nLo siento, has agotado tus intentos.")

print(f"\nLa palabra era: {palabra_secreta}")
 