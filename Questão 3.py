# Questão 3 - Faça um programa em Python que leia 10 números inteiros, calcule e 
# mostre a quantidade de números pares.

numeros = []
numeros_pares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

def calcular_numeros():
    resultado = sum(numeros)
    print(f"O resultado da soma dos números calculados é de: {resultado}")

def calcular_numeros_pares():
    for i in numeros:
        if i %2==0:
            numeros_pares.append(i)   
        else:
            pass

def mostrar_numeros_pares():
    if len(numeros_pares) >= 1:
        print(f'Os números pares são: {numeros_pares}.')
    else:
        print('Não existem números pares entre os números inseridos.')
    

calcular_numeros()
calcular_numeros_pares()
mostrar_numeros_pares()