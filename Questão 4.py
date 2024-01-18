# Questão 4 - Faça um programa em Python que leia 8 números e informe a soma e a 
# média dos números.

# Letra A) Altere o programa acime e crie uma função para cálculo de 
# soma e média dos números. Cada função deve apresentar o 
# escopo calculaSoma ( ) e calculaMedia ( ).

#  AQUI O PROGRAMA NORMAL SEM AS FUNÇÕES, RETIRE AS 3 ASPAS PARA FUNCIONAR

'''numeros = []
contador = 8
for i in range(contador):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)


print(sum(numeros))
print((sum(numeros))/8)'''

# ====================================FIM======================================== #


#   LOGO ABAIXO O PROGRAMA COM A ALTERAÇÃO REQUISITADA PELA LETRA 4 DA QUESTÃO 4

numeros = []
contador = 8

for i in range(contador):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

def calculaSoma():
    soma = sum(numeros)
    print(f"A soma total dos números inseridos é de: {soma}.")

def calculaMedia():
    media = (sum(numeros)) / contador
    print(f"A média dos números inseridos é de: {media}")

calculaSoma()
calculaMedia()

