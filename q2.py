numero = int(input('Digite o número que deseja consultar: '))
anterior = 0
proximo = 1

while anterior < numero:
    anterior, proximo = proximo, anterior + proximo
if anterior == numero:
    print('O número pertence a Sequência de Fibonacci')
else:
    print('O número não pertence a Sequência de Fibonacci')