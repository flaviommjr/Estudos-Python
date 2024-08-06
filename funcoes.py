
import math

def funcaoPrimeiroGrau(lista):
    
    resultado = (lista[0]*lista[2])+lista[1]

    return resultado


# Função do primeiro grau:

# Y = A x X + B ou f(x) = ax + b

def funcaoSegundoGrau(lista):

    delta = (lista[1]**2)-4*lista[0]*lista[2]
    
    x1 = (-lista[1]+(delta**(1/2)))/(2*lista[0])
    x2 = (-lista[1]-(delta**(1/2)))/(2*lista[0])

    raizes = [x1, x2]

    return raizes


segundo_grau = [1, (-3), (-10)]

resposta = funcaoSegundoGrau(segundo_grau)

print(resposta)




# Função do segundo grau:

# Delta = B² - 4 x A x C ou ∆= b²-4ac

# X´s -> x = - b ± √∆ / 2a ou X = -B +- Delta**(1/2) / 2*A

