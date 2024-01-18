# Questão 7 - Faça um Programa que pergunte quanto um profissional ganha por hora 
# e o número de horas trabalhadas no mês. Calcule e mostre o total do seu 
# salário no referido mês, sabendo-se que são descontados 17% para o 
# Imposto de Renda, 9% para o INSS e 3% para o sindicato, faça um 
# programa em Python que apresente o salário bruto, o valor pago ao INSS
# e ao sindicato, bem como o salário líquido. Calcule o salário líquido, 
# conforme a tabela abaixo: 
# Salário Bruto – (IR (%) + INSS(%) + Sindicato(%)) = Salário Liquido
# OBS.: Salário Bruto - Descontos = Salário Líquido

taxa_IR = 0.17
taxa_inss = 0.09
taxa_sindicato = 0.03

nome = (input("Boa noite, digite seu nome por favor: "))
salario_por_hora = float(input("Digite quanto você recebe de salário por hora trabalhada: R$ "))
horas_trabalhadas_por_mes = int(input("Digite quantas horas foram trabalhadas no mês: "))

salario_bruto = salario_por_hora*horas_trabalhadas_por_mes

descontos = (salario_bruto*taxa_IR) + (salario_bruto*taxa_inss) + (salario_bruto*taxa_sindicato)

salario_liquido = salario_bruto - descontos


print(f"\nO salario bruto do Sr.(a) {nome} foi de: R$ {salario_bruto:.2f}\n")
print(f"O salario com descontos de Imposto de Renda, INSS\ne taxa do sindicato do Sr.(a) {nome} foi de: R$ {salario_liquido:.2f}\n")
print(f"Foram pagos para o Imposto de Renda um total de R$: {salario_bruto*taxa_IR}.")
print(f"Foram pagos para o INSS um total de R$: {salario_bruto*taxa_inss}.")
print(f"Foram pagos para o Sindicato um total de R$: {salario_bruto*taxa_sindicato}.")