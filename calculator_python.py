def math(calculator):
    if calculator == 'soma':
        return lambda a, b: a + b
    elif calculator == 'subtrair':
        return lambda a, b: a - b
    elif calculator == 'multiplicar':
        return lambda a, b: a * b
    elif calculator == 'dividir':
        return lambda a, b: a / b
    else:
        return None

try:
    operacao = input('Digite uma dessas operações: soma, subtrair, multiplicar, dividir: ').strip().lower()
    if operacao not in ['soma', 'subtrair', 'multiplicar', 'dividir']:
        print('Operação inválida.')
    else:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        
        funcao = math(operacao)
        if funcao:
            try:
                resultado = funcao(numero1, numero2)
                print(f'O resultado de {numero1} e {numero2} é igual a: {resultado}')
            except ZeroDivisionError:
                print('Erro: Não é possível dividir por zero.')
        else:
            print('Operação não suportada.')
except ValueError:
    print('Erro: Entrada inválida. Por favor, insira uma operação e números válidos.')



