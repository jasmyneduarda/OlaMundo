'''
Elabore um programa que pergunte ao aluno as suas 3 notas escolares.
o programa deverá calcular a média das 3 notas inseridas e exibir esta média .
'''

# Etapa 1: entrada de dados
print("Olá, me imforme suas notas")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

# Etapa 2: processamento de dados
media = (nota1 + nota2 + nota3) / 3

# Etapa 3: Saída de dados ( resposta na tela do usuário)
print ("Sua média é", media)