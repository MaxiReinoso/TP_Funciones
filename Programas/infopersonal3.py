def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia)

# Programa principal
nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
edad_usuario = input("Ingresa tu edad: ")
residencia_usuario = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)