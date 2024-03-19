# -*- coding: utf-8 -*-
"""Exercicos_Estrutura_de_Repetição_While.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/188fFprqKAUWKC_SMtaPGsAuP_dkQRBHz
"""

s = 1000

while s < 5000:
 s += 100

print(f"Seu novo salário é: {s} ")

"""1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""

nota =  int(input("Digite uma nota entre 0 e 10 "))

while nota > 10 or nota < 0:
  nota =  int(input("Valor Inválido : Digite uma nota entre 0 e 10: "))

"""2 . Faça um programa que calcule o mostre a média aritmética de N notas."""

nota = 0
total = 0

N = int(input("Qual o total de notas: "))

while nota < N :
  total += int(input("Digite uma nota: "))
  nota +=1

print(f"Sua nota e: {total/N}")

"""3 . Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
"""

usuario = str(input("Digite seu nome de usuario: "))
senha = str(input("Digite sua senha"))

while usuario == senha:
  print("Digite o Usuario e senha novamente: ")
  print(input("Entre com uma nova senha: "))
  senha = str(input("Digite sua senha: "))

"""4 . Um funcionário de uma empresa recebe aumento salarial anualmente.
Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$
1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de
1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior. Faça um programa que determine o salário atual desse
funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.

"""

salario_inicial = float(input("Digite o salário inicial do funcionário: "))

ano_atual = 1995
aumento = 0.015

while ano_atual < 2024:
    ano_atual += 1
    salario_inicial = salario_inicial * (1 + aumento)
    aumento *= 2

print("O salário atual do funcionário em 2024 é: R$", salario_inicial)

"""5 . Faça um programa que leia e valide as seguintes informações:
 Nome: maior que 3 caracteres;
 Idade: entre 0 e 150;
 Salário: maior que zero;
 Sexo: 'f' ou 'm';
 Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite o seu nome completo: ")

while len(nome) <= 3:
  nome = input("O nome precisa ter mais que três caracteres, digite seu nom novamente:  ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
  idade = int(input("Idade inválida, digite sua idade novamente: "))

salario = int(input("Digite o seu salario: "))
while salario <= 0:
  salario = float(input("Seu pobre! Tenha mais dinheiro na sua conta, digite seu salario novamente: "))

sexo = input("Digite o seu sexo: [f, m] ")
while sexo != 'f' and sexo != 'm':
  sexo = input("Opção inválida! Digite seu sexo novamente: ")

estado_civil = input("Digite seu estado civil [s = solteiro; c = casado; v = viuvo; d = divorciado]")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
  estado_civil = input("Entrada Inválida! Digite seu estado civil novamente: ")

"""6.  Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""

A = 80000
B = 200000

a = 0.03
b = 0.015

anos = 0

while A < B:
  anos += 1
  A = A + (A * a)
  B = B + (B * b)

print(f"A cidade A vai demorar: {anos} anos, para se igualar a cidade B")

"""7 . Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input("Digite o numero que você quer calcular o fatorial: "))

resultado = 1
contador = 1

while contador <= numero:
  resultado *= contador
  contador += 1

print(f"O Fatorial do Numero {numero} é: {resultado}")

"""8 . Faça um programa que solicite ao usuário números indefinidamente até que ele
digite 0. Em seguida, o programa deve imprimir a média dos números digitados.
"""

soma = 0
quantidade = 0

while True:
  numero = float(input("Digite um Numero Qualquer e 0 para sair: "))
  if numero == 0:
    break
  soma += numero
  quantidade += 1

if quantidade > 0:
  media = soma / quantidade
  print(f"A média dos numeros digitados é: {media}")
else:
  print("Nenhum numero foi digitado!")

"""9 . A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.

"""

termos =10

total = 0
numero1 = 1
numero2 = 1
contador = 0

while contador < termos:
  total = numero1 + numero2
  numero1 = numero2
  numero2 = total
  contador +=1
  print(f"O numero de total é: {total}")

"""10 . O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências. Faça um programa que implemente uma
caixa registradora rudimentar.
 O programa deverá receber um número desconhecido de valores referentes
aos preços das mercadorias. Um valor zero deve ser informado pelo
operador para indicar o final da compra.
 O programa deve então mostrar o total da compra e perguntar o valor em
dinheiro que o cliente forneceu, para então calcular e mostrar o valor do
troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
registrar a próxima compra.
 A saída deve ser conforme o exemplo abaixo:
 Lojas Tabajara
 Produto 1: R$ 2.20
 Produto 2: R$ 5.80
 Produto 3: R$ 0
 Total: R$ 9.00
 Dinheiro: R$ 20.00
 Troco: R$ 11.00
"""

print("Lojas Tabajara")

total = 0
produto = 0
valor = 0

while True:
  produto += 1
  valor= float(input(f"Produto {produto}: R$"))
  if valor == 0:
    break
  total += valor

print(f"O Total da compra foi R${total:.2f}")

dinheiro = float(input("Dinheiro Recebifo: "))
print(f"Troco: {dinheiro - total:.2f}")

"""11 . O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
 Cachorro Quente 100 R$ 1,20
 Bauru Simples 101 R$ 1,30
 Bauru com ovo 102 R$ 1,50
 Hambúrguer 103 R$ 1,20
 Cheeseburguer 104 R$ 1,30
 Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do
pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

# ler o codigo dos itens pedido
# leia as quantidades desejadas
# Calcule o valor a ser pago por item
# mostre o valor a ser pago por item
# calcule o valor a ser geral do pedido
# mostre o valor a ser geral do pedido
# o cliente deve informar quando o pedido deve ser encerrado

quantidade_produto_100 = 0
quantidade_produto_101 = 0
quantidade_produto_102 = 0
quantidade_produto_103 = 0
quantidade_produto_104 = 0
quantidade_produto_105 = 0
total = 0

print("""
    Produto          Codigo      Preco
    n----------------------------------
    Cachorro quente   100       R$ 1.20
    Bauro Simples     101       R$ 1.30
    Bauru com Ovo     102       R$ 1.50
    Hamburguer        103       R$ 1.30
    Cheeseburguer     104       R$ 1.30
    Refrigerante      105       R$ 1.00
"""
)

while True:
  codigo = int(input("Digite o codigo do produto que deseja adquirir: (ou 0 para encerrar)"))
  if codigo == 0:
    break
  if codigo > 105 or codigo < 100:
    print("Codigo invalido!!!")
    continue

  quantidade = int(input("Digite a quantidade desse produto: "))
  if codigo == 100:
    quantidade_produto_100 += quantidade
  if codigo == 101:
    quantidade_produto_101 += quantidade
  if codigo == 102:
    quantidade_produto_102 += quantidade
  if codigo == 103:
    quantidade_produto_103 += quantidade
  if codigo == 104:
    quantidade_produto_104 += quantidade
  if codigo == 105:
    quantidade_produto_105 += quantidade

  print("""
        Fechamento do Pedido
        Codigo   -   Quantidade   -   Preco unidade   -    Preco Total
  """)

  if quantidade_produto_100 > 0:
    print(f"""
      100   -   {quantidade_produto_100}    -   R$1.20    - {quantidade_produto_100 * 1.2:.2f}
    """)
    total += quantidade_produto_100 * 1.2

  if quantidade_produto_101 > 0:
    print(f"""
      101   -   {quantidade_produto_101}    -   R$1.20    - {quantidade_produto_101 * 1.3:.2f}
    """)
    total += quantidade_produto_101 * 1.3

  if quantidade_produto_102 > 0:
    print(f"""
      102   -   {quantidade_produto_102}    -   R$1.20    - {quantidade_produto_102 * 1.5:.2f}
    """)
    total += quantidade_produto_102 * 1.5

  if quantidade_produto_103 > 0:
    print(f"""
      103   -   {quantidade_produto_103}    -   R$1.20    - {quantidade_produto_103 * 1.2:.2f}
    """)
    total += quantidade_produto_103 * 1.2

  if quantidade_produto_104 > 0:
    print(f"""
      104   -   {quantidade_produto_104}    -   R$1.20    - {quantidade_produto_104 * 1.3:.2f}
    """)
    total += quantidade_produto_104 * 1.3

  if quantidade_produto_105 > 0:
    print(f"""
      105   -   {quantidade_produto_105}    -   R$1.20    - {quantidade_produto_105 * 1:.2f}
    """)
    total += quantidade_produto_105 * 1

print(f"Total do pedido: R$ {total:.2f}")

"""12. Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código.
Os códigos utilizados são:
 1, 2, 3, 4 - Votos para os respectivos candidatos
 (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
 5 - Voto Nulo
 6 - Voto em Branco
Faça um programa que calcule e mostre:
 O total de votos para cada candidato;
 O total de votos nulos;
 O total de votos em branco;
 A percentagem de votos nulos sobre o total de votos;
 A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero
"""

# apresentar candidatos
# informar nulo, sair e branco
# Calcule e mostre o total de votos para candidato
# Calcule e mostre brancos
# Calcule e mostre nulos
# % de nulos sobre o total
# % de brancos sobre o total

print("candidatos: \n1 - Pericles\n2 - Sosia do pele\n3 - Zeca Pagodinho\n4 - Hulk Magrelo ")
print("Digite 0 para sair, 5 para nulo e  para branco")

votos = 0
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulos = 0
brancos = 0

while True:
  voto = int(input(f"Digite o voto numero {votos + 1}:"))
  if voto == 0:
    break
  votos += 1
  if voto == 1:
    candidato_1 += 1
  elif voto == 2:
    candidato_2 += 1
  elif voto == 3:
    candidato_3 += 1
  elif voto == 4:
    candidato_4 += 1
  elif voto == 5:
    nulos += 1
  elif voto == 6:
    brancos += 1
  else:
    print("Voto invalido")
    votos -= 1

print(f"""
      Resultado da Eleição:
      Pericles teve {candidato_1} votos
      Sosia do pele teve {candidato_2} votos
      Zeca Pagodinho teve {candidato_3} votos
      Hulk Magrelo teve {candidato_4} votos
      {nulos} votos foram anulados, um total de {100 * nulos / votos:.2f}%
      {brancos} votos foram em branco, um total de {100 * brancos / votos:.2f}%



""")