def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

promedio_resultado = calcular_promedio(numero1, numero2, numero3)

print("El promedio de los tres números es: " + str(promedio_resultado))