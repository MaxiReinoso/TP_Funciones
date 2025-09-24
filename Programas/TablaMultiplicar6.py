def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(str(numero) + " x " + str(i) + " = " + str(resultado))

# Programa principal
numero_usuario = int(input("Ingresa el número para la tabla de multiplicar: "))

tabla_multiplicar(numero_usuario)