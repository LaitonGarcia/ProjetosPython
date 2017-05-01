def quantidade_de_letras (palavra) :
    quantidade = len (palavra)
    return quantidade


a = input ('Digite uma palavra...     ')
b = input ('Digite outra palavra...     ')


if quantidade_de_letras (a) > quantidade_de_letras (b):
    print ('A menor palavra e '+ b)
elif quantidade_de_letras (a) == quantidade_de_letras (b):
    print ('As duas palavras tem a mesma quantidade de letras')
else:
    print ('A menor palavra e '+ a)
