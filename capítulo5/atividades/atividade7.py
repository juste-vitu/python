def fahrenheit(celcius):
    return celcius* 1.8+32

def temperatura(celcius, grausFahrenheit):
    print(f'A temperatura de {celcius}° para fahrenheit é {fahrenheit}')

celcius = int(input("Digite a temperatura em graus celcius: "))
grausFahrenheit = fahrenheit (celcius)
temperatura(celcius, grausFahrenheit)