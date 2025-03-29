S = 255.50
D = 305.50
T = 360.50

print("Bem vindo! \n Tipos de diárias disponiveis: \n S - Simples (Valor da diária: R$255,50) \n D - Duplo (Valor da diária: R$305,50) \n T - Triplo (Valor da diária: R$360,50) \n")

td = input('Qual tipo de diária você quer? ') 
qd = int(input('Quantas diárias você quer? '))

if td == 'S':
  total = qd * S
  print(f'Você quer diária simples, e o total a ser pago por {qd} dias será: R${total}') 

elif td == 'D':
  total = qd * D
  print(f'Você quer diária dupla, e o total a ser pago por {qd} dias será: R${total}') 

elif td == 'T':
  total = qd * T
  print(f'Você quer diária tripla, e o total a ser pago por {qd} dias será: R${total}') 

else:
  print('Tipo de diária inválida')
