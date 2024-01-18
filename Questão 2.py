# Questão 2 - Escreva uma função que receba uma lista como parâmetro e retorne uma 
# nova lista contendo apenas os números pares da lista original.

numeros = []
pares = []


def encontrar_numeros_pares():

    for i in range(10):
        numero = int(input(f"Digite o valor do {i+1}º numero: "))
        numeros.append(numero)

        if numero %2==0:
            pares.append(numero)
        else:
            pass

    print(f'Os números inseridos foram: {numeros}.')
    print(f'Os números pares entre esses números inseridos são: {pares}.')

encontrar_numeros_pares()