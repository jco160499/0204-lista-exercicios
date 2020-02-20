import math as mt
def area(raio):
    if type(raio) == float:
        calculo = mt.pi * (raio * raio)
    elif type(raio) == int:
        calculo = mt.pi * (raio * raio)
    else:
        calculo = "Insira valor numérico"   
    return calculo

r = float(input('Digite o raio do círculo: '))
print('A área é:    ',area(r))

def comprimento(raio):
    if type(raio) == float:
        calculo = 2* (mt.pi *raio)
    elif type(raio) == int:
        calculo = 2* (mt.pi *raio)
    else:
        calculo = "Insira valor numérico"   
    return calculo
print('O comprimento é: ',comprimento(r))
