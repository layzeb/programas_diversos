# Início desenvolvimento: 29 NOV 2017
# Python 3
# Desenvolvedora: Layze Brandão

# Verifica se um servidor vinculado ao RGPS pode requerer Aposentadoria por Invalidez
# se não for possível aposentar, informar o tempo faltante
# exibir um relatório com as informações em arquivo externo

from datetime import date
from time import sleep

# hipótese de invalidez (2 anos ininterruptos de aux. doença)
    
# OBSERVAÇÃO: TRATAR EXCEÇÕES
# DATAS FUTURAS


def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True

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


    
def formataData(qt_dias):
    '''Função que recebe uma quantidade de dias e retorna data formatada em anos, meses e dias.'''
    
    anos = qt_dias // 365
    meses = (qt_dias % 365) // 30
    if meses == 12:
        meses -= 1
    dias = (qt_dias % 365) % 30
    
    return anos,meses,dias  # retorna uma tupla



print('-='*30)
print('CALCULADORA DE APOSENTADORIA POR INVALIDEZ'.center(60))
print('-='*30)

nome = input('Nome do servidor: ').upper()
cargo = input('Cargo: ').upper()


ini_lic = input('Digite a data inicial do recebimento do auxílio-doença [DD/MM/AAAA]: ').strip().split('/')
fim_lic = input('Digite a data atual [DD/MM/AAAA]: ').strip().split('/')

dias_lic = calculaTempo(ini_lic,fim_lic)

lic_formatada = formataData(dias_lic)


print('\nCalculando tempo de auxílio doença...')
sleep(3)

print('\nServidor está há {} dias recebendo auxílio doença, convertidos para {} anos, {} meses e {} dias.\n'.format(dias_lic,lic_formatada[0],lic_formatada[1],lic_formatada[2]))

if lic_formatada[0] >= 2 or dias_lic >= 730:
    print('Servidor apto a requerer Aposentadoria por Invalidez.')
else:
    dias_lic = 730 - dias_lic
    lic_formatada = formataData(dias_lic)
    
    print('O servidor poderá requerer Aposentadoria por invalidez em {} dias, correspondentes a {} ano(s), {} meses e {} dias.'.format(dias_lic,lic_formatada[0],lic_formatada[1],lic_formatada[2]))
