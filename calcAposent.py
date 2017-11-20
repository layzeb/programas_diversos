# Início desenvolvimento: 10 NOV 2017
# Python 3
# Desenvolvedora: Layze Brandão

# Programa que informa se um servidor SP pode solicitar aposentadoria
# Solicitar idade, incorporações
# No relatório: mostrar tempo de serviço, tempo total de incorporações,
# se já é possível solicitar aposentadoria
# o(s) tipo(s) de aposentadoria possível(is)
# se não for possível aposentar, informar o tempo (idade ou svc) restante
# exibir um relatório com as informações em arquivo externo

from datetime import date
from time import sleep



# compulsoria: 70 idade
# voluntária integral: 60 idade e 35 contrib H / 55 idade e 30 contrib M
# voluntária proporcional ao tempo de contrib: 65 idade H / 60 idade M
# hipótese de invalidez (2 anos consecutivos de aux. doença)
    
    


def somaDatas():
    '''Função que irá somar a data das incorporações + tempo contrib'''
    pass

def calculaIdade(data):
    '''Função que recebe uma data de nascimento e informa a idade.'''
    hoje = date.today()

    data = date(int(data[2]),int(data[1]),int(data[0]))

    idade = hoje.year - data.year

    if data.month > hoje.month:
        idade -= 1
    elif data.month == hoje.month:
        if data.day > hoje.day:
            idade -= 1
    
    return idade

def calculaTempo(inicial, final):
    '''Função que calcula o tempo decorrido, dadas data inicial e final.'''
    
    inicial = date(int(inicial[2]),int(inicial[1]),int(inicial[0]))
    
    if final == hoje:
        final = date.today()
    else:
        final = date(int(final[2]),int(final[1]),int(final[0]))
    

    dic_meses = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


    anos = final.year - inicial.year
    meses = 0
    dias = 0

    if final.month > inicial.month:
        meses = final.month - inicial.month
        dias = abs(inicial.day - final.day)
        if inicial.day > final.day:
            meses -= 1
            dias = (dic_meses.get(inicial.month - 1)) - (inicial.day - final.day)
        

    elif final.month < inicial.month:
        anos -= 1
        meses = (final.month + inicial.month) % 12
        dias = abs(inicial.day - final.day)
        if inicial.day > final.day:
            meses -= 1
            dias = (dic_meses.get(inicial.month - 1)) - (inicial.day - final.day)


    else:
        dias = abs(inicial.day - final.day)
        
    return anos,meses,dias  # retorna uma tupla

    
    
def tempoServico():
    '''Função usada para gerar uma data válida de tempo de serviço trabalhado'''
    pass

    


print('-='*20)
print('CALCULADORA DE APOSENTADORIA'.center(40))
print('-='*20)

nome = input('Nome do servidor: ').upper()
sexo = input('Gênero [M/F]: ').strip().lower()
nasc = input('Data de nascimento [DD/MM/AAAA]: ').strip().split('/')
adm = input('Data de admissão na SEMED [DD/MM/AAAA]: ').strip().split('/')
exercicio = input('Servidor em exercício? [S/N]: ').strip().lower()
hoje = date.today()

# Aposentadoria por idade

print('\n\nCalculando idade...')
sleep(5)

anos_idade = calculaIdade(nasc)

if anos_idade >= 70:
    print('Servidor com {} anos. Aposentadoria Compulsória.'.format(anos_idade))
elif 70 > anos_idade >= 65 and sexo == 'm':
    print('Servidor com {} anos. Apto para Aposentadoria voluntária proporcional ao tempo de contribuição.'.format(anos_idade))
elif 70 > anos_idade >= 60 and sexo == 'f':
    print('Servidora com {} anos. Apta para Aposentadoria voluntária proporcional ao tempo de contribuição.'.format(anos_idade))
else:
    print('Servidor(a) com {} anos. Não preenche os requisitos para aposentadoria proporcional ao tempo de contribuição.'.format(anos_idade))


# Aposentadoria voluntária integral
# 60 idade e 35 contrib H / 55 idade e 30 contrib M

print('\n\nCalculando tempo de serviço...')
sleep(5)

# servidor em exercício sem tempo a incorporar
# data final == hoje

tempo = calculaTempo(adm,hoje)  # retorna uma tupla
print('Servidor possui {} anos, {} meses e {} dias de tempo de contribuição'.format(tempo[0],tempo[1],tempo[2]))

if tempo[0] >= 35 and sexo == 'm' and anos_idade >= 60:
    print('Servidor apto para Aposentadoria Voluntária Integral.')
elif tempo[0] >= 30 and sexo == 'f' and anos_idade >= 55:
    print('Servidora apta para Aposentadoria Voluntária Integral.')
else:
    print('Servidor(a) não preenche os requisitos para Aposentadoria Voluntária Integral.')


    

