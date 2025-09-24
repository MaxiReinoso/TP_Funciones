def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Programa principal
celsius_usuario = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit_resultado = celsius_a_fahrenheit(celsius_usuario)

print("La temperatura en Fahrenheit es: " + str(fahrenheit_resultado) + "°F")