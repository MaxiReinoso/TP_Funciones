def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Programa principal
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones_basicas(numero1, numero2)

print("Suma: " + str(numero1) + " + " + str(numero2) + " = " + str(resultado_suma))
print("Resta: " + str(numero1) + " - " + str(numero2) + " = " + str(resultado_resta))
print("Multiplicación: " + str(numero1) + " x " + str(numero2) + " = " + str(resultado_multiplicacion))
print("División: " + str(numero1) + " / " + str(numero2) + " = " + str(resultado_division))