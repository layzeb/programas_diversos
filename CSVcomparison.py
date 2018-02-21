# Programa que compara um campo entre dois documentos .csv
# Cria um terceiro documento .csv com um campo adicional
# Desenvolvido por: Layze Brandão
# 20 FEB 2018
# Python 3.6.2

# importa o módulo csv
import csv

# abre os arquivos de leitura e escrita para análise e manipulação
with open('arqOriginal.csv', 'r') as original, open('arqComparativo.csv', 'r') as comparativo, open('arqEditado.csv', 'w') as editado:  

    # cria objetos iteráveis para leitura (reader) e escrita (writer)
    lerOriginal = csv.reader(original)
    lerComp = csv.reader(comparativo)
    escEdit = csv.writer(editado)
    
    # iteração pelos dois arquivos de leitura, procurando um campo especificado em comun entre ambos
    
    for linhaComp in lerComp:   # analisando cada linha do arquivo comparado
        for linhaOrig in lerOriginal:   # com cada linha do arquivo original
            if linhaComp[0] == linhaOrig[0]:    # se o campo do índice[0] - no caso em tela, campo NOME - forem iguais em ambos:
                linhaOrig[4] = 'SUPORTE PEDAGOGICO' # o valor do campo no índice [4] é alterado pela string desejada
                escEdit.writerow(linhaOrig)         # e após a modificação, a linha inteira é escrita no arquivo novo (editado)
                break       # após o encontro da ocorrência, finaliza a iteração e passa para o item seguinte
            else:
                escEdit.writerow(linhaOrig)     # se não houver campos iguais, apenas escrever a linha do arquivo original
