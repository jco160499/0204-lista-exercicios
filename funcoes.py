def somar(a,b):
    if a + b > 40:
        resultado = a + b
    else:
        resultado = 'Ops, só retorno valores acima de 40'
    return resultado        

#print(somar(40,34))
# fazer o ifelse fora da função a tornaria utilizável por outras pessoas.
a = int(input('Digite o primeiro número:    '))
b = int(input('Digite o segundo número: '))

somado = somar(a,b)
print(somado)
