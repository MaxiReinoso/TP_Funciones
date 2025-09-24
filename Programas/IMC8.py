def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# Programa principal
peso_usuario = float(input("Ingresa tu peso en kilogramos: "))
altura_usuario = float(input("Ingresa tu altura en metros: "))

resultado_imc = calcular_imc(peso_usuario, altura_usuario)

print("Tu IMC es: " + str(round(resultado_imc, 2)))