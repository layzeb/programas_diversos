# Início desenvolvimento: 10 NOV 2017
# Python 3
# Desenvolvedora: Layze Brandão

# Programa que informa se um servidor SP pode solicitar aposentadoria
# No relatório: mostrar tempo de serviço, tempo total de incorporações,
# se já é possível solicitar aposentadoria
# o(s) tipo(s) de aposentadoria possível(is)
# se não for possível aposentar, informar o tempo (idade ou svc) restante
# exibir um relatório com as informações em arquivo externo

from datetime import date, datetime
from time import sleep

#RGPS

# compulsória: 75 idade
# voluntária integral: 60 idade e 35 contrib H / 55 idade e 30 contrib M
# voluntária proporcional ao tempo de contrib: 65 idade H / 60 idade M

hoje = date.today()


def check_date(year, month, day):
    '''Função que checa se uma data inserida é válida.'''
    correctDate = None
    
    try:
        newDate = datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    
    return correctDate

def is_future(year, month, day):
    
    valid = None
    
    data = datetime(year, month, day)
    if data > datetime.now():
        print('Data futura, tente novamente.')
        valid = False
    else:
        valid = True
    
    return valid


def bissexto(ano):
    '''Verifica se o ano passado como argumento é bissexto.'''
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True


def calculaIdade(data):
    '''Função que recebe uma data de nascimento e informa a idade.'''
    

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



def somaDias(valor1,valor2):
    '''Função que recebe quantidade de dias trabalhados e dias incorporados para gerar o total.'''
    return valor1 + valor2


    
def tempoServico(qt_dias):
    '''Função usada para gerar uma data válida de tempo de serviço trabalhado em anos, meses e dias.'''
    
    anos = qt_dias // 365
    meses = (qt_dias % 365) // 30
    if meses == 12:
        meses -= 1
    dias = (qt_dias % 365) % 30
    
    return anos,meses,dias  # retorna uma tupla
    

# ############################################################################ 


print('-='*20)
print('CALCULADORA DE APOSENTADORIA'.center(40))
print('-='*20)

nome = input('Nome do servidor: ').upper()
cargo = input('Cargo: ').upper()

while True:
    
    sexo = input('Gênero [M/F]: ').strip().lower()
    if sexo != 'm' and sexo != 'f':
        print('Campo "Gênero" inválido. Digite "M" para Masculino ou "F" para Feminino.\n')
    else:
        break

while True:
    
    try:
        nasc = input('Data de nascimento [DD/MM/AAAA]: ').strip().split('/')

        valid = check_date(int(nasc[2]),int(nasc[1]),int(nasc[0]))
        future = is_future(int(nasc[2]),int(nasc[1]),int(nasc[0]))
        
        if valid and future:
            break
    
    except (ValueError, IndexError) as e:
        print('Insira uma data válida.')

        
        
# Aposentadoria por idade

print('\n\nCalculando idade...')
sleep(5)

anos_idade = calculaIdade(nasc)

if anos_idade >= 75:
    print('Servidor com {} anos. Aposentadoria Compulsória.\n'.format(anos_idade))
elif 75 > anos_idade >= 65 and sexo == 'm':
    print('Servidor com {} anos. Apto para Aposentadoria voluntária proporcional ao tempo de contribuição.\n'.format(anos_idade))
elif 75 > anos_idade >= 60 and sexo == 'f':
    print('Servidora com {} anos. Apta para Aposentadoria voluntária proporcional ao tempo de contribuição.\n'.format(anos_idade))
else:
    print('Servidor(a) com {} anos. Não preenche os requisitos para aposentadoria proporcional ao tempo de contribuição.\n'.format(anos_idade))
    
    if sexo == 'f':
        print('A servidora estará apta a requerer aposentadoria proporcional ao tempo de contribuição em {} anos.'.format(60 - anos_idade))
    elif sexo == 'm':
        print('O servidor estará apto a requerer aposentadoria proporcional ao tempo de contribuição em {} anos.'.format(65 - anos_idade))


# Aposentadoria voluntária integral
# 60 idade e 35 contrib H / 55 idade e 30 contrib M

print('\nTEMPO DE CONTRIBUIÇÃO\n')

while True:
    
    try:
        
        inicio = input('\nDigite a data inicial do vínculo atual no formato [DD/MM/AAAA]. \nSe o servidor não estiver trabalhando, digite a data de admissão do último vínculo: ').strip().split('/')
        
        valid_ini = check_date(int(inicio[2]),int(inicio[1]),int(inicio[0]))
        fut_ini = is_future(int(inicio[2]),int(inicio[1]),int(inicio[0]))
        
        if valid_ini and fut_ini:
            break
        
    except (ValueError, IndexError) as e:
        print('Insira uma data válida.')
    
while True:
    
    try:
        
        fim = input('Digite a data final do vínculo no formato [DD/MM/AAAA]. \nSe o servidor estiver em exercício, digite a data de hoje: ').strip().split('/')
        
        valid_fim = check_date(int(fim[2]),int(fim[1]),int(fim[0]))
        fut_fim = is_future(int(fim[2]),int(fim[1]),int(fim[0]))
        
        if valid_fim and fut_fim:
            break
        
    except (ValueError, IndexError) as e:
        print('Insira uma data válida.')


dias_trab = calculaTempo(inicio,fim)

dias_incorp = 0

while True:
    
    inc = input('\nServidor possui período de tempo a ser incorporado [S/N] ?  ').strip().lower()

    if inc != 's' and inc != 'n':
        print('Campo inválido. Digite "S" para adicionar período de tempo a ser incorporado ou "N" se não houver incorporações.\n')
        continue
        
    elif inc == 's':
        
        while True:
            
            while True:
                
                try:
                
                    ini_incorp = input('\nDigite a data inicial do vínculo [DD/MM/AAAA]: ').strip().split('/')

                    valid_inc = check_date(int(ini_incorp[2]),int(ini_incorp[1]),int(ini_incorp[0]))
                    fut_fim = is_future(int(ini_incorp[2]),int(ini_incorp[1]),int(ini_incorp[0]))

                    if valid_fim and fut_fim:
                        break
                
                except (ValueError, IndexError) as e:
                    print('Insira uma data válida.')

            while True:
                
                try:
                    
                    fim_incorp = input('Digite a data final do vínculo [DD/MM/AAAA]: ').strip().split('/')
                    
                    valid_fim_inc = check_date(int(fim_incorp[2]),int(fim_incorp[1]),int(fim_incorp[0]))
                    fut_fim_inc = is_future(int(fim_incorp[2]),int(fim_incorp[1]),int(fim_incorp[0]))

                    if valid_fim_inc and fut_fim_inc:
                        break
                
                except (ValueError, IndexError) as e:
                    print('Insira uma data válida.')
                    
            dias_incorp += calculaTempo(ini_incorp,fim_incorp)
            
            outra_inc = input('\nPara adicionar mais um período de incorporação, digite "S". \nPara prosseguir, pressione qualquer tecla: ').strip().lower()
            
            if outra_inc == 's':
                continue
            else:
                break
    
    break
    
    
total = somaDias(dias_trab,dias_incorp)        
        
tempo = tempoServico(total)     


print('\n\nCalculando tempo de contribuição...\n')
sleep(5)

print('\nServidor(a) possui {} dias de tempo de contribuição, convertidos para {} anos, {} meses e {} dias.'.format(total,tempo[0],tempo[1],tempo[2]))

if tempo[0] >= 35 and sexo == 'm' and anos_idade >= 60:
    print('Servidor apto para Aposentadoria Voluntária Integral.')
elif tempo[0] >= 30 and sexo == 'f' and anos_idade >= 55:
    print('Servidora apta para Aposentadoria Voluntária Integral.')
else:
    print('Servidor(a) não preenche os requisitos para Aposentadoria Voluntária Integral.')
    
    if sexo == 'f':
        
        tempo_faltante = 10950 - total
        faltante_formatado = tempoServico(tempo_faltante)
        
        print('\nServidora poderá requerer aposentadoria voluntária integral em {} dias, correspondentes a {} anos, {} meses e {} dias.'.format(tempo_faltante,faltante_formatado[0],faltante_formatado[1],faltante_formatado[2]))
    
    elif sexo == 'm':
        
        tempo_faltante = 12775 - total
        faltante_formatado = tempoServico(tempo_faltante)
        
        print('\nServidor poderá requerer Aposentadoria Voluntária Integral em {} dias, correspondentes a {} anos, {} meses e {} dias.'.format(tempo_faltante,faltante_formatado[0],faltante_formatado[1],faltante_formatado[2]))
