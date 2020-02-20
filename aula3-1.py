import datetime as dt
def dias_de_vida(ano,mes,dia):
    data_nascimento = dt.date(ano,mes,dia)
    idade_dias =  dt.date.today() - data_nascimento
    return idade_dias

print(dias_de_vida(1999,4,16))
dias = str(dias_de_vida(1999,4,16)).replace(' days, 0:00:00','')
idade = round(float(dias)/365,1)
print('Você tem:    ',idade, ' anos')

