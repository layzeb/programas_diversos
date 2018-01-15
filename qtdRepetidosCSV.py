# Programa que compara o campo Nome de dois arquivos CSV e retorna a quantidade de duplicados
# Desenvolvedora: Layze Brandão
# Em 2017 OUT 18
# Python 3.4.3


# ABRINDO OS ARQUIVOS EM MODO DE LEITURA
arq1 = open('MAGIST.csv', 'r')
arq2 = open('SELETIVO.csv','r')


aux = []    # CRIA UMA LISTA AUXILIAR
i = 0       # INICIALIZA UM CONTADOR DE OCORRÊNCIAS EM DUPLICIDADE

for line in arq1.readlines():       # ITERA LINHA A LINHA PELO arq1
    campo = line.split(',')         # SEPARA OS CAMPOS
    aux.append(campo[0])            # ADICIONA O CONTEÚDO [NOME DO SERVIDOR] À LISTA AUXILIAR

for row in arq2.readlines():        # ITERA LINHA A LINHA PELO arq2
    field = row.split(',')          # SEPARA OS CAMPOS
    if field[0] in aux:             # VERIFICA SE O CAMPO 'NOME' NO arq2 JÁ ESTÁ NA LISTA AUXILIAR
        print(field[0])             # MOSTRA O NOME DO SERVIDOR QUE ESTÁ EM DUPLICIDADE
        i += 1                      # INCREMENTA O CONTADOR

print('\nQuantidade de repetidos: {}.'.format(i-1))     # MOSTRA O TOTAL DE OCORRÊNCIAS DE DUPLICIDADE

# FECHANDO OS ARQUIVOS
arq1.close()
arq2.close()
