freq = int(input('Digite sua frequencia: '))
media = float(input('Digite sua media: '))

if freq >= 75:
  if media >= 6:
    print('Você passou!')
  else:
    print('Você não passou por nota!')

else:
  print('Você não passou por falta!')
