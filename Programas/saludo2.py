def saludar_usuario(nombre):
    saludo = "Hola " + nombre + "!"
    return saludo

# Programa principal
nombre_usuario = input("Por favor, ingresa tu nombre: ")

mensaje_saludo = saludar_usuario(nombre_usuario)

print(mensaje_saludo)