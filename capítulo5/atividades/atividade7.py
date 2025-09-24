def fahrenheit(celcius):
    return celcius * 1.8 + 32


def temperatura(celcius, fahrenheit):
    print(f"A temperatura de {celcius}° em fahrenheit é {fahrenheit}")


celcius = int(input("Digite alguma temperatura em celcius: "))
GrausFahrenheit = fahrenheit(celcius)
temperatura(celcius,tempFahrenheit)