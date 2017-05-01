print(3.14, int(3.14))
print(3.9999, int(3.9999))       # Isto não arredonda para o inteiro mais próximo
print(3.0,int(3.0))
print(-3.999,int(-3.999))        # Observe que o resultado está mais próximo de zero

print("2345",int("2345"))        # examina um string para produzir um int
print(17,int(17))                # int também funciona sobre inteiros
print(int("23"))                 # a string "23" é um valor válido e possível de converter

print(float("123"))
print(float("123.45"))
print(float("123,45"))           #causa um erro devido a virgula

print(int("23garafas"))          # garrafas não é um valor válido



