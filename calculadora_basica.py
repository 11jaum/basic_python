print('Bem vindo a calculadora básico do python')
print(' ')
print('Você quer fazer que tipo de operação? ')

while True:
    operador = int(input("""
    [1] Digite 1 para adiçao (+)
    [2] Digite 2 para subtração (-)
    [3] Digite 3 para multiplicação (x)
    [4] Digite 4 para divisão (/)
                 
                """))
    
    if operador >= 1 and operador <=4:
        x1 = float(input('Insira o primeiro número aqui: '))
        x2 = float(input('Insira o segundo número aqui: '))
        print(' ')
        print(' ')
        
        if operador == 1:
            print('O resultado é ' ,x1 + x2)
            
        elif operador == 2:
            print('O resultado é ' ,x1 - x2)
            
        elif operador == 3:
            print('O resultado é ' ,x1 * x2)
            
        elif operador == 4:
            print('O resultado é ' ,x1 / x2)
        break
        
    else:
        print('Opção inválida, escolha novamente')
        print(' ')





