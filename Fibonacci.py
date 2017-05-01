def fibonacci(n):
    a=1
    b=1
    while n>0:
        print(a)
        c = a+b
        a = b
        b = c 
        n -= 1 
    return a

def main():
    n=int(input("Numero de vezes:"))
    r=fibonacci(n)
    print(r)
main()
