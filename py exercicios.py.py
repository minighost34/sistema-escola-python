import math

# 1)
falta1 = int(input())
falta2 = int(input())
soma = falta1 + falta2
print(soma)

# 2)
n1 = float(input())
n2 = float(input())
n3 = float(input())
soma = n1 + n2 + n3
print(soma)

# 3)
n1 = float(input())
n2 = float(input())
n3 = float(input())
media = (n1 + n2 + n3) / 3
print(media)

# 4)
horas = int(input())
minutos = int(input())
total = (horas * 60) + minutos
print(total)

# 5)
celsius = float(input())
fahrenheit = 32 + (1.8 * celsius)
print(fahrenheit)

# 6)
cat1 = float(input())
cat2 = float(input())
hipotenusa = math.sqrt(cat1**2 + cat2**2)
print(hipotenusa)

# 7)
A = int(input())
B = int(input())
C = int(input())
D = int(input())
media = (A*3 + B*4 + C*2 + D*5) / 14
print(media)

# 8)
A = int(input())
B = int(input())
C = int(input())
D = int(input())
media = (A*7 + B*3 + C*4 + D*2) / 16
print(media)

# 9)
prestacao = float(input())
taxa = float(input())
dias = int(input())
nova = prestacao + (prestacao * taxa * dias / 100)
print(nova)

# 10)
raio = float(input())
altura = float(input())
volume = 3.14 * (raio**2) * altura
print(volume)

# 11)
raio = float(input())
altura = float(input())
volume = (3.14 * (raio**2) * altura) / 3
print(volume)

# 12)
raio = float(input())
altura = float(input())
area_base = 3.14 * (raio**2)
area_lateral = 2 * 3.14 * raio * altura
area = 2 * area_base + area_lateral
print(area)