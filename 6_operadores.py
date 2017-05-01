print(2 + 3)    # soma
print(2 - 3)    # subtração
print(2 * 3)    # multiplicação
print(2 ** 3)   # expoente
print(3 ** 2)   # expoente

minutos = 645
horas = minutos / 60     # divisão float
print(horas,' horas')

horas = minutos // 60     # divisão que retorna somente o inteiro
print(horas,' horas')

print('o resto da divisao ', 7%5)  # operador modulo, resto de divisão

#O operador resto é surpreendentemente útil. Por exemplo,
#você pode utilizá-lo para verificar se um número é divisível
#por outro — se x % y é zero, então x é divisível por y.
#Também, você pode extrair o dígito ou dígitos mais
#à direita de um número. Por exemplo, x % 10 é o
#dígito mais a direita de x (na base 10).
#Similarmente x % 100 é o número formao pelos dois último
#dígitos de x.
#Finalmente, retornando ao nosso exemplo de tempo,
#o operador resto é extremamente útil para fazermos
#conversões, digamos, de segundos para horas,
#minutos e segundos. Se começamos com um certo número de
#segundos, digamos 7684, o programa a seguir usa
#divisão inteira e resto de divisão para converter
#segundos para uma forma mais clara. Siga o código
#passo a passo para se certificar que você entende como os
#operadores divisão e resto são usados para computar
#os valores corretos.
total_segs = 7684
horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos =  segs_restantes // 60
segs_restantes_final = segs_restantes  % 60
print(total_segs,' segundos sao exatamente:')
print(horas,' horas')
print(minutos,' minutos')
print(segs_restantes_final,' segundos')
