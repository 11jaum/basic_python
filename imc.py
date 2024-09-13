kg = float(input('Insira seu peso: '))
alt = float(input('Insira sua altura: '))

altura = alt ** 2  
imc = kg / altura   

if imc < 18.5: 
    print(f' Seu IMC é {imc}, você está abaixo do peso.')
    
elif imc > 18.5 and imc < 24.9:
    print(f'Seu IMC é {imc}, você está no seu peso adequado.')
    
elif imc > 25 and imc < 29.9:
    print(f'Seu IMC é {imc}, você está no sobrepeso.')
    
elif imc > 30:
    print(f'Seu IMC é {imc}, você está obeso.')
