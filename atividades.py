# 1) Olá, usuário!
nome = input("Digite seu nome: ")
print("Olá,", nome)


# 2) Soma de dois números
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
print("Soma:", n1 + n2)


# 3) Média de 3 notas
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
print("Média:", media)


# 4) Par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# 5) Tabuada
num = int(input("Digite um número: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 6) Contador de vogais
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Vogais:", contador)


# 7) Lista: maior, menor e média
N = int(input("Quantos números: "))
lista = []

for i in range(N):
    valor = float(input("Digite um número: "))
    lista.append(valor)

print("Maior:", max(lista))
print("Menor:", min(lista))
print("Média:", sum(lista)/len(lista))


# 8) Jogo de adivinhação
import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Adivinhe (1 a 100): "))
    tentativas += 1

    if chute == numero:
        print("Acertou em", tentativas, "tentativas!")
        break
    elif chute < numero:
        print("Maior")
    else:
        print("Menor")


# 9) Calculadora simples
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro"
    return a / b

print("1-Somar 2-Subtrair 3-Multiplicar 4-Dividir")
op = int(input("Escolha: "))

a = float(input("A: "))
b = float(input("B: "))

if op == 1:
    print(somar(a,b))
elif op == 2:
    print(subtrair(a,b))
elif op == 3:
    print(multiplicar(a,b))
elif op == 4:
    print(dividir(a,b))


# 10) Arquivo tarefas
while True:
    print("1-Adicionar 2-Listar 3-Sair")
    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        with open("tarefas.txt", "a") as f:
            f.write(tarefa + "\n")

    elif op == "2":
        with open("tarefas.txt", "r") as f:
            print(f.read())

    elif op == "3":
        break