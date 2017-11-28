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
    
    

def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True


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
    
    ano_ini = int(inicial[2])
    ano_fim = int(final[2])
    
    inicial = date(int(inicial[2]),int(inicial[1]),int(inicial[0]))
    final = date(int(final[2]),int(final[1]),int(final[0]))
    
    
    total_dias = abs((final - inicial).days)
    
    for anos in range(ano_ini,ano_fim+1):
        if bissexto(anos):
            total_dias += 1
    
    return total_dias

    
    
def tempoServico(qt_dias):
    '''Função usada para gerar uma data válida de tempo de serviço trabalhado em anos, meses e dias.'''
    
    anos = qt_dias // 365
    meses = (qt_dias % 365) // 30
    if meses == 12:
        meses -= 1
    dias = (qt_dias % 365) % 30
    
    return anos,meses,dias  # retorna uma tupla
    

    


print('-='*20)
print('CALCULADORA DE APOSENTADORIA'.center(40))
print('-='*20)

nome = input('Nome do servidor: ').upper()
sexo = input('Gênero [M/F]: ').strip().lower()
nasc = input('Data de nascimento [DD/MM/AAAA]: ').strip().split('/')

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
    print('Servidor(a) com {} anos. Não preenche os requisitos para aposentadoria proporcional ao tempo de contribuição.\n'.format(anos_idade))


# Aposentadoria voluntária integral
# 60 idade e 35 contrib H / 55 idade e 30 contrib M


    
inicio = input('\nDigite a data inicial do vínculo [DD/MM/AAAA]: ').strip().split('/')
fim = input('Digite a data final do vínculo. \nSe o servidor estiver em exercício, digite a data de hoje [DD/MM/AAAA]: ').strip().split('/')

print('\n\nCalculando tempo de serviço...\n')
sleep(5)
dias_trab = calculaTempo(inicio,fim)

# ADICIONAR TEMPO DE INCORPORAÇÃO

inc = input('Servidor possui período de tempo a ser incorporado [S/N] ?  ').strip().lower()

if inc == 's':
    
    while True:
        pass

tempo = tempoServico(dias_trab)     # ARGUMENTO DEVE SER DIAS_TRAB + DIAS INCORP
    

    
    

print('Servidor possui {} dias de tempo de contribuição, convertidos para {} anos, {} meses e {} dias.'.format(dias_trab,tempo[0],tempo[1],tempo[2]))

if tempo[0] >= 35 and sexo == 'm' and anos_idade >= 60:
    print('Servidor apto para Aposentadoria Voluntária Integral.')
elif tempo[0] >= 30 and sexo == 'f' and anos_idade >= 55:
    print('Servidora apta para Aposentadoria Voluntária Integral.')
else:
    print('Servidor(a) não preenche os requisitos para Aposentadoria Voluntária Integral.')

    

