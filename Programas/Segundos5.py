def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa principal
segundos_usuario = int(input("Ingresa la cantidad de segundos: "))

horas_resultado = segundos_a_horas(segundos_usuario)

print("La cantidad de horas es: " + str(horas_resultado))