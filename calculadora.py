numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = input('Digite a opeção: (+, -, /, *): ')

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultadora = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = 'Erro: divisão por zero'
else:
    resultado = 'Operação inválida!'

print('resultado:', resultado)


