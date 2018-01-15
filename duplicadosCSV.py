# Programa que compara campos repetidos em um arquivo csv e gera um arquivo sem os repetidos e outro só de repetidos
# Desenvolvedora: Layze Brandão
# Em 2017 OUT 18
# Python 3.4.3


entrada = open('arquivo.csv','r')    # abre o arquivo original para leitura
saida = open('unicos.csv','w')      # cria o arquivo sem campos duplicados
repetidos = open('repetidos.csv', 'w')      # cria o arquivo só de duplicados

aux = []    # cria uma lista auxiliar

for line in entrada.readlines():    # iterando linha a linha pelo arquivo de entrada
    campo = line.split(',')         # separa os campos
    if campo[0] not in aux:         # verifica se o conteúdo do campo Nome não está na lista auxiliar
        aux.append(campo[0])        # se não estiver, adiciona à lista auxiliar
        saida.write(line)           # e escreve a linha inteira no arquivo sem duplicados
    else:
        repetidos.write(line)       # escreve a linha repetida no arquivo de repetidos

# fechando todos os arquivos
entrada.close()
saida.close()
repetidos.close()
