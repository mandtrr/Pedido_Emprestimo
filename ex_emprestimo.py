# valor da casa
#salario do comprador
# quantos anos de financiamento
# a prestação nao pode exceder 30% do salario da pessoa
valor_casa = float(input('Qual é o valor da casa? '))
salario_comprador = float(input('Qual é o seu salário? '))
tempo_financiamento = int(input('Em quantos anos quer financiar? '))

prestacao = valor_casa / (tempo_financiamento * 12)
limite_prestacao = salario_comprador * 30 / 100

if prestacao <= limite_prestacao:
    print(f'Para pagar uma casa no valor de {valor_casa}')
    print(f'em {tempo_financiamento} anos, sua prestação será de {prestacao:.2f}')
    print(f'Seu empréstimo foi aprovado!')

else: 
    print(f'Para pagar uma casa no valor de {valor_casa}')
    print(f'em {tempo_financiamento} anos, sua prestação será de {prestacao:.2f}')
    print('Sendo assim, seu empréstimo foi NEGADO.')


