#14 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

valorCelcius = float(input('Informe a temperatura em Celsius (°C): '))
valorEmFahrenheit = valorCelcius*9/5+32
valorEmKelvin = valorCelcius+273.15
print('O valor de {}°C corresponde a {:.2f}°F e {}K'.format(valorCelcius,valorEmFahrenheit,valorEmKelvin))
