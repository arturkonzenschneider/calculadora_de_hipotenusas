print('Essa é a calculadora de hipotenusas')
print('Feito por: Artur Konzen Schneider')

cateto1 = int(input('coloque o valor de um dos catetos:   '))
cateto2 = int(input('coloque o valor do segundo cateto:   '))

hipotenusa = (cateto1 * cateto1 + cateto2 * cateto2 )

raiz_quadrada = hipotenusa ** 0.5

print('o valor da hipotenusa é')
print(raiz_quadrada)