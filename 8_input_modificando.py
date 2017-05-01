# todo valor captado pelo shell é uma string
# então deverá modificar segundo necessidades, ex.:

# leia o numero de segundos
segundos_str = input("Por favor, digite o numero de segundos que deseja converter: ")

total_segs = int(segundos_str) # aqui faz a conversão para int

# calcule o numero de horas
horas = total_segs // 3600
segs_restantes = total_segs % 3600

# calcule o numero de minutos
minutos =  segs_restantes // 60

# calcule o numero de segundos
segs_restantes_final = segs_restantes  % 60

print("Hrs=", horas, "mins=", minutos, "segs=", segs_restantes_final)

#A variável segundos_str irá se referir ao atring que foi
#digitado pelo usuário. Como dissemos anteriormente, mesmo
#que esse string seja 7684`, ele é ainda um string e não um
#número. Para convertê-lo para um inteiro usamos a função
#``int. O resultado será referenciado por total_segs. Agora,
#cada vez que executamos o programa, você pode entrar
#com um novo valor para o número de segundos a serem convertidos.
