# Questão 5 - Faça um programa em Python que realize a leitura de 3 notas de um 
# aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# (A). A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# (B). A mensagem "Reprovado", se a média for menor do que sete; 
# (C). A mensagem "Aprovado com Distinção", se a média for igual a dez.

aluno = input("Digite o nome do aluno: ")
notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota do aluno: "))
    notas.append(nota)

media = (sum(notas))/ (len(notas))

print(f"\nO aluno {aluno} teve a média de {media:.2f}\n")

if media >= 7 and media <10:
    print(f"O aluno {aluno} foi Aprovado.")
elif media == 10:
    print(f"O aluno {aluno} foi Aprovado com Distinção!")
else:
    print(f"O aluno {aluno} foi Reprovado!")