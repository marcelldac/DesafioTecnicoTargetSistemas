estados = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']

faturamento = list()
for c in estados:
    while True:
        try:
            faturamentoMensal = float(input(f'Digite o faturamento mensal de {c}: '))
            if faturamentoMensal < 0:
                print('\033[31mValor INVÁLIDO! Digite apenas valores maiores ou iguais a "0":\033[m')
            break
        except:
            print('\033[31mValor INVÁLIDO! Digite apenas valores reais!\033[m')

    faturamento.append(faturamentoMensal)
    
faturamentoTotal = sum(faturamento)
print(f'\033[32mO faturamento total da Distribuidora foi: R$ {faturamentoTotal:.2f}'.replace('.', ','))

cont = 0
for i in faturamento:
    cont += 1
    percentual = ((i / faturamentoTotal) * 100)
    print(f'O percentual de faturamento de {estados[cont - 1]} é: {percentual:.2f} %')