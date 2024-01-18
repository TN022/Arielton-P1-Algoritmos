# Questão 6 - A empresa TPVFR (Todo Programador Vai ficar Rico) resolveu conceder
# aumento salarial aos seus programadores. Para isso você foi contratado
# para desenvolver o programa que calculará todo os reajustes. Dessa 
# forma desenvolva um programa em Pyhton que recebe o salário de um 
# determinado programador e apresente o salário atualizado de acordo com 
# os critérios de salários.

#       • Salários até R$ 2800,00 (incluindo): aumento de 20% 
#       • Salários entre R$ 2800,00 e R$ 7000,00: aumento de 15% 
#       • Salários entre R$ 7000,00 e R$ 15000,00: aumento de 10% 
#       • Salários de R$ 15000,00 em diante: aumento de 5%,

funcionario = input("Digite o nome do funcionário: ")
salario = float(input(f"Digite o salário do funcionário(a) {funcionario}: R$ "))

if salario <=2800:
    salario_com_aumento = (salario*0.20) + salario
    print(f"O funcionário(a) {funcionario} obteve 20% de aumento no seu salário esse mês.\nTotalizando: R$ {salario_com_aumento:.2f}")
elif salario >2800 and salario<=7000:
    salario_com_aumento = (salario*0.15) + salario
    print(f"O funcionário(a) {funcionario} obteve 15% de aumento no seu salário esse mês.\nTotalizando: R$ {salario_com_aumento:.2f}")
elif salario >7000 and salario<=15000:
    salario_com_aumento = (salario*0.10) + salario
    print(f"O funcionário(a) {funcionario} obteve 10% de aumento no seu salário esse mês.\nTotalizando: R$ {salario_com_aumento:.2f}")
else:
    salario_com_aumento = (salario*0.05) + salario
    print(f"O funcionário(a) {funcionario} obteve 5% de aumento no seu salário esse mês.\nTotalizando: R$ {salario_com_aumento:.2f}")

