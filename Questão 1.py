#Questão 1 - Faça um programa com uma função chamada calculaImposto. A função 
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
# sobre vendas expressa em porcentagem e custo, que é o custo de um 
# item antes do imposto. A função “altera” o valor de custo para incluir o 
# imposto sobre vendas.

custo_produto = float(input('Digite o custo do produto: '))
taxa_imposto = float(input('Digite a taxa do imposto: '))
print(f"O custo do produto é de R${custo_produto:.2f}.\nE o valor da taxa é de {taxa_imposto:.2f}%.")


def calcula_imposto():
    produto_taxado = ((taxa_imposto/100) * custo_produto) + custo_produto

    print(f"O custo total do produto COM a taxa de imposto fica no valor de: R$ {produto_taxado:.2f}.")
    print(f"O valor antes do imposto era de R$ {custo_produto:.2f}.")
    
    

calcula_imposto()
