# Programa que compara campos repetidos em um arquivo csv e gera um arquivo sem os repetidos e outro só de repetidos
# Desenvolvedora: Layze Brandão
# Em 2017 OUT 17
# Python 3.4.3


#Programa que lê um arquivo de texto contendo nomes de servidores, localiza as duplicidades e as armazena em um novo arquivo.

arq = open('servidores.txt', 'r')   #abre o arquivo original para leitura
rep = open('repetidos.txt','w')     #cria um arquivo chamado repetidos.txt para edição
listaNomes = arq.readlines()    #lê cada linha do arquivo e armazena em uma lista
listaAux = []       #lista auxiliar 
listaRep = []       #lista de repetidos

for valor in listaNomes:    #itera pelos valores da lista de nomes original
    nome = valor.split('\n')    #separa os caracteres de nova linha do nome do servidor
    if nome[0] in listaAux:     #verifica se o nome do servidor já está na lista auxiliar
        listaRep.append(nome[0])    #se já tiver na auxiliar, então copia o valor pra lista de repetidos
        #print(nome[0])
    else:
        listaAux.append(nome[0]) #senão, copia o dado não repetido na lista auxiliar q guarda valores únicos

listaRep.sort() #coloca a lista de repetidos em ordem alfabética

for i in listaRep:  #itera sobre a lista já ordenada
    rep.write(i + '\n') #escreve cada item da lista de repetidos no arquivo de edição
    
print(len(listaRep))    #mostra no shell a quantidade de ocorrências de duplicidade
arq.close() #encerra a utilização do arquivo em uso
rep.close()
