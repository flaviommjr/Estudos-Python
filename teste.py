# from datetime import date
# from datetime import datetime

# nome_usuario = 'Freud Manganês'

# hoje = date.today()

# nascimento = '20/08/2005'

# data_nasc = datetime.strptime(nascimento, '%d/%m/%Y').date()

# idade = hoje - data_nasc

# idade2 = round((idade.days / 365) // 1)

# teste = idade2.is_integer()


# print(data_nasc)
# print(idade)
# print(idade2)
# print(teste)


# km     hm    dam  m  dm  cm   mm
# /1000  /100  /10  1  *10 *100 *1000
# 0,001  0,01  0,1      10  100  1000

# import math

# a = 6.1234567
# print(math.trunc(a))
# print(math.ceil(a))
# print(math.floor(a))

# a = int(input('Digite o valor do cateto oposto do triângulo: '))
# b = int(input('Digite o valor do cateto adjacente do triângulo: '))
# c = math.sqrt((math.pow(a , 2) + math.pow(b , 2)))
# print(f'\n\nNo triângulo retângulo cujo cateto oposto é {a} e o cateto adjacente é {b}, a hipotenusa é igual a {c:.0f}')

# ang = int(input('Digite o ângulo que deseja calcular: '))
# # print(f'O ângulo de {ang} tem o SENO de {math.sin(math.radians(ang)):.2f}\nO ângulo de {ang} tem o COSSENO de {math.cos(math.radians(ang)):.2f}\nO ângulo de {ang} tem a TANGENTE de {math.tan(math.radians(ang)):.2f}')
# print(math.radians(ang))

import random

nomes = []
for cont in range (4):
    nomes.append(input(f'nome do {cont+1}º aluno: '))

random.shuffle(nomes)
print(f'A ordem da apresentação será: {nomes}')
