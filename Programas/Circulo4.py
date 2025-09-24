#Funcion1
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * radio * radio
    return area
#Funcion2
def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro

# Programa principal
radio_usuario = float(input("Ingresa el radio del círculo: "))

area_resultado = calcular_area_circulo(radio_usuario)
perimetro_resultado = calcular_perimetro_circulo(radio_usuario)

print("El área del círculo es: " + str(area_resultado))
print("El perímetro del círculo es: " + str(perimetro_resultado))