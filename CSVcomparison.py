# Programa que compara um campo entre dois documentos .csv
# Cria um terceiro documento .csv com um campo adicional
# Desenvolvido por: Layze Brandão
# 20 FEB 2018
# Python 3.6.2

# importação do módulo csv
import csv

comuns = [] # lista que irá armazenar todos os dados

# abrindo os arquivos para leitura
with open('folhaSemed.csv', 'r') as original, open('comparativo.csv', 'r') as readaptados:  

    # tornando os arq iteráveis para leitura
    lerOriginal = csv.reader(original)
    lerReadap = csv.reader(readaptados)

    # comparando as entradas de cada arquivo

    for linhaReadap in lerReadap:
        for linhaOrig in lerOriginal:
            if linhaReadap[1] == linhaOrig[1]:
                comuns.append(linhaReadap)
                break
            else:
                comuns.append(linhaOrig)


# abre o arquivo para edição
with open('especialistas.csv', 'w') as suporte:
    escSuporte = csv.writer(suporte)
    for linha in comuns:
        escSuporte.writerow(linha)
