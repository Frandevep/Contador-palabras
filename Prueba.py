# Pedimos una frase al usuario
frase = input("Ingresa una frase: ")

# Contamos las palabras separándolas por espacios
cantidad_palabras = len(frase.split())

# Mostramos el resultado
print("La frase tiene", cantidad_palabras, "palabras.")
