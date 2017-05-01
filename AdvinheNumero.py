
import time
resp=1
print ('Tente adivinhar o Número que eu estou pensando.')
print ('Você só tem 5 chances e o número está entre 0 e 100.')
while resp != '0':
    t = time.localtime()
    x=(((t[5]*3)/2)+t[4])-t[3]
    if x>100:
        x=100-(x-100)

    elif x<0:
        x=0
        
    i=1
    
    print
    try:
        a=input('tentativa %d: ' % i)
        a= int(a)
    except:
        a = ''
        print ('Digite um número inteiro válido.')
            
    if a!='':
        while a!=x and i<5:
                if a==x:
                    break

                elif a<x:
                    print ('o numero é mais alto(+)')
                    print

                elif a>x and a!='':
                    print ('o numero é mais baixo(-)')
                    print

                if a!='':
                    i=i+1
                    
                try:
                    a=input('tentativa %d: ' % i)
                    a= int(a)
                except:
                    a = ''
                    print ('Digite um número inteiro válido.')
                    print

        if i==5 and a!=x:
            print
            print ('suas chances acabaram você perdeu!!!')
            print ('o número era', x)
            print

        else:
            print
            print ('Você acertou. Parabens!!!', a)
            print
        resp=input('Para jogar novamente aperte 1 - para sair aperte 0: ')
